# [DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria

- Redmine: `#1015930`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015911`
- Estimativa: `3h`

## Descrição

## Entrega

Permitir cadastrar receita ou despesa e conferir imediatamente os campos lidos do registro persistido. O titular pode guardar o endereço dessa consulta individual, sair, entrar novamente e reabrir o mesmo registro para confirmar sua persistência.

## Escopo e limites

Não entrega a descoberta do conjunto, histórico, filtros nem botões de edição/exclusão. A leitura individual é a mesma que o histórico reutilizará; não criar uma segunda tela de detalhes. Receitas e despesas permanecem juntas por compartilharem campos, validação e leitura.

## Critérios de aceite

- Tipo receita/despesa, valor positivo em reais, descrição, categoria e data são obrigatórios; tipo determina entrada ou saída.
- Valor entre R$ 0,01 e R$ 999.999.999,99 com até duas casas; não arredondar entrada com precisão maior. Descrição entre 1 e 120 caracteres após aparar extremidades. Data válida de 01/01/1900 a 31/12/9999.
- Oferecer somente receitas: Salário, Freelance, Rendimentos, Outras receitas; despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas. Sem manutenção de categorias.
- Vincular cadastro ao usuário autenticado com e-mail confirmado, sem aceitar outro proprietário; persistência permanece após sair e entrar.
- R10 e dados percebidos, consulta individual: conferir descrição, tipo, valor em reais com centavos, categoria e data brasileira do registro persistido, inclusive ao reabrir após novo login.
- Salvar receita/despesa válida cria um registro próprio, mostra sucesso e mantém dados após novo acesso.
- Ausências, categoria incompatível, valores/datas fora de R2 e descrição vazia/longa impedem salvar, mostram erros e preservam o formulário.
- CA7, consulta individual: titular habilitado consulta todos os campos do próprio registro; identificador de outra conta não revela seus dados.
- CA9: cancelar cadastro não modifica registros nem totais.
- CA10: falha ao cadastrar não grava parcialmente nem mostra sucesso; orienta nova tentativa.
- CA10: registro indisponível não revela dados de terceiros e a interface informa indisponibilidade.
- CA12: duas operações distintas com dados iguais podem criar duas transações, sem deduplicação automática.
- Categorias disponíveis correspondem exatamente a R3; trocar tipo não mantém categoria incompatível silenciosamente nem permite concluir com ela.
- Depois de salvar, a consulta individual mostra valores lidos da persistência, não apenas dados retidos no formulário. Ao sair, entrar e reabrir o endereço do registro, os mesmos campos continuam disponíveis ao titular.

## Dependências

Para iniciar: autenticação e confirmação de e-mail existentes. Para concluir este corte: cadastro válido, consulta individual autorizada e reabertura após novo login, sem depender do histórico completo.

## Referências

Item pai Redmine #1015911; regras/critérios R1, R2, R3, R4, R10-campos, CA1, CA2, CA7-consulta, CA9-cadastro, CA10-cadastro, CA10-consulta, CA12-cadastro, CA11.

<!-- project-slices-child:0c1705409538d39dfa727aaed478a66c7a8005dba7a60dd1622164eefd66e5f7 -->

## Relações

- `#1015930` blocks `#1015931`
- `#1015930` blocks `#1015933`
- `#1015930` blocks `#1015934`
- `#1015930` blocks `#1015935`
- `#1015930` blocks `#1015936`
