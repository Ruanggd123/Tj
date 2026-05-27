# Guia de Estudos Definitivo — Segunda-feira 25/05/2026
## Semana 2 | Dia 8 | TJ-CE 2026 (Analista TI - Sistemas)
### Foco Absoluto: Banca FCC — Doutrina, Detalhes Ocultos, Pegadinhas e Casos Práticos

---

## 🗺️ Mapa de Estudos do Dia

```mermaid
graph TD
    A[Segunda-feira de Alto Rendimento] --> B[BLOCO 1: Eng. Software — Engenharia de Requisitos]
    A --> C[BLOCO 2: Banco de Dados — SQL Específicos (Oracle, PostgreSQL, H2)]
    A --> D[BLOCO 3: Português — Classes de Palavras e Pronomes]
    
    B --> B1[Tipos de Requisitos: Funcionais e Não Funcionais]
    B --> B2[Casos de Uso: Atores, Includes e Extends]
    B --> B3[Rastreabilidade e Dicionário de Dados]
    
    C --> C1[Oracle: DUAL, ROWNUM e Sequências]
    C --> C2[PostgreSQL: Sintaxes Específicas e Comandos Comuns]
    C --> C3[H2 Database: Funcionalidades em Memória]
    
    D --> D1[Classes Variáveis: Substantivos, Adjetivos, Verbos]
    D --> D2[Classes Invariáveis: Advérbios, Preposições]
    D --> D3[Pronomes: Emprego e Colocação (Próclise, Mesóclise, Ênclise)]
```

---

## 💾 SEÇÃO 1: Engenharia de Software — Engenharia de Requisitos

A FCC adora cobrar a diferenciação entre requisitos funcionais e não funcionais, bem como detalhes sobre diagramas de casos de uso (include/extend).

### 1. Tipos de Requisitos
*   **Requisitos Funcionais:** Descrevem o que o sistema deve fazer. São as funcionalidades, os serviços que o sistema deve prover, como o sistema deve reagir a entradas específicas e como deve se comportar em determinadas situações. Ex: "O sistema deve permitir o cadastro de usuários".
*   **Requisitos Não Funcionais:** Descrevem atributos de qualidade, restrições e propriedades emergentes do sistema. Focam em *como* o sistema deve ser. Dividem-se em:
    *   **Requisitos do Produto:** Usabilidade, eficiência, confiabilidade, portabilidade. (Ex: "O sistema deve processar a requisição em menos de 2 segundos").
    *   **Requisitos Organizacionais:** Padrões da empresa, infraestrutura.
    *   **Requisitos Externos:** Legislação, ética, interoperabilidade (Ex: "O sistema deve atender à LGPD").
*   **Requisitos de Domínio:** Derivados do domínio de aplicação do sistema, podem ser funcionais ou não funcionais.

### 2. Casos de Uso
Um diagrama de casos de uso na UML descreve a funcionalidade proposta para um novo sistema (ou a funcionalidade atual).
*   **Ator:** Representa um papel desempenhado por um usuário ou por outro sistema que interage com o sistema em questão.
*   **Caso de Uso:** Descreve uma sequência de ações que produzem um resultado observável de valor para um ator.
*   **Relacionamentos:**
    *   **&lt;&lt;include&gt;&gt;:** O caso de uso base **obrigatoriamente** incorpora o comportamento do caso de uso incluído. É usado para evitar repetição.
    *   **&lt;&lt;extend&gt;&gt;:** O caso de uso base **opcionalmente** incorpora o comportamento do caso de uso estendido, dependendo de uma condição.

### 3. Rastreabilidade e Dicionário de Dados
*   **Rastreabilidade:** É a capacidade de descrever e seguir a vida de um requisito, tanto para a frente (direção ao produto final) quanto para trás (direção à origem do requisito). Ajuda na gestão de mudanças.
*   **Dicionário de Dados:** É um repositório centralizado de informações sobre os dados. Define o significado, a estrutura (tipo, tamanho), o formato e o relacionamento dos elementos de dados do sistema. Garante consistência e padronização.

### 🚨 Pegadinhas Clássicas da FCC sobre Engenharia de Requisitos
*   **Tentar confundir requisitos não funcionais organizacionais com requisitos do produto.**
    *   *Realidade:* Requisitos organizacionais referem-se às políticas e infraestrutura da empresa (ex: "o sistema deve ser desenvolvido usando a linguagem homologada Java"). Requisitos de produto referem-se ao comportamento do software em execução (ex: "o tempo de resposta deve ser de 1s").
*   **Inverter os conceitos de `<<include>>` e `<<extend>>`.**
    *   *Realidade:* A FCC adora dizer que o `<<include>>` é opcional e o `<<extend>>` é obrigatório. Lembre-se sempre: include = inclui sempre (obrigatório); extend = estende se necessário (opcional).

---

## 🌐 SEÇÃO 2: Banco de Dados — SQL Específicos (Oracle, PostgreSQL, H2)

O edital exige conhecimentos específicos de SGBDs diferentes. A FCC costuma cobrar as peculiaridades de cada um, especialmente funções exclusivas ou sintaxes proprietárias.

### 1. Oracle
*   **DUAL:** Uma tabela especial pertencente ao usuário SYS e acessível por todos. Possui uma única coluna (DUMMY) e uma única linha. É usada para realizar cálculos ou invocar funções que não dependem de dados de uma tabela real. Ex: `SELECT SYSDATE FROM DUAL;`.
*   **ROWNUM:** Uma pseudo-coluna que retorna um número indicando a ordem em que a linha foi selecionada pelo Oracle (1, 2, 3...). Muito usada para paginação ou para limitar resultados, embora exija cuidado com ordenações (ORDER BY ocorre *após* a atribuição do ROWNUM).
*   **Sequences:** Objetos de banco de dados usados para gerar valores numéricos únicos, geralmente para chaves primárias. Ex: `CREATE SEQUENCE seq_id; SELECT seq_id.NEXTVAL FROM DUAL;`.

### 2. PostgreSQL
*   Conhecido pela conformidade com padrões ANSI SQL e por seus recursos avançados.
*   **Tipos de Dados e Funcionalidades:** Suporte avançado a JSON, arrays, e tipos geométricos.
*   **Paginação:** Em vez de ROWNUM, usa as cláusulas padrão `LIMIT` e `OFFSET`. Ex: `SELECT * FROM tabela LIMIT 10 OFFSET 20;`.
*   **Sequências (Auto-incremento):** Usa tipos como `SERIAL` ou `BIGSERIAL`, que implicitamente criam uma sequência. (Ex: `id SERIAL PRIMARY KEY`).

### 3. H2 Database
*   SGBD relacional escrito em Java, muito rápido e leve.
*   **Modo em Memória:** É amplamente utilizado para testes (JUnit) ou aplicações embarcadas, operando diretamente na memória RAM (`jdbc:h2:mem:testdb`). Quando a aplicação encerra, os dados se perdem (a menos que configurado para persistir em disco).
*   **Compatibilidade:** Possui modos de compatibilidade com outros bancos (como Oracle, PostgreSQL, MySQL), emulando algumas de suas sintaxes.

### 🚨 Pegadinhas Clássicas da FCC sobre SQL Específicos
*   **Colocar a condição `ROWNUM` com operadores impossíveis (ex: `ROWNUM = 2` ou `ROWNUM > 1`).**
    *   *Realidade:* No Oracle, o `ROWNUM` é processado antes da linha ser retornada. A primeira linha tem `ROWNUM = 1`. Se você pedir `ROWNUM > 1`, a primeira linha (que é 1) falha no teste e é descartada. Como ela foi descartada, a "próxima" linha passa a ser a candidata ao `ROWNUM = 1`. Ela também falhará. Resultado: a consulta com `ROWNUM > 1` nunca retorna nenhuma linha!
*   **Afirmar que a tabela `DUAL` pode ter várias linhas inseridas pelo usuário.**
    *   *Realidade:* A tabela `DUAL` tem estritamente uma única linha. Inserir mais linhas nela quebra o funcionamento interno de funções do banco de dados, sendo uma péssima prática (e bloqueada em versões mais recentes).

---

## ⚖️ SEÇÃO 3: Língua Portuguesa — Classes de Palavras e Pronomes

A FCC gosta de misturar a classificação das palavras com as funções sintáticas e o emprego de pronomes, principalmente a colocação pronominal.

### 1. Classes de Palavras Principais
*   **Substantivo:** Nomeia seres, lugares, sentimentos, conceitos. Pode sofrer flexão de gênero e número. A FCC costuma testar substantivos abstratos derivados de verbos ou adjetivos.
*   **Adjetivo:** Caracteriza o substantivo. A FCC adora questões que pedem a conversão de uma oração adjetiva em um adjetivo ou vice-versa.
*   **Verbo:** Expressa ação, estado ou fenômeno da natureza. O emprego dos tempos e modos verbais é muito cobrado, assim como a correlação entre eles.

### 2. Pronomes: Emprego e Colocação
Pronomes substituem ou acompanham substantivos. A Colocação Pronominal (pronomes oblíquos átonos: *me, te, se, o, a, lhe, nos, vos, os, as, lhes*) é figurinha carimbada.

*   **Próclise (antes do verbo):** Obrigatória quando há palavras atrativas:
    *   Palavras negativas (não, nunca, jamais).
    *   Advérbios (aqui, muito, hoje) sem vírgula após eles.
    *   Pronomes relativos (que, qual, onde).
    *   Pronomes indefinidos (alguém, tudo).
    *   Conjunções subordinativas (embora, se, que, quando).
    *   Em + gerúndio: "Em se tratando de...".
*   **Mesóclise (no meio do verbo):** Usada com verbos no **Futuro do Presente** ou **Futuro do Pretérito**, desde que NÃO haja palavra que atraia a próclise.
    *   Ex: *Realizar-se-á a prova.* / *Dar-te-ia o livro.*
*   **Ênclise (depois do verbo):** Usada quando a próclise e mesóclise não são aplicáveis. Principalmente no **início de frases** ou com verbo no **imperativo afirmativo** ou **gerúndio** (sem preposição 'em' antes).
    *   Ex: *Entreguei-lhe o documento.* / *Saiu, deixando-nos sozinhos.*

### 🚨 Pegadinhas Clássicas da FCC sobre Colocação Pronominal
*   **Esconder o pronome relativo "que" longe do verbo.**
    *   *Realidade:* O "que" (mesmo implícito ou distante) atrai o pronome obrigando a próclise. A FCC gosta de colocar locuções ou adjuntos entre o "que" e o verbo (ex: "...os documentos que, no dia seguinte, se perderam" e a FCC tentará usar "...perderam-se").
*   **Verbos no particípio aceitando ênclise.**
    *   *Realidade:* O particípio (verbos terminados em -ado, -ido) **nunca** aceita ênclise! Ex: A frase "Havia avisado-lhe" é um erro crasso e muito cobrado; o correto seria "Havia-lhe avisado".
*   **Locuções verbais e o pronome "solto".**
    *   *Realidade:* Em locuções verbais, se houver palavra atrativa, o pronome deve ficar *antes* do verbo auxiliar ou *depois* do verbo principal (no infinitivo/gerúndio). Ex: "Não lhe quero falar" ou "Não quero falar-lhe". A FCC tenta emplacar "Não quero-lhe falar".

---

## 🎯 SEÇÃO 4: Questões Inéditas FCC-Style Comentadas Passo a Passo

### Questão 1: Engenharia de Software (Casos de Uso)
**(FCC - Adaptada)** Durante a modelagem de um sistema de processo judicial eletrônico para o TJ-CE, o analista identificou que o caso de uso "Emitir Certidão de Antecedentes" deve, obrigatoriamente, registrar em log a consulta realizada e, caso o usuário solicite, pode enviar uma cópia em PDF por e-mail. No diagrama de casos de uso da UML, as interações de registro em log e envio por e-mail devem ser modeladas a partir do caso de uso "Emitir Certidão de Antecedentes", respectivamente, com os relacionamentos:

A) `<<extend>>` e `<<extend>>`.
B) `<<include>>` e `<<include>>`.
C) `<<include>>` e `<<extend>>`.
D) `<<extend>>` e `<<include>>`.
E) Associação Direta e Generalização.

#### 💡 Resolução Comentada da Questão 1:
*   **Análise das Alternativas:**
    *   O relacionamento `<<include>>` é usado para um comportamento que é **obrigatório** (ou sempre executado) pelo caso de uso base. Como o registro de log é obrigatório toda vez que a certidão for emitida, usa-se `<<include>>`.
    *   O relacionamento `<<extend>>` é usado para um comportamento **opcional** ou condicional. O envio de e-mail ocorre apenas "caso o usuário solicite", logo, é um `<<extend>>`.
*   **Gabarito correto: C.**

---

### Questão 2: Banco de Dados (Oracle e SQL)
**(FCC - Adaptada)** Em um banco de dados Oracle, um Analista de TI precisa obter o nome do funcionário mais bem pago do tribunal. Para isso, ele ordenou a tabela `SERVIDORES` pelo campo `salario` em ordem decrescente e usou a pseudo-coluna `ROWNUM`. Considere a consulta SQL abaixo:
```sql
SELECT nome FROM SERVIDORES ORDER BY salario DESC WHERE ROWNUM = 1;
```
Sobre a instrução acima e seu resultado esperado no Oracle, é correto afirmar:

A) Retornará corretamente o nome do servidor com maior salário.
B) Retornará um erro de sintaxe, pois a cláusula `WHERE` deve preceder a cláusula `ORDER BY`.
C) Retornará o nome de um servidor aleatório e não necessariamente o de maior salário, pois o `ROWNUM` é processado antes da ordenação `ORDER BY`.
D) Retornará erro semântico, pois `ROWNUM` só pode ser avaliado com os operadores `>`, `>=`, ou `!=`.
E) Executará perfeitamente, mas se houver salários iguais no topo, retornará duas linhas.

#### 💡 Resolução Comentada da Questão 2:
*   **Análise das Alternativas:**
    *   Pela regra padrão da linguagem SQL (e especificamente no Oracle), a cláusula `WHERE` deve obrigatoriamente vir antes da cláusula `ORDER BY`. A sintaxe escrita pelo analista na questão gera erro imediato porque colocou o `WHERE` no final.
    *   (Nota: mesmo que ele colocasse `WHERE ROWNUM = 1 ORDER BY salario DESC`, o comportamento seria pegar a primeira linha física encontrada e só depois ordenar, caindo na pegadinha conceitual da alternativa C, mas a sintaxe estrutural já é um erro fatal na alternativa B).
*   **Gabarito correto: B.**

---

### Questão 3: Língua Portuguesa (Colocação Pronominal)
**(FCC - Adaptada)** Assinale a alternativa em que a colocação do pronome átono está inteiramente de acordo com a norma-padrão da Língua Portuguesa:

A) Me disseram que a ata da reunião seria publicada ainda hoje.
B) Os documentos que anexaram-se ao processo foram revisados pelo juiz.
C) Não repassaremos-lhe a nova senha até que o formulário esteja assinado.
D) Em se tratando de segurança da informação, todo cuidado com senhas é vital.
E) Realizaria-se o backup completo do banco de dados na madrugada de domingo.

#### 💡 Resolução Comentada da Questão 3:
*   **Análise das Alternativas:**
    *   **A:** Errada. Não se inicia frase com pronome oblíquo átono (o correto é *Disseram-me*).
    *   **B:** Errada. O "que" (pronome relativo) é palavra atrativa, exigindo a próclise (o correto é *que se anexaram*).
    *   **C:** Errada. A palavra "Não" atrai obrigatoriamente o pronome (o correto é *Não lhe repassaremos*).
    *   **D:** **Correta.** A estrutura preposição *em* + pronome + verbo no *gerúndio* atrai a próclise (em se tratando). Regra clássica!
    *   **E:** Errada. Com verbos no futuro do pretérito (realizaria), usa-se mesóclise caso não haja palavra atrativa (o correto é *Realizar-se-ia*).
*   **Gabarito correto: D.**

---

## 🧠 SEÇÃO 5: Flashcards de Memorização Ativa (Estilo Anki)

*   **Frente (Pergunta):** O que diferencia um Requisito Funcional de um Não Funcional?
*   **Verso (Resposta):** O Funcional define *o que* o sistema faz (serviços e funções). O Não Funcional define *como* o sistema deve ser (qualidades, restrições de desempenho, segurança, etc).

*   **Frente (Pergunta):** Num diagrama de casos de uso, qual a diferença entre `<<include>>` e `<<extend>>`?
*   **Verso (Resposta):** `<<include>>` denota um relacionamento obrigatório (o caso de uso base sempre executa o incluído). `<<extend>>` denota um relacionamento opcional (ocorre sob certas condições).

*   **Frente (Pergunta):** Para que serve a tabela DUAL no Oracle?
*   **Verso (Resposta):** É uma tabela "dummy" de apenas uma linha e uma coluna. Serve para garantir a sintaxe do `SELECT` quando se quer consultar algo que não está em uma tabela (ex: chamar funções de sistema como `SYSDATE` ou sequências).

*   **Frente (Pergunta):** Quais os casos de Próclise obrigatória em Língua Portuguesa?
*   **Verso (Resposta):** Com palavras atrativas antes do verbo: Negativas, Advérbios (sem vírgula), Pronomes Relativos e Indefinidos, Conjunções Subordinativas e preposição EM seguida de gerúndio.

---

## 🏆 Roteiro de Estudos Sugerido para Hoje (25/05/2026)

1.  **Manhã (Bloco 1 - 2h):** Leia e resuma a **Seção 1**. Foque na diferença de tipos de requisitos e nas associações (include/extend) dos casos de uso, que são campeões na FCC.
2.  **Tarde (Bloco 2 - 2h):** Estude a **Seção 2**. Pratique ou visualize comandos de `ROWNUM` e sequências. Lembre-se do foco do H2 em memória.
3.  **Noite (Bloco 3 - 1h30):** Estude a **Seção 3**. Foque em exercícios de Colocação Pronominal, que são garantidos na prova. Memorize as "palavras atrativas" da próclise.
4.  **Bateria de Questões:** Como hoje começa uma nova semana de tópicos, ainda não há simulados prontos no nosso app. Faça questões na sua plataforma ou me peça para gerar as novas questões da FCC!

Bons estudos! 🚀
