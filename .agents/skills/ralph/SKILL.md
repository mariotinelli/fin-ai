---
name: ralph
description: Planeja e executa pelo Ralph uma filha DEV identificada pelo ID do Redmine. Use para iniciar, retomar ou substituir seu planejamento; delega planos novos a plan-issue e aguarda aprovação antes de executar.
---

# Ralph

Conduza a execução de um `planning.md` pelo `ralph.sh` instalado com `plan-issue`. O script implementa as fases; esta skill identifica a tarefa, delega o planejamento quando ausente, recebe a aprovação ou escolha de executar e acompanha o processo. Use somente os artefatos locais, sem consultar ou alterar Redmine ou YouTrack. O usuário também pode usar `plan-issue` independentemente.

## 1. Identificar a filha e o plano

Receba o ID da filha no Redmine. Se o usuário não informou o código, peça-o e aguarde; título, caminho e ID do pai não o substituem.

Na raiz do projeto, leia as instruções aplicáveis e localize exatamente um `tasks/dev-<id>-<slug>/task.md` sob `docs/harness/features` ou `docs/harness/bugs`. Confira o ID no documento e verifique se existe `planning.md` na mesma pasta. QA e Study não são elegíveis.

Quando não houver uma correspondência inequívoca ou a identidade divergir, informe os arquivos encontrados e o impedimento, sem escolher outra tarefa. Se o plano existir, leia-o e siga para a etapa 2. Se estiver ausente, siga [planejamento novo](references/new-planning.md) até sua aprovação e preparação no Git antes de retornar à etapa 2.

**Concluído quando:** uma filha DEV foi identificada e seu plano existente foi lido ou seu plano novo foi aprovado e preparado no Git, ou o impedimento foi explicado e o fluxo parou.

## 2. Apresentar e executar

Para um plano que já existia ao entrar no fluxo, mostre ID, título completo da filha e caminho do planejamento e ofereça:

- **Executar:** mantém o plano e a retomada existentes e chama o Ralph.
- **Substituir:** remove somente esse plano e seu estado de retomada e gera outro considerando o projeto atual; preserva código, commits e logs. O novo conteúdo será apresentado para aprovação antes de executar.

A escolha de executar autoriza a chamada do script sem confirmação adicional. Se essa escolha já foi feita nesta conversa para o mesmo plano apresentado, prossiga. Escolher substituir autoriza a remoção específica explicada na opção: siga [substituição de planejamento](references/replace-planning.md). Para um plano novo ou substituto aprovado e preparado no Git pelo fluxo compartilhado, continue diretamente para o comando abaixo, sem reapresentar as opções: a aprovação já autoriza a execução na mesma conversa.

Resolva `../plan-issue/ralph.sh` a partir da localização desta skill instalada, não a partir do diretório corrente. Leia [a referência do executor](../plan-issue/references/ralph-execution.md) para seu contrato de execução e retomada. Se a dependência estiver ausente, informe o problema de instalação e pare.

Use os caminhos reais e proteja cada argumento conforme o shell em uso:

```sh
bash <plan-issue>/ralph.sh execute <pasta-dev>/planning.md
```

Execute na raiz do projeto com as ferramentas do agente que permitem obter saída incremental e continuar acompanhando o mesmo processo. Preserve as opções padrão do executor; encaminhe opções suportadas apenas quando solicitadas pelo usuário. Os agentes da sessão podem ser Codex, Claude Code ou OpenCode; o backend do executor continua sendo o configurado nele.

Deixe o script decidir se é possível iniciar ou retomar. Não imponha uma checagem de worktree limpa que impeça retomar uma fase com mudanças. Não edite o plano, o estado, o código ou a configuração para contornar uma recusa do executor.

**Concluído quando:** o script foi chamado uma única vez para o plano escolhido e o processo está disponível para acompanhamento, ou a falha ao iniciar foi explicada.

## 3. Acompanhar até terminar

Conserve o identificador da execução e acompanhe esse mesmo processo até obter seu resultado. Esperas curtas, de no máximo 60 segundos, devem permitir feedback contínuo ao usuário.

Comunique mudanças observadas em mensagens curtas, com **fase**, nome da etapa e **resultado** destacados. Prefira os nomes Desenvolvimento, Validação, Testes e Commit; mantenha o número do gate como referência secundária. Use o total de fases e o título do plano quando conhecidos. O Gate 1 termina como **finalizado**, não como aprovado. Preserve a diferença entre reprovação interna seguida de nova tentativa pelo script e interrupção do processo.

Exemplos de apresentação, preenchidos somente com fatos observados:

- **Fase 1 de 2 — Política de senha** · **Desenvolvimento em andamento** (Gate 1).
- **Fase 1 de 2** · **Validação aprovada**. Iniciando os testes (Gate 3).
- **Fase 1 de 2 concluída** — testes aprovados e commit criado. **Próxima: Fase 2 de 2 — Desenvolvimento**.
- **Fase 2 de 2** · **Testes reprovados — tentativa 2 de 3**. O executor iniciou a correção nesta mesma fase.

Cada atualização deve conter apenas o avanço novo. Não reproduza uma lista crescente de mensagens anteriores nem envie uma mensagem por consulta ao processo. Sem novidade, mantenha o acompanhamento e, quando for necessário atualizar o usuário, use uma única linha: **Fase 2 de 2 · Desenvolvimento** — sem nova saída desde a última atualização. Respeite a frequência de comunicação exigida pelo ambiente; evite variações repetidas da mesma frase. Ausência de saída não comprova atividade ou travamento: não invente progresso, percentual ou horário.

Ao mudar de fase, anuncie explicitamente a conclusão da anterior e o início da próxima, para não parecer retorno ao Gate 1 da mesma fase. Horários e identificadores de commit entram somente quando disponíveis e úteis; não use blocos de código para status em prosa.

Mantenha as conversas internas, prompts e logs extensos fora do acompanhamento. Não use `--verbose` por padrão nem abra outro processo Ralph para verificar progresso. Se a ferramenta deixar de permitir acompanhamento, informe a limitação sem declarar conclusão, reiniciar ou encerrar um processo que possa continuar ativo.

**Concluído quando:** o processo terminou com resultado observado e o usuário recebeu o resumo, ou uma perda de acompanhamento foi informada explicitamente.

## 4. Informar o resultado

Em sucesso, informe a conclusão observada e os resultados disponíveis, incluindo a orientação do executor para revisar as mudanças. Fases já concluídas permanecem sob o controle da retomada existente.

Comece por **Tarefa #ID concluída** ou **Tarefa #ID interrompida**, conforme observado. Resuma fases concluídas e verificações relevantes; em interrupção, destaque **fase e etapa**, causa e próximo passo. Prefira parágrafos curtos ou poucos itens a um histórico de polling.

Em interrupção, leia o diagnóstico apontado pelo script, resuma a causa comprovada e indique como retomar a mesma tarefa. Se não houver diagnóstico ou causa conclusiva, diga isso. Mostre apenas os trechos necessários e sanitizados, preservando segredos e conversas internas.

Após a interrupção, aguarde a orientação do usuário para corrigir ou executar novamente. Não remova estado, desfaça commits nem reinicie por conta própria. As tentativas internas e os commits por fase pertencem exclusivamente ao script.

**Concluído quando:** o usuário conhece o resultado e, em caso de interrupção, o diagnóstico disponível e o próximo passo, sem execução adicional não solicitada.
