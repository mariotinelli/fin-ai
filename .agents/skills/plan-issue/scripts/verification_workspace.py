"""Own declared generated outputs without exempting repository source from checks."""
from __future__ import annotations

import hashlib
import os
import re
import shutil
import stat
import subprocess
from pathlib import Path, PurePosixPath
from ralph_runtime import RuntimeFailure


PROTECTED = {".git", ".flow", ".agents", ".claude", ".opencode", "node_modules", "vendor"}


def declared_artifacts(phase: str) -> list[str]:
    sections = list(re.finditer(r"^### Artefatos de verificação[ \t]*\r?$", phase, re.MULTILINE))
    if not sections:
        return []
    if len(sections) != 1:
        raise RuntimeFailure("phase requires at most one Artefatos de verificação section")
    body = re.split(r"^#{1,3} ", phase[sections[0].end():], maxsplit=1, flags=re.MULTILINE)[0].strip()
    if re.fullmatch(r"Não se aplica: [^\r\n]+", body):
        return []
    paths = []
    for line in body.splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r"- `([^`]+)`", line.strip())
        if not match:
            raise RuntimeFailure("Artefatos de verificação must list repository-relative output directories")
        name = match.group(1)
        path = PurePosixPath(name)
        if path.is_absolute() or path.as_posix() != name or name == "." or ".." in path.parts or any(c in name for c in "\\:*?[]") or any(ord(c) < 32 for c in name) or any(p.casefold() in PROTECTED for p in path.parts):
            raise RuntimeFailure("artifact directories must be normalized relative paths without traversal, globs or protected metadata")
        comparison = PurePosixPath(name.casefold()) if os.name == "nt" else path
        for other in paths:
            existing = PurePosixPath(other.casefold() if os.name == "nt" else other)
            if comparison == existing or comparison.is_relative_to(existing) or existing.is_relative_to(comparison):
                raise RuntimeFailure("artifact directories must not repeat or overlap")
        paths.append(name)
    if not paths:
        raise RuntimeFailure("declare artifact output directories or explain Não se aplica")
    return paths


def _normal(path: Path, base: Path) -> None:
    if base.resolve() != base:
        raise RuntimeFailure("artifact directory anchor was redirected")
    if not path.is_relative_to(base):
        raise RuntimeFailure("artifact path is outside its owned directory")
    current = base
    for part in path.relative_to(base).parts:
        current = current / part
        try:
            info = current.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400):
            raise RuntimeFailure("artifact paths must not use symlinks or junctions")
    if not path.resolve().is_relative_to(base.resolve()):
        raise RuntimeFailure("artifact path was redirected outside its owned directory")


class VerificationWorkspace:
    def __init__(self, repo: Path, roots: list[str], directory: Path) -> None:
        self.repo = repo.resolve()
        self.roots = [self.repo / name for name in roots]
        self.directory = directory.resolve()
        self.generated = self.directory / "generated"
        self.artifacts: list[dict[str, str]] = []
        self.prepared = False

    def _tracked(self) -> set[str]:
        result = subprocess.run(["git", "ls-files", "--cached", "--full-name", "-z"], cwd=self.repo, capture_output=True, check=False)
        if result.returncode:
            raise RuntimeFailure("cannot check tracked files before collecting artifacts")
        return set(filter(None, result.stdout.decode("utf-8").split("\0")))

    def _files(self, root: Path, base: Path) -> list[Path]:
        _normal(root, base)
        if not root.exists():
            return []
        if not root.is_dir():
            raise RuntimeFailure("declared artifact output must be a directory")
        files = []
        for current, directories, names in os.walk(root, followlinks=False):
            for name in [*directories, *names]:
                path = Path(current) / name
                _normal(path, base)
                if name.casefold() in PROTECTED:
                    raise RuntimeFailure("protected metadata found inside an artifact directory")
                mode = path.lstat().st_mode
                if stat.S_ISREG(mode):
                    files.append(path)
                elif not stat.S_ISDIR(mode):
                    raise RuntimeFailure("artifact outputs must contain only regular files and directories")
        return sorted(files)

    def _workspace_files(self) -> list[Path]:
        tracked = self._tracked()
        protected = {name.casefold() if os.name == "nt" else name for name in tracked}
        files = []
        for root in self.roots:
            _normal(root, self.repo)
            for path in self._files(root, self.repo):
                relative = path.relative_to(self.repo).as_posix()
                if (relative.casefold() if os.name == "nt" else relative) not in protected:
                    files.append(path)
        return files

    def _copy(self, source: Path, target: Path) -> str:
        _normal(source, self.repo)
        _normal(target, self.directory)
        target.parent.mkdir(parents=True, exist_ok=True)
        original = source.lstat()
        with source.open("rb") as incoming:
            opened = os.fstat(incoming.fileno())
            if not stat.S_ISREG(opened.st_mode) or (opened.st_dev, opened.st_ino) != (original.st_dev, original.st_ino):
                raise RuntimeFailure("artifact changed identity while staging")
            with target.open("xb") as outgoing:
                shutil.copyfileobj(incoming, outgoing)
        digest = self._digest(target)
        _normal(source, self.repo)
        if self._digest(source) != digest:
            raise RuntimeFailure("artifact changed while staging; original preserved")
        return digest

    @staticmethod
    def _digest(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def _archive(self, files: list[Path], stage: str) -> None:
        staged = []
        # Complete all copies before removing any workspace output.
        for source in files:
            relative = source.relative_to(self.repo)
            target = self.directory / stage / relative
            digest = self._copy(source, target)
            staged.append((source, target, digest))
        for source, target, _ in staged:
            self.artifacts.append({"source": source.relative_to(self.repo).as_posix(), "path": str(target), "origin": stage})
        removed = []
        try:
            for source, _, digest in staged:
                _normal(source, self.repo)
                if self._digest(source) != digest:
                    raise RuntimeFailure("artifact changed before archival; preserved copies require inspection")
                source.unlink()
                removed.append(source)
        except (OSError, RuntimeFailure):
            # Restore only absent outputs, never overwrite a concurrent change.
            for source, target, _ in staged:
                if source in removed:
                    _normal(source, self.repo)
                    source.parent.mkdir(parents=True, exist_ok=True)
                    if not source.exists():
                        with source.open("xb") as restored, target.open("rb") as archived:
                            shutil.copyfileobj(archived, restored)
            raise

    def prepare(self) -> None:
        files = self._workspace_files()
        self.generated.mkdir(parents=True, mode=0o700)
        self._archive(files, "before")
        self.prepared = True

    def finish(self) -> list[dict[str, str]]:
        if not self.prepared:
            return self.artifacts
        files = self._workspace_files()
        direct = self._files(self.generated, self.directory)
        self._archive(files, "after")
        for path in direct:
            self.artifacts.append({"source": "RALPH_ARTIFACTS_DIR/" + path.relative_to(self.generated).as_posix(), "path": str(path), "origin": "direct"})
        return self.artifacts
