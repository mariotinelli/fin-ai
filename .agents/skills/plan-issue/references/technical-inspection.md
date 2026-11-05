# Inspeção técnica

## Seguir o comportamento efetivo

Inspecione somente os caminhos relevantes às decisões e critérios da tarefa. Identifique implementação, configuração, inicialização, providers/plugins e versões instaladas que podem alterar o resultado. Ausência de configuração na aplicação não prova ausência de configuração por uma dependência.

Siga o caminho até o efeito observável. Confira sobrescritas e diferenças pertinentes entre produção, desenvolvimento e testes. Cite arquivo e símbolo, ou comando e resultado sanitizado, para afirmações que sustentam estado atual, arquitetura e riscos. Separe leitura de código de verificação executada; não exponha credenciais nem despeje configurações sensíveis.

Para dependência externa relevante, confira sucesso, falha e indisponibilidade no código instalado ou documentação compatível. Descreva o resultado real; se conflitar com o requisito, apresente a decisão necessária e o impacto. Não invente fallback ou alteração de política para fechar o plano. Registre como incerteza aquilo que não pôde confirmar.

**Concluído quando:** cada afirmação decisiva tem origem localizável, condições de ambiente relevantes estão explícitas e nenhuma hipótese foi apresentada como comportamento confirmado.

## Conferir o alcance da solução

Antes de propor mudança em default, configuração global ou componente compartilhado, localize seus consumidores e compare o comportamento afetado com o escopo aprovado, inclusive por ambiente. Registre os consumidores relevantes e a evidência que sustenta essa avaliação na arquitetura ou nos riscos.

Se a proposta modificar comportamento fora do escopo, prefira uma aplicação localizada que preserve o compartilhamento necessário. Se ampliar o alcance for necessário, apresente o impacto e a decisão de produto pendente antes de tratar a arquitetura como pronta. Declarar um fluxo fora do escopo não neutraliza alterações nele; adaptar suas fixtures também não demonstra preservação funcional. Uma mudança compartilhada é válida quando os efeitos estão autorizados ou a inspeção sustenta a preservação dos demais consumidores.

**Concluído quando:** o alcance real da solução é compatível com os limites da tarefa, e efeitos externos estão preservados com evidência ou dependem de decisão explícita.

## Descobrir verificadores e pré-requisitos

Expanda os scripts agregados até identificar verificadores, opções e configurações relevantes. Inclua formatação, análise estática, refatoração em modo de verificação, tipos, testes e cobertura conforme existirem; não imponha ferramentas de outra stack. Consulte CI pertinente sem declarar equivalência se não a verificou.

Confira runtime, gerenciadores e suporte à cobertura exigidos. Distinga comandos que apenas verificam daqueles que corrigem arquivos. Identifique um caminho reproduzível de execução no ambiente do projeto e do Ralph; não reduza exigências nem instale dependências para contornar um baseline bloqueado.

**Concluído quando:** o comando completo, sua composição e pré-requisitos são conhecidos, e seus efeitos permitem uma observação inicial sem modificar arquivos versionados.
