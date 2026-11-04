# Planejamento novo

Use este caminho quando a filha DEV identificada não possui `planning.md`, originalmente ou após a [substituição autorizada](replace-planning.md). O planejamento pertence a `plan-issue`; a continuidade, a preparação do plano aprovado no Git e a chamada do executor pertencem a `ralph`.

## 1. Delegar preservando o trabalho existente

Antes de delegar, observe o estado Git do projeto: mudanças preparadas, não preparadas e arquivos não rastreados. Leia o diff de um `.gitignore` já alterado na pasta da filha, se existir. Mantenha essa observação na conversa para distinguir mudanças preexistentes das produzidas pelo planejamento; não crie estado ou manifesto para isso.

Ao chegar pela substituição, mantenha também a observação feita antes da remoção: a exclusão autorizada do plano é parte desse fluxo, não uma alteração alheia. O plano substituto deve considerar o código atual, preservando a implementação existente.

Leia e aplique [plan-issue](../../plan-issue/SKILL.md) para o ID da filha. Resolva a referência a partir deste pacote instalado. Se a dependência estiver ausente, informe o problema de instalação e pare.

Deixe a skill delegada conduzir a inspeção do projeto e do pai, o baseline, a escrita e a revisão do plano. Não reproduza seu procedimento nem implemente código da tarefa. O uso independente de `plan-issue` permanece igual; quando chamado por `ralph`, a entrega do comando ao final devolve o controle a este fluxo, em vez de encerrar a conversa.

**Concluído quando:** o fluxo de planejamento produziu o plano completo da filha, com seus ajustes de ignore previstos, ou explicou um impedimento sem iniciar o executor.

## 2. Revisar e aprovar

Garanta que o desenvolvedor recebeu o plano completo e incorpore os ajustes solicitados pelo fluxo delegado. Aguarde aprovação explícita da versão final. Informe que a aprovação permite commitar os arquivos do planejamento com `--no-verify`, quando houver diferenças, e iniciar o Ralph na mesma conversa.

Reutilize a aprovação já obtida durante `plan-issue` para esse conteúdo; não peça a mesma confirmação novamente. Se o conteúdo mudar depois da aprovação, apresente a mudança e aguarde aprovação do resultado antes de continuar. Não registre aprovação, hash ou readback em arquivos adicionais.

**Concluído quando:** o conteúdo final foi apresentado e aprovado pelo desenvolvedor. Sem aprovação, não faça commit nem execute.

## 3. Commitar somente o planejamento

Compare o estado Git atual com a observação anterior e inspecione os diffs. Os únicos candidatos a este commit são o `planning.md` da filha e o ajuste necessário de seu `.gitignore`, quando produzido pelo planejamento. A autorização cobre esse conteúdo, não todos os arquivos da pasta.

Se houver alterações alheias, inclusive código, arquivos não rastreados ou conteúdo já preparado no índice, informe os caminhos e aguarde o desenvolvedor resolver o impedimento. Preserve arquivos e índice; não use stash, descarte mudanças ou faça um commit adicional para limpar o projeto. Se o mesmo `.gitignore` contiver mudanças preexistentes alheias, não inclua o arquivo inteiro nem tente separá-las automaticamente. Depois da resolução, confira novamente o plano aprovado e o estado Git.

Com apenas o conteúdo autorizado pendente, prepare explicitamente os caminhos pertinentes e confira o diff do índice antes de commitar. Use caminhos relativos ao repositório, argumentos protegidos para o shell e pathspecs literais; não use seleção global ou da pasta inteira.

Se o plano aprovado e o `.gitignore` pertinente já estiverem versionados e idênticos ao `HEAD`, com índice e worktree sem alterações pendentes, informe que não há diferenças para commitar e siga para a execução. Não crie commit vazio. Confirme o conteúdo no Git: a ausência de diff sozinha não comprova que um arquivo ignorado ou não rastreado esteja versionado.

Sequência de referência, substituindo os marcadores pelos caminhos revisados e omitindo o `.gitignore` se não precisar entrar no commit:

```sh
git --literal-pathspecs add -- <planning.md> <.gitignore-se-alterado>
git diff --cached --name-only
git diff --cached
git --literal-pathspecs commit --no-verify --only -m "docs: plan DEV <id>" -- <planning.md> <.gitignore-se-alterado>
```

O diff preparado deve conter somente o planejamento aprovado e o ajuste pertinente de ignore. Se aparecer conteúdo alheio ou o plano tiver mudado, pare antes do commit. O commit limitado aos caminhos é uma proteção adicional; não autoriza ignorar alterações alheias encontradas.

Em falha do commit, explique o erro e aguarde orientação. Não altere configurações do Git, identidade ou hooks para contorná-lo e não chame o executor. Em sucesso, confira os arquivos e o diff do commit e o estado atual do projeto; se ainda houver alterações pendentes, informe o impedimento antes de iniciar. Não faça push.

**Concluído quando:** o plano aprovado e seu ajuste de ignore estão versionados por um commit limitado bem-sucedido ou já eram idênticos ao `HEAD`, e o projeto não tem alterações pendentes que impeçam o início.

## 4. Continuar na mesma conversa

Retorne à etapa de execução da skill `ralph` e chame o executor existente para esse plano, sem outra chamada de skill ou confirmação. Reutilize o acompanhamento e o tratamento de interrupções existentes.

Este caminho não gera nem remove estado de retomada. Se houver um estado antigo ou outro impedimento, não o apague para forçar o início: preserve-o e informe a situação. A checagem de alterações deste planejamento novo não se aplica ao caminho separado de retomada de plano existente.

**Concluído quando:** o plano aprovado e preparado no Git foi encaminhado uma única vez à execução acompanhada, ou o impedimento foi informado sem iniciar o processo.
