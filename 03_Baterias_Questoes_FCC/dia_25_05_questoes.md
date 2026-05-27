# Bateria de Questões FCC — Segunda-feira 25/05

Este arquivo contém 45 questões aprofundadas da banca FCC (15 por tema estudado no dia) com gabarito comentado detalhado.

---

## 📝 TEMA 1: Engenharia de Software — Engenharia de Requisitos

### Questão 1 (FCC)
No levantamento e análise de requisitos, a equipe classificou as seguintes necessidades:
I. O sistema deve emitir o relatório em, no máximo, 5 segundos.
II. O sistema deve validar a assinatura digital ICP-Brasil.
III. O desenvolvimento da interface deve ser realizado no framework Angular homologado pelo tribunal.
De acordo com Sommerville, os itens I, II e III correspondem a requisitos:
A) Não funcional de produto; Funcional; Não funcional organizacional.
B) Funcional; Não funcional de produto; Não funcional externo.
C) Não funcional de desempenho; Não funcional de segurança; Funcional.
D) Funcional; Funcional; Não funcional de produto.
E) Não funcional externo; Funcional; Não funcional organizacional.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. I = Desempenho (Produto); II = Ação (Funcional); III = Restrição corporativa (Organizacional).
</details>

### Questão 2 (FCC)
Em um diagrama de Casos de Uso, quando o comportamento de B só é executado caso certa regra ocorra durante A, esse relacionamento é:
A) `<<include>>`, B para A.
B) Generalização, A para B.
C) `<<extend>>`, B para A.
D) `<<extend>>`, A para B.
E) `<<include>>`, A para B.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Relacionamento opcional é `<<extend>>`, apontando do estendido (B) para o base (A).
</details>

### Questão 3 (FCC)
A capacidade de relacionar um requisito a um trecho de código que o implementa é:
A) Rastreabilidade de origem.
B) Rastreabilidade de requisitos.
C) Rastreabilidade de projeto (forward traceability).
D) Rastreabilidade de design.
E) Rastreabilidade horizontal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Forward traceability liga requisitos aos artefatos gerados (design, código).
</details>

### Questão 4 (FCC)
A respeito do Dicionário de Dados na engenharia de requisitos, ele atua para:
A) Gerar automaticamente o modelo físico.
B) Armazenar logs de falhas.
C) Evitar conflitos de nomes, definindo a semântica e formato dos dados.
D) Substituir os casos de uso.
E) Permitir alteração de tabelas em produção.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. O dicionário centraliza definições de dados, prevenindo redundâncias e inconsistências.
</details>

### Questão 5 (FCC)
Um requisito do tipo "O sistema deve estar adequado à Lei Geral de Proteção de Dados (LGPD)" é classicamente definido como:
A) Funcional de Produto.
B) Não Funcional Externo.
C) Não Funcional Organizacional.
D) Não Funcional de Eficiência.
E) Requisito de Interface.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. Leis e regulamentações governamentais impõem restrições de cunho externo à organização e ao produto.
</details>

### Questão 6 (FCC)
O relacionamento `<<include>>` em Casos de Uso serve fundamentalmente para:
A) Representar funcionalidades que ocorrem apenas em erros.
B) Evitar a repetição de um fluxo de eventos que é comum a dois ou mais casos de uso.
C) Substituir a herança de atores.
D) Demonstrar a ordem cronológica de execução.
E) Descrever requisitos não funcionais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. O `<<include>>` extrai comportamentos comuns e obrigatórios para reutilização.
</details>

### Questão 7 (FCC)
Qual das alternativas apresenta exclusivamente requisitos não funcionais?
A) Calcular folha de pagamento; Tempo de resposta de 2s.
B) Emitir nota fiscal; Autenticar usuário.
C) Criptografia AES-256; Interface compatível com leitores de tela; Disponibilidade de 99,9%.
D) Exportar para PDF; Tolerância a falhas.
E) Exibir histórico; Compatibilidade com navegadores web.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Todos os três definem "como" o sistema deve ser (segurança, usabilidade, confiabilidade).
</details>

### Questão 8 (FCC)
Um ator em um diagrama de casos de uso:
A) Deve ser sempre um usuário humano.
B) Pode ser um sistema externo interagindo com o sistema atual.
C) Representa uma classe de dados no banco.
D) Executa os requisitos não funcionais.
E) Recebe os relacionamentos de `<<extend>>`.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. Atores representam papéis interagindo com o sistema, podendo ser pessoas, hardwares ou outros sistemas.
</details>

### Questão 9 (FCC)
Durante a elicitação, a técnica que envolve criar uma versão inicial rápida do software para validação do usuário é chamada de:
A) JAD (Joint Application Development).
B) Prototipação.
C) Brainstorming.
D) Etnografia.
E) Entrevista Estruturada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. A prototipação constrói modelos descartáveis ou evolutivos para refinar requisitos.
</details>

### Questão 10 (FCC)
Sobre a técnica de Etnografia na elicitação:
A) Foca em reuniões fechadas com a diretoria.
B) Exige questionários de múltipla escolha.
C) Consiste na observação imersiva do trabalho no ambiente real do usuário.
D) Baseia-se exclusivamente no Dicionário de Dados.
E) Substitui o levantamento de requisitos funcionais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. A Etnografia observa a rotina diária real para descobrir requisitos implícitos.
</details>

### Questão 11 (FCC)
Um "Requisito de Domínio" (Domain Requirement):
A) Sempre diz respeito à rede de computadores (domínio Windows).
B) Deriva do campo de aplicação do sistema e pode criar novos requisitos ou restringir os existentes.
C) É obrigatoriamente um requisito não funcional.
D) É aplicável apenas em metodologias ágeis.
E) Não pode ser modelado em Casos de Uso.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. Requisitos de domínio refletem as regras do negócio (ex: regras médicas em um sistema de saúde).
</details>

### Questão 12 (FCC)
No modelo de Casos de Uso, a "Generalização" pode ser aplicada a:
A) Apenas Casos de Uso.
B) Apenas Atores.
C) Atores e Casos de Uso.
D) Relacionamentos de Include e Extend.
E) Requisitos Não Funcionais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. A generalização (herança) aplica-se tanto a atores (ator "Gerente" herda de "Funcionário") quanto a Casos de Uso (Validar Senha herda de Validar Acesso).
</details>

### Questão 13 (FCC)
A validação de requisitos responde à pergunta:
A) Estamos construindo o produto corretamente?
B) Estamos construindo o produto correto (aquele que o cliente realmente quer)?
C) O código possui bugs?
D) Qual a linguagem ideal para o sistema?
E) Quanto custará o projeto?

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. Validação verifica se o software atende à necessidade real do cliente. (A alternativa A refere-se à Verificação).
</details>

### Questão 14 (FCC)
A matriz de rastreabilidade é uma ferramenta clássica para:
A) Compilar o código-fonte.
B) Analisar o impacto de mudanças em um requisito sobre os demais artefatos do projeto.
C) Gerar os diagramas UML automaticamente.
D) Definir a arquitetura de rede.
E) Medir o desempenho do banco de dados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. A matriz cruza os requisitos com os artefatos, mostrando o que será afetado se um requisito mudar.
</details>

### Questão 15 (FCC)
Em Engenharia de Requisitos, "Elicitação" significa:
A) Programar o requisito no código.
B) O processo de descobrir, levantar e compreender as necessidades dos stakeholders.
C) Excluir requisitos obsoletos.
D) Publicar o manual do usuário.
E) Traduzir requisitos funcionais para linguagem de máquina.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. Elicitação é a primeira fase: extrair/descobrir a informação junto ao cliente.
</details>

---

## 📝 TEMA 2: Banco de Dados — SGBDs Oracle, PostgreSQL e H2

### Questão 16 (FCC)
No Oracle, a pseudo-coluna ROWNUM:
A) É alocada após a cláusula ORDER BY ser executada.
B) Aceita comparações do tipo `ROWNUM = 2` diretamente no WHERE.
C) Indica a ordem em que o Oracle seleciona a linha da tabela antes da ordenação.
D) Substitui a Primary Key.
E) É idêntica ao LIMIT do PostgreSQL.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. ROWNUM é atribuído *antes* da ordenação, o que causa pegadinhas em paginações sem subconsultas.
</details>

### Questão 17 (FCC)
A tabela especial do Oracle que possui apenas uma linha e a coluna DUMMY chama-se:
A) SYSTEM
B) DUAL
C) SINGLE
D) TEMP
E) ROOT

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. A tabela `DUAL` garante retornos de uma única linha para avaliações de funções (ex: SYSDATE).
</details>

### Questão 18 (FCC)
Para criar uma chave primária auto-incrementada no PostgreSQL (versões clássicas), utiliza-se o tipo:
A) AUTO_INCREMENT
B) SEQUENCE_ID
C) IDENTITY
D) SERIAL
E) ROWNUM

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. O tipo `SERIAL` cria implicitamente uma sequência para gerenciar o auto-incremento.
</details>

### Questão 19 (FCC)
Para pular 50 registros e retornar 10 em PostgreSQL, usa-se:
A) LIMIT 10 OFFSET 50
B) ROWS 50 TO 60
C) ROWNUM BETWEEN 51 AND 60
D) SKIP 50 TAKE 10
E) LIMIT 50, 10

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. A sintaxe ANSI suportada pelo PostgreSQL usa `LIMIT` (quantidade) e `OFFSET` (quantos pular).
</details>

### Questão 20 (FCC)
Sobre o H2 Database:
A) É um banco NoSQL orientado a grafos.
B) Roda exclusivamente no Linux.
C) Permite execução em memória RAM ("In-Memory"), útil para testes isolados sem persistência obrigatória.
D) Não suporta JDBC.
E) Exige licenciamento comercial pago.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. O H2 é relacional, feito em Java, e famoso por rodar em memória (perfeito para JUnit/Spring).
</details>

### Questão 21 (FCC)
No Oracle, para gerar o próximo valor de uma Sequence criada chamada SEQ_EMP, usa-se:
A) SELECT SEQ_EMP.NEXTVAL FROM DUAL;
B) SELECT NEXT_ID(SEQ_EMP);
C) SELECT SEQ_EMP.INCREMENT;
D) GET NEXT SEQ_EMP;
E) SELECT SEQ_EMP.VAL FROM SYSTEM;

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. Usa-se a pseudo-coluna `NEXTVAL` associada ao nome da sequência, lendo da tabela `DUAL`.
</details>

### Questão 22 (FCC)
No PostgreSQL, o suporte nativo a dados estruturados permite indexar e consultar diretamente colunas do tipo:
A) VARCHAR2 e CLOB (exclusivos).
B) JSON e JSONB.
C) ROWID.
D) DUAL_DATA.
E) MEMORY_TABLE.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. O PostgreSQL é famoso por tratar muito bem documentos JSON (especialmente o JSONB, que é binário e indexável).
</details>

### Questão 23 (FCC)
Ao realizar uma consulta `SELECT * FROM tab WHERE ROWNUM > 1;` no Oracle, o resultado será:
A) Apenas a última linha.
B) Todas as linhas, exceto a primeira.
C) Nenhuma linha (conjunto vazio).
D) Um erro de sintaxe.
E) A segunda linha em diante, ordenada pela PK.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Como a 1ª linha falha na condição `> 1` e é descartada, a "próxima" lida ganha o ROWNUM 1 de novo e falha também. O resultado é sempre vazio.
</details>

### Questão 24 (FCC)
Como o PostgreSQL e o Oracle diferem fundamentalmente no uso de aspas?
A) O Oracle usa aspas duplas para strings, o PostgreSQL usa simples.
B) Ambos usam aspas duplas para literais de string.
C) No PostgreSQL (e padrão ANSI), aspas simples delimitam strings literais, e aspas duplas delimitam identificadores (nomes de tabelas/colunas).
D) Aspas não são permitidas no PostgreSQL.
E) O Oracle exige backticks (`) para tabelas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Regra ANSI adotada pelo PgSQL: `'string'` e `"identificador"`.
</details>

### Questão 25 (FCC)
O modo de compatibilidade do H2 Database permite:
A) Conectar-se fisicamente ao Oracle via dblink nativo.
B) Emular sintaxes e comportamentos específicos de outros SGBDs (como PostgreSQL, Oracle e MySQL) facilitando testes.
C) Replicar dados automaticamente para a AWS.
D) Converter código Java para PL/SQL.
E) Desabilitar o padrão ANSI.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. O H2 possui modos de compatibilidade (ex: `;MODE=PostgreSQL`) que aceitam funções nativas desses bancos para não quebrar queries nos testes.
</details>

### Questão 26 (FCC)
Em PostgreSQL, se uma coluna é declarada como `SERIAL`, após inserir dados e querer acessar o último valor gerado nesta sessão, usa-se a função:
A) LAST_INSERT_ID()
B) currval() ou lastval()
C) SYSDATE()
D) SEQ.LASTVAL
E) RETURNING ID

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. As funções `currval('nome_seq')` ou `lastval()` retornam o valor gerado na transação/sessão atual. A cláusula `RETURNING` também é usada no `INSERT`.
</details>

### Questão 27 (FCC)
No Oracle, a função `NVL(coluna, valor_padrao)` é utilizada para:
A) Navegar entre registros.
B) Substituir valores nulos (NULL) pelo valor padrão informado.
C) Converter números para VARCHAR.
D) Retornar a linha atual do ROWNUM.
E) Calcular a nova visão (New View Level).

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. `NVL` (Null Value Logic) troca NULL por um valor pré-determinado (similar ao `COALESCE`).
</details>

### Questão 28 (FCC)
Ao definir uma Sequence no Oracle com a cláusula `CACHE 20`, o banco de dados irá:
A) Limitar a sequência a apenas 20 valores máximos.
B) Prealocar e manter 20 valores em memória RAM para acesso mais rápido, reduzindo I/O em disco.
C) Criar uma tabela DUAL secundária de 20 linhas.
D) Bloquear inserções concorrentes após 20 tentativas.
E) Limpar o buffer de memória a cada 20 minutos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. O `CACHE` melhora o desempenho das sequências guardando blocos numéricos na memória.
</details>

### Questão 29 (FCC)
Diferentemente do PostgreSQL, para concatenar strings no Oracle, o operador nativo clássico (além da função CONCAT) é:
A) `+`
B) `&`
C) `||`
D) `.`
E) `::`

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Tanto Oracle quanto PostgreSQL suportam o operador padrão ANSI `||` para concatenação de strings.
</details>

### Questão 30 (FCC)
O termo "ACID" aplicado aos SGBDs relacionais como Oracle e PostgreSQL significa:
A) Asynchronous, Consistent, Isolated, Distributed.
B) Atomicidade, Consistência, Isolamento e Durabilidade.
C) Always Consistent In Database.
D) Array, Character, Integer, Double.
E) Access Control, Identity, Domain.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. ACID é a fundação do processamento seguro de transações em bancos relacionais.
</details>

---

## 📝 TEMA 3: Língua Portuguesa — Classes de Palavras e Pronomes

### Questão 31 (FCC)
Assinale a frase gramaticalmente correta quanto à colocação pronominal:
A) Me entregaram o processo ontem.
B) Não manifestou-se a respeito do caso.
C) Os colegas que dispuseram-se a ajudar folgarão amanhã.
D) Quando me disseram a verdade, encerrei o caso.
E) Daria-te a resposta se a tivesse.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. A conjunção "Quando" atrai a próclise. (Em E, o certo seria "Dar-te-ia").
</details>

### Questão 32 (FCC)
A próclise em "Em se confirmando a suspeita..." ocorre por causa de:
A) Início de período.
B) Preposição "em" associada a verbo no gerúndio.
C) Palavra atrativa negativa.
D) Verbo no particípio.
E) Mesóclise deslocada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. Regra clássica: EM + PRONOME + GERÚNDIO atrai a próclise.
</details>

### Questão 33 (FCC)
Assinale a alternativa incorreta quanto à colocação em locução verbal:
A) O sistema estava testando-se.
B) Ele não havia avisado-nos.
C) Pretendiam apresentar-lhe os dados.
D) A equipe vinha preparando-se para o deploy.
E) Não se podia compreender a falha.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. O verbo principal "avisado" está no particípio. Particípios JAMAIS aceitam ênclise.
</details>

### Questão 34 (FCC)
Na frase "O juiz considerou a alegação incabível", "incabível" é:
A) Adjetivo.
B) Advérbio.
C) Substantivo.
D) Pronome.
E) Preposição.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. Caracteriza o substantivo "alegação".
</details>

### Questão 35 (FCC)
Em qual frase a palavra "bastante" deve ser flexionada no plural?
A) Eles trabalharam bastante.
B) Elas estavam bastante cansadas.
C) Havia bastante tarefa no projeto.
D) Correram bastante hoje.
E) São alunos bastante aplicados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Acompanha substantivo (tarefa), logo é variável (bastantes tarefas). Nas demais, modifica verbo/adjetivo (advérbio invariável).
</details>

### Questão 36 (FCC)
Assinale a alternativa em que há erro de colocação pronominal:
A) Nunca se esqueça dos requisitos.
B) Jamais me perdoaria por isso.
C) Alguém avisou-me do prazo limite.
D) Tudo se resolve com calma.
E) Poucos se importaram com o erro.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. O pronome indefinido "Alguém" é palavra atrativa. O correto é "Alguém me avisou".
</details>

### Questão 37 (FCC)
Os pronomes oblíquos átonos "o, a, os, as", quando ligados a verbos terminados em R, S ou Z, assumem as formas:
A) no, na, nos, nas.
B) lho, lha.
C) mo, ma.
D) lo, la, los, las.
E) me, te, se.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. O verbo perde a letra final (r, s, z) e o pronome ganha L (ex: fazer + o = fazê-lo).
</details>

### Questão 38 (FCC)
Nas locuções verbais cujo verbo principal está no infinitivo ou gerúndio e HÁ palavra atrativa (ex: NÃO), onde o pronome pode ser colocado?
A) Apenas antes do auxiliar.
B) Apenas depois do principal.
C) Antes do auxiliar ou depois do principal (ênclise ao infinitivo/gerúndio).
D) No meio do auxiliar (mesóclise).
E) Antes do principal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Ex: "Não o quero ver" ou "Não quero vê-lo". Ambas corretas! (A FCC tenta colocar no meio com hífen "Não quero-o ver" - incorreto).
</details>

### Questão 39 (FCC)
Em "Aquela foi a solução **que** nos salvou", a próclise ocorreu porque:
A) "Aquela" atrai o pronome.
B) O verbo está no passado.
C) O pronome relativo "que" exige a próclise.
D) "solução" é substantivo feminino.
E) A frase é negativa.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. O pronome relativo (que, o qual, onde) é uma forte palavra atrativa para a próclise.
</details>

### Questão 40 (FCC)
Assinale a opção em que o uso do pronome lhe está INCORRETO sintaticamente:
A) Entreguei-lhe o documento.
B) Obedeço-lhe cegamente.
C) Vi-lhe na rua ontem à noite.
D) Não lhe disseram a verdade.
E) A decisão foi-lhe favorável.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. O verbo Ver é transitivo direto, exigindo o pronome "o/a" (Vi-o), e não o "lhe" (que atua como objeto indireto).
</details>

### Questão 41 (FCC)
Das classes gramaticais abaixo, a única invariável (que não sofre flexão de gênero e número) é:
A) Substantivo.
B) Adjetivo.
C) Pronome.
D) Advérbio.
E) Numeral.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. Advérbios, preposições e conjunções são invariáveis.
</details>

### Questão 42 (FCC)
Mesóclise é obrigatória quando:
A) O verbo inicia a frase e está no presente.
B) O verbo está no futuro do presente ou futuro do pretérito, e NÃO HÁ palavra atrativa justificando próclise.
C) A oração é exclamativa ou interrogativa.
D) Ocorre gerúndio precedido de preposição.
E) O verbo está no particípio.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. Ex: "Convidar-te-ei para a festa". Se houvesse atrativa: "Não te convidarei".
</details>

### Questão 43 (FCC)
A palavra "certo" atua como adjetivo (flexível) e como pronome indefinido dependendo de sua posição em relação ao substantivo. Assinale a alternativa onde "certo" é Pronome Indefinido:
A) O resultado estava certo.
B) Ele sempre pega o caminho certo.
C) Certas pessoas não merecem confiança.
D) Falou a coisa certa na hora certa.
E) O relógio não está certo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Quando vem ANTES do substantivo de forma vaga ("Certas pessoas"), atua como pronome indefinido. Depois do substantivo, significa "correto" (adjetivo).
</details>

### Questão 44 (FCC)
Assinale a frase em que o adjetivo exerce função de predicativo do sujeito:
A) O analista competente resolveu o bug.
B) Comprei um computador rápido.
C) O sistema rápido falhou hoje.
D) O diretor considerou o sistema lento.
E) O tribunal permanece fechado aos domingos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: E**. O adjetivo "fechado" modifica o sujeito "tribunal" através do verbo de ligação "permanece". (Na D, é predicativo do objeto).
</details>

### Questão 45 (FCC)
"Dar-nos-ia muito prazer sua presença." A colocação pronominal apresentada:
A) Está incorreta, o certo seria "Daria-nos".
B) Está incorreta, o certo seria "Nos daria".
C) Está correta (mesóclise), justificada pelo verbo no futuro do pretérito iniciando a oração sem palavra atrativa.
D) Está correta, pois o pronome "nos" só pode atuar como objeto direto.
E) É facultativa em relação a "Daria-nos".

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Verbo no futuro iniciando a frase exige obrigatoriamente a mesóclise na norma-padrão.
</details>
