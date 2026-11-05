# [DEV] [WEB] [USUARIO] Dashboard financeiro - Movimentações recentes e detalhes

- Redmine: `#1015938`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015912`
- Estimativa: `1.5h`

## Descrição

## Entrega

Apresentar as cinco movimentações elegíveis mais recentes do titular, independentemente do mês dos indicadores, com abertura da consulta individual existente.

## Escopo e limites

Não cria outra tela de detalhes nem usa o mês selecionado para restringir a lista. Operações e retorno integrado pertencem à entrega específica.

## Critérios de aceite

- Recentes usa todo histórico elegível, independente do mês, data decrescente e cadastro mais recente em empate, limite5; com menos5 exibe todos e futuras só entram na data.
- Identificar que recentes considera todo histórico até hoje; listar descrição, tipo, valor, categoria e data, com campos completos nos detalhes se layout compacto reduzir a lista.
- Mostrar cinco elegíveis mais recentes por data/cadastro ou todos se menos5, incluindo outros meses.
- Sem elegíveis recentes fica vazio; só futuras não preenche recentes com agendadas e informa consulta pelo histórico.
- Abrir detalhes reutiliza a consulta de Gestão de transações, sem construir leitura duplicada.
- Lista mostra carregamento/indisponibilidade e nova tentativa quando sua leitura falha; não confundir falha com lista realmente vazia.
- Recentes/detalhes não revelam registros alheios; transação removida antes de abrir informa indisponibilidade e permite atualizar a lista.

## Dependências

Para iniciar: layout e contrato funcional aprovados permitem preparar lista e casos de teste. Para concluir: integrar registros/leitura individual de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria (#1015930)’ e elegibilidade de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira (#1015933)’; lista e detalhe devem usar dados reais, sem implementar essas capacidades novamente.

## Referências

Item pai Redmine #1015912; regras/critérios R4, R8-recentes, CA5, CA6-recentes, CA7-detalhes, CA9-recentes, CA10-recentes.

<!-- project-slices-child:581857ee0b7442f1d5cf5e4d402d194495ee2d791c6972678eaccc9b8556822e -->

## Relações

- `#1015938` blocks `#1015939`
- `#1015938` blocks `#1015940`
