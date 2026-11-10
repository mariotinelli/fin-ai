# The `planning.md` contract

The plan lives beside `task.md` and is the only artifact handed to Ralph. It contains no hashes, approvals, Redmine copies or operational state. Write the resulting document in Brazilian Portuguese; the Portuguese headings below are user-facing content and parser contracts.

## Structure

Gate 3 uses the interpreter identified by the baseline fence: `sh`, `bash`, `shell` or an unlabeled fence use Bash; `powershell` uses Windows PowerShell, `pwsh` uses PowerShell 7 and `cmd`/`bat` use cmd. The interpreter must be on PATH; interactive profiles are not loaded. Use syntax and paths compatible with the chosen interpreter and explicitly propagate intermediate command failures, particularly in PowerShell. Check subprocesses too: starting Composer from Bash does not automatically change the shell used by its internal scripts on Windows.

Use these second-level sections before the phases:

- `Identidade e fontes`: child, parent requirement and local source paths.
- `Referências visuais`: required-reading source list under the contract below, or an explicit reason it does not apply.
- `Objetivo`: observable task outcome.
- `Estado atual`: discovered behavior and implementation.
- `Escopo`: inclusions and exclusions.
- `Arquitetura`: existing patterns and decisions guiding implementation.
- `Estratégia`: general sequence and testing approach.
- `Baseline`: aggregate command, verifier composition, prerequisites, initial results and known failures or obstacles.
- `Riscos`: regressions, migrations, security and concerns.

In an executable plan, put exactly one fenced block containing the suite's executable command in `Baseline`. If no safe complete command can be determined, retain only an explicitly blocked draft without a fictitious block. That draft does not satisfy the parser and must not be handed off for execution; complete the command first. The result is an initial observation; every phase still requires the test gate to pass:

````markdown
## Baseline

Comando da suíte completa:

```sh
composer test
```

Resultado inicial: impedido pelo ambiente; nenhum teste funcional executado.
Pré-requisito pendente: runtime compatível com o projeto. O comando acima só poderá ser usado após sua seleção no ambiente do executor.

| Verificador | Invocação/configuração | Exigência relevante | Resultado observado |
| --- | --- | --- | --- |
| Análise estática | `composer test:types` | Runtime declarado no projeto | Falhou ao inicializar: runtime incompatível |
| Testes | `composer test:unit` | Cobertura configurada pelo projeto | Não executado: etapa anterior interrompeu o comando |
````

The example is illustrative: use the project's actual verifiers and results. Keep individual commands inline in the table without extra fenced blocks inside `Baseline`. Distinguish passed, failed and not executed; if aggregate output does not expose individual results, state that limitation. An interruption does not authorize assigning results to subsequent steps.

Record sanitized failures and execution prerequisites. The single command must represent the complete gate and work in the executor environment, including runtime selection where necessary. Without a known safe path, mark the plan operationally blocked instead of inventing an approved command or announcing readiness. Focused tests belong in phases and do not replace the complete gate. During implementation, changes made by fixing tools must be reviewed in the diff.

## Visual source handoff

Every executable plan contains exactly one `## Referências visuais` section before the phases. Its body contains only a bullet list of existing normalized Markdown source paths, relative to the repository, using forward slashes and one backtick-wrapped path per line:

```markdown
## Referências visuais

- `docs/harness/scopes/mvp/sources/design-001.md`
```

The executor adds these files to development, correction and validation required reading and rejects missing files, symlinks and paths outside the repository. Descriptions, screen/state locators and adaptation decisions belong in `Identidade e fontes`, architecture and phase criteria, not in this path-only section.

Without applicable visual work, the section contains only `Não se aplica: <specific reason>`. For a backend phase in a task that later delivers UI, retain the task's source list and identify where visual acceptance will be demonstrated. Existing plans without this section need review/amendment before execution; do not reset completed phases or silently classify historical UI work as not applicable.

The primary design governs appearance; canonical requirements govern approved fields/behavior, with adaptations reconciled explicitly. Explain how the design maps to the target components, including shared identity, typography, colors, composition and applicable responsive/state evidence. A reused starter theme or dark mode is preserved only when compatible with the approved visual contract; a new visual variant needs an explicit boundary rather than silently taking priority over the reference.

Each UI phase's acceptance and focused checks identify the reference screen/state, approved adaptations, relevant viewport and how rendered evidence will be compared. Choose proportional browser inspection or visual tests without requiring pixel-perfect automation. Backend-only phases explain non-applicability and their UI consumer when relevant. A required visual comparison blocked by the environment remains unverified and prevents that UI phase's validation approval; static types, functional tests and merely generating a screenshot do not replace comparison.

Then write one or more phases in ascending order, retaining these Portuguese headings:

```markdown
## Fase 1 — Nome da entrega

### Objetivo
...

### Dependências
...

### Mudanças esperadas
...

### Arquivos prováveis
...

### Limites
...

### Estratégia
...

### Aceite
...

### Verificação focada
...
```

Each phase must be implementable in a fresh session, leave a coherent change ready for commit and include criteria independent validation can demonstrate. Paths are grounded hypotheses, not obligations to edit every listed file.

## Review

Before presenting, compare every task behavior with expected changes and acceptance evidence in its responsible phase. Include success, relevant failures and valid/invalid boundaries when specified. Internal state suffices only when it demonstrates the required outcome; permissions and access need evidence of protected behavior, including after an operation where pertinent.

Identify what existing tests already demonstrate and gaps to fill. Reuse suitable coverage, preserving existing tests and avoiding duplication. Choose endpoint, integration or browser according to the outcome to prove rather than testing only implementation declarations. Express this mapping in phase acceptance and checks; no separate manifest or matrix is required. Gaps do not authorize expanding requirements or implementing sibling tasks.

For required preservation, identify the existing test or dataset and inspect inputs, exercised paths and assertions before claiming coverage. Record that reference beside the relevant check; if coverage is partial, describe only the gap to add. Saying “manter testes existentes” does not demonstrate criteria absent from those tests. Fixture changes must preserve each test's purpose rather than disguise out-of-scope functional changes as data updates. Also verify architecture underwent the shared-consumer analysis from technical inspection.

Show the complete file to the developer. Edit `planning.md` directly until they agree. Do not record approval in another structure. If presented content changes, show the new version before execution. Ralph reads the current file; restarting all phases requires deleting `.flow/ralph-state.json` only after deciding the fate of existing commits and changes.
