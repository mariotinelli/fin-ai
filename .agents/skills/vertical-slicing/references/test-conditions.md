# Condições de teste do item completo

## Preparar com evidência

Ao estimar QA, aplique [estimativa e calibração](estimation.md). Agrupe execução com dados e preparação compartilhados, preservando todas as condições e seus resultados. Distinga testes manuais necessários de evidências automatizadas disponíveis; quantidade de condições não determina horas. Mantenha explícitos preparação, reteste e verificações de integração que não estejam cobertas pela DEV.

Depois da inspeção, derive do requisito aprovado o que o profissional de QA deve verificar e qual resultado observável deve encontrar. A condição pertence à Feature ou ao Bug inteiro: inclua capacidades existentes relevantes, interações entre fatias e preservações necessárias. Uma regressão fora da entrega precisa de uma relação de impacto justificável pela inspeção; explicite essa justificativa.

Para Bugs, represente a situação de reprodução, o resultado corrigido e as regressões relacionadas. No caminho somente QA, use a mesma análise de cobertura, mesmo sem fatias DEV.

Avalie sucesso, alternativas, erros, permissões, limites, integrações e preservação conforme a relevância. Essa avaliação não impõe grupos nem quantidade mínima por categoria. Dados, contexto e passos entram quando necessários para eliminar ambiguidade; agrupamentos servem à leitura. Prioridade e objetivo de risco separados não são obrigatórios.

**Concluído quando:** cada comportamento aprovado tem condições verificáveis, as capacidades existentes e interações relevantes estão contempladas e toda regressão externa tem impacto justificável.

## Resolver lacunas e revisar significado

Uma condição contém ID estável, título, verificação, resultado esperado e origem no requisito; contexto é incluído quando necessário. Preserve o ID quando a condição continuar representando o mesmo comportamento, inclusive após ajustes editoriais. Uma condição nova recebe um novo ID; IDs removidos permanecem reservados no histórico.

Compare condições, requisito, evidências da inspeção e proposta de fatias. Referenciar um ID de requisito comprova o vínculo estrutural, mas não comprova que o resultado esperado é correto nem que todos os cenários foram cobertos. Se a inspeção revelar comportamento ausente ou contraditório, devolva a lacuna ao fluxo chamador para resolver o requisito antes da aprovação das condições afetadas.

Use os [cenários de avaliação](test-condition-scenarios.json) ao revisar a disciplina. Eles avaliam decisões semânticas; não representam execução do produto.

**Concluído quando:** nenhuma condição inventa comportamento, cada resultado é observável e sustentado, e a revisão conjunta com as fatias não deixa lacunas ou contradições abertas. O fluxo chamador coleta a aprovação, persiste a fonte e gera o documento.
