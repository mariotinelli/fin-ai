# Fatiamento sequencial de escopo

Use este ramo quando o tech lead pedir um escopo ou não indicar uma Feature ou Bug. Ele coordena várias execuções do fluxo principal; cada item conserva sua própria inspeção, aprovação da prévia completa, publicação e releitura.

## Selecionar

Sem entrada, execute `manage_scope.py list <docs/harness>` e apresente somente escopos que tenham ao menos uma Feature ou Bug ativo, aprovado e ainda pendente ou em andamento. Mostre também `fatiadas/total` e as quantidades `pendente`, `em andamento`, `concluída` e `aguardando requisitos`, então pergunte qual escopo processar. O total inclui toda Feature e todo Bug ativo do catálogo; itens retirados não entram.

O helper valida o estado real do `project-flow`, a aprovação da projeção completa do catálogo e sua ordem. Um item sem artefato ou requisito concluído fica `aguardando requisitos`; ele não desaparece do total e não impede trabalhar outro item elegível. Caminho inseguro, vínculo de catálogo obsoleto, tipo, entrega ou ID Redmine divergente é erro, não espera.

**Concluído quando:** o tech lead escolheu uma das opções derivadas do catálogo aprovado e viu a distribuição integral das Features e Bugs ativos.

## Iniciar ou retomar

Para uma seleção nova, execute:

```sh
python <project-slices>/scripts/manage_scope.py start <scope-dir> --actor "<tech lead>" --at "<ISO-8601>"
```

O estado fica em `<scope-dir>/.flow/slices-scope-state.json`, separado do progresso de requisitos e execução do `project-flow`. Ele se vincula ao `internal_identity`, projeto e hash da projeção aprovada do catálogo, não aos bytes mutáveis de `scope-state.json`.

Se o estado estiver pausado, execute `resume`. Se estiver ativo, execute `refresh`. Retome `current_item_id`; jamais escolha por um flag informado em conversa. A conclusão prévia só vale quando `slices-publication.json` passa pelo validador RST13, possui a aprovação final corrente, todas as criações e relações concluídas e evidência de readback. Assim, uma retomada pula o item já publicado sem repetir seus gates ou operações.

**Concluído quando:** o estado durável aponta para o primeiro item elegível ainda não processado na ordem aprovada, ou explicita que só restam requisitos em espera.

## Processar uma Feature ou Bug

Execute integralmente o ramo de item pai deste skill para `current_item_id`. Dependências do catálogo explicam a ordem, mas não bloqueiam o fatiamento. Um bloqueio de implementação pertence às filhas e também não interrompe o processamento dos próximos itens.

Cada item mantém separadamente:

1. conferência do requisito aprovado e publicado;
2. uma decisão sobre a prévia completa da decomposição e publicação pelo tech lead;
3. reutilização dessa decisão enquanto o conteúdo autorizado permanecer válido;
4. criação e relações reconciliadas;
5. readback integral das filhas e bloqueios.

Não agregue aprovações ou publicações entre itens.

**Concluído quando:** a publicação individual está `completed` com seu readback validado, ou o item permanece explicitamente pendente/em andamento sem alegação de conclusão.

## Mostrar progresso e continuar

Reaproveite a [preferência de formato das condições](test-conditions.md#escolher-e-reaproveitar-o-formato) em todos os itens. Passe o mesmo arquivo de preferências a `record-proposal`; uma retomada conserva o formato já aprovado sem perguntar por Word novamente.

O pedido de processamento do escopo autoriza avançar entre itens elegíveis. Após cada conclusão, execute `refresh`, mostre concluídos, pendentes, impedimentos e próximo passo, e processe `current_item_id` sem nova pergunta de continuar/parar. `refresh` também libera uma espera legada em `awaiting_decision_for`; conserva `continuation_decisions` como histórico, sem exigir novos registros. Decisões de produto e aprovação da prévia de publicação continuam necessárias; autorizações válidas não são renovadas na retomada.

Quando faltar uma decisão ou capacidade necessária ao item, registre o impedimento e a condição concreta para resolvê-lo:

```sh
python <project-slices>/scripts/manage_scope.py block <scope-dir> --item <catalog-item-id> --reason "<decisão/capacidade ausente e condição de retomada>" --actor "<responsável>" --at "<ISO-8601>"
```

O helper seleciona o próximo item independente na ordem preferencial. Registre também os itens cujo fatiamento realmente depende da decisão ausente; uma dependência de implementação entre filhas, por si só, não impede preparar ou publicar seu fatiamento. Mostre os eventos de bloqueio ainda não resolvidos junto ao progresso. Após verificar a resolução, use `unblock` com os mesmos argumentos e evidência em `--reason`, depois execute `refresh` para revalidar os artefatos antes de agir.

Atenda imediatamente um pedido de pausa, inclusive durante um item. Finalize somente uma escrita local atômica em curso e execute, sem novas operações remotas:

```sh
python <project-slices>/scripts/manage_scope.py pause <scope-dir> --reason "<pedido do usuário>" --actor "<tech lead>" --at "<ISO-8601>"
```

`pause` salva o progresso sem depender de acesso remoto. `refresh` preserva a pausa; `resume <scope-dir> --actor "<tech lead>" --at "<ISO-8601>"` registra a retomada e recalcula o próximo elegível. Antes de repetir qualquer operação incerta, reconcilie seu resultado no fluxo individual; mantenha operações concluídas, conteúdo humano e aprovações válidas.

**Concluído quando:** o progresso está persistido e o próximo passo coincide com o estado validado, ou a pausa está registrada e nenhuma nova operação é iniciada.

## Concluir

O helper conclui automaticamente apenas quando `fatiadas == total`. Uma Feature ou Bug ativo aguardando requisitos mantém o escopo incompleto, mesmo que não exista outro item elegível agora. Reporte essa espera sem transformar requisitos ausentes em item retirado. Mostre também `dependency_status`: ele acompanha se relações externas estão `pending`, `refining` ou `ready` sem desfazer a publicação concluída nem afirmar que a capacidade bloqueadora já foi implementada.

**Concluído quando:** todas as Features e Bugs ativos possuem roteamento DEV/QA individual completo e verificado; caso contrário, informe escopo incompleto, itens concluídos e pendentes, decisão/capacidade que falta e próximos passos. Preserve exatamente o progresso e a razão observável da espera.
