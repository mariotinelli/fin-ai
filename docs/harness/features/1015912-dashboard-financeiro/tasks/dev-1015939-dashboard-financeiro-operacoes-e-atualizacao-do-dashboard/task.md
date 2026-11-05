# [DEV] [WEB] [USUARIO] Dashboard financeiro - Operações e atualização do dashboard

- Redmine: `#1015939`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015912`
- Estimativa: `1.5h`

## Descrição

## Entrega

Conectar cadastro e histórico existentes ao dashboard e atualizar os indicadores e recentes após operações concluídas ou retorno, preservando valores ao cancelar ou falhar.

## Escopo e limites

Não reimplementa cadastro, edição, exclusão ou histórico. Sem atualização contínua da tela ociosa nem sincronização instantânea entre dispositivos.

## Critérios de aceite

- Duplicados permitidos contam individualmente; edição/exclusão recalculam indicadores e podem mudar recentes.
- Ao retornar de outras áreas e após alteração concluída no dashboard consultar valores atuais. Tela ociosa na virada só precisa atualizar ao ser consultada novamente; não exige polling nem sincronização instantânea entre dispositivos.
- Futuras não entram em indicadores/recentes antes da data; próxima consulta após início da data em Brasília inclui automaticamente, sem confirmar pagamento/recebimento.
- Nova transação reutiliza cadastro; Ver todas abre histórico integral, sem transportar filtro mensal que contradiga recentes globais.
- Cadastro/edição/exclusão concluídos a partir do dashboard atualizam números/recentes sem recarga manual; cancelar conserva valores; retornar de outras áreas consulta dados atuais.
- Fluxos alternativos: só refletir alterações efetivamente persistidas; cancelamento ou falha das operações não gera alteração financeira falsa.

## Dependências

Para iniciar: ‘Dashboard financeiro - Indicadores e consulta por mês’ e ‘Dashboard financeiro - Movimentações recentes e detalhes’ fornecem os blocos a conectar. Para concluir: integrar ‘[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria (#1015930)’, ‘[DEV] [WEB] [USUARIO] Gestão de transações - Histórico por período (#1015931)’, ‘[DEV] [WEB] [USUARIO] Gestão de transações - Edição de transação com efeitos financeiros (#1015934)’ e ‘[DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada com efeito único (#1015935)’, com os cálculos de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira (#1015933)’. Operações reais e seus efeitos devem estar verificados; navegação isolada não conclui.

## Referências

Item pai Redmine #1015912; regras/critérios R5, R7-retorno, CA4, CA7-atalhos, CA8, F-persistencia.

<!-- project-slices-child:85ff1eb34d7c936fc3d8273754e6f5adfd026391a6e043c0e0071e22afa996fb -->

## Relações

- `#1015937` blocks `#1015939`
- `#1015938` blocks `#1015939`
- `#1015939` blocks `#1015940`
