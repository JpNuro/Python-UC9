## Pedido recebido
Precisamos controlar empréstimos de equipamentos, consultar disponibilidade e registrar saídas e devoluções. O cliente pediu rapidez e segurança, ainda sem critérios definidos.

## Problema e resultado desejado
- Problema observado no cenário: utilidade e sensibilidade de dados com fácil acesso
- Quem utilizará (papel, não nome real): funcionário
- Resultado desejado: um sistema que seja capaz de registrar fluxo (entrada e saída) e disponibilidade de equipamentos com rapidez e segurança 
- Dentro do escopo inicial: consultar a disponibilidade dos equipamentos; registrar a saída de equipamentos; registrar a devolução de equipamentos; utilizar três equipamentos fictícios do CSV como amostra; documentar regras, critérios de aceite e simulações em papel.
- Fora do escopo inicial: conexão com banco de dados; integração com sistemas externos; implementação do aplicativo nesta atividade; uso de dados reais de pessoas; definição definitiva de regras ainda não confirmadas pelo cliente.

## Perguntas ao cliente
| ID | Pergunta | Impacto da resposta | Resposta ou “a confirmar” |
|---|---|---|---|
| D01 | Quem poderá consultar, registrar saídas e confirmar devoluções? | Define os usuários e as permissões de acesso necessárias. | Apenas funcionários autorizados poderão registrar empréstimos e devoluções. |
| D02 | Quando um equipamento deve ser considerado disponível: apenas quando não estiver emprestado ou também quando estiver em manutenção ou indisponível por outro motivo? | Define os critérios usados para apresentar a disponibilidade. | Disponível significa não emprestado, em manutenção ou com defeito. |
| D03 | Como deverá funcionar uma devolução parcial, quando apenas parte dos equipamentos emprestados for devolvida? | Define como atualizar os registros e calcular a disponibilidade após a devolução. | Devoluções parciais atualizam individualmente cada equipamento devolvido. |

## Decisões
| ID | Decisão/hipótese | Estado (proposta/confirmada) | Evidência da confirmação |
|---|---|---|---|
| DEC01 | Utilizar três equipamentos fictícios do CSV como amostra inicial. | Confirmada | Orientação da atividade |
| DEC02 | Permitir que funcionários autorizados consultem a disponibilidade e registrem saídas e devoluções. | Proposta | Resposta D01 |
| DEC03 | Considerar disponíveis somente equipamentos que não estejam emprestados nem indisponíveis por manutenção ou defeito. | Proposta | Resposta D02 |
| DEC04 | Permitir devoluções parciais e atualizar a disponibilidade de cada equipamento devolvido individualmente. | Proposta | Resposta D03 |
| DEC05 | Não utilizar banco de dados nem implementar o aplicativo nesta atividade. | Confirmada | Orientação da atividade |

## Revisão
O revisor consegue separar pedido, hipótese e decisão? Registre observação e melhoria.
Concluído quando problema, escopo, três dúvidas e decisões pendentes estão claros.
Dica: pergunte qual informação mudaria o comportamento do futuro aplicativo.