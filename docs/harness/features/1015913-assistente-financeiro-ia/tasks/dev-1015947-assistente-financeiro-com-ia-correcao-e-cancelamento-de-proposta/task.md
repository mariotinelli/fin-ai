# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Correção e cancelamento de proposta

- Redmine: `#1015947`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015913`
- Estimativa: `3h`

## Descrição

## Entrega

Permitir corrigir todos os campos ou cancelar a preparação atual, preservando o histórico e tornando confirmações anteriores inválidas.

## Escopo e limites

Correção salva proposta, não movimentação. Cancelamento não exclui transações; não inclui edição de mensagens ou de registros já salvos.

## Critérios de aceite

- Corrigir todos os campos atualiza proposta, exige nova revisão e invalida confirmação antiga; cancelar não grava e registra cancelamento; ‘sim’ escrito não grava e orienta botão atual.
- Correção de tipo/valor/descrição/categoria/data mantém limites deR2/R3: R$0,01..999.999.999,99 até2 casas, descrição1..120 aparada, data1900..9999, categoria predefinida compatível; erro não cria transação.
- Cancelar descarta preparação sem excluir transações salvas; resultado fica na conversa e permite iniciar novo registro.

## Dependências

Para iniciar: ‘Assistente financeiro com IA - Preparação e retomada de proposta’. Para concluir: correção/cancelamento persistidos e contrato de versão integrado com ‘Assistente financeiro com IA - Confirmação única e reconciliação’, provando que ação antiga não grava.

## Referências

Item pai Redmine #1015913; regras/critérios CA4, F-correcao-validacao, F-cancelamento.

<!-- project-slices-child:f4dea2c9bb57abe8a39f1d648a600315d20d3f916de75b0772b1df72f6ccf935 -->

## Relações

- `#1015946` blocks `#1015947`
- `#1015947` blocks `#1015949`
