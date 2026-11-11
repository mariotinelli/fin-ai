# Condições de teste

## Contexto

Titulares A/B confirmados, visitante e conta não confirmada; dados financeiros de teste em meses e datas diferentes/empatadas, descrições com acentos/caixa diferentes e mais de100 correspondências para paginação. Preparar limites de valor/descrição/data, calendário local distinto de UTC quando relevante e falhas controladas de consulta/persistência. Consumir base visual FinAI implementada e verificada. Condições são para execução posterior com evidência ou impedimento explícito, sem resultado de teste presumido.

## Cadastro

### CT-001 — Receita e despesa válidas

Verificação: Cadastrar um item de cada tipo, conferir seus cinco campos e reabrir pela mesma conta.

Resultado esperado: Uma transação por envio concluído, dados corretos persistidos e confirmação sem registros de demonstração.

Origem no requisito: R1: Transações representam somente receitas ou despesas já realizadas. Todos os registros pertencem ao titular e são persistidos no sistema, independentemente do navegador usado. Não há armazenamento apenas local como fonte dos registros.; CA1: Como titular confirmado, cadastrar uma Receita e uma Despesa com campos válidos; persistir uma transação por envio concluído, mostrar confirmação e permitir consultar os dados salvos. Ao sair e voltar, inclusive em outro navegador, os registros continuam disponíveis para a mesma conta.

### CT-002 — Valores de fronteira

Verificação: Cadastrar/editar comR$0,01,limiteR$999.999.999,99,zero,negativo,valor inválido,excesso e mais de duas casas.

Resultado esperado: Aceitar positivos até limite com precisão de centavos; recusar inválidos sem alterar registros.

Origem no requisito: R2: Campos obrigatórios: tipo Receita ou Despesa, valor, descrição, categoria e data. Descrição com até 120 caracteres e ao menos um caractere além de espaços. Valor em reais, maior que zero e até R$ 999.999.999,99, com no máximo duas casas decimais; apresentar moeda e datas no formato brasileiro.; CA2: Omitir cada campo obrigatório, usar descrição vazia/somente espaços ou com mais de 120 caracteres, valor inválido, zero, negativo, acima do limite ou com mais de duas casas; impedir cadastro e edição com erro correspondente, sem alterar os registros.

### CT-003 — Descrição e obrigatoriedade

Verificação: Omitir cada campo; usar descrição vazia,só espaços,120 e121caracteres em cadastro/edição.

Resultado esperado: Obrigatoriedade e limite120aplicados com erro e possibilidade de correção;sem persistência indevida.

Origem no requisito: R2: Campos obrigatórios: tipo Receita ou Despesa, valor, descrição, categoria e data. Descrição com até 120 caracteres e ao menos um caractere além de espaços. Valor em reais, maior que zero e até R$ 999.999.999,99, com no máximo duas casas decimais; apresentar moeda e datas no formato brasileiro.; CA2: Omitir cada campo obrigatório, usar descrição vazia/somente espaços ou com mais de 120 caracteres, valor inválido, zero, negativo, acima do limite ou com mais de duas casas; impedir cadastro e edição com erro correspondente, sem alterar os registros.

### CT-004 — Datas válidas e inválidas

Verificação: Tentar data inexistente,anterior01/01/1900,hoje,anterior válida e amanhã em cadastro/edição.

Resultado esperado: Aceitar intervalo válido até hoje;recusar demais sem salvar.

Origem no requisito: R3: Aceitar somente data de calendário válida, a partir de 01/01/1900 e até hoje, inclusive, tanto no cadastro quanto na edição. Hoje e o mês corrente seguem o calendário local percebido pelo usuário, como na referência. Não incluir horário, agendamento ou estado de pagamento na transação.; CA3: Informar data inválida, anterior a 01/01/1900 ou posterior a hoje; recusar no cadastro e na edição. Data de hoje e datas anteriores válidas dentro do limite são aceitas.

### CT-005 — Calendário local

Verificação: Conferir hoje inicial e validação em contexto em que o dia local difira deUTC,incluindo mudança de dia.

Resultado esperado: Usar o calendário local percebido pelo usuário na data e mês,sem recusar hoje local nem aceitar amanhã indevidamente.

Origem no requisito: R3: Aceitar somente data de calendário válida, a partir de 01/01/1900 e até hoje, inclusive, tanto no cadastro quanto na edição. Hoje e o mês corrente seguem o calendário local percebido pelo usuário, como na referência. Não incluir horário, agendamento ou estado de pagamento na transação.; CA3: Informar data inválida, anterior a 01/01/1900 ou posterior a hoje; recusar no cadastro e na edição. Data de hoje e datas anteriores válidas dentro do limite são aceitas.; R5: O histórico começa no mês corrente e permite selecionar outro mês. Busca por trecho de descrição ignora diferenças de maiúsculas/minúsculas e acentos. Mês, descrição, tipo e categoria são combinados; sem filtro de um campo, considerar todos os seus valores. A contagem mostra o total correspondente, e não somente a página atual.

### CT-006 — Categorias por tipo

Verificação: Alternar Receita/Despesa e tentar categoria anterior incompatível ou fora da lista.

Resultado esperado: Somente quatro categorias de receita e oito de despesa aprovadas;categoria salva corresponde ao tipo,sem gestão de categorias pelo titular.

Origem no requisito: R4: Categorias de Receita: Salário, Freelance, Rendimentos e Outras receitas. Categorias de Despesa: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras e Outras despesas. A categoria deve pertencer ao tipo selecionado. As categorias são predefinidas; não há criação, edição ou exclusão de categorias pelo usuário nesta entrega.; CA4: Alternar Receita e Despesa; apresentar somente as categorias de R4 correspondentes. Não aceitar categoria do outro tipo nem categoria fora da lista. Os nomes e itens disponíveis correspondem à lista aprovada.

### CT-007 — Processamento e cancelamento

Verificação: Abrir cadastro padrão Despesa/hoje,cancelar/fechar e salvar com processamento observado.

Resultado esperado: Cinco campos obrigatórios;cancelar não cria;botão não permite novo envio enquanto processa;sucesso fecha e confirma um registro.

Origem no requisito: R1: Transações representam somente receitas ou despesas já realizadas. Todos os registros pertencem ao titular e são persistidos no sistema, independentemente do navegador usado. Não há armazenamento apenas local como fonte dos registros.; CA1: Como titular confirmado, cadastrar uma Receita e uma Despesa com campos válidos; persistir uma transação por envio concluído, mostrar confirmação e permitir consultar os dados salvos. Ao sair e voltar, inclusive em outro navegador, os registros continuam disponíveis para a mesma conta.; CA8: Abrir detalhes de uma transação; visualizar os cinco campos. Editar e salvar dados válidos altera o mesmo registro e atualiza a consulta sem criar outro. Fechar ou cancelar cadastro/edição não modifica os dados persistidos.

### CT-008 — Falha no cadastro

Verificação: Provocar falha de persistência em dados válidos e retomar.

Resultado esperado: Sem falso sucesso ou alteração concluída fictícia;dados digitados conservados e nova tentativa disponível.

Origem no requisito: CA10: Provocar falha de salvamento ou exclusão; não apresentar sucesso nem tratar a alteração como aplicada. Conservar dados de formulário em falha de cadastro/edição e permitir nova tentativa. Falha de carregamento informa indisponibilidade sem confundir com histórico vazio.

### CT-009 — Persistência entre sessões

Verificação: Salvar,sair/voltar e acessar a mesma conta em outro navegador.

Resultado esperado: Registros próprios continuam no sistema,sem depender de armazenamento apenas local.

Origem no requisito: R1: Transações representam somente receitas ou despesas já realizadas. Todos os registros pertencem ao titular e são persistidos no sistema, independentemente do navegador usado. Não há armazenamento apenas local como fonte dos registros.; CA1: Como titular confirmado, cadastrar uma Receita e uma Despesa com campos válidos; persistir uma transação por envio concluído, mostrar confirmação e permitir consultar os dados salvos. Ao sair e voltar, inclusive em outro navegador, os registros continuam disponíveis para a mesma conta.

## Consulta

### CT-010 — Histórico mensal

Verificação: Com registros em meses distintos,abrir Transações e selecionar outro mês/ano.

Resultado esperado: Iniciar no mês corrente local e listar somente os próprios registros do mês escolhido.

Origem no requisito: R5: O histórico começa no mês corrente e permite selecionar outro mês. Busca por trecho de descrição ignora diferenças de maiúsculas/minúsculas e acentos. Mês, descrição, tipo e categoria são combinados; sem filtro de um campo, considerar todos os seus valores. A contagem mostra o total correspondente, e não somente a página atual.; CA5: Consultar o histórico inicial e selecionar outro mês; apresentar somente os registros próprios daquele mês. Combinar descrição, tipo e categoria com o mês; a lista e a contagem correspondem à interseção. Buscar descrições com diferenças de caixa e acentos encontra as correspondências esperadas.

### CT-011 — Filtros combinados

Verificação: Combinar mês,trecho de descrição,tipo e categoria com massa conhecida.

Resultado esperado: Lista e contagem são a interseção correta;campo sem filtro considera todos os valores;contagem refere-se a todas as correspondências.

Origem no requisito: R5: O histórico começa no mês corrente e permite selecionar outro mês. Busca por trecho de descrição ignora diferenças de maiúsculas/minúsculas e acentos. Mês, descrição, tipo e categoria são combinados; sem filtro de um campo, considerar todos os seus valores. A contagem mostra o total correspondente, e não somente a página atual.; CA5: Consultar o histórico inicial e selecionar outro mês; apresentar somente os registros próprios daquele mês. Combinar descrição, tipo e categoria com o mês; a lista e a contagem correspondem à interseção. Buscar descrições com diferenças de caixa e acentos encontra as correspondências esperadas.

### CT-012 — Busca com caixa e acentos

Verificação: Buscar trecho de descrição alternando maiúsculas/minúsculas e acentos em dados conhecidos.

Resultado esperado: Encontrar correspondências independentemente de caixa/acentos,no banco utilizado.

Origem no requisito: R5: O histórico começa no mês corrente e permite selecionar outro mês. Busca por trecho de descrição ignora diferenças de maiúsculas/minúsculas e acentos. Mês, descrição, tipo e categoria são combinados; sem filtro de um campo, considerar todos os seus valores. A contagem mostra o total correspondente, e não somente a página atual.; CA5: Consultar o histórico inicial e selecionar outro mês; apresentar somente os registros próprios daquele mês. Combinar descrição, tipo e categoria com o mês; a lista e a contagem correspondem à interseção. Buscar descrições com diferenças de caixa e acentos encontra as correspondências esperadas.

### CT-013 — Limpar também o mês

Verificação: Aplicar os quatro filtros e acionar Limpar filtros.

Resultado esperado: Remover todos,inclusive mês,mostrar todo histórico próprio e reiniciar página.

Origem no requisito: R5: O histórico começa no mês corrente e permite selecionar outro mês. Busca por trecho de descrição ignora diferenças de maiúsculas/minúsculas e acentos. Mês, descrição, tipo e categoria são combinados; sem filtro de um campo, considerar todos os seus valores. A contagem mostra o total correspondente, e não somente a página atual.; CA6: Limpar filtros; consultar todo o histórico sem restrição de mês, descrição, tipo ou categoria. Sem registros, orientar o primeiro cadastro; sem correspondências em um histórico com registros, orientar alteração dos filtros.

### CT-014 — Registro fora do filtro

Verificação: Salvar com data/categoria fora do recorte ativo e depois alterar/limpar filtros.

Resultado esperado: Registro fica persistido sem aparecer indevidamente no recorte;ao consultar recorte compatível,é encontrado.

Origem no requisito: CA1: Como titular confirmado, cadastrar uma Receita e uma Despesa com campos válidos; persistir uma transação por envio concluído, mostrar confirmação e permitir consultar os dados salvos. Ao sair e voltar, inclusive em outro navegador, os registros continuam disponíveis para a mesma conta.; R5: O histórico começa no mês corrente e permite selecionar outro mês. Busca por trecho de descrição ignora diferenças de maiúsculas/minúsculas e acentos. Mês, descrição, tipo e categoria são combinados; sem filtro de um campo, considerar todos os seus valores. A contagem mostra o total correspondente, e não somente a página atual.; CA5: Consultar o histórico inicial e selecionar outro mês; apresentar somente os registros próprios daquele mês. Combinar descrição, tipo e categoria com o mês; a lista e a contagem correspondem à interseção. Buscar descrições com diferenças de caixa e acentos encontra as correspondências esperadas.; CA6: Limpar filtros; consultar todo o histórico sem restrição de mês, descrição, tipo ou categoria. Sem registros, orientar o primeiro cadastro; sem correspondências em um histórico com registros, orientar alteração dos filtros.

### CT-015 — Vazio e sem resultados

Verificação: Usar conta sem registros e conta com histórico que não corresponda aos filtros.

Resultado esperado: Primeiro caso orienta cadastro;segundo orienta filtros,sem confundir estados.

Origem no requisito: CA6: Limpar filtros; consultar todo o histórico sem restrição de mês, descrição, tipo ou categoria. Sem registros, orientar o primeiro cadastro; sem correspondências em um histórico com registros, orientar alteração dos filtros.

### CT-016 — Falha de carregamento

Verificação: Provocar falha de consulta e tentar novamente após restabelecer.

Resultado esperado: Indicar indisponibilidade/nova tentativa,sem apresentar lista vazia como sucesso;retomada recupera dados reais.

Origem no requisito: CA10-Consulta: Desdobramento de CA10: falha de carregamento do histórico é indisponibilidade, não lista vazia.

### CT-017 — Ordem e empate

Verificação: Usar datas distintas e empates com cadastros em instantes diferentes;editar um registro empatado.

Resultado esperado: Data decrescente,depois cadastro mais recente;editar não muda ordem de cadastro usada no desempate.

Origem no requisito: R6: Ordenar por data da transação decrescente; em mesma data, mostrar primeiro o registro cadastrado mais recentemente. Edição conserva a identidade e a ordem de cadastro do registro. Paginar em até 50 transações por página, com Anterior, Próxima e indicação de página; indisponibilizar navegação além dos limites.; CA7: Com mais de 50 correspondências, navegar entre páginas sem exceder os limites e com contagem total correta. Verificar ordem por data decrescente e, em empate, pelo cadastro mais recente. Alterar filtros ou excluir o último item de uma página mantém navegação válida.

### CT-018 — Paginação e contagem

Verificação: Com mais de100 correspondências,navegar nas páginas e alterar filtros.

Resultado esperado: Até50por página,contagem total,Anterior/Próxima/indicação corretos,sem ultrapassar limites;alterar filtros volta à primeira página válida.

Origem no requisito: R6: Ordenar por data da transação decrescente; em mesma data, mostrar primeiro o registro cadastrado mais recentemente. Edição conserva a identidade e a ordem de cadastro do registro. Paginar em até 50 transações por página, com Anterior, Próxima e indicação de página; indisponibilizar navegação além dos limites.; CA7: Com mais de 50 correspondências, navegar entre páginas sem exceder os limites e com contagem total correta. Verificar ordem por data decrescente e, em empate, pelo cadastro mais recente. Alterar filtros ou excluir o último item de uma página mantém navegação válida.

### CT-019 — Detalhes desktop e celular

Verificação: Abrir pelo texto e pela ação de detalhes em lista desktop e compacta móvel.

Resultado esperado: Cinco campos reais acessíveis;descrição,categoria,data,valor/sinal e acesso conforme composição,sem perder dados no celular.

Origem no requisito: R9: As telas usam a base visual FinAI. Preservar a composição de Transações do design, seus filtros, lista e diálogos, adaptando-a a dados reais do sistema. No desktop, apresentar descrição, categoria, data, valor e acesso aos detalhes. No celular, usar a lista compacta da referência e manter os dados completos acessíveis nos detalhes. Conservar claro, escuro e acompanhar o sistema.; CA8: Abrir detalhes de uma transação; visualizar os cinco campos. Editar e salvar dados válidos altera o mesmo registro e atualiza a consulta sem criar outro. Fechar ou cancelar cadastro/edição não modifica os dados persistidos.; CA12: Utilizar filtros, lista e diálogos em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; manter a composição e linguagem visual do design, lista compacta no celular e acesso aos dados completos nos detalhes.

## Manutenção

### CT-020 — Edição válida e identidade

Verificação: Editar os cinco campos permitidos para valores válidos,incluindo mudança de tipo/categoria.

Resultado esperado: Mesmo registro atualizado,sem duplicar ou mudar ordem de cadastro;categoria compatível e consulta atualizada segundo filtros.

Origem no requisito: R2: Campos obrigatórios: tipo Receita ou Despesa, valor, descrição, categoria e data. Descrição com até 120 caracteres e ao menos um caractere além de espaços. Valor em reais, maior que zero e até R$ 999.999.999,99, com no máximo duas casas decimais; apresentar moeda e datas no formato brasileiro.; R3: Aceitar somente data de calendário válida, a partir de 01/01/1900 e até hoje, inclusive, tanto no cadastro quanto na edição. Hoje e o mês corrente seguem o calendário local percebido pelo usuário, como na referência. Não incluir horário, agendamento ou estado de pagamento na transação.; R4: Categorias de Receita: Salário, Freelance, Rendimentos e Outras receitas. Categorias de Despesa: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras e Outras despesas. A categoria deve pertencer ao tipo selecionado. As categorias são predefinidas; não há criação, edição ou exclusão de categorias pelo usuário nesta entrega.; R6: Ordenar por data da transação decrescente; em mesma data, mostrar primeiro o registro cadastrado mais recentemente. Edição conserva a identidade e a ordem de cadastro do registro. Paginar em até 50 transações por página, com Anterior, Próxima e indicação de página; indisponibilizar navegação além dos limites.; R7: Edição altera a mesma transação; exclusão confirmada remove definitivamente o registro. A confirmação deve informar a remoção do histórico e dos totais e que não pode ser desfeita. A atualização dos totais visíveis será aceita na Feature Dashboard financeiro; os dados persistidos precisam refletir a manutenção realizada aqui.; CA8: Abrir detalhes de uma transação; visualizar os cinco campos. Editar e salvar dados válidos altera o mesmo registro e atualiza a consulta sem criar outro. Fechar ou cancelar cadastro/edição não modifica os dados persistidos.

### CT-021 — Cancelar e falhar edição

Verificação: Cancelar/fechar e depois provocar falha ao salvar edição válida.

Resultado esperado: Cancelamento não altera;falha conserva dados digitados,informa problema e permite nova tentativa sem falso sucesso.

Origem no requisito: CA8: Abrir detalhes de uma transação; visualizar os cinco campos. Editar e salvar dados válidos altera o mesmo registro e atualiza a consulta sem criar outro. Fechar ou cancelar cadastro/edição não modifica os dados persistidos.; CA10-Manutencao: Desdobramento de CA10: falhas de edição/exclusão não aplicam alteração fictícia e permitem retomar.

### CT-022 — Exclusão e cancelamento

Verificação: Pedir exclusão,cancelar e depois confirmar com persistência disponível.

Resultado esperado: Aviso de remoção de histórico/totais e irreversibilidade;cancelar mantém;confirmar remove definitivamente e detalhes deixam de estar disponíveis.

Origem no requisito: R7: Edição altera a mesma transação; exclusão confirmada remove definitivamente o registro. A confirmação deve informar a remoção do histórico e dos totais e que não pode ser desfeita. A atualização dos totais visíveis será aceita na Feature Dashboard financeiro; os dados persistidos precisam refletir a manutenção realizada aqui.; CA9: Pedir exclusão; apresentar aviso e confirmação. Cancelar mantém o registro. Confirmar com persistência bem-sucedida remove a transação do histórico próprio e ela deixa de estar disponível nos detalhes.

### CT-023 — Falha de exclusão

Verificação: Provocar falha ao excluir e retomar após restabelecimento.

Resultado esperado: Não remover como concluído nem informar sucesso na falha;nova tentativa disponível.

Origem no requisito: CA10-Manutencao: Desdobramento de CA10: falhas de edição/exclusão não aplicam alteração fictícia e permitem retomar.

### CT-024 — Último item da página

Verificação: Excluir o último item de uma página e o último registro do resultado sob filtros.

Resultado esperado: Navegação passa para página válida ou estado vazio aplicável,com contagem e consulta coerentes.

Origem no requisito: R6: Ordenar por data da transação decrescente; em mesma data, mostrar primeiro o registro cadastrado mais recentemente. Edição conserva a identidade e a ordem de cadastro do registro. Paginar em até 50 transações por página, com Anterior, Próxima e indicação de página; indisponibilizar navegação além dos limites.; R7: Edição altera a mesma transação; exclusão confirmada remove definitivamente o registro. A confirmação deve informar a remoção do histórico e dos totais e que não pode ser desfeita. A atualização dos totais visíveis será aceita na Feature Dashboard financeiro; os dados persistidos precisam refletir a manutenção realizada aqui.; CA7: Com mais de 50 correspondências, navegar entre páginas sem exceder os limites e com contagem total correta. Verificar ordem por data decrescente e, em empate, pelo cadastro mais recente. Alterar filtros ou excluir o último item de uma página mantém navegação válida.; CA9: Pedir exclusão; apresentar aviso e confirmação. Cancelar mantém o registro. Confirmar com persistência bem-sucedida remove a transação do histórico próprio e ela deixa de estar disponível nos detalhes.

## Permissões

### CT-025 — Titularidade do cadastro/detalhes

Verificação: Como titularB,tentar criar emA e abrir registro deA,inclusive parâmetros/acesso direto.

Resultado esperado: Não escolher outra conta proprietária,não revelar detalhe ou criar registro alheio.

Origem no requisito: R8: Todas as operações e consultas respeitam a titularidade, inclusive contagem, filtros, detalhes, edição, exclusão e acesso direto. Não oferecer compartilhamento de transações entre contas.; CA11: Como outro titular, tentar listar, contar, abrir detalhes, editar ou excluir registros alheios, inclusive por acesso direto; não revelar dados nem executar alterações. Visitante ou conta sem confirmação não acessa as operações conforme a Feature de acesso.

### CT-026 — Titularidade da consulta

Verificação: ComoB,listar/filtrar/contar e tentar detalhes deA;usar também registro inexistente/removido.

Resultado esperado: Somente dados próprios;sem revelar existência/conteúdo alheio,com orientação de voltar/atualizar quando aplicável.

Origem no requisito: R8: Todas as operações e consultas respeitam a titularidade, inclusive contagem, filtros, detalhes, edição, exclusão e acesso direto. Não oferecer compartilhamento de transações entre contas.; CA11-Consulta: Desdobramento de CA11: titularidade em lista, contagem e detalhes do histórico.

### CT-027 — Titularidade da manutenção

Verificação: ComoB,tentar editar/excluir registro deA por acesso direto,e repetir com registro removido/inexistente.

Resultado esperado: Não alterar/remover indevidamente nem expor dados alheios.

Origem no requisito: R8: Todas as operações e consultas respeitam a titularidade, inclusive contagem, filtros, detalhes, edição, exclusão e acesso direto. Não oferecer compartilhamento de transações entre contas.; CA11-Manutencao: Desdobramento de CA11: titularidade na edição, exclusão e acessos diretos.

### CT-028 — Visitante e não-confirmado

Verificação: Tentar cadastro,consulta,detalhes,edição e exclusão sem sessão e com conta não confirmada.

Resultado esperado: Exigir acesso conforme auth/confirmado,sem permitir operações ou revelar finanças.

Origem no requisito: R8: Todas as operações e consultas respeitam a titularidade, inclusive contagem, filtros, detalhes, edição, exclusão e acesso direto. Não oferecer compartilhamento de transações entre contas.; CA11: Como outro titular, tentar listar, contar, abrir detalhes, editar ou excluir registros alheios, inclusive por acesso direto; não revelar dados nem executar alterações. Visitante ou conta sem confirmação não acessa as operações conforme a Feature de acesso.

## Visual

### CT-029 — Visual e estados da tela nova

Verificação: Comparar filtros,lista e diálogos com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (#transactions,#transaction-dialog,#detail-dialog,#delete-dialog),em computador/tablet/celular e claro/escuro/sistema,incluindo vazio,erros e processamento.

Resultado esperado: Composição da referência,identidade fornecida,lista compacta móvel e dados completos nos detalhes;sem reconstrução da fundação visual.

Origem no requisito: R9: As telas usam a base visual FinAI. Preservar a composição de Transações do design, seus filtros, lista e diálogos, adaptando-a a dados reais do sistema. No desktop, apresentar descrição, categoria, data, valor e acesso aos detalhes. No celular, usar a lista compacta da referência e manter os dados completos acessíveis nos detalhes. Conservar claro, escuro e acompanhar o sistema.; CA12: Utilizar filtros, lista e diálogos em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; manter a composição e linguagem visual do design, lista compacta no celular e acesso aos dados completos nos detalhes.
