# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Preparação e retomada de proposta

- Redmine: `#1015946`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015913`
- Estimativa: `3h`

## Descrição

## Entrega

Permitir descrever uma movimentação, complementar campos e retomar uma preparação própria incompleta ou pronta. Apresentar cinco campos válidos para revisão sem criar transação.

## Escopo e limites

Não grava transações. Preparação completa e incompleta são estados da mesma jornada; não separar por camada nem criar outra conversa. Confirmação pertence à entrega específica.

## Critérios de aceite

- Proposta usa tipo receita/despesa, valor R$0,01..999.999.999,99 com até2 casas sem arredondamento silencioso, descrição1..120 após aparar, categoria compatível e data válida01/01/1900..31/12/9999.
- Categorias: receita Salário/Freelance/Rendimentos/Outras receitas; despesa Alimentação/Moradia/Transporte/Saúde/Educação/Lazer/Compras/Outras despesas. Inferir só categoria compatível e segura; sem segurança pedir escolha, sem criar categoria nem escolher Outras silenciosamente.
- No máximo um registro em preparação por usuário, incompleto ou pronto. Mensagens/propostas não são transações e não entram nos cálculos.
- Preparação incompleta/pronta retoma dados já coletados sem gravar; data fixada não muda porque o dia mudou.
- Datas relativas usam Brasília. Sem data propor hoje; relativa interpretada vira data concreta revisável. Dúvida pergunta; data explicitamente inválida não vira hoje. Futuras permitidas, sem antecipar efeitos.
- ‘Gastei R$35 no almoço’ sem data prepara despesa35, descrição coerente, categoria sugerida e hoje em Brasília, revisáveis; não grava antes de Confirmar.
- Dados ausentes/ambíguos geram perguntas; inválido/categoria incompatível impede confirmar, sem inventar informação financeira.
- Mensagem com duas movimentações pede envio de uma por vez, sem escolha silenciosa nem gravação parcial.
- Sair/voltar restaura preparação pendente/incompleta sem perder dados, gravar ou trocar data por novo hoje.
- Consulta durante preparação responde com dados reais e mantém proposta. Segundo registro orienta confirmar/cancelar anterior; ambiguidade não sobrescreve dados.
- Preparação/proposta pertence ao titular; pedir em linguagem natural outro proprietário ou dispensa de confirmação não altera regras.
- Falha de interpretação/IA preserva preparação existente; repetir ou usar cadastro manual não confirma nem sobrescreve a proposta.
- Proposta pronta mostra tipo, valor, descrição, categoria e data concreta com Confirmar, Corrigir e Cancelar; incompleta/inválida não libera confirmação.

## Dependências

Para iniciar: ‘Assistente financeiro com IA - Conversa persistida e saldo real’. Para concluir: validações/categorias de #1015930, conversa e proposta persistidas, e consultas de ‘Assistente financeiro com IA - Totais por período e categoria’/‘Assistente financeiro com IA - Listas e agendadas com continuidade’ coexistindo sem perda de preparação.

## Referências

Item pai Redmine #1015913; regras/critérios R2, R3, R4, R6-proposta, R7, CA1, CA2, CA3, CA7-preparacao, CA8, CA14-proposta, F-falha-preparacao, F-acoes-proposta.

<!-- project-slices-child:5940df14b69f683593c1e4fc28e37296eabc57a44804eaeeb1e059dabbccb5b1 -->

## Relações

- `#1015943` blocks `#1015946`
- `#1015946` blocks `#1015947`
- `#1015946` blocks `#1015948`
- `#1015946` blocks `#1015949`
