# Contrato de `planning.md`

O planejamento fica ao lado de `task.md` e é o único artefato entregue ao Ralph. Ele não contém hashes, aprovações, cópias do Redmine nem estado operacional.

## Estrutura

Use estas seções de segundo nível antes das fases:

- `Identidade e fontes`: filha, requisito pai e caminhos locais usados.
- `Objetivo`: resultado observável da tarefa.
- `Estado atual`: comportamento e implementação encontrados.
- `Escopo`: o que entra e o que fica fora.
- `Arquitetura`: padrões e decisões existentes que orientam a implementação.
- `Estratégia`: ordem geral e abordagem de testes.
- `Baseline`: comando agregado, composição dos verificadores, pré-requisitos, resultado inicial e falhas ou impedimentos conhecidos.
- `Riscos`: regressões, migrações, segurança e pontos de atenção.

Em um plano executável, coloque em `Baseline` exatamente um bloco cercado com o comando executável da suíte. Se nenhum comando seguro completo puder ser determinado, mantenha somente um rascunho explicitamente impedido, sem bloco fictício. Esse rascunho não atende ao parser e não deve ser entregue para execução; complete o comando antes do encaminhamento ao Ralph. O resultado é uma observação inicial; cada fase continua exigindo que o gate de testes passe:

````markdown
## Baseline

Comando da suíte completa:

```sh
composer test
```

Resultado inicial: impedido pelo ambiente; nenhum teste funcional executado.
Pré-requisito pendente: runtime compatível com o projeto. O comando acima só poderá ser usado após sua seleção no ambiente do executor.

| Verificador | Invocação/configuração | Exigência relevante | Resultado observado |
| --- | --- | --- | --- |
| Análise estática | `composer test:types` | Runtime declarado no projeto | Falhou ao inicializar: runtime incompatível |
| Testes | `composer test:unit` | Cobertura configurada pelo projeto | Não executado: etapa anterior interrompeu o comando |
````

O exemplo é ilustrativo: use os verificadores e resultados efetivos do projeto. Comandos individuais ficam inline na tabela, sem novos blocos cercados dentro de `Baseline`. Diferencie passou, falhou e não executado; se a saída agregada não permite conhecer o resultado individual, declare essa limitação. Uma interrupção não autoriza atribuir resultado às etapas seguintes.

Registre falhas sanitizadas e pré-requisitos de execução. O comando único deve representar o gate completo e funcionar no ambiente do executor, incluindo a seleção de runtime quando necessária. Se não houver caminho seguro conhecido, marque o plano como operacionalmente impedido, sem inventar comando aprovado ou anunciar prontidão. Testes focados ficam nas fases e não substituem o gate completo. Durante implementação, alterações feitas por ferramentas de correção precisam ser revisadas no diff.

Depois, escreva uma ou mais fases em ordem crescente:

```markdown
## Fase 1 — Nome da entrega

### Objetivo
...

### Dependências
...

### Mudanças esperadas
...

### Arquivos prováveis
...

### Limites
...

### Estratégia
...

### Aceite
...

### Verificação focada
...
```

Cada fase deve ser implementável em uma sessão nova, deixar uma mudança coerente para commit e incluir critérios que a validação independente consiga comprovar. Os caminhos são hipóteses fundamentadas, não uma obrigação de editar todos os arquivos listados.

## Revisão

Antes de apresentar, confronte cada comportamento da tarefa com as mudanças e a evidência de aceite da fase responsável. Inclua sucesso, falhas relevantes e limites válidos e inválidos quando definidos pelo requisito. Um estado interno só basta quando comprova o resultado exigido; permissões ou acesso precisam de evidência do comportamento protegido, inclusive após a operação quando pertinente.

Identifique o que os testes existentes já demonstram e as lacunas a preencher. Reutilize cobertura adequada, preservando testes existentes e evitando duplicação. Escolha endpoint, integração ou navegador conforme o resultado a comprovar, sem testar apenas declarações da implementação. Essa correspondência aparece no aceite e nas verificações das fases; não exige manifesto ou matriz separada. Nenhuma lacuna autoriza ampliar o requisito ou implementar tarefas irmãs.

Mostre o arquivo completo ao desenvolvedor. Edite diretamente `planning.md` até ele concordar. Não registre aprovação em outra estrutura. Se o conteúdo apresentado mudar, mostre a nova versão antes de executar. O Ralph lê o arquivo atual; para reiniciar todas as fases, apague `.flow/ralph-state.json` somente depois de decidir o destino dos commits e mudanças existentes.
