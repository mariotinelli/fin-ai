# [QA] [WEB] [USUARIO] Gestão de transações

- Redmine: `#1016126`
- Tipo: `QA`
- Tracker: Deliverable (`5`)
- Item pai: `#1016105`
- Estimativa: `1.5h`

## Descrição

## Objetivo

Verificar cadastro,consulta e manutenção de transações próprias persistidas,com categorias,validações,estados,permissões e composição visual aprovados.

## Jornadas integradas

- Receita e despesa válidas: Cadastrar um item de cada tipo, conferir seus cinco campos e reabrir pela mesma conta. Resultado esperado: Uma transação por envio concluído, dados corretos persistidos e confirmação sem registros de demonstração.
- Valores de fronteira: Cadastrar/editar comR$0,01,limiteR$999.999.999,99,zero,negativo,valor inválido,excesso e mais de duas casas. Resultado esperado: Aceitar positivos até limite com precisão de centavos; recusar inválidos sem alterar registros.
- Descrição e obrigatoriedade: Omitir cada campo; usar descrição vazia,só espaços,120 e121caracteres em cadastro/edição. Resultado esperado: Obrigatoriedade e limite120aplicados com erro e possibilidade de correção;sem persistência indevida.
- Datas válidas e inválidas: Tentar data inexistente,anterior01/01/1900,hoje,anterior válida e amanhã em cadastro/edição. Resultado esperado: Aceitar intervalo válido até hoje;recusar demais sem salvar.
- Calendário local: Conferir hoje inicial e validação em contexto em que o dia local difira deUTC,incluindo mudança de dia. Resultado esperado: Usar o calendário local percebido pelo usuário na data e mês,sem recusar hoje local nem aceitar amanhã indevidamente.
- Categorias por tipo: Alternar Receita/Despesa e tentar categoria anterior incompatível ou fora da lista. Resultado esperado: Somente quatro categorias de receita e oito de despesa aprovadas;categoria salva corresponde ao tipo,sem gestão de categorias pelo titular.
- Processamento e cancelamento: Abrir cadastro padrão Despesa/hoje,cancelar/fechar e salvar com processamento observado. Resultado esperado: Cinco campos obrigatórios;cancelar não cria;botão não permite novo envio enquanto processa;sucesso fecha e confirma um registro.
- Falha no cadastro: Provocar falha de persistência em dados válidos e retomar. Resultado esperado: Sem falso sucesso ou alteração concluída fictícia;dados digitados conservados e nova tentativa disponível.
- Persistência entre sessões: Salvar,sair/voltar e acessar a mesma conta em outro navegador. Resultado esperado: Registros próprios continuam no sistema,sem depender de armazenamento apenas local.
- Histórico mensal: Com registros em meses distintos,abrir Transações e selecionar outro mês/ano. Resultado esperado: Iniciar no mês corrente local e listar somente os próprios registros do mês escolhido.
- Filtros combinados: Combinar mês,trecho de descrição,tipo e categoria com massa conhecida. Resultado esperado: Lista e contagem são a interseção correta;campo sem filtro considera todos os valores;contagem refere-se a todas as correspondências.
- Busca com caixa e acentos: Buscar trecho de descrição alternando maiúsculas/minúsculas e acentos em dados conhecidos. Resultado esperado: Encontrar correspondências independentemente de caixa/acentos,no banco utilizado.
- Limpar também o mês: Aplicar os quatro filtros e acionar Limpar filtros. Resultado esperado: Remover todos,inclusive mês,mostrar todo histórico próprio e reiniciar página.
- Registro fora do filtro: Salvar com data/categoria fora do recorte ativo e depois alterar/limpar filtros. Resultado esperado: Registro fica persistido sem aparecer indevidamente no recorte;ao consultar recorte compatível,é encontrado.
- Vazio e sem resultados: Usar conta sem registros e conta com histórico que não corresponda aos filtros. Resultado esperado: Primeiro caso orienta cadastro;segundo orienta filtros,sem confundir estados.
- Falha de carregamento: Provocar falha de consulta e tentar novamente após restabelecer. Resultado esperado: Indicar indisponibilidade/nova tentativa,sem apresentar lista vazia como sucesso;retomada recupera dados reais.
- Ordem e empate: Usar datas distintas e empates com cadastros em instantes diferentes;editar um registro empatado. Resultado esperado: Data decrescente,depois cadastro mais recente;editar não muda ordem de cadastro usada no desempate.
- Paginação e contagem: Com mais de100 correspondências,navegar nas páginas e alterar filtros. Resultado esperado: Até50por página,contagem total,Anterior/Próxima/indicação corretos,sem ultrapassar limites;alterar filtros volta à primeira página válida.
- Detalhes desktop e celular: Abrir pelo texto e pela ação de detalhes em lista desktop e compacta móvel. Resultado esperado: Cinco campos reais acessíveis;descrição,categoria,data,valor/sinal e acesso conforme composição,sem perder dados no celular.
- Edição válida e identidade: Editar os cinco campos permitidos para valores válidos,incluindo mudança de tipo/categoria. Resultado esperado: Mesmo registro atualizado,sem duplicar ou mudar ordem de cadastro;categoria compatível e consulta atualizada segundo filtros.
- Cancelar e falhar edição: Cancelar/fechar e depois provocar falha ao salvar edição válida. Resultado esperado: Cancelamento não altera;falha conserva dados digitados,informa problema e permite nova tentativa sem falso sucesso.
- Exclusão e cancelamento: Pedir exclusão,cancelar e depois confirmar com persistência disponível. Resultado esperado: Aviso de remoção de histórico/totais e irreversibilidade;cancelar mantém;confirmar remove definitivamente e detalhes deixam de estar disponíveis.
- Falha de exclusão: Provocar falha ao excluir e retomar após restabelecimento. Resultado esperado: Não remover como concluído nem informar sucesso na falha;nova tentativa disponível.
- Último item da página: Excluir o último item de uma página e o último registro do resultado sob filtros. Resultado esperado: Navegação passa para página válida ou estado vazio aplicável,com contagem e consulta coerentes.
- Titularidade do cadastro/detalhes: Como titularB,tentar criar emA e abrir registro deA,inclusive parâmetros/acesso direto. Resultado esperado: Não escolher outra conta proprietária,não revelar detalhe ou criar registro alheio.
- Titularidade da consulta: ComoB,listar/filtrar/contar e tentar detalhes deA;usar também registro inexistente/removido. Resultado esperado: Somente dados próprios;sem revelar existência/conteúdo alheio,com orientação de voltar/atualizar quando aplicável.
- Titularidade da manutenção: ComoB,tentar editar/excluir registro deA por acesso direto,e repetir com registro removido/inexistente. Resultado esperado: Não alterar/remover indevidamente nem expor dados alheios.
- Visitante e não-confirmado: Tentar cadastro,consulta,detalhes,edição e exclusão sem sessão e com conta não confirmada. Resultado esperado: Exigir acesso conforme auth/confirmado,sem permitir operações ou revelar finanças.
- Visual e estados da tela nova: Comparar filtros,lista e diálogos com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (#transactions,#transaction-dialog,#detail-dialog,#delete-dialog),em computador/tablet/celular e claro/escuro/sistema,incluindo vazio,erros e processamento. Resultado esperado: Composição da referência,identidade fornecida,lista compacta móvel e dados completos nos detalhes;sem reconstrução da fundação visual.

## Regras e permissões

- Somente receitas/despesas realizadas,cinco campos obrigatórios,BRL com até duas casas,descrição120,data1900atéhoje local e categorias fixas por tipo.
- Dados próprios em todas as operações e acessos diretos;visitante/não-confirmado sem acesso.
- Histórico combina filtros,limpa mês,conta todas as correspondências,ordena por data/cadastro e pagina50;edição não muda identidade/ordem.
- Falhas não apresentam sucesso fictício;exclusão requer confirmação e é definitiva.

## Impactos relacionados

- Reutilizar autenticação e base visual fornecidas,sem reimplementar acesso,marca ou temas.
- Integrar manutenção ao histórico sob filtros e paginação,sem duplicar o registro ou perder o salvo fora do recorte.
- Disponibilizar os dados persistidos para futuros dashboard e IA,sem implementar essas capacidades aqui.

## Critérios de conclusão

- Executar CT-001 aCT-029 do documento aprovado,registrando resultado observado e evidência por condição.
- Conferir os trêsDEV integrados,fronteiras,estados,falhas,isolamento e visual;registrar desvios e impedimentos sem aprovar condição não executada.
- Manter a revisão do documento associada à QA e registrar preparação,resultados e reteste delimitado conforme execução.

## Referências

Item pai Redmine #1016105; regras/critérios R1, R2, R3, R4, R5, R6, R7, R8, R9, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CA9, CA10, CA11, CA12, CA10-Consulta, CA10-Manutencao, CA11-Consulta, CA11-Manutencao.

<!-- project-slices-child:70a52131290d8d1bae91bec162dbee2feb19a0259480bb1a6eb1e886c042baa6 -->

## Relações

- `#1016123` blocks `#1016126`
- `#1016124` blocks `#1016126`
- `#1016125` blocks `#1016126`
