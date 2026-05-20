# Guia de Estudo — Sábado 16/05/2026
## Semana 1 | Dia 1 | TJ-CE 2026 (Analista TI - Sistemas)

---

## ⏰ Rotina do Dia

| Horário | Atividade |
|---|---|
| 07:30 | Acorde, café, revise brevemente este guia (5 min) |
| 08:00 - 11:00 | **BLOCO 1 — Manhã:** Engenharia de Software |
| 11:00 - 13:00 | Almoço + descanso |
| 13:00 - 16:00 | **BLOCO 2 — Tarde:** Banco de Dados |
| 16:00 - 16:30 | Pausa |
| 16:30 - 17:00 | Revisão rápida dos dois blocos anteriores (Flashcards) |
| 19:00 - 21:00 | **BLOCO 3 — Noite:** Português |
| 21:00 - 21:30 | Atualize o Edital Verticalizado com os [x] dos tópicos estudados |

---

## BLOCO 1 — MANHÃ (3h): Engenharia de Software

### Tópico 1.1: Ciclo de Vida de Software (1h30)

**O que é?**
O processo pelo qual um software passa desde a sua concepção até a descontinuação. A FCC cobra os **nomes das fases**, **o que acontece em cada fase** e **as diferenças entre os modelos**.

---

#### As Fases do Ciclo de Vida (memorize a ordem):

1. **Planejamento** — Define o escopo, viabilidade e recursos. Responde: "Vale a pena fazer?"
2. **Análise de Requisitos** — Levanta o que o sistema deve fazer (funcionais) e como deve se comportar (não-funcionais). Responde: "O que o sistema faz?"
3. **Projeto (Design)** — Define a arquitetura, componentes, banco de dados. Responde: "Como o sistema vai ser feito?"
4. **Implementação (Codificação)** — O código é escrito. Responde: "Construção do sistema."
5. **Testes** — Verificação (o sistema foi construído certo?) e Validação (o sistema certo foi construído?). Responde: "Funciona conforme esperado?"
6. **Implantação (Deploy)** — O sistema vai para produção e é entregue ao cliente.
7. **Manutenção** — Correção de bugs, melhorias e adaptações pós-entrega.

> ⚠️ **Pegadinha FCC:** A banca frequentemente troca a ordem das fases ou confunde "Verificação" com "Validação". Decore:
> - **Verificação** = "Estou construindo o sistema CERTO?" (processo interno, revisão de artefatos)
> - **Validação** = "Estou construindo o sistema CORRETO para o cliente?" (produto final vs. necessidade do usuário)

---

#### Modelo Cascata (Waterfall):

**Características principais:**
- Fases **sequenciais e lineares** — uma fase só começa depois que a anterior termina
- Cada fase gera um **artefato/documento** de saída
- **Difícil de voltar atrás** — mudanças tardias são caras
- Funciona bem quando os requisitos são **estáveis e bem definidos**

**Diagrama mental:**
```
Requisitos → Projeto → Implementação → Testes → Implantação → Manutenção
     ↓            ↓           ↓            ↓           ↓
  Documento   Documento    Código       Relatório   Sistema em produção
```

**Vantagens:**
- Simples de entender e gerenciar
- Fases bem definidas com entregáveis claros
- Bom para projetos pequenos e estáveis

**Desvantagens:**
- Cliente só vê o produto no final
- Mudanças nos requisitos são muito custosas
- Alto risco de o produto final não atender as necessidades reais

> ⚠️ **Pegadinha FCC:** A banca gosta de perguntar sobre o **Modelo em V** (variante do Cascata). No Modelo em V, cada fase de desenvolvimento tem uma fase de teste correspondente:
> - Requisitos ↔ Testes de Aceitação
> - Projeto Arquitetural ↔ Testes de Sistema
> - Projeto Detalhado ↔ Testes de Integração
> - Codificação ↔ Testes Unitários

---

#### Outros Modelos (saiba diferenciar):

| Modelo | Característica Principal |
|---|---|
| **Cascata** | Linear e sequencial. Sem volta. |
| **Incremental** | Entrega o sistema em partes (incrementos) funcionais. |
| **Espiral** | Foco em gerenciamento de risco. Ciclos repetitivos. |
| **Prototipação** | Cria protótipos para validar requisitos com o cliente. |
| **RAD (Rapid Application Development)** | Desenvolvimento rápido com reuso de componentes. |

---

### Tópico 1.2: Modelo Cascata — Exercícios Mentais (30 min)

Responda mentalmente (ou em papel) estas perguntas que a FCC costuma fazer:

1. Em qual fase do ciclo de vida ocorre a codificação do sistema?
   - ✅ Implementação

2. A fase que define "o que o sistema deve fazer" é chamada de:
   - ✅ Análise de Requisitos

3. O Modelo Cascata é adequado para projetos com requisitos:
   - ✅ Estáveis e bem definidos desde o início

4. No Modelo em V, qual fase de teste corresponde à fase de codificação?
   - ✅ Testes Unitários

5. Verificação e Validação: qual garante que o produto atende às necessidades do usuário?
   - ✅ Validação

---

## BLOCO 2 — TARDE (3h): Banco de Dados

### Tópico 2.1: Modelo Relacional (1h30)

**O que é?**
O modelo que organiza dados em **tabelas (relações)**, onde cada linha é um registro (tupla) e cada coluna é um atributo. É a base de todos os bancos SQL.

---

#### Conceitos Fundamentais:

| Termo | O que é | Exemplo |
|---|---|---|
| **Tabela (Relação)** | Conjunto de dados organizado em linhas e colunas | Tabela FUNCIONARIOS |
| **Linha (Tupla)** | Um registro individual | João, 30, TI |
| **Coluna (Atributo)** | Uma propriedade dos dados | nome, idade, departamento |
| **Domínio** | O conjunto de valores possíveis para um atributo | idade: inteiros positivos |
| **Grau** | Número de colunas de uma tabela | Tabela com 5 colunas = grau 5 |
| **Cardinalidade** | Número de linhas (tuplas) de uma tabela | Tabela com 100 registros |

---

#### Chaves — o coração do modelo relacional:

| Tipo de Chave | Definição | Exemplo |
|---|---|---|
| **Chave Primária (PK)** | Identifica unicamente cada tupla. **Não pode ser NULL. Não pode se repetir.** | CPF em uma tabela de pessoas |
| **Chave Estrangeira (FK)** | Referencia a PK de outra tabela. Garante **integridade referencial**. | Coluna `id_departamento` em FUNCIONARIOS referencia PK de DEPARTAMENTOS |
| **Chave Candidata** | Qualquer atributo que poderia ser PK (único e não nulo). A PK é escolhida entre as candidatas. | CPF e RG ambos podem identificar uma pessoa |
| **Chave Alternativa** | Chave candidata que NÃO foi escolhida como PK | RG (quando o CPF foi escolhido como PK) |
| **Chave Composta** | PK formada por mais de um atributo | (id_aluno + id_disciplina) em uma tabela de matrículas |
| **Chave Surrogada** | PK artificial gerada pelo sistema (auto-incremento) | id SERIAL ou AUTO_INCREMENT |

> ⚠️ **Pegadinha FCC:** A banca troca "Chave Alternativa" com "Chave Candidata". Lembre:
> - **Todas** as chaves únicas e não nulas são **candidatas**
> - A que **foi escolhida** é a **primária**
> - As que **não foram escolhidas** são as **alternativas**

---

#### Restrições de Integridade:

| Restrição | O que garante |
|---|---|
| **Integridade de Entidade** | A PK nunca pode ser NULL |
| **Integridade Referencial** | Um valor de FK deve existir na tabela referenciada (ou ser NULL) |
| **Integridade de Domínio** | Os valores de um atributo devem pertencer ao seu domínio |

---

### Tópico 2.2: SQL Básico (1h30)

#### Comandos que você precisa dominar:

**Categorias DDL (Data Definition Language):**
```sql
CREATE TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2),
    id_dept INT REFERENCES departamentos(id)
);

ALTER TABLE funcionarios ADD COLUMN data_admissao DATE;

DROP TABLE funcionarios;
```

**Categorias DML (Data Manipulation Language):**
```sql
-- Inserir
INSERT INTO funcionarios (nome, salario) VALUES ('João', 5000.00);

-- Consultar
SELECT nome, salario FROM funcionarios WHERE salario > 3000;

-- Atualizar
UPDATE funcionarios SET salario = 5500 WHERE id = 1;

-- Deletar
DELETE FROM funcionarios WHERE id = 1;
```

**SELECT avançado — o mais cobrado pela FCC:**
```sql
-- Ordenação
SELECT nome, salario FROM funcionarios ORDER BY salario DESC;

-- Agrupamento (muito cobrado!)
SELECT id_dept, AVG(salario) as media
FROM funcionarios
GROUP BY id_dept
HAVING AVG(salario) > 4000;

-- Funções de agregação (saiba todas!)
SELECT
    COUNT(*) as total,
    SUM(salario) as total_salarios,
    AVG(salario) as media,
    MAX(salario) as maior,
    MIN(salario) as menor
FROM funcionarios;
```

**JOINs — essencial para a prova:**
```sql
-- INNER JOIN: retorna apenas os registros com correspondência nos dois lados
SELECT f.nome, d.nome as departamento
FROM funcionarios f
INNER JOIN departamentos d ON f.id_dept = d.id;

-- LEFT JOIN: retorna TODOS do lado esquerdo, mesmo sem correspondência
SELECT f.nome, d.nome as departamento
FROM funcionarios f
LEFT JOIN departamentos d ON f.id_dept = d.id;

-- RIGHT JOIN: retorna TODOS do lado direito
-- FULL OUTER JOIN: retorna TODOS de ambos os lados
```

> ⚠️ **Pegadinha FCC:** A banca adora perguntar qual JOIN retorna registros sem correspondência. Lembre:
> - **INNER JOIN** = somente correspondência. Se não tem par, **some**.
> - **LEFT/RIGHT/FULL JOIN** = traz registros sem par (com NULL no lado sem correspondência).

---

#### Exercícios Mentais de SQL:

1. Qual cláusula filtra grupos após o agrupamento?
   - ✅ HAVING (não WHERE — WHERE filtra antes de agrupar)

2. Para listar todos os funcionários mesmo os que não têm departamento, qual JOIN usar?
   - ✅ LEFT JOIN (com funcionários no lado esquerdo)

3. Qual a diferença entre DELETE e TRUNCATE?
   - ✅ DELETE remove linha a linha (pode ter WHERE), TRUNCATE remove tudo de uma vez (mais rápido, não tem WHERE)

---

## BLOCO 3 — NOITE (2h): Língua Portuguesa

### Tópico 3.1: Compreensão e Interpretação de Textos (2h)

**O DNA da FCC em Português:**
A FCC adora textos jornalísticos e de opinião de alta densidade semântica. As questões testam se você entendeu a **ideia central**, as **relações lógicas** entre os parágrafos, o **sentido de palavras no contexto** e as **inferências possíveis**.

---

#### Os 5 tipos de questão FCC de Interpretação:

**1. Ideia Central / Tema do Texto**
- O que o texto defende ou discute?
- Estratégia: leia o primeiro e último parágrafos com atenção. A tese está geralmente no início ou no fim.

**2. Inferência (o que o texto permite concluir)**
- A resposta NÃO está explícita — você precisa deduzir.
- Cuidado: a alternativa correta deve ser **necessariamente verdadeira** a partir do texto, não apenas possível.
- ⚠️ Armadilha: afirmações "possíveis mas não garantidas" são erradas na FCC.

**3. Referência de pronome / palavra (coesão referencial)**
- "A palavra X no 2º parágrafo refere-se a..."
- Estratégia: substitua o pronome pela palavra e veja se o sentido se mantém.

**4. Sentido de palavras no contexto**
- "O termo X, no contexto, pode ser substituído por..."
- Estratégia: leia o parágrafo inteiro com a alternativa e veja se o sentido semântico é preservado.

**5. Estrutura e Organização do Texto**
- "O trecho X exerce qual função no parágrafo?"
- Funções comuns: exemplificar, contrastar, concluir, introduzir, explicar, retificar.

---

#### Palavras de Relação Lógica (essenciais para a FCC):

| Relação | Conectivos/Expressões |
|---|---|
| **Adição** | e, além disso, também, ademais, outrossim |
| **Oposição/Contraste** | mas, porém, contudo, entretanto, todavia, no entanto |
| **Conclusão** | logo, portanto, assim, por isso, consequentemente |
| **Explicação** | porque, pois, já que, uma vez que |
| **Concessão** | embora, ainda que, mesmo que, apesar de |
| **Condição** | se, caso, desde que, a não ser que |
| **Finalidade** | para que, a fim de que, com o intuito de |
| **Comparação** | assim como, bem como, da mesma forma que |

> ⚠️ **Pegadinha FCC:** A banca diferencia "explicação" de "conclusão". "Pois" no início da oração = explicação. "Pois" no meio da oração pode ser conclusão. Preste atenção no contexto.

---

#### Estratégia de Leitura para a Prova:

1. **Leia as questões ANTES do texto** — você já sabe o que procurar
2. **Primeira leitura rápida** — entenda o assunto geral (2 min)
3. **Segunda leitura detalhada** — foque nos parágrafos citados nas questões
4. **Elimine alternativas absurdas** — reduza para 2 e escolha a mais conservadora
5. **Desconfie de extremos** — "sempre", "nunca", "todo", "nenhum" quase sempre são errados

---

#### Exercício de Fixação (Faça Agora):

Leia qualquer texto de jornal (G1, Folha, Estadão) por 10 minutos e tente:
1. Identificar a tese central do texto
2. Encontrar os conectivos e identificar a relação lógica
3. Identificar 2 inferências que o texto permite concluir

---

## ✅ Antes de Dormir (21h - 21h30)

Abra o arquivo `edital_verticalizado_tj_ce.md` e marque com `[x]` os tópicos estudados hoje:

- [x] Ciclo de vida de software
- [x] Modelos de desenvolvimento (Cascata)
- [x] Modelo Relacional
- [x] SQL (PostgreSQL) — básico
- [x] Compreensão e interpretação de textos
- [x] Tipologia textual *(se chegou a estudar)*

---

## 📌 Resumo do que você vai aprender amanhã

| Área | Tópicos |
|---|---|
| Eng. Software | Fases do ciclo de vida, Modelo Cascata, Modelo em V, Verificação vs Validação |
| Banco de Dados | Tabelas, Tuplas, Atributos, PK, FK, Chaves candidatas/alternativas, SQL SELECT/JOIN/GROUP BY |
| Português | Tipos de questão FCC, Inferência, Coesão referencial, Conectivos lógicos |
