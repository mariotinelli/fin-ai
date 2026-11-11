# [WEB] [USUARIO] Gestão de transações

## Objetivo

Permitir que o titular autenticado e com e-mail confirmado registre, consulte, edite e exclua suas receitas e despesas realizadas, usando categorias predefinidas. Persistir os registros no sistema e manter as finanças de cada titular separadas.

## Resultado esperado

O usuário mantém um histórico próprio de transações, encontra registros por período, descrição, tipo e categoria, consulta seus detalhes e corrige ou remove movimentações. O histórico conserva os dados após sair, voltar ao sistema ou acessar a conta em outro navegador. Alterações persistidas ficam disponíveis para as futuras consultas do dashboard e da IA.

## Atores e permissões

O titular autenticado e com e-mail confirmado pode cadastrar e manter somente suas próprias transações. Visitantes e contas sem confirmação seguem as restrições da Feature de acesso. Nenhum usuário pode visualizar detalhes, listar, editar ou excluir transações de outra conta, inclusive por acesso direto a um registro.

## Histórias de usuário

1. Como titular, quero registrar uma receita ou despesa realizada para manter minhas finanças organizadas.
2. Como titular, quero classificar cada transação em uma categoria predefinida adequada ao tipo.
3. Como titular, quero consultar o histórico e combinar filtros para encontrar uma movimentação.
4. Como titular, quero ver os detalhes e editar uma transação para corrigir informações.
5. Como titular, quero excluir uma transação após confirmação para remover um registro indevido.
6. Como titular, quero manter meus registros salvos e separados dos de outras contas.

## Fluxo principal

1. Ao abrir Transações, apresentar o histórico próprio no mês corrente, com filtros de descrição, tipo e categoria, contagem de resultados e navegação de páginas quando necessária.
2. Acionar Nova transação. Abrir o formulário com tipo, valor em reais, descrição, categoria e data, todos obrigatórios. Iniciar com tipo Despesa e data de hoje, conforme a referência.
3. Escolher Receita ou Despesa, informar valor positivo, descrição, categoria compatível e data até hoje. Exibir no campo de categoria somente as opções do tipo selecionado.
4. Salvar dados válidos. Durante o salvamento, indicar o processamento e impedir novo envio pelo mesmo botão; após sucesso, persistir uma transação vinculada ao titular, fechar o formulário e apresentar confirmação.
5. Atualizar o histórico segundo os filtros ativos. Um registro fora do mês ou dos filtros selecionados permanece salvo e pode ser encontrado ao alterar ou limpar esses filtros.
6. Pesquisar por parte da descrição e combinar mês, tipo e categoria. Exibir os resultados ordenados da data mais recente para a mais antiga, com paginação quando houver mais de 50 registros correspondentes.
7. Abrir uma transação pela descrição ou ação de detalhes. Apresentar descrição, tipo, valor, categoria e data; oferecer edição e exclusão.
8. Na edição, preencher o formulário com os dados atuais. Validar e salvar as alterações no mesmo registro; após sucesso, apresentar confirmação e atualizar a consulta.
9. Na exclusão, apresentar confirmação de remoção definitiva. Somente após confirmar e concluir a persistência, remover o registro e atualizar o histórico.

## Fluxos alternativos e exceções

- Dados ausentes ou inválidos apresentam erros nos campos, impedem salvar e conservam o formulário para correção. Data futura, valor zero/negativo, descrição vazia e categoria incompatível são recusados.
- Ao mudar o tipo, atualizar as categorias disponíveis; não persistir a categoria anterior se ela não pertencer ao novo tipo. O formulário deve apresentar a classificação que será salva.
- Cancelar ou fechar cadastro/edição sem salvar não cria nem altera registros. Cancelar a confirmação de exclusão mantém a transação.
- Falha de persistência não apresenta sucesso nem aplica a alteração como concluída. Informar o problema e permitir nova tentativa; no cadastro/edição, conservar os dados digitados para correção ou reenvio.
- Falha ao carregar o histórico apresenta indisponibilidade e possibilidade de tentar novamente; não apresentar a falha como histórico vazio ou ausência de registros.
- Sem transações, apresentar estado inicial com orientação para registrar a primeira. Com registros existentes, mas sem correspondências aos filtros, mostrar estado sem resultados e orientar alterar ou limpar filtros.
- Limpar filtros remove descrição, tipo, categoria e mês, permitindo consultar todo o histórico. Alterar os filtros reinicia na primeira página; páginas fora do resultado atual não permanecem selecionadas.
- Excluir o último item de uma página ajusta a navegação para uma página válida. Sem resultados após exclusão, apresentar o estado vazio aplicável.
- Tentar acessar ou modificar registro de outra conta, inexistente ou já removido não revela seus dados nem altera registros indevidamente; orientar voltar à consulta e atualizá-la quando necessário.

## Regras de negócio

R1. Transações representam somente receitas ou despesas já realizadas. Todos os registros pertencem ao titular e são persistidos no sistema, independentemente do navegador usado. Não há armazenamento apenas local como fonte dos registros.

R2. Campos obrigatórios: tipo Receita ou Despesa, valor, descrição, categoria e data. Descrição com até 120 caracteres e ao menos um caractere além de espaços. Valor em reais, maior que zero e até R$ 999.999.999,99, com no máximo duas casas decimais; apresentar moeda e datas no formato brasileiro.

R3. Aceitar somente data de calendário válida, a partir de 01/01/1900 e até hoje, inclusive, tanto no cadastro quanto na edição. Hoje e o mês corrente seguem o calendário local percebido pelo usuário, como na referência. Não incluir horário, agendamento ou estado de pagamento na transação.

R4. Categorias de Receita: Salário, Freelance, Rendimentos e Outras receitas. Categorias de Despesa: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras e Outras despesas. A categoria deve pertencer ao tipo selecionado. As categorias são predefinidas; não há criação, edição ou exclusão de categorias pelo usuário nesta entrega.

R5. O histórico começa no mês corrente e permite selecionar outro mês. Busca por trecho de descrição ignora diferenças de maiúsculas/minúsculas e acentos. Mês, descrição, tipo e categoria são combinados; sem filtro de um campo, considerar todos os seus valores. A contagem mostra o total correspondente, e não somente a página atual.

R6. Ordenar por data da transação decrescente; em mesma data, mostrar primeiro o registro cadastrado mais recentemente. Edição conserva a identidade e a ordem de cadastro do registro. Paginar em até 50 transações por página, com Anterior, Próxima e indicação de página; indisponibilizar navegação além dos limites.

R7. Edição altera a mesma transação; exclusão confirmada remove definitivamente o registro. A confirmação deve informar a remoção do histórico e dos totais e que não pode ser desfeita. A atualização dos totais visíveis será aceita na Feature Dashboard financeiro; os dados persistidos precisam refletir a manutenção realizada aqui.

R8. Todas as operações e consultas respeitam a titularidade, inclusive contagem, filtros, detalhes, edição, exclusão e acesso direto. Não oferecer compartilhamento de transações entre contas.

R9. As telas usam a base visual FinAI. Preservar a composição de Transações do design, seus filtros, lista e diálogos, adaptando-a a dados reais do sistema. No desktop, apresentar descrição, categoria, data, valor e acesso aos detalhes. No celular, usar a lista compacta da referência e manter os dados completos acessíveis nos detalhes. Conservar claro, escuro e acompanhar o sistema.

## Dados percebidos pelo usuário

Tipo, valor em reais, descrição, categoria e data de cada transação; sinal positivo para receita e negativo para despesa na listagem; categoria, data e descrição nos detalhes; mês e filtros selecionados, contagem de resultados, paginação e mensagens de validação, processamento, sucesso, erro ou ausência de registros. O titular não escolhe outra conta proprietária para os seus registros.

## Critérios de aceite

CA1. Como titular confirmado, cadastrar uma Receita e uma Despesa com campos válidos; persistir uma transação por envio concluído, mostrar confirmação e permitir consultar os dados salvos. Ao sair e voltar, inclusive em outro navegador, os registros continuam disponíveis para a mesma conta.

CA2. Omitir cada campo obrigatório, usar descrição vazia/somente espaços ou com mais de 120 caracteres, valor inválido, zero, negativo, acima do limite ou com mais de duas casas; impedir cadastro e edição com erro correspondente, sem alterar os registros.

CA3. Informar data inválida, anterior a 01/01/1900 ou posterior a hoje; recusar no cadastro e na edição. Data de hoje e datas anteriores válidas dentro do limite são aceitas.

CA4. Alternar Receita e Despesa; apresentar somente as categorias de R4 correspondentes. Não aceitar categoria do outro tipo nem categoria fora da lista. Os nomes e itens disponíveis correspondem à lista aprovada.

CA5. Consultar o histórico inicial e selecionar outro mês; apresentar somente os registros próprios daquele mês. Combinar descrição, tipo e categoria com o mês; a lista e a contagem correspondem à interseção. Buscar descrições com diferenças de caixa e acentos encontra as correspondências esperadas.

CA6. Limpar filtros; consultar todo o histórico sem restrição de mês, descrição, tipo ou categoria. Sem registros, orientar o primeiro cadastro; sem correspondências em um histórico com registros, orientar alteração dos filtros.

CA7. Com mais de 50 correspondências, navegar entre páginas sem exceder os limites e com contagem total correta. Verificar ordem por data decrescente e, em empate, pelo cadastro mais recente. Alterar filtros ou excluir o último item de uma página mantém navegação válida.

CA8. Abrir detalhes de uma transação; visualizar os cinco campos. Editar e salvar dados válidos altera o mesmo registro e atualiza a consulta sem criar outro. Fechar ou cancelar cadastro/edição não modifica os dados persistidos.

CA9. Pedir exclusão; apresentar aviso e confirmação. Cancelar mantém o registro. Confirmar com persistência bem-sucedida remove a transação do histórico próprio e ela deixa de estar disponível nos detalhes.

CA10. Provocar falha de salvamento ou exclusão; não apresentar sucesso nem tratar a alteração como aplicada. Conservar dados de formulário em falha de cadastro/edição e permitir nova tentativa. Falha de carregamento informa indisponibilidade sem confundir com histórico vazio.

CA11. Como outro titular, tentar listar, contar, abrir detalhes, editar ou excluir registros alheios, inclusive por acesso direto; não revelar dados nem executar alterações. Visitante ou conta sem confirmação não acessa as operações conforme a Feature de acesso.

CA12. Utilizar filtros, lista e diálogos em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; manter a composição e linguagem visual do design, lista compacta no celular e acesso aos dados completos nos detalhes.

## Dependências

Acesso à conta pessoal, issue #1016104: fornece autenticação, confirmação de e-mail e identificação do titular. Adequação visual #1016101 é pré-requisito transitivo. A implementação deve seguir essas dependências; a publicação dos requisitos não significa implementação concluída.

Dashboard e assistente serão consumidores dos registros persistidos e das categorias, mas não bloqueiam esta entrega. Não duplicar a dependência visual transitiva como relação direta.

## Designs e evidências

Referência principal design-input-001: ../../scopes/2026-11-11-finai-mvp/sources/design-input-001.md. Original C:/Users/maari/Downloads/FinAI-Controle-Financeiro.zip. Localizadores: #transactions, #transaction-dialog, #detail-dialog, #delete-dialog; funções cats, categoryOptions, renderHistory, sorted, fieldError e persist, além dos estilos de filtros/lista/diálogos e media queries. Aparência compartilhada conforme docs/harness/features/1016101-adequacao-visual-do-finai/feature.md. Critérios visuais em R9 e CA12.

Adaptações confirmadas nesta conversa: persistência no sistema substitui localStorage; dados isolados por usuário; somente movimentações realizadas até hoje; categorias do design mantidas. A restrição de datas futuras adapta o comportamento do protótipo sem substituir sua linguagem visual. A variante escura decorre da base visual aprovada.

Fontes de negócio: conversation-input-001, §§3.2, 3.3 e 4; decisões de contas/persistência em conversation-input-002; respostas Q8 e Q9 em history/interview.md. O código atual não possui modelos ou migrações financeiros; nenhuma task antiga do Redmine é considerada fonte ou entrega concluída.

## Dentro do escopo

Cadastro manual, consulta de detalhes e histórico, filtros e paginação, edição, exclusão com confirmação, categorias predefinidas, validações descritas, persistência no sistema e isolamento por titular; telas e estados da gestão de transações conforme o design e a base visual.

## Fora do escopo

Datas futuras, agendamento, contas a pagar/receber, estado de pagamento, recorrência, parcelamento, transferências entre contas, moedas adicionais e manutenção de categorias pelo usuário. Integração bancária, extratos, cartões, metas, relatórios avançados e gestão empresarial permanecem fora do MVP. Dashboard e IA são entregas das próximas Features. Esta etapa não implementa código nem decompõe tarefas técnicas.
