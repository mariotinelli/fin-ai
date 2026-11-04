#!/usr/bin/env python3
"""Local test-condition validation and dependency-free Word document rendering."""

from __future__ import annotations

import io
import re
from typing import Any
from xml.etree import ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


WORD = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
ET.register_namespace("w", WORD)


def text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    if any(not (code in (9, 10, 13) or 32 <= code <= 0xD7FF or 0xE000 <= code <= 0xFFFD or 0x10000 <= code <= 0x10FFFF) for code in map(ord, value)):
        raise ValueError(f"{label} contains characters unsupported by DOCX")
    return value


def validate_conditions(proposal: dict[str, Any]) -> None:
    source = proposal["test_conditions"]
    if not isinstance(source, dict) or not {"context", "conditions"} <= set(source) or set(source) - {"context", "conditions", "document_format"}:
        raise ValueError("test_conditions fields are invalid")
    if source.get("document_format", "docx") not in {"markdown", "docx"}:
        raise ValueError("test_conditions.document_format must be markdown or docx")
    text(source["context"], "test_conditions.context")
    conditions = source["conditions"]
    if not isinstance(conditions, list) or not conditions:
        raise ValueError("test_conditions.conditions must be a non-empty array")
    requirements = {item["id"] for item in proposal["requirements"]}
    covered: set[str] = set()
    ids: set[str] = set()
    for index, condition in enumerate(conditions):
        label = f"test_conditions.conditions[{index}]"
        required = {"id", "title", "verification", "expected_result", "requirement_ids"}
        optional = {"context", "group", "impact_justification"}
        if not isinstance(condition, dict) or not required <= set(condition) or not set(condition) <= required | optional:
            raise ValueError(f"{label} fields are invalid")
        for field in (required - {"requirement_ids"}) | (set(condition) & optional):
            text(condition[field], f"{label}.{field}")
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", condition["id"]):
            raise ValueError(f"{label}.id must be a stable identifier")
        if condition["id"] in ids:
            raise ValueError("test condition IDs must be unique")
        ids.add(condition["id"])
        origins = condition["requirement_ids"]
        if not isinstance(origins, list) or not origins or any(not isinstance(origin, str) or origin not in requirements for origin in origins):
            raise ValueError(f"{label}.requirement_ids must reference the approved proposal requirements")
        if len(origins) != len(set(origins)):
            raise ValueError(f"{label}.requirement_ids must not duplicate references")
        covered.update(origins)
    if covered != requirements:
        raise ValueError("test conditions must reference every proposal requirement; semantic coverage still requires tech lead review")


def validate_condition_history(revisions: list[dict[str, Any]]) -> None:
    seen: set[str] = set()
    active: set[str] = set()
    started = False
    for revision in revisions:
        source = revision["proposal"].get("test_conditions")
        if source is None:
            if started:
                raise ValueError("new revisions cannot discard the test conditions contract")
            continue
        started = True
        current = {condition["id"] for condition in source["conditions"]}
        if current & (seen - active):
            raise ValueError("removed test condition IDs cannot be reused")
        seen.update(current)
        active = current


def condition_sections(proposal: dict[str, Any]) -> list[tuple[str, str]]:
    source = proposal["test_conditions"]
    sections = [("Heading2", "Contexto"), ("Normal", source["context"])]
    requirements = {item["id"]: item["summary"] for item in proposal["requirements"]}
    group = None
    for condition in source["conditions"]:
        current_group = condition.get("group")
        if current_group and current_group != group:
            sections.append(("Heading2", current_group))
        group = current_group
        sections.append(("Heading3", f"{condition['id']} — {condition['title']}"))
        if condition.get("context"):
            sections.append(("Normal", "Contexto: " + condition["context"]))
        sections.extend([
            ("Normal", "Verificação: " + condition["verification"]),
            ("Normal", "Resultado esperado: " + condition["expected_result"]),
            ("Normal", "Origem no requisito: " + "; ".join(f"{origin}: {requirements[origin]}" for origin in condition["requirement_ids"])),
        ])
        if condition.get("impact_justification"):
            sections.append(("Normal", "Impacto que justifica a regressão: " + condition["impact_justification"]))
    return sections


def document_requested(proposal: dict[str, Any]) -> bool:
    # Missing format belongs to historical approvals, which required Word.
    return proposal["test_conditions"].get("document_format", "docx") == "docx"


def conditions_markdown(proposal: dict[str, Any]) -> str:
    return "# Condições de teste\n\n" + "\n\n".join(
        ("## " if style == "Heading2" else "### " if style == "Heading3" else "") + content
        for style, content in condition_sections(proposal)
    ) + "\n"


def element(parent: ET.Element, tag: str, **attributes: str) -> ET.Element:
    return ET.SubElement(parent, f"{{{WORD}}}{tag}", {f"{{{WORD}}}{key}": value for key, value in attributes.items()})


def docx_bytes(proposal: dict[str, Any], revision: int, proposal_sha: str, approval: dict[str, Any], *, decomposition_revision: int | None = None) -> bytes:
    feature = proposal["feature"]
    kind = "Bug" if feature["artifact_path"].endswith("bug.md") else "Feature"
    paragraphs = [
        ("Title", "Condições de teste"),
        ("Subtitle", f"{kind} #{feature['issue_id']} — {feature['title']}"),
        ("Normal", f"Revisão do documento e da decomposição: r{revision:03d}" if decomposition_revision is None else f"Revisão do documento: r{revision:03d}; decomposição: r{decomposition_revision:03d}"),
        ("Normal", f"Revisão do requisito (SHA-256): {feature['requirement_sha256']}"),
        ("Normal", f"Fonte do requisito: {feature['artifact_path']}"),
        ("Normal", f"Proposta aprovada (SHA-256): {proposal_sha}"),
        ("Normal", f"Aprovado por {approval['approved_by']} em {approval['approved_at']}"),
        *condition_sections(proposal),
    ]
    document = ET.Element(f"{{{WORD}}}document")
    body = element(document, "body")
    for style, content in paragraphs:
        text(content, "DOCX paragraph")
        paragraph = element(body, "p")
        properties = element(paragraph, "pPr")
        element(properties, "pStyle", val=style)
        for index, line in enumerate(content.split("\n")):
            run = element(paragraph, "r")
            if index:
                element(run, "br")
            node = element(run, "t")
            node.set(XML_SPACE, "preserve")
            node.text = line
    section = element(body, "sectPr")
    element(section, "pgSz", w="11906", h="16838")
    element(section, "pgMar", top="1134", right="1134", bottom="1134", left="1134")

    styles = ET.Element(f"{{{WORD}}}styles")
    defaults = element(styles, "docDefaults")
    run_defaults = element(element(defaults, "rPrDefault"), "rPr")
    element(run_defaults, "rFonts", ascii="Calibri", hAnsi="Calibri")
    element(run_defaults, "sz", val="22")
    element(run_defaults, "lang", val="pt-BR")
    for name, size in [("Normal", "22"), ("Title", "40"), ("Subtitle", "28"), ("Heading2", "28"), ("Heading3", "24")]:
        style_node = element(styles, "style", type="paragraph", styleId=name)
        element(style_node, "name", val=name)
        properties = element(style_node, "pPr")
        element(properties, "spacing", before="200" if name != "Normal" else "0", after="120")
        if name != "Normal":
            element(properties, "keepNext")
        if name.startswith("Heading"):
            element(properties, "outlineLvl", val="1" if name == "Heading2" else "2")
        run = element(style_node, "rPr")
        element(run, "sz", val=size)
        if name in ("Title", "Heading2", "Heading3"):
            element(run, "b")

    parts = {
        "[Content_Types].xml": b'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>''',
        "_rels/.rels": b'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>''',
        "word/_rels/document.xml.rels": b'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>''',
        "word/document.xml": ET.tostring(document, encoding="utf-8", xml_declaration=True),
        "word/styles.xml": ET.tostring(styles, encoding="utf-8", xml_declaration=True),
    }
    output = io.BytesIO()
    with ZipFile(output, "w") as archive:
        for name, content in parts.items():
            info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, content)
    return output.getvalue()
