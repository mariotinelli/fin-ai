---
name: plan-issue
description: Planeja tecnicamente uma tarefa filha DEV em fases executáveis e gera o único planning.md consumido pelo Ralph. Use quando um desenvolvedor pedir o planejamento de uma filha; não use para implementar as fases.
---

# Plan issue

Transforme uma filha DEV em um `planning.md` claro para humanos e executável pelo Ralph. Use `task.md` e o requisito pai como fontes de produto, inspecione o repositório para fatos técnicos e nunca leia ou altere o Redmine.

## 1. Localizar a tarefa

Receba o ID da filha DEV e localize exatamente um `tasks/dev-<id>-<slug>/task.md` em `docs/harness/features` ou `docs/harness/bugs`. Leia também `feature.md` ou `bug.md` do pai. Study e QA não entram neste fluxo.

Leia as instruções aplicáveis do repositório, arquitetura, ADRs, convenções, automações, implementação relacionada e testes existentes. Antes de descrever estado atual, arquitetura e riscos, aplique [inspeção técnica](references/technical-inspection.md). Descubra o comando agregado e seus verificadores pela configuração real, sem inferir seu conteúdo pelo nome.

**Concluído quando:** tarefa, requisito pai, padrões e verificadores foram compreendidos, e as afirmações que sustentam decisões possuem evidências localizáveis.

## 2. Observar o baseline

Confira runtime, ferramentas e pré-requisitos do comando antes da execução. Use um runtime compatível disponível pelo mecanismo do projeto ou seleção local ao processo, sem alterar configuração global ou requisitos. A seleção precisa funcionar também no ambiente do Ralph, não apenas em um alias da sessão atual.

Execute a suíte completa uma vez, sem alterar arquivos versionados. Confira primeiro se os scripts fazem correções: use o modo de verificação equivalente previsto pelo projeto; se não existir, registre o impedimento em vez de executar mutações silenciosas. Leia [o contrato do planejamento](references/planning-contract.md) para registrar comando, composição do gate e resultados por verificador.

Se o ambiente impedir a execução, identifique a preparação necessária e as etapas não executadas. Isso não demonstra falha funcional da aplicação. O baseline observado não autoriza falhas no gate de testes e não possui aprovação, hash ou estado separado.

**Concluído quando:** o comando reproduzível, os pré-requisitos e os resultados observados estão descritos no `planning.md`, distinguindo falhas de etapas não executadas e impedimentos de ambiente.

## 3. Escrever o planejamento

Leia [o contrato do planejamento](references/planning-contract.md) e crie somente `<pasta-dev>/planning.md`. Garanta que `<pasta-dev>/.gitignore` contenha `/.flow/`; adicione essa linha se estiver ausente. A pasta `.flow` guarda somente a retomada local do Ralph.

Divida o trabalho em fases pequenas e sequenciais. Cada fase deve caber em uma sessão nova, produzir uma mudança verificável e terminar em condição de commit. Escreva para um desenvolvedor humano: explique comportamento, arquivos prováveis, limites, aceite e verificação, sem transformar o plano em uma sequência mecânica de comandos.

Confira a correspondência entre requisitos, mudanças e evidências de aceite conforme o contrato. Uma tarefa localizada pode ter uma única fase; evite repetir a mesma explicação em objetivo, estratégia e mudanças esperadas.

Apresente o plano completo ao desenvolvedor e incorpore os ajustes pedidos. O desenvolvedor decide quando commitar o planejamento.

**Concluído quando:** o desenvolvedor revisou o conteúdo, existe exatamente um `planning.md` e todas as fases possuem aceite observável.

## 4. Entregar ao Ralph

Leia [a execução do Ralph](references/ralph-execution.md). Se ainda não foi possível determinar o comando seguro completo do baseline, entregue apenas o rascunho impedido e a informação faltante; não encaminhe esse rascunho ao Ralph. Caso contrário, entregue o comando abaixo com o caminho real:

```sh
bash <plan-issue>/ralph.sh execute <pasta-dev>/planning.md
```

Não gere estado, manifesto, readback, aprovação ou hash. O Ralph cria seu estado mínimo automaticamente quando começar. Se houver impedimento operacional pendente, entregue o plano com a preparação necessária e apresente o comando como condicionado à resolução, sem anunciar prontidão para execução.

**Concluído quando:** o comando simples foi informado e nenhum código da tarefa foi implementado.

Ao avaliar a skill ou construir regressões semânticas, use [cenários de avaliação](references/evaluation-scenarios.json). Eles avaliam decisões do planejador, não comprovam execução do produto.
