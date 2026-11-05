# Execução pelo Ralph

Execute:

```sh
bash <plan-issue>/ralph.sh execute <pasta-dev>/planning.md
```

O Ralph lê as fases e o comando da suíte diretamente de `planning.md`. Ele cria automaticamente `.flow/ralph-state.json` ao lado do plano, contendo somente a fase atual, o gate atual, fases concluídas e seus commits. Apague esse arquivo para esquecer o progresso local; isso não desfaz commits nem mudanças do Git.

O Gate 3 seleciona o interpretador pelo bloco do baseline conforme [o contrato](planning-contract.md), inclusive no Windows, sem profiles interativos. Interpretador ausente, sintaxe Bash inválida, saída Bash 126/127 e saída cmd 9009 interrompem a execução como falha operacional, preservando alterações e estado, sem retornar ao desenvolvimento nessa execução. Outros códigos não zero continuam no ciclo de correção; essa classificação não identifica toda falha de ambiente possível. Scripts internos de ferramentas como Composer podem usar outro shell; confira sua portabilidade ao preparar o baseline.

## Gates de cada fase

1. **Desenvolvimento:** abre uma sessão nova do Codex para implementar somente a fase, sem commit.
2. **Validação:** abre outra sessão nova e somente leitura para revisar requisito, diff, testes, segurança e padrões.
3. **Testes:** o script executa diretamente a suíte completa declarada no baseline.
4. **Commit:** o script executa `git commit --no-verify` e segue para a próxima fase.

Uma reprovação da validação ou dos testes inicia outra sessão de desenvolvimento com o erro encontrado e repete os gates. O padrão é parar depois de três tentativas; altere com `--max-attempts N`. Falhas operacionais interrompem imediatamente e preservam as mudanças.

O executor usa `gpt-6.1-sol` por padrão nos gates de desenvolvimento e validação. Para escolher outro modelo, execute `ralph.sh execute <planning.md> --model <modelo>`. O esforço continua vindo da configuração do Codex CLI. O executor não acessa Redmine ou YouTrack e não usa subagentes. Por padrão, suas fases dependem da Codex CLI; `RALPH_AGENT_COMMAND_JSON` pode fornecer outro runner compatível como um array JSON de argumentos, e o modelo escolhido fica disponível em `RALPH_MODEL`. Essa dependência do backend é distinta da skill `ralph`, que pode ser conduzida no Codex, Claude Code ou OpenCode.

## Retomada e segurança mínima

Uma tarefa possui somente uma execução simultânea. Uma fase nova exige worktree limpo. Quando uma tentativa da fase já deixou mudanças, executar o mesmo comando novamente retoma essa fase pelo desenvolvimento. Se o processo terminou logo após o commit, um estado no gate de commit com worktree limpo reconhece o `HEAD` atual como commit da fase e continua.

O diretório `.flow` deve estar ignorado pelo Git. Não existem hashes, fingerprints, manifests, aprovação de baseline, prova por trailer ou reconciliação de evidências. O desenvolvedor continua responsável por revisar o histórico e decidir quando apagar o estado ou desfazer trabalho.

## Saída

Por padrão, o terminal mostra apenas mensagens humanas:

```text
Fase 1 iniciada
[DESENVOLVIMENTO] Gate 1 em andamento [08:48]
[DESENVOLVIMENTO] Gate 1 finalizado [08:52]
[VALIDAÇÃO] Gate 2 aprovado [08:55]
[TESTES] Gate 3 aprovado [08:58]
[COMMIT] Gate 4 finalizado [08:58]
Fase 1 finalizada
```

Erros mostram a causa sanitizada e o caminho do diagnóstico. Prompts, stdout, stderr, testes e eventos estruturados permanecem em `.git/ralph-runtime`. Use `--verbose` para exibir os eventos técnicos no terminal.

Os timeouts padrões são 60 minutos para desenvolvimento, 30 para validação e 60 para testes. Ajuste com `--dev-timeout-minutes`, `--validation-timeout-minutes` e `--tests-timeout-minutes`.
