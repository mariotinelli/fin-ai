# Inspeção técnica

## Seguir o comportamento efetivo

Inspecione somente os caminhos relevantes às decisões e critérios da tarefa. Identifique implementação, configuração, inicialização, providers/plugins e versões instaladas que podem alterar o resultado. Ausência de configuração na aplicação não prova ausência de configuração por uma dependência.

Siga o caminho até o efeito observável. Confira sobrescritas e diferenças pertinentes entre produção, desenvolvimento e testes. Cite arquivo e símbolo, ou comando e resultado sanitizado, para afirmações que sustentam estado atual, arquitetura e riscos. Separe leitura de código de verificação executada; não exponha credenciais nem despeje configurações sensíveis.

Para dependência externa relevante, confira sucesso, falha e indisponibilidade no código instalado ou documentação compatível. Descreva o resultado real; se conflitar com o requisito, apresente a decisão necessária e o impacto. Não invente fallback ou alteração de política para fechar o plano. Registre como incerteza aquilo que não pôde confirmar.

**Concluído quando:** cada afirmação decisiva tem origem localizável, condições de ambiente relevantes estão explícitas e nenhuma hipótese foi apresentada como comportamento confirmado.

## Descobrir verificadores e pré-requisitos

Expanda os scripts agregados até identificar verificadores, opções e configurações relevantes. Inclua formatação, análise estática, refatoração em modo de verificação, tipos, testes e cobertura conforme existirem; não imponha ferramentas de outra stack. Consulte CI pertinente sem declarar equivalência se não a verificou.

Confira runtime, gerenciadores e suporte à cobertura exigidos. Distinga comandos que apenas verificam daqueles que corrigem arquivos. Identifique um caminho reproduzível de execução no ambiente do projeto e do Ralph; não reduza exigências nem instale dependências para contornar um baseline bloqueado.

**Concluído quando:** o comando completo, sua composição e pré-requisitos são conhecidos, e seus efeitos permitem uma observação inicial sem modificar arquivos versionados.
