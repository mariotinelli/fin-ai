# [QA] [WEB] [USUARIO] Acesso à conta pessoal

- Redmine: `#1016122`
- Tipo: `QA`
- Tracker: Deliverable (`5`)
- Item pai: `#1016104`
- Estimativa: `1h`

## Descrição

## Objetivo

Verificar o acesso completo com ajustes de senha, restrição e retomada, preservando as jornadas existentes e consumindo a base visual FinAI.

## Jornadas integradas

- Cadastro público e confirmação: Cadastrar nome/e-mail válidos, senha conforme R3 e confirmação igual. Resultado esperado: Uma conta, sem convite/dados financeiros; enviar link e orientar confirmar, sem acesso ao produto.
- Campos obrigatórios: Omitir separadamente nome/e-mail/senha/confirmação no cadastro e os campos aplicáveis na redefinição. Resultado esperado: Impedir conclusão com erro; sem conta ou senha alterada indevidamente.
- Nome e e-mail nos limites: Usar entradas válidas de255 e256caracteres; e-mail inválido e duplicado. Resultado esperado: Até255aceito; excesso/formato/duplicação recusados, sem nova conta indevida.
- Senha nos limites: Nos dois fluxos usar senhas de composição completa não-vazadas com11,12,255 e256caracteres. Resultado esperado: 12/255aceitas;11/256recusadas com erro; mesma regra em teste e uso.
- Composição da senha: Nos dois fluxos omitir separadamente maiúscula, minúscula, número e símbolo, mantendo demais condições. Resultado esperado: Cada falta recusada; composição completa não rejeitada por esse motivo.
- Senha conhecida em vazamentos: Com dado controlado da verificação de senha vazada, tentar os dois fluxos com tamanho/composição válidos. Resultado esperado: Recusar ambos com erro e sem persistência indevida.
- Confirmação diferente: Informar senha válida com confirmação diferente no cadastro e redefinição. Resultado esperado: Impedir e indicar erro sem criar conta ou alterar senha.
- Visitante na área protegida: Sem sessão, abrir área inicial, perfil e configurações protegidas. Resultado esperado: Exigir login sem mostrar funcionalidades do produto.
- Conta não confirmada: Entrar sem confirmar e tentar área inicial, perfil GET/PATCH e configurações; repetir com lembrar. Resultado esperado: Manter restrição, orientação, reenvio e saída; sem acesso/alteração indevida no produto.
- Recuperar antes de confirmar: Como não-confirmado autenticado, sair e seguir ao pedido público existente. Resultado esperado: Permitir a jornada sem liberar produto ou dispensar confirmação.
- Confirmar link próprio: Abrir link próprio válido iniciando com e sem sessão. Resultado esperado: Autenticar quando necessário, confirmar titular e liberar área inicial.
- Confirmação inválida: Alterar dados/assinatura do link e abrir como titular não confirmado. Resultado esperado: Não confirmar nem liberar; orientar novo link próprio.
- Confirmação expirada: Abrir link após sua validade. Resultado esperado: Não confirmar/liberar; orientar e oferecer novo pedido.
- Confirmação de outra conta: Como A não confirmado, abrir link válido de B. Resultado esperado: Não confirmar A/B indevidamente; caminho de novo pedido próprio de A.
- Reabrir confirmação: Confirmar conta e reabrir o mesmo link ainda válido. Resultado esperado: Manter confirmação e permitir área inicial.
- Falha de envio inicial: Provocar falha no cadastro, restaurar envio e repetir conforme orientação. Resultado esperado: Informar falha/retomada sem falso sucesso, duplicação ou titular sem caminho de confirmação/recuperação.
- Falha no reenvio: Como não-confirmado, provocar falha de reenvio, restaurar e tentar de novo. Resultado esperado: Não alegar envio concluído; após retomada, receber link e confirmar.
- Login e destino: Entrar diretamente e após solicitar destino protegido; testar credenciais incorretas. Resultado esperado: Corretas acessam área inicial/destino; incorretas não autenticam.
- Cinco falhas e espera: Para mesmo e-mail/origem, falhar cinco vezes e tentar durante bloqueio e após espera. Resultado esperado: Informar espera sem autenticar durante bloqueio; após prazo, aceitar credenciais válidas.
- Saída e lembrança: Entrar/sair e reabrir área protegida com lembrar marcado e desmarcado. Resultado esperado: Retornar à página pública e exigir novo login, inclusive após lembrança.
- Pedido genérico: Com envio disponível, pedir recuperação para conta existente e inexistente. Resultado esperado: Mesma resposta; titular cadastrado recebe link sem revelação pela resposta.
- Redefinição válida: Com link próprio não usado antes de60min, informar senha conforme R3/confirmação e testar senha anterior/nova. Resultado esperado: Retornar ao login; nova funciona e antiga não permite novos logins.
- Redefinir sem confirmar e-mail: Redefinir conta não confirmada e entrar com senha nova. Resultado esperado: Senha muda, e-mail permanece não confirmado e produto continua restrito.
- Recuperação inválida: Tentar redefinir com link inválido e usar novo pedido. Resultado esperado: Não alterar; orientar e oferecer novo link para retomada.
- Recuperação expirada: Tentar após ultrapassar60min da emissão; solicitar outro link. Resultado esperado: Recusar sem alterar e permitir retomar com novo link válido.
- Recuperação já usada: Redefinir e reutilizar o mesmo link para outra senha. Resultado esperado: Não alterar de novo; recusar e oferecer novo pedido.
- Falha de envio de recuperação: Provocar falha, restaurar e solicitar de novo. Resultado esperado: Orientar sem sucesso fictício/revelação explícita da conta; titular recebe link após retomada.
- Integração visual: Em computador/tablet/celular, claro/escuro/sistema, percorrer as telas e os novos estados de erro/retomada. Comparar com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101 e o fornecedor de composição #1016114 após base verificada. Resultado esperado: Identidade, campos, botões, erros e ações coerentes/usáveis, sem reconstruir a aparência fornecida.

## Regras e permissões

- Cadastro aberto e campos/limites de R2, com R3 consistente nos dois fluxos em teste e uso.
- Produto exige autenticação e e-mail próprio confirmado; receber mensagem ou redefinir senha não confirma a conta.
- Recuperação60min e uso único; preservar cinco falhas/espera no login e saída explícita com lembrar.
- Consumir base visual implementada/verificada; conferir os estados de acesso novos sem repetir a homologação visual integral do fornecedor.

## Impactos relacionados

- Preservar login, saída, lembrar e limitação existentes, sem criar DEV para reconstruí-los.
- Restrições incluem acessos diretos a perfil e configurações e o estado de e-mail confirmado.
- Falhas de transporte/links não causam duplicação, senha alterada indevidamente ou sucesso fictício.

## Critérios de conclusão

- Executar CT-001 a CT-028 do documento aprovado, com resultado observado e evidência por condição.
- Confirmar jornadas, fronteiras, titularidade/tempo, retomada e preservação; indicar desvios e impedimentos sem aprovar condição não executada.
- Conservar a revisão de condições associada à QA e registrar preparação, resultado e reteste delimitado conforme executado.

## Referências

Item pai Redmine #1016104; regras/critérios R1, R2, R3, R4, R5, R6, R7, R8, R9, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CA9, CA10, CA11, CA12, CA11-Confirmacao, CA11-Recuperacao.

<!-- project-slices-child:262e0702dd9d2eac558430f4f55ac36eda8088a664ea86031402145037c82d5e -->

## Relações

- `#1016119` blocks `#1016122`
- `#1016120` blocks `#1016122`
- `#1016121` blocks `#1016122`
