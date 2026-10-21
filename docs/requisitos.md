# A02 — EX02 — Requisitos, regras e aceite
Objetivo: ligar necessidade a evidência observável. Ferramenta: editor e simulação em papel.
Complete três RF, duas RN e um RQ. Os IDs abaixo são espaços de trabalho, não respostas.
Não há código ou aplicação implementada nesta atividade.

## Requisitos
| ID | Descrição verificável | Necessidade atendida | Prioridade e justificativa | Regra vinculada |
|---|---|---|---|---|
| RF01 | O sistema deve exibir a identificação do equipamento e a quantidade disponível após uma consulta. | Encontrar equipamentos disponíveis. | Alta — é necessário saber o que pode ser emprestado. | RN01 |
| RF02 | O sistema deve registrar a saída informando equipamento, quantidade e responsável pelo empréstimo. | Controlar as saídas dos equipamentos. | Alta — evita empréstimos sem registro e permite identificar o responsável. | RN01 |
| RF03 | O sistema deve registrar devoluções totais ou parciais e atualizar a quantidade disponível. | Controlar as devoluções dos equipamentos. | Alta — mantém o controle do estoque atualizado. | RN02 |
| RQ01 | A consulta de disponibilidade deve apresentar o resultado em até 2 segundos, em condições normais de uso. O tempo será observado em 10 consultas. | Encontrar informações rapidamente. | Média — melhora a agilidade, mas o limite precisa ser validado pelo cliente. | Nenhuma; requisito de qualidade. |

## Regras do domínio
| ID | Regra proposta | Confirmada ou a confirmar? |
|---|---|---|
| RN01 | A quantidade solicitada para empréstimo deve ser maior que zero e não pode ultrapassar a quantidade disponível. | Confirmado |
| RN02 | A quantidade devolvida deve ser maior que zero e não pode ultrapassar a quantidade ainda emprestada. | Confirmado |

## Critérios e simulações da funcionalidade prioritária
| ID | RF/RQ | Condição inicial | Ação | Resultado esperado | Tipo de caso |
|---|---|---|---|---|---|
| CA01 | RF02 | Existem 10 unidades disponíveis e um responsável identificado. | Registrar a saída de 3 unidades. | A saída é registrada e a quantidade disponível passa para 7. | Válido |
| CA02 | RF02 | Existem 10 unidades disponíveis. | Tentar registrar a saída de 12 unidades. | A operação é rejeitada, uma mensagem informa a quantidade insuficiente e o estoque permanece com 10 unidades disponíveis. | Inválido |
| CA03 | RF02 | Existem 10 unidades disponíveis. | Registrar a saída de exatamente 10 unidades. | A saída é registrada e a quantidade disponível passa para zero. | Fronteira |

Resultado observado na simulação em papel (não é teste de software):
Ambiguidades descobertas: 
Não foi definido se o sistema deverá permitir reservas de equipamentos.
Não foi definido como identificar o responsável pelo empréstimo.
Decisão de correção:
Manter RN01 e RN02 como propostas até a revisão com o cliente
## Esboço de duas telas
Descreva título, campos, ações, resultado/erro e destino da navegação.
- Tela 1:
Título: Consulta de equipamentos.
Campos: nome ou código do equipamento.
Ações: botão “Consultar” e botão “Registrar saída”.
Resultado: identificação do equipamento e quantidade disponível.
Erro: se nenhum equipamento for encontrado, exibir “Equipamento não encontrado”.
Destino da navegação: ao selecionar “Registrar saída”, abrir a Tela 2.
- Tela 2:
Título: Registrar empréstimo.
Campos: código do equipamento, quantidade solicitada e identificação do responsável.
Ações: botão “Confirmar saída” e botão “Cancelar”.
Resultado: mensagem de sucesso e quantidade disponível atualizada.
Erro: se a quantidade for inválida ou superior à disponível, exibir uma mensagem e não registrar a saída.
Destino da navegação: após confirmar, retornar à Tela 1 com a disponibilidade atualizada; ao cancelar, retornar à Tela 1 sem alterar os dados.
## Dados e finalidade
| Campo | Para qual tarefa? | Exemplo sintético | Necessário ou dúvida? |
|---|---|---|---|
| codigo | Identificar o equipamento | EQ-001 | Necessário |
| descricao | Apresentar o nome do equipamento ao usuário | Notebook didático | Necessário para identificação |
| quantidade_disponivel | Informar quantas unidades podem ser emprestadas | 3 | Necessário |
| quantidade_solicitada | Informar quantas unidades serão emprestadas | 2 | Necessário |
| identificacao_responsavel | Registrar quem está retirando o equipamento | FUNC-001 | Necessário |
| quantidade_devolvida | Registrar quantas unidades estão sendo devolvidas | 1 | Necessário |
| condicao_equipamento | Identificar se o equipamento devolvido pode voltar a ficar disponível | Em condições de uso | Necessário |

Critério de conclusão: outra dupla consegue repetir a simulação e localizar os IDs ligados.
Dica: compare entradas válidas, inválidas e exatamente no limite que sua regra definiu.