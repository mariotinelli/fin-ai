# [DEV] [WEB] [USUARIO] Gestão de transações - Edição e exclusão confirmada

- Redmine: `#1016125`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016105`
- Estimativa: `2h`

## Descrição

## Entrega

Permitir corrigir e remover as transações próprias persistidas, reutilizando formulário, validações e detalhes do cadastro. Conservar identidade/ordem na edição e remover somente após confirmação, integrando os resultados à consulta e aos estados de falha/cancelamento.

## Escopo e limites

Responsável pela alteração/remoção e integração do resultado. Não reconstruir categorias, validação ou histórico completo. Totais do dashboard serão aceitos na Feature correspondente; aqui os dados salvos refletem a manutenção.

## Critérios de aceite

- Abrir detalhes próprios e editar com os dados atuais preenchidos. Aplicar as mesmas cinco obrigatoriedades, limites monetários/descrição/data local e categorias compatíveis; dados inválidos impedem salvar e permitem correção.
- Salvar alteração válida modifica o mesmo registro, sem nova identidade ou mudança na ordem de cadastro usada no desempate. Trocar tipo atualiza categorias; nunca persistir categoria incompatível.
- Fechar/cancelar edição não altera; falha de salvamento conserva os dados digitados, informa problema e permite nova tentativa sem afirmar sucesso ou aplicar mudança fictícia.
- Pedir exclusão mostra que o registro sai do histórico e dos totais e que não pode ser desfeito; cancelar conserva a transação. Confirmar com persistência bem-sucedida remove definitivamente e impede consulta posterior dos detalhes.
- Falha de exclusão não remove como se concluída e permite retomar. Acesso alheio,inexistente ou já removido não revela dados ou altera outro registro; restringir visitante e conta não confirmada.
- Depois da edição/exclusão bem-sucedida, atualizar a consulta conforme filtros,contagem e ordem; excluir o último item de uma página leva a uma página válida ou ao estado vazio aplicável.
- Nas novas superfícies, preservar a composição aplicável do design e consumir a identidade FinAI fornecida, em computador/tablet/celular, claro/escuro/sistema, sem reconstruir marca, temas ou navegação compartilhada.

## Dependências

Início bloqueado por Cadastro de receitas e despesas com conferência do registro. Pode iniciar sem esperar Histórico, filtros e paginação; para concluir o aceite, integrar com essa consulta, incluindo filtros ativos,contagem,página válida e estados vazios após manutenção. O marco visual é transitivo pelo cadastro.

## Referências

Item pai Redmine #1016105; regras/critérios R1, R2, R3, R4, R6, R7, R8, R9, CA2, CA3, CA4, CA7, CA8, CA9, CA10-Manutencao, CA11-Manutencao, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #detail-dialog,#transaction-dialog,#delete-dialog; edição,confirmação/cancelamento e estados dos diálogos
- Adaptações aprovadas: persistência no sistema e por titular, somente datas até hoje, categorias do design mantidas e variante escura da base visual.

<!-- project-slices-child:e440c3a9f6d2a3c3044353414b1c6a0c65db7ee948ed9468a3de05e32873b33a -->

## Relações

- `#1016123` blocks `#1016125`
- `#1016125` blocks `#1016126`
