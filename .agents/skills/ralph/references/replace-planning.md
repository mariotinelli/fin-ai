# Substituição de planejamento

Use somente após o desenvolvedor escolher substituir o plano identificado, sabendo que o plano e seu estado de retomada serão removidos. Essa escolha autoriza a remoção específica; a aprovação do conteúdo novo acontece depois.

## 1. Conferir antes de remover

Confira o estado Git completo, incluindo alterações preparadas, não preparadas e arquivos não rastreados. Qualquer alteração pendente, inclusive no plano antigo ou em seu `.gitignore`, impede a substituição. Informe os caminhos e aguarde o desenvolvedor resolver, preservando arquivos e índice. Não faça stash, descarte ou commit de limpeza. Depois da resolução, confira novamente antes de remover.

Confirme a disponibilidade de [plan-issue](../../plan-issue/SKILL.md) e do executor instalado. Resolva os caminhos exatos de `planning.md` e de `.flow/ralph-state.json` dentro da pasta da filha escolhida. Preserve destinos ambíguos, diretórios no lugar dos arquivos e links ou componentes de caminho que redirecionem para fora da tarefa; informe o impedimento.

Confira se há execução ativa para essa tarefa, usando o processo acompanhado e, quando necessário, os registros existentes de `ralph-locks` no diretório administrativo obtido pelo Git. O `owner.json` identifica `state_path` e o processo proprietário; consulte o contrato instalado do executor quando precisar interpretar esses registros. Se uma execução estiver ativa ou não for possível determinar se terminou, pare antes da remoção. Preserve processos e locks; não use uma nova chamada ao executor para sondar a atividade.

**Concluído quando:** a escolha está autorizada, o Git está sem alterações pendentes, dependências e destinos foram conferidos e não há execução ativa ou situação indeterminada para a tarefa.

## 2. Remover apenas os dois arquivos escolhidos

Mantenha na conversa a observação do Git anterior à remoção e os caminhos autorizados. Remova somente `planning.md` e, quando existir, `.flow/ralph-state.json` dessa filha. Use caminhos literais protegidos para o shell; no PowerShell, operações com `-LiteralPath`. Não faça remoção recursiva de diretórios.

Preserve a pasta `.flow`, seus demais arquivos, tarefas vizinhas, logs em `ralph-runtime`, locks, código e histórico Git. A ausência do estado é válida. Verifique que os dois arquivos escolhidos ficaram ausentes. Se qualquer operação falhar, informe quais remoções ocorreram e pare; não amplie a limpeza, restaure progresso antigo automaticamente ou inicie o executor.

**Concluído quando:** apenas o plano e seu estado correspondente foram removidos, com o restante preservado, ou uma falha foi informada sem continuar.

## 3. Planejar a partir do projeto atual

Siga [planejamento novo](new-planning.md), levando a observação anterior à remoção e identificando a exclusão do plano como parte autorizada da substituição. Deixe `plan-issue` inspecionar o código, o requisito e os testes atuais; não reaproveite a lista de fases concluídas do plano descartado.

Reutilize desse fluxo a apresentação completa, os ajustes, a aprovação explícita, o commit limitado com `--no-verify` quando houver diferenças e a execução acompanhada. Quando o conteúdo aprovado já estiver versionado sem diferenças, prossiga sem commit vazio. A escolha inicial de substituir não aprova antecipadamente o novo plano.

Se o planejamento falhar ou o estado antigo reaparecer, informe a situação e pare. Não restaure nem reutilize o progresso descartado. O executor criará seu estado mínimo ao iniciar o plano aprovado.

**Concluído quando:** o novo plano passou pela revisão e preparação do fluxo compartilhado e foi encaminhado uma única vez à execução, ou o impedimento foi informado sem executá-lo.
