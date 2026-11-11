# Histórico da entrevista — Dashboard financeiro

## Contexto herdado e passagem de contexto

Item 4: [WEB] [USUARIO] Dashboard financeiro. Titular autenticado e confirmado visualiza saldo geral, receitas/despesas do mês, balanço simples, resultado mensal e movimentações recentes. Dependência direta: transações #1016105; acesso #1016104 e base visual #1016101 são transitivos. Requisitos publicados, sem presumir implementação. Assistente é consumidor independente das transações e não bloqueia este requisito.

## Reconciliação funcional da referência

Scope §§3.1 e 4 pede números reais refletindo os registros. Design #overview e render definem saldo geral como receitas de todo o histórico menos despesas de todo o histórico, totais/contagens do mês selecionado e resultado do mês como a diferença desses totais. Gráfico compara duas barras de receitas/despesas, não uma evolução temporal. Recentes são os cinco registros mais recentes por data, com desempate pelo cadastro, em todo o histórico; não mudam com o seletor de mês.

Reutilizar decisões anteriores: contas separadas e confirmação obrigatória; registros realizados até hoje; moeda real; categorias aprovadas; claro/escuro/sistema. Não usar tasks antigas. Não introduzir saldo inicial manual, múltiplas contas ou dados simulados. Essas propostas explícitas serão confirmadas na revisão integral, não presumidas como decisões novas do usuário.

## Aplicação de requirements-grilling

Fontes e decisões anteriores já determinam as regras centrais de cálculo, períodos, limites e fluxos. Não há pergunta material que exija outra rodada antes da revisão. A entrevista proporcional segue diretamente para proposta do requisito completo. Aceite deve distinguir dados vazios de indisponibilidade, zeros de saldo negativo, meses sem movimento, atualização após manutenção e isolamento entre titulares.

O convite visual para o assistente pertence ao design; a ação só é utilizável quando a Feature do assistente estiver disponível, sem antecipar chat/IA ou afirmar entrega. Antes disso, a ação permanece indisponível. A manutenção financeira reutiliza a Feature de transações, sem duplicar operações. As regras serão apresentadas na prévia final para aprovação.


## Prévia pronta para revisão

Requisito integral e plano reproduzidos e comparados com todas as seções da criação/publicação. A prévia inclui cálculos, recortes, estados, visual e as três operações com relação transacoes-blocks-dashboard. Estado validado; aguardando aprovação única. Nenhuma mutação remota executada neste item.


## Aprovação e publicação concluídas

O usuário aprovou a prévia integral. Consentimento único registrado para requisito e plano, com criação, publicação e relação transacoes-blocks-dashboard. Criada #1016106, Sprint 1, Sequencing 4, estado New preservado. Conteúdo integral conferido pelo checker funcional; relação 837 (#1016105 blocks #1016106) confirmada em ambos os extremos. Requisito concluído não significa implementação concluída. Baseline de comparação normaliza apenas CRLF/LF no conteúdo funcional, preservando a resposta original.
