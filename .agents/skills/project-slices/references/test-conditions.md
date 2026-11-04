# Condições de teste e DOCX local

Para alterar condições depois de uma publicação concluída, inclusive ajustes no Word sem mudança do requisito, siga [revisão localizada das condições](condition-revisions.md). O ramo abaixo prepara a decomposição e seu documento inicial.

## Usar DOCX nas novas publicações

Toda nova decomposição de Feature, Bug e caminho somente QA entrega as condições em DOCX e anexa esse arquivo à tarefa QA. O Markdown legível continua sendo gerado como prévia e artefato local complementar; ele não substitui o documento Word nem conclui a publicação.

Registre `test_conditions.document_format: docx`. Quando o campo estiver ausente em uma proposta nova, `record-proposal` o define como `docx`; uma proposta ou preferência nova que selecione Markdown é rejeitada antes da aprovação. O formato fica vinculado ao hash da proposta aprovada, e a publicação só pode ser concluída depois de gerar, enviar, associar e observar o DOCX na QA.

Estados históricos sem o campo conservam seu contrato DOCX. Uma nova revisão pode mudar o formato com a aprovação da prévia, preservando todos os arquivos, anexos e decisões anteriores. Uma leitura ou retomada não migra históricos.

**Concluído quando:** a proposta registra DOCX e nenhuma nova publicação pode interpretar o Markdown local como substituto do anexo QA.

## Preparar e revisar

Depois da inspeção e junto da proposta, aplique a [disciplina de condições de teste](../../vertical-slicing/references/test-conditions.md). Registre as condições em `test_conditions` da proposta `.work/slices-proposal.json`; `record-proposal` preserva essa fonte estruturada integralmente em cada revisão de `.flow/slices-state.json`.

Exemplo de campos, usando IDs reais de `requirements` da proposta:

```json
{
  "test_conditions": {
    "context": "Operador autenticado na área de gestão de usuários.",
    "conditions": [
      {
        "id": "CT-001",
        "title": "Consultar o cadastro concluído",
        "context": "Conta com a permissão aprovada de gestão.",
        "verification": "Cadastrar um usuário permitido e consultar seu cadastro.",
        "expected_result": "A consulta apresenta os dados persistidos do usuário cadastrado.",
        "requirement_ids": ["R1"]
      }
    ]
  }
}
```

`context` do documento e a lista não vazia de condições são obrigatórios. Em cada condição, `id`, `title`, `verification`, `expected_result` e `requirement_ids` são obrigatórios; `context`, `group` e `impact_justification` são textos opcionais, presentes quando úteis. Use `impact_justification` para registrar o impacto que sustenta uma regressão externa. Omita campos opcionais sem conteúdo. O schema está em `schemas/slices-state.schema.json`.

Cada condição referencia ao menos um ID de `requirements`; todas as regras/critérios da proposta precisam de referência nas condições. Os IDs de requisitos são o mapa local do requisito aprovado: confira semanticamente suas origens no documento canônico. O helper verifica campos, referências e IDs únicos, não o significado ou a suficiência dos cenários. IDs de condições removidas ficam reservados no histórico; reordenar ou editar uma condição mantida conserva sua identidade.

Execute `record-proposal` e `render` pelo contrato de [entrada e persistência](input-and-persistence.md). A prévia `slices/slices.md` apresenta contexto, condições e resultados esperados junto das fatias. Resolva lacunas no requisito antes de aprovar as condições afetadas. Obtenha a aprovação conjunta do tech lead e execute `approve`, seguido de `validate --previous` com o estado anterior preservado.

**Concluído quando:** a revisão corrente contém as condições revisadas semanticamente, e uma aprovação válida do tech lead referencia o hash exato da proposta completa. Alterações exigem novo `record-proposal` e nova aprovação, preservando as revisões anteriores.

## Entregar Markdown e gerar o DOCX obrigatório

Além do DOCX, a publicação gera `slices/condicoes-teste-rNNN.md` a partir da fonte aprovada e inclui as condições na prévia completa. Entregue o Markdown legível e o documento Word ao tech lead junto dos links das filhas. A descrição existente da QA permanece preservada.

Execute a geração com `document_format: docx`:

Use Python 3.10+ com sua biblioteca padrão, sem instalar bibliotecas adicionais:

```sh
python <project-slices>/scripts/manage_slices.py render-test-conditions .flow/slices-state.json slices/condicoes-teste-r001.docx
```

Substitua `001` pela revisão corrente da decomposição, com ao menos três dígitos. O documento identifica Feature/Bug, ID Redmine, revisão da decomposição, hash da proposta, revisão do requisito por SHA-256, contexto e condições com suas origens. O título é **Condições de teste**. Trata-se de orientação para a verificação futura, sem resultados de execução ou evidências inventadas.

O helper exige aprovação válida, reconfere o requisito e gera bytes determinísticos para a mesma fonte e aprovação. Ele informa caminho e SHA-256 do DOCX. Revisões anteriores permanecem em seus arquivos. Uma repetição idêntica é permitida; um arquivo existente com bytes diferentes é preservado. Se houve edição no Word, incorpore os ajustes à fonte estruturada, revise e aprove uma nova proposta antes da geração seguinte.

**Concluído quando:** o tech lead revisou as condições na prévia completa, recebe o Markdown versionado e o documento determinístico da mesma fonte, e o arquivo Word foi incluído conforme [publicação e retomada do anexo](attachment-publication.md). O registro de publicação reaproveita a decisão da prévia completa, sem nova pergunta equivalente; divergência entre fonte, documento e conteúdo apresentado exige nova prévia.

## Compatibilidade

Após mudança do requisito, siga [condições após mudança do requisito](requirement-condition-revisions.md). Novos documentos identificam o requisito aprovado que os fundamenta; uma mudança exclusivamente editorial pode conservar o documento original mediante revisão semântica aprovada. Os IDs de condições mantêm o mesmo histórico nos ramos localizado e funcional.

Propostas novas exigem condições em DOCX. Revisões e aprovações históricas sem esse campo ou com formato Markdown continuam válidas e não são migradas automaticamente; o gerador apenas informa o contrato histórico. Uma vez incluído o contrato DOCX, revisões seguintes não podem descartá-lo. A geração local não modifica a descrição QA, a publicação corrente, o estado do pai nem artefatos canônicos de filhas.
