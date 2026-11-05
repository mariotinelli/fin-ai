# Estimativa e calibração

## Estabelecer a base

Identifique requisito e revisão, contexto da equipe, capacidades existentes, adaptações e fornecedores pendentes. Use a referência indicada pelo usuário ou pelas instruções do projeto; não exija arquivo novo nem procure configuração pessoal. Sem histórico, estime pela evidência e declare as premissas. Valores de outro projeto não são padrões universais.

Trate horas como esforço de trabalho, distinguindo espera de execução. Declare quais atividades DEV e QA estão incluídas, ferramentas e familiaridade relevantes, preparação e reteste. Pergunte apenas sobre premissas desconhecidas que alterem materialmente a proposta; não presuma uso de IA ou ambiente pronto.

Diferencie as fontes:

- Número herdado sem contexto: não copiar como autoridade.
- Referência calibrada pelo tech lead: usar por analogia, explicitando semelhanças e diferenças de escopo e execução.
- Correção explícita da proposta: registrar autoria e preservar o valor anterior, sem chamá-la de cálculo independente.
- Tempo realizado: registrar escopo executado, preparação e espera separadamente. Estimativa corrigida não é medição de execução.

**Concluído quando:** contexto e fontes estão identificados e nenhuma premissa desconhecida é apresentada como fato.

## Estimar o trabalho restante

Considere mudança, integração e verificação relevante. Preparação comum tem um dono e é contabilizada uma vez. Capacidade publicada mas não implementada é fornecedor pendente, não reuso comprovado. Estime o esforço do consumidor sem reconstruir o fornecedor.

Explique o esforço dominante de forma curta; decomponha horas somente quando ajudar uma decisão. Não acrescente blocos mínimos automáticos por camada, critério, revisão ou regressão. Tarefas simples com reuso podem ser rápidas; integrações iniciais complexas e muitos testes manuais podem exigir mais horas. Não aplique desconto uniforme nem distribua horas igualmente entre tarefas.

Explicite a dúvida técnica e seu impacto concreto antes de acrescentar esforço por incerteza. Inspecione fatos verificáveis; use Study apenas quando a dúvida impedir uma proposta coerente. Confira reuso, duplicação e calibração antes de dividir por ultrapassar seis horas. Se continuar acima, refine o resultado funcional ou encaminhe para revisão de escopo; não reduza horas para passar no limite.

**Concluído quando:** trabalho, reuso, verificação e diferenças em relação à referência têm justificativa revisável.

## Dimensionar QA

Estime preparação efetiva, jornadas, testes manuais específicos, conferência de evidências automatizadas pertinentes e registro dos resultados. QA integrada e verificação da DEV têm objetivos distintos; explicite a razão de repetições necessárias.

Agrupe execução com preparação e dados compartilhados, preservando a rastreabilidade de todas as condições. Não use porcentagem do DEV nem minutos fixos por condição. Muitos critérios simples podem ser mais rápidos que poucas jornadas com IA, concorrência ou resultado incerto. Automação só reduz execução manual quando há evidência adequada; não presuma cobertura nem remova critérios para caber nas horas.

Declare massa, ambiente, relógio e falhas controláveis necessários. Preparação inexistente não é gratuita; espera não é esforço ativo. Explicite o tratamento de retestes sem acrescentar campanha indefinida.

**Concluído quando:** QA mantém cobertura completa e sua estimativa distingue execução manual, evidências automatizadas e preparação.

## Revisar e aprender

Forneça aos avaliadores o mesmo contexto e referências comparáveis, sem revelar a estimativa candidata um do outro. Um verifica entrega e esforço restante; outro, reuso, sobreposição e testes. Reconcilie premissas pela evidência, não pela maior estimativa, média automática ou concordância dos agentes.

Entregue ao fluxo chamador base, premissas e correções para persistência nas decisões da proposta. Ao mudar os cortes, compare por comportamento e revisão, não por posição na lista. Preserve referências locais no projeto, sem transferir seus números automaticamente para outras equipes.

**Concluído quando:** estimativa do agente e correção humana são distinguíveis e a próxima revisão pode recuperar o contexto que sustenta as horas.
