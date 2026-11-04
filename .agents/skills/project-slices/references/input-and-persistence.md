# Entrada e persistência local

## Layout

Preserve o layout canônico do `project-flow`: `feature.md` ou `bug.md` continua sendo o único documento de requisito na raiz do item pai. Use:

- `.work/slices-remote.json` para o snapshot sanitizado e descartável da leitura Redmine;
- `.flow/slices-input-check.json` para a evidência durável da conferência funcional;
- `.work/slices-proposal.json` para a proposta corrente antes de registrá-la;
- `.work/slices-existing-children.json` para a paginação sanitizada e descartável das filhas preexistentes;
- `.flow/slices-state.json` para revisões, hashes e aprovações duráveis;
- `.flow/slices-divergence.json` para correções materiais, decisão do tech lead, alinhamentos local/remoto, tentativas e readback;
- `.flow/slices-change-review.json` para a comparação semântica append-only entre o requisito atual e o baseline publicado;
- `.flow/slices-revision-application.json` para o delta autorizado, aprovações por tarefa, tentativas, observações e readback;
- `slices/slices.md` para a prévia humana corrente.
- `slices/condicoes-teste-r<revisão>.docx` para o documento local gerado da fonte estruturada aprovada, preservando revisões anteriores;
- `slices/divergence.md` para a correção exata e o impacto apresentados antes de alinhar o pai;
- `slices/change-review.md` para classificação, impacto localizado e itens que permanecem válidos;
- `slices/revision-application.md` para a prévia concreta das mutações e preservações;
- `.flow/slices-publication.json` para revisão final, aprovação, IDs, tentativas, observações e conclusão da publicação;
- `.flow/slices-condition-revisions.json`, `.flow/condition-evidence/` e `slices/conditions-revision-rNNN.md` para o histórico imutável e as prévias de [revisões localizadas das condições](condition-revisions.md), sem reescrever a publicação original;
- `.flow/slices-reconciliation.json` e `slices/reconciliation.md` para a decisão e a prévia exata de uma materialização local de publicação histórica;
- `.flow/slices-dependencies.json` para revisões, aprovações, operações e readbacks de dependências externas;
- `slices/publication.md` para a prévia final aprovada;
- `tasks/dev-<id>-<slug>/task.md`, `tasks/qa-<id>-<slug>/task.md` e `tasks/study-<id>-<slug>/task.md` para as representações canônicas criadas somente depois do readback integral do respectivo fluxo.

Rejeite links simbólicos em qualquer caminho gravado. Grave candidatos na mesma pasta e substitua atomicamente somente depois de validar. Preserve o estado anterior para executar a validação de transição; revisões e aprovações são append-only.

## Conferência do item pai

O helper aceita estados v2–v5 do `project-flow`, mas a entrada deve ser Feature ou Bug, estar `completed`, conter `redmine.issue_id`, uma aprovação `requirement` válida e nenhuma divergência pendente. O snapshot sanitizado é a resposta estruturada da issue, limitada aos campos públicos necessários pelo verificador (`id`/`issue_id`, `subject`, `description` e, quando presentes, `status`, `status_id` e `relations`). Ele não contém cabeçalhos, credenciais ou configuração do MCP. Exemplo abreviado:

```json
{
  "issue": {
    "id": 123,
    "subject": "[WEB] [OPERACIONAL] Gestão de Usuários",
    "description": "<!-- project-flow:start -->...<!-- project-flow:end -->"
  }
}
```

Quando o Redmine estiver indisponível, valide o documento e o estado locais, inspecione o código e prepare fontes, evidências, condições e candidato somente em `.work`. Não crie `slices-state.json`, aprovação ou artefato que alegue alinhamento remoto. A indisponibilidade é um bloqueio da conferência e da publicação, não da análise local. Preserve o candidato para retomada e identifique a conferência pendente; quando o acesso voltar, obtenha um snapshot novo, rode `check-input` e revise apenas o que a comparação efetivamente invalidar.

Execute:

```sh
python <project-slices>/scripts/manage_slices.py check-input <feature-dir> --remote .work/slices-remote.json --output .flow/slices-input-check.json --at "<ISO-8601>"
```

O agente obtém a projeção remota; o script faz a comparação efetiva de identidade, título e seções funcionais gerenciadas e não chama a API. Conteúdo, atribuição ou delimitadores divergentes bloqueiam a proposta. O validador estrutural não prova legibilidade ou qualidade semântica dos cortes; aplique a disciplina e seus cenários de avaliação antes da aprovação.

Quando existir `.flow/slices-divergence.json`, `check-input`, aprovação e publicação das filhas permanecem bloqueados até o estado `completed`, com correção local atual e readback remoto verificado. Estados `pending`, `rejected`, `approved`, `local-aligned` e `aligning` são retomáveis, mas não autorizam filhas.

## Proposta e aprovação

Crie `.work/slices-proposal.json` conforme `schemas/slices-state.schema.json` e os exemplos de campo em `templates/slices.md`. O objeto da proposta possui `feature`, `inspection`, `requirements`, `slices`, `coverage`, `decisions` e, nas propostas novas, `test_conditions`. Prepare esse campo conforme [condições de teste e DOCX local](test-conditions.md); a revisão persistida é sua fonte estruturada durável. Registre e renderize:

```sh
python <project-slices>/scripts/manage_slices.py record-proposal .flow/slices-state.json .work/slices-proposal.json --input-check .flow/slices-input-check.json --actor "<tech lead>" --at "<ISO-8601>" --reason "<motivo da revisão>"
python <project-slices>/scripts/manage_slices.py render .flow/slices-state.json slices/slices.md
```

`record-proposal` é o primeiro passo que transforma o candidato em revisão durável e exige o `input-check` remoto corrente. Um candidato preparado offline não possui autoridade adicional e não contorna essa conferência.

Para propostas novas, `record-proposal` rejeita qualquer slice acima de seis horas e exige `estimate_exception: null`; o campo existe apenas para leitura de estados históricos. A publicação aplica o mesmo teto à QA, e o ramo de Study aplica o teto à filha excepcional. Estimativas encontradas nas fontes não entram no cálculo nem na evidência passada a agentes estimadores.

Cada execução de `record-proposal` acrescenta uma revisão imutável e invalida a aprovação corrente. Depois da confirmação explícita do tech lead, preserve uma cópia do estado anterior e execute:

```sh
python <project-slices>/scripts/manage_slices.py approve .flow/slices-state.json --actor "<tech lead>" --at "<ISO-8601>"
python <project-slices>/scripts/manage_slices.py validate .flow/slices-state.json --previous <estado-anterior.json>
```

`approve` relê o requisito e o estado aprovados e confere título, identidade e caminhos contra o `input-check`; uma alteração desde a conferência exige novo `check-input` e nova proposta. `technical_context` pode ser omitido ou `null`; inclua texto e renderize a seção somente quando uma decisão aprovada tornar esse contexto necessário.

**Concluído quando:** a revisão aprovada, sua prévia Markdown, o hash e a atribuição sobrevivem em arquivos versionáveis fora de `.work/`, e nenhuma revisão anterior foi alterada.

Gere o DOCX local da revisão aprovada conforme [condições de teste](test-conditions.md). Essa geração não altera a descrição QA nem autoriza publicação do arquivo.

Depois desta aprovação local, siga [publicação DEV e QA](publication.md). O plano e snapshots remotos continuam descartáveis em `.work/`; estado, aprovações e progresso permanecem em `.flow/`, e a prévia fica em `slices/` até a materialização canônica por ID em `tasks/`.

Quando a publicação já foi concluída por um contrato histórico v1, siga [reconciliação local](legacy-reconciliation.md) em vez de preparar ou repetir operações remotas.

## Estado operacional e retomada

Os helpers persistem e validam o progresso local; mantenha essa manuten??o interna. Registre decis?es de produto e suas fontes uma vez, sem copiar toda a conversa. No escopo, novos estados omitem `awaiting_decision_for`, `continuation_decisions` e `resumes`; registros hist?ricos continuam leg?veis e preservados. `resume` reconcilia o progresso e seleciona o primeiro item eleg?vel sem nova confirma??o de continuidade. Pausas e impedimentos preservam a raz?o necess?ria para retomar. IDs, revis?es de conte?do, opera??es incertas e evid?ncias de publica??o continuam dur?veis; retomar n?o autoriza repetir muta??es remotas.

**Conclu?do quando:** o helper valida o estado persistido, preserva as publica??es verificadas e seleciona o pr?ximo item eleg?vel ou mant?m o impedimento real.
