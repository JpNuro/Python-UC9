# A02 — EX03 — Organização do trabalho
Ferramentas: editor, IDE, terminal PowerShell e Git local quando disponível.
Use papéis da equipe, não dados pessoais. Alterne autor e revisor durante a aula.

## Backlog e quadro
Estados: A fazer / Em andamento / Em revisão / Concluído.
Prioridade expressa valor/urgência; dependência indica o que precisa existir antes.
| ID | Ação pequena | Requisito | Prioridade | Depende de | Responsável | Revisor | Estado | Evidência de conclusão |
|---|---|---|---|---|---|---|---|---|
| T01 | Revisar o briefing e conferir se o problema, o usuário, o escopo e as dúvidas estão documentados. | Briefing; RF01, RF02 e RF03 | Alta | Nenhuma | João | Luisa | Feito | Arquivo briefing.md revisado, com fatos, hipóteses e decisões pendentes identificados |
| T02 | Preencher os três requisitos funcionais, as duas regras de negócio e o requisito de qualidade. | RF01, RF02, RF03, RQ01, RN01 e RN02 | Alta | T01 | João | Luisa | Feito | Arquivo requisitos.md preenchido, com IDs, prioridades e vínculos entre requisitos e regras. |
| T03 | Conferir os dados dos três equipamentos e repetir as simulações de saída válida, inválida e de fronteira. | RF01, RF02 e RN01 | Alta | T02 | Luisa | João | Feito | CSV conferido e três simulações documentadas com entradas, ações e resultados esperados coerentes. |
| T04 | Revisar os esboços das duas telas e verificar os campos, as ações, as mensagens e a navegação. | RF01, RF02 e RF03 | Média | T02 | Luisa | João | Feito | Duas telas descritas em texto e revisadas, com mensagens de sucesso e erro previstas. |
| T05 | Conferir os documentos da entrega e inspecionar a pasta e a raiz do Git pelo terminal, conforme o guia de apoio. | Todos os requisitos documentados | Alta | T01, T02, T03 e T04 | João | Luisa | Feito | Quatro documentos localizados, raiz Git verificada e plano de revisão anterior ao primeiro commit registrado. |

## Plano de versionamento
- Pasta nova de trabalho e raiz Git (sem expor nome de usuário): 
- Ferramenta/versão observada: VS Code e PowerShell; versão do Git git version 2.47.1.windows.1
- Arquivos que serão revisados antes do primeiro commit em A04: briefing.md, requisitos.md, backlog.md
- Arquivos que não devem entrar no histórico: senhas, tokens, credenciais, arquivos .env com segredos e dados pessoais desnecessários.
- Como conferir estado e alterações: utilizar git status --short, revisar o conteúdo dos arquivos alterados
- Quem revisa e qual evidência deve existir: A evidência é o documento revisado e o resultado das verificações realizadas.
- Pendência de instalação/permissão, se houver: 
- Plano de cópia de segurança autorizado pela instituição (Git local não substitui backup):

Concluído: cinco tarefas rastreáveis, papéis, dependências e evidências; estado Git confirmado ou pendência explícita.
Dica: “fazer sistema” é amplo; que pequena entrega outra pessoa consegue verificar?