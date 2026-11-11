# Histórico da entrevista — Gestão de transações

## Contexto herdado do catálogo aprovado

Item 3: [WEB] [USUARIO] Gestão de transações. Titular confirmado cadastra receitas/despesas, consulta detalhes/histórico, edita e exclui, usando categorias predefinidas. Registros persistidos no sistema, isolados por titular. Inclui formulário, filtros e histórico do design. Não inclui totais do dashboard nem chat/IA; essas Features consomem os registros depois.

Dependência direta: acesso à conta pessoal #1016104; base visual #1016101 é pré-requisito transitivo. Requisitos publicados, issues New, sem alegação de implementação concluída. Nenhuma task antiga é fonte de contexto ou conclusão.

Fontes compartilhadas em ../../scopes/2026-11-11-finai-mvp/sources/. Código ainda não possui modelos ou migrações financeiras; inventário atual apenas User e tabelas de suporte. Design demonstra tipo, valor em reais, descrição, categoria e data, todos obrigatórios; histórico por mês, busca por descrição, tipo e categoria, limpeza, paginação e detalhes; edição e exclusão com confirmação. A persistência no sistema substitui localStorage, já decidido pelo usuário.

### Q8 — Datas futuras

Contexto: não há estado de pagamento ou agendamento no escopo; o protótipo permite escolher uma data e não impede datas futuras.
Por que importa: define quais registros entram no histórico e como interpretar uma transação futura nas próximas consultas e no saldo.
Pergunta: nesta primeira versão, aceitar somente movimentações já realizadas, com data até hoje, ou também permitir datas futuras sem controle de pagamento?
Opções: A — somente realizadas, data até hoje; B — permitir datas futuras como registros, sem status pago/pendente ou agendamento automático.
Recomendação: A, para manter o MVP focado nos registros já ocorridos sem confundir previsão e saldo realizado. É proposta de adaptação ao protótipo, não regra já aprovada.
Resposta: aguardando usuário.
Estado: bloqueante.

### Q9 — Lista de categorias predefinidas

Contexto: o design demonstra quatro categorias de receita e oito de despesa; o escopo pede categorias predefinidas, sem gestão própria.
Por que importa: fixa quais classificações estarão disponíveis no formulário e no histórico, e depois na IA.
Pergunta: usar a lista do design ou ajustar seus nomes/itens?
Receitas: Salário, Freelance, Rendimentos, Outras receitas.
Despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas.
Opções: A — usar essa lista; B — usuário informa ajustes.
Recomendação: A, porque já corresponde à referência fornecida e cobre o caso genérico com Outras receitas e Outras despesas.
Resposta: aguardando usuário.
Estado: bloqueante.

## Pontos para reconciliação após a rodada

Revisar validações observáveis e datas relativas conforme Q8; dados monetários em reais e limites, filtros/mês/ordem/paginação do protótipo, proteção contra acesso a registros de outro titular, manutenção após falhas e confirmação de exclusão. Formular novas perguntas somente para ambiguidades materiais, preservando os fluxos claros do design na prévia para revisão.


## Resolução de Q8 e Q9

Resposta exata do usuário: “q8. a q9. sim concordo”.

Q8 resolvida: somente movimentações realizadas, com data até hoje. Isso adapta a validação de data do protótipo, que não restringia o futuro; não muda a linguagem visual. Q9 resolvida: conservar as quatro categorias de receitas e oito de despesas do design.

As demais regras observáveis claras do protótipo serão preservadas na prévia para revisão: reais, valor positivo até R$ 999.999.999,99 com até duas casas decimais; descrição obrigatória até 120 caracteres; data válida a partir de 1900; mês corrente inicial, busca de descrição sem diferenciar caixa/acentos, filtros combinados, limpar filtros inclui o mês, histórico em data decrescente com desempate pelo registro mais recente, 50 itens por página; detalhes, edição e confirmação de exclusão. Hoje e o mês corrente seguem o calendário local percebido pelo usuário, como no protótipo, sem adicionar preferência de fuso à conta. Isolamento e persistência no sistema vêm das decisões anteriores. Não restam perguntas funcionais abertas nesta Feature.

A prévia propõe Sequencing 3 pela posição deste catálogo e pela exceção já aprovada para ignorar as tasks antigas. A única relação direta nova é acesso-blocks-transacoes, da #1016104 criada neste fluxo para a issue a criar. A base visual #1016101 é pré-requisito transitivo; não duplicar a aresta transitiva.


## Prévia pronta para revisão

Q8 e Q9 resolvidas. Requisito e prévia integrais em feature.md e .flow/publications/c98f9183-8a43-4cb5-a6bd-804475ce23bd/. Todas as seções funcionais comparadas com criação e publicação; plano reproduzido deterministicamente e estado validado. Aguardando aprovação única do requisito, criação, publicação e relação acesso-blocks-transacoes. Nenhuma mutação remota realizada neste item.


## Aprovação e publicação concluídas

O usuário aprovou a prévia integral. Consentimento único registrado para requisito e plano, com criação, publicação e relação acesso-blocks-transacoes. Criada #1016105, Sprint 1, Sequencing 3, estado New preservado. Conteúdo integral conferido pelo checker funcional; relação 836 (#1016104 blocks #1016105) confirmada em ambos os extremos. Requisito concluído não significa implementação concluída. Resposta de criação retida antes de mover o diretório; baseline de comparação normaliza apenas CRLF/LF no conteúdo funcional.
