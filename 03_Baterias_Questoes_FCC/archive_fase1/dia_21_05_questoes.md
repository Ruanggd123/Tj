# Bateria de Questões FCC — Quinta-feira 21/05

Este arquivo contém 45 questões inéditas no padrão de cobrança da banca FCC (15 por tema estudado hoje) com gabarito comentado ocultável.

---

## 📝 TEMA 1: Banco de Dados — SQL Avançado (GROUP BY, HAVING e Subqueries)

### Questão 1 (FCC - Adaptada)
Durante a análise de uma query SQL complexa que apresenta múltiplos filtros e agregações, um desenvolvedor do TJ-CE precisa identificar a ordem física de processamento (ordem lógica de execução) das cláusulas pelo interpretador do SGBD. Assinale a alternativa que apresenta a sequência correta dessa execução:
A) SELECT ➔ FROM ➔ WHERE ➔ GROUP BY ➔ HAVING ➔ ORDER BY
B) FROM ➔ WHERE ➔ GROUP BY ➔ HAVING ➔ SELECT ➔ ORDER BY
C) FROM ➔ GROUP BY ➔ WHERE ➔ HAVING ➔ SELECT ➔ ORDER BY
D) SELECT ➔ FROM ➔ WHERE ➔ HAVING ➔ GROUP BY ➔ ORDER BY
E) FROM ➔ WHERE ➔ SELECT ➔ GROUP BY ➔ HAVING ➔ ORDER BY

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O SGBD executa as cláusulas na seguinte sequência lógica:
1. **FROM (e JOINs):** Identifica as tabelas de origem dos dados.
2. **WHERE:** Filtra as linhas individuais com base em condições não agregadas.
3. **GROUP BY:** Agrupa as linhas filtradas em subgrupos.
4. **HAVING:** Filtra os grupos resultantes com base em funções agregadas.
5. **SELECT:** Projeta as colunas finais e calcula as funções de agregação.
6. **ORDER BY:** Ordena o conjunto de resultados final.
</details>

---

### Questão 2 (FCC - Analista Judiciário - Apoio Especializado - TI)
Considere uma tabela chamada `processos` com as colunas `id` (int), `assunto` (varchar) e `custas` (numeric). O administrador do banco de dados deseja listar a soma das custas por assunto, mas apenas para os assuntos cujo valor médio de custas seja superior a R$ 1.000,00. A instrução SQL que realiza essa tarefa de forma correta e eficiente é:
A) `SELECT assunto, SUM(custas) FROM processos WHERE AVG(custas) > 1000 GROUP BY assunto;`
B) `SELECT assunto, SUM(custas) FROM processos GROUP BY assunto HAVING AVG(custas) > 1000;`
C) `SELECT assunto, SUM(custas) FROM processos HAVING AVG(custas) > 1000 GROUP BY assunto;`
D) `SELECT assunto, SUM(custas) FROM processos WHERE custas > 1000 GROUP BY assunto;`
E) `SELECT assunto, AVG(custas) FROM processos GROUP BY assunto WHERE SUM(custas) > 1000;`

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Condições envolvendo funções de agregação (como `AVG(custas)`) não podem ser colocadas na cláusula `WHERE`, que atua sobre linhas individuais antes do agrupamento. Elas devem ser inseridas na cláusula `HAVING` posicionada logo após o `GROUP BY`.
</details>

---

### Questão 3 (FCC - Pegadinha de Lógica de 3 Valores - 3VL)
Considere a tabela `funcionarios` que contém a coluna `supervisor_id` (que permite valores nulos). Um analista executa a seguinte consulta SQL:
```sql
SELECT nome 
FROM funcionarios 
WHERE id NOT IN (SELECT supervisor_id FROM funcionarios);
```
Se a tabela contiver pelo menos um registro onde `supervisor_id` seja `NULL`, o resultado retornado por esta consulta será:
A) Todos os funcionários que não possuem supervisor, excluindo os nulos.
B) Todos os funcionários da tabela, pois a subquery falha e retorna o conjunto completo.
C) Conjunto vazio (nenhuma linha retornada).
D) Um erro de sintaxe em tempo de execução no SGBD.
E) Apenas os funcionários cujos IDs não coincidam com os IDs válidos (não nulos) da subquery.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** Esta é uma pegadinha clássica da FCC sobre a Lógica de 3 Valores (3VL) no SQL. A cláusula `NOT IN` equivale a comparar a expressão com cada elemento usando `id <> valor` combinado com operadores `AND`. 
Se um dos elementos retornados pela subquery for `NULL`, a expressão lógica avaliada para cada linha torna-se: `id <> 1 AND id <> 2 AND id <> NULL`. 
Como qualquer comparação direta com `NULL` resulta em `UNKNOWN`, a conjunção de `AND` com um valor `UNKNOWN` resultará sempre em `UNKNOWN` ou `FALSE`. Logo, a cláusula `WHERE` nunca será avaliada como `TRUE` e a query retornará zero linhas.
</details>

---

### Questão 4 (FCC - TRT - Analista)
Em consultas relacionais, uma subconsulta (subquery) é dita **correlacionada** quando:
A) Ela é executada exatamente uma única vez, antes da execução da query externa, armazenando o resultado em memória temporária.
B) Ela utiliza operadores de comparação de múltiplos elementos, como `ANY` ou `ALL`.
C) Ela faz referência a uma ou mais colunas das tabelas presentes na query externa, exigindo que a subconsulta seja executada repetidamente para cada linha processada pela query externa.
D) Ela é declarada dentro da cláusula `FROM` como uma tabela derivada.
E) Ela retorna apenas dados estruturados em formato XML ou JSON.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** Diferente da subquery independente, a subquery correlacionada depende de valores da linha corrente da query externa (usando alias da tabela externa). Por isso, o SGBD conceitualmente a executa para cada linha da tabela externa, o que pode impactar a performance se não houver índices adequados.
</details>

---

### Questão 5 (FCC - Saneamento)
A cláusula `HAVING` pode ser utilizada em uma instrução SQL sem a presença explícita da cláusula `GROUP BY`. Nesse cenário específico, a cláusula `HAVING`:
A) Causará um erro de compilação em SGBDs padrão ANSI SQL como PostgreSQL e Oracle.
B) Tratará a tabela inteira como se fosse um único grupo de dados agregados.
C) Agirá exatamente da mesma forma que a cláusula `WHERE`, aplicando filtros em linhas individuais.
D) Agrupará os dados automaticamente pela coluna de chave primária da tabela.
E) Filtrará apenas registros duplicados (comportando-se como o `DISTINCT`).

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Sob o padrão SQL, se a cláusula `HAVING` for declarada sem um `GROUP BY`, a tabela inteira é tratada como um único grupo de linhas. A condição do `HAVING` será avaliada e, se verdadeira para a agregação global da tabela, todas as linhas serão retornadas; caso contrário, nenhuma será.
</details>

---

### Questão 6 (FCC - Concursos de Tribunais)
Considere as tabelas `lotacao` (com colunas `servidor_id` e `setor_id`) e `servidores` (com colunas `id` e `nome`). Deseja-se listar os nomes dos servidores que **não** estão associados a nenhuma lotação. Assinale a alternativa que executa essa tarefa usando o operador `EXISTS` de forma correlacionada e correta:
A) 
```sql
SELECT s.nome FROM servidores s 
WHERE NOT EXISTS (SELECT 1 FROM lotacao l WHERE l.servidor_id = s.id);
```
B) 
```sql
SELECT s.nome FROM servidores s 
WHERE EXISTS (SELECT s.id FROM lotacao l WHERE l.servidor_id <> s.id);
```
C) 
```sql
SELECT s.nome FROM servidores s 
WHERE NOT EXISTS (SELECT * FROM lotacao l);
```
D) 
```sql
SELECT s.nome FROM servidores s 
WHERE EXISTS (SELECT 1 FROM lotacao l HAVING l.servidor_id = s.id);
```
E) 
```sql
SELECT s.nome FROM servidores s 
WHERE s.id NOT EXISTS (SELECT l.servidor_id FROM lotacao l);
```

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** O operador `NOT EXISTS` verifica se a subconsulta associada retorna alguma linha. Na subconsulta correlacionada `WHERE l.servidor_id = s.id`, se houver correspondência na tabela `lotacao` para o servidor corrente, a subquery retornará uma linha (o valor `1`), fazendo com que `NOT EXISTS` retorne `FALSE` e o servidor seja descartado. Se não houver lotação, a subquery é vazia, o `NOT EXISTS` retorna `TRUE` e o nome do servidor é exibido.
</details>

---

### Questão 7 (FCC - Metrô - Analista)
Em uma query SQL, o operador `ANY` é utilizado em conjunto com uma subquery que retorna uma lista de valores. A condição `valor > ANY (subquery)` é avaliada como verdadeira se:
A) O `valor` for maior do que o maior elemento retornado pela subquery.
B) O `valor` for maior do que pelo menos um dos elementos individuais retornados pela subquery.
C) O `valor` for maior do que a média aritmética de todos os elementos da subquery.
D) Todos os elementos da subquery forem maiores do que o `valor`.
E) A subquery retornar um conjunto vazio de dados.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O operador `ANY` (equivalente ao `SOME`) exige que a condição seja verdadeira para **pelo menos um** elemento do conjunto retornado. Portanto, `valor > ANY (10, 20, 30)` é verdadeiro se o valor for maior que 10. Para exigir que seja maior que todos, deve-se usar o operador `ALL`.
</details>

---

### Questão 8 (FCC - TRF)
Qual o comportamento da expressão `valor > ALL (subquery)` no SQL caso a subquery retorne uma lista contendo os valores `(15, 30, NULL)`?
A) A expressão será avaliada como verdadeira se `valor` for maior que 30.
B) A expressão será avaliada como falsa para qualquer `valor` testado.
C) O SGBD apresentará um erro de conversão de dados.
D) A expressão retornará sempre o valor lógico `UNKNOWN`, não selecionando nenhum registro.
E) A expressão ignorará o valor `NULL` e testará apenas contra 15 e 30.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** O operador `ALL` expande a comparação para `valor > 15 AND valor > 30 AND valor > NULL`. Como a comparação `valor > NULL` resulta em `UNKNOWN`, a conjunção final via `AND` resultará sempre em `UNKNOWN` (se `valor > 30` for verdadeiro) ou `FALSE` (se `valor <= 30`). Portanto, nenhuma linha atenderá ao filtro.
</details>

---

### Questão 9 (FCC - TRT)
Considere a seguinte query SQL estruturada:
```sql
SELECT departamento_id, COUNT(*)
FROM funcionarios
GROUP BY departamento_id
HAVING COUNT(*) > (SELECT AVG(qtd) FROM (
    SELECT COUNT(*) as qtd 
    FROM funcionarios 
    GROUP BY departamento_id
) as sub);
```
O objetivo desta consulta é listar os departamentos que possuem:
A) Uma quantidade de funcionários superior à média de funcionários por departamento da empresa.
B) A quantidade máxima de funcionários da empresa.
C) Pelo menos um funcionário alocado.
D) Menos funcionários do que a média global de departamentos vazios.
E) Apenas os departamentos cuja contagem de funcionários seja par.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** A subquery interna calcula a contagem de funcionários agrupados por departamento (`SELECT COUNT(*) as qtd...`). A subquery intermediária calcula a média dessas contagens (`SELECT AVG(qtd)...`). A query externa filtra via `HAVING` os departamentos cuja contagem individual (`COUNT(*)`) é maior do que essa média calculada.
</details>

---

### Questão 10 (FCC - Assembleia Legislativa)
Ao escrever uma subquery na cláusula `FROM` de um comando `SELECT`, o desenvolvedor está criando o que a literatura de bancos de dados chama de:
A) View Materializada estática.
B) Subquery correlacionada de projeção.
C) Tabela derivada (ou Inline View), sendo obrigatória a especificação de um alias (nome alternativo) para a subquery na maioria dos SGBDs.
D) Gatilho (Trigger) dinâmico de execução.
E) Índice de cobertura lógico.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** Uma subquery na cláusula `FROM` gera uma tabela temporária em memória chamada **tabela derivada** ou **inline view**. SGBDs relacionais como PostgreSQL, MySQL e SQL Server exigem sintaticamente que essa tabela receba um alias (ex: `SELECT * FROM (SELECT ...) AS temp;`) para que suas colunas possam ser referenciadas.
</details>

---

### Questão 11 (FCC - TRT 11ª Região - Analista Judiciário - TI)
Deseja-se criar um relatório que mostre o ID do processo e a diferença entre o valor das custas daquele processo específico e a média de custas de todos os processos da mesma classe judicial. Qual técnica SQL atende a essa necessidade de forma direta e elegante?
A) Subquery correlacionada na cláusula `SELECT`.
B) Cláusula `GROUP BY` contendo o ID do processo.
C) Cláusula `WHERE` associada a uma subquery não correlacionada.
D) Uma junção externa (`LEFT JOIN`) sem chave de correspondência.
E) Cláusula `HAVING` com filtro no ID do processo.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** Para calcular um valor de comparação individualizado (linha a linha) que necessita de agregação contextualizada (mesma classe judicial), pode-se projetar uma subquery correlacionada diretamente no `SELECT`:
`SELECT id, custas - (SELECT AVG(custas) FROM processos p2 WHERE p2.classe = p1.classe) AS diferenca FROM processos p1;`
</details>

---

### Questão 12 (FCC - Metrô - Analista)
Considere a tabela `projetos` (com colunas `id` e `nome`). Para selecionar todos os dados de `projetos` cujos IDs existam na tabela `alocacoes`, a consulta com `EXISTS` é muito eficiente. No entanto, é comum vermos na subquery interna a projeção `SELECT 1` ou `SELECT *`. Em relação ao desempenho e processamento dessas projeções na cláusula `EXISTS`, é correto afirmar que:
A) O uso de `SELECT 1` é muito mais rápido do que `SELECT *` porque evita que o SGBD carregue todas as colunas da tabela interna em disco.
B) O uso de `SELECT *` é proibido pelo padrão SQL ANSI dentro de operadores `EXISTS`.
C) Ambas as projeções possuem desempenho idêntico, pois o operador `EXISTS` avalia apenas a existência de linhas retornadas, ignorando a lista de colunas projetadas na subquery.
D) O SGBD falhará se `SELECT NULL` for utilizado dentro do `EXISTS`.
E) A cláusula `EXISTS` exige obrigatoriamente que a chave primária da tabela interna seja projetada na subquery.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O otimizador de consultas de SGBDs modernos ignora completamente a lista de seleção (projeção) dentro do `EXISTS`, pois o operador se preocupa apenas em receber um sinalizador de "linha encontrada" (verdadeiro/falso). Portanto, `SELECT 1`, `SELECT *` ou `SELECT NULL` têm exatamente o mesmo plano de execução e desempenho.
</details>

---

### Questão 13 (FCC - TRF - Analista)
Considere o seguinte comando SQL executado em um banco PostgreSQL 15:
```sql
SELECT classe_judicial, COUNT(*)
FROM processos
WHERE data_distribuicao >= '2026-01-01'
GROUP BY classe_judicial
HAVING COUNT(*) > 500;
```
Para otimizar a velocidade desta consulta, o especialista em banco de dados deve sugerir a criação de um índice composto nas colunas:
A) `(classe_judicial, count)`
B) `(data_distribuicao, classe_judicial)`
C) `(classe_judicial)` apenas, pois a data está no `WHERE` e não afeta o agrupamento.
D) Um índice do tipo Hash na coluna `data_distribuicao`.
E) Índices separados nas colunas `classe_judicial` e `data_distribuicao`.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Um índice composto que inicia pela coluna filtrada no `WHERE` (`data_distribuicao`) seguido pela coluna de agrupamento no `GROUP BY` (`classe_judicial`) permite ao SGBD filtrar rapidamente os registros válidos e já ler os dados ordenados para o agrupamento, evitando um custo elevado de ordenação temporária (Sort) ou hash em disco.
</details>

---

### Questão 14 (FCC - TRT)
Considere a tabela `vendas` com as colunas `vendedor`, `produto` e `valor`. Executa-se a seguinte consulta:
```sql
SELECT vendedor, produto, SUM(valor) 
FROM vendas 
GROUP BY vendedor, produto;
```
Para que um registro seja agrupado na mesma linha de saída, ele deve possuir:
A) O mesmo vendedor ou o mesmo produto.
B) O mesmo vendedor e o mesmo produto.
C) O mesmo valor, independentemente do vendedor.
D) Apenas o mesmo vendedor (o produto será agregado automaticamente pelo primeiro registro).
E) A tabela inteira será agrupada em uma única linha se o vendedor for idêntico.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Quando informamos múltiplas colunas na cláusula `GROUP BY` (`vendedor, produto`), o SGBD cria grupos com base na combinação única de valores de todas as colunas listadas. Assim, registros de um mesmo vendedor com produtos diferentes formarão linhas separadas no resultado.
</details>

---

### Questão 15 (FCC - TRT 24ª Região)
Qual a restrição correta imposta à lista de colunas projetadas na cláusula `SELECT` quando a cláusula `GROUP BY` é utilizada?
A) Nenhuma coluna que não esteja no `GROUP BY` pode ser referenciada no `SELECT`.
B) O `SELECT` pode projetar qualquer coluna da tabela, desde que a tabela tenha chave primária definida.
C) Apenas funções agregadas (como `SUM`, `AVG`, `COUNT`) podem ser projetadas.
D) Colunas projetadas no `SELECT` que não constem na cláusula `GROUP BY` devem, obrigatoriamente, estar contidas dentro de funções de agregação.
E) A cláusula `SELECT` deve conter exatamente as mesmas colunas do `GROUP BY`, sendo proibido o uso de agregadores.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** Para manter a integridade relacional do resultado agrupado, cada coluna projetada no `SELECT` deve ter um valor único por grupo. Isso significa que ela deve fazer parte do critério de agrupamento (`GROUP BY`) ou ser reduzida a um valor único através de uma função agregada (ex: `MAX`, `MIN`, `SUM`).
</details>

---

## 📝 TEMA 2: Infraestrutura e Redes — Roteamento (RIP, OSPF, BGP) + DNS + DHCP

### Questão 16 (FCC - TRT - Analista Judiciário - TI)
O protocolo RIP (Routing Information Protocol) é um protocolo de roteamento interno clássico. Assinale a alternativa que apresenta características corretas do RIP versão 2 (RIPv2):
A) Utiliza o algoritmo de Dijkstra (Shortest Path First), com métrica baseada em largura de banda.
B) É um protocolo do tipo Distance Vector, utiliza contagem de saltos (hop count) como métrica (limite de 15 saltos) e envia suas atualizações via multicast.
C) Opera na camada de Rede do modelo OSI diretamente sobre o protocolo IP (protocolo número 89).
D) É classificado como um Exterior Gateway Protocol (EGP) e utiliza sessões TCP na porta 179.
E) Não oferece suporte a máscaras de sub-rede de tamanho variável (VLSM) por ser classful.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O RIPv2 é um protocolo IGP de vetor de distância classless (suporta VLSM e CIDR). A sua métrica é o número de saltos, sendo que o valor máximo permitido é 15 (16 significa destino inacessível). As atualizações são enviadas via multicast para o endereço `224.0.0.9` (porta UDP 520).
</details>

---

### Questão 17 (FCC - TRT 15ª Região - Analista)
Considere o funcionamento do protocolo OSPF (Open Shortest Path First) em redes corporativas de grande porte. Em relação à organização em áreas e à otimização de tráfego, o OSPF estabelece que:
A) Todas as áreas OSPF devem se conectar fisicamente ou logicamente à área backbone (Área 0).
B) O roteador central que conecta a rede interna à internet é denominado DR (Designated Router).
C) O protocolo utiliza contagem de saltos como métrica padrão, descartando links com mais de 10 saltos.
D) O OSPF não exige o envio de mensagens do tipo Hello para manter a vizinhança ativa.
E) A convergência de rotas no OSPF é mais lenta do que no protocolo RIP devido à complexidade do algoritmo Bellman-Ford.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** A arquitetura OSPF exige uma estrutura hierárquica em áreas para limitar a propagação de LSAs e simplificar a tabela de rotas. A Área 0 (Backbone) é o núcleo de trânsito da rede, e todas as outras áreas devem estar conectadas a ela (diretamente ou via link virtual).
</details>

---

### Questão 18 (FCC - TRF 3ª Região - Analista)
O Border Gateway Protocol (BGP) é o protocolo de roteamento padrão utilizado para conectar Sistemas Autônomos (AS) na infraestrutura global da Internet. Em relação ao BGP, é correto afirmar que:
A) É um protocolo do tipo Link State que utiliza o algoritmo SPF.
B) Utiliza o protocolo de transporte UDP na porta 179 para garantir mensagens rápidas de controle.
C) É um protocolo do tipo Path Vector, utiliza conexões TCP (porta 179) estáveis para trocar informações de roteamento e gerencia políticas de tráfego através de atributos (ex: AS-Path, Local Preference).
D) Roteadores que rodam BGP dentro do mesmo AS utilizam obrigatoriamente a versão EBGP (Exterior BGP).
E) A métrica de seleção do BGP baseia-se unicamente na menor latência (RTT) do link físico.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O BGP é um protocolo Path Vector classificado como EGP. Para garantir confiabilidade, o BGP estabelece conexões ponto a ponto persistentes via TCP na porta 179. Ele não usa métricas simples como largura de banda ou saltos, mas sim atributos de caminho (`AS-Path`, `Local Preference`, `MED`, `Weight`) avaliados em uma ordem de decisão estrita.
</details>

---

### Questão 19 (FCC - METRÔ)
No protocolo OSPF, em uma rede do tipo multiacesso (como uma rede Ethernet LAN contendo vários roteadores interconectados por meio de um switch), para evitar que cada roteador estabeleça adjacências completas com todos os outros (gerando uma explosão de tráfego de sincronização de banco de dados), elege-se:
A) Um Servidor DHCP Centralizado e um Agente de Retransmissão (Relay Agent).
B) Um Roteador de Borda (ASBR) e um Roteador de Área (ABR).
C) Um Roteador Designado (DR - Designated Router) e um Roteador Designado de Backup (BDR).
D) Um Servidor DNS Secundário e uma Zona de Transferência ativa.
E) Um gateway padrão redundante utilizando o protocolo VRRP.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** Em redes multiacesso, o OSPF elege um **DR** e um **BDR** com base na prioridade do roteador ou no maior Router ID. Todos os outros roteadores (DRothers) estabelecem adjacência completa apenas com o DR e o BDR, reduzindo o número de adjacências de $N \times (N-1)/2$ para apenas $2N - 3$.
</details>

---

### Questão 20 (FCC - TRT 6ª Região)
O serviço DNS (Domain Name System) realiza a resolução de nomes amigáveis em endereços IP. Para sua operação, o DNS utiliza primariamente a porta:
A) UDP 53 para consultas e respostas comuns de clientes; e TCP 53 para transferências de zona entre servidores e respostas que excedam o limite clássico de tamanho de pacote UDP.
B) TCP 80 para consultas HTTP seguras e UDP 443 para transferências de zonas criptografadas.
C) UDP 67 para consultas do cliente e TCP 68 para atualizações do servidor de nomes.
D) TCP 53 exclusivamente, pois o DNS não suporta tráfego não confiável via UDP.
E) UDP 161 para gerenciar as tabelas de consultas locais (MIBs).

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** O DNS opera na porta 53. Consultas iterativas e recursivas padrão feitas por clientes (resolvers) utilizam **UDP 53** para menor overhead. No entanto, se o pacote de resposta for maior que 512 bytes (ou o limite do EDNS), ou durante transferências de zonas (AXFR/IXFR) entre servidores Master e Slave, utiliza-se a confiabilidade do **TCP 53**.
</details>

---

### Questão 21 (FCC - ARTESP)
Um administrador de rede precisa configurar um servidor DNS corporativo para que ele aponte o nome do domínio principal do tribunal para o endereço IPv6 do servidor web correspondente. O registro de recurso (Resource Record) do DNS que realiza essa associação é o tipo:
A) A
B) AAAA
C) CNAME
D) PTR
E) MX

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** 
- **AAAA:** Associa um nome de domínio a um endereço **IPv6** (128 bits).
- **A:** Associa um nome a um endereço **IPv4** (32 bits).
- **CNAME:** Cria um codinome/apelido (alias) para um nome canônico.
- **PTR:** Registro reverso (associa um IP a um nome).
- **MX:** Aponta para os servidores de correio eletrônico (mail exchange) do domínio.
</details>

---

### Questão 22 (FCC - TRT)
No contexto de servidores de nomes DNS, a funcionalidade na qual um servidor secundário (Slave) copia periodicamente todo ou parte do banco de dados de zonas de um servidor primário (Master) para fins de redundância é conhecida como:
A) Consulta Recursiva Direta.
B) Transferência de Zona (Zone Transfer - AXFR/IXFR).
C) Delegação de Subdomínio.
D) Encaminhamento (Forwarding) de DNS Iterativo.
E) Cache Poisoning de DNS.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A **Transferência de Zona** é o mecanismo de sincronização de registros DNS entre servidores Master e Slave. Pode ser do tipo **AXFR** (Full Zone Transfer - copia a zona completa) ou **IXFR** (Incremental Zone Transfer - copia apenas as alterações).
</details>

---

### Questão 23 (FCC - PGE-CE)
O protocolo DHCP (Dynamic Host Configuration Protocol) automatiza a atribuição de endereços de rede a hosts clientes. O processo clássico de troca de mensagens DHCP entre o cliente e o servidor para a concessão de um novo endereço IP compreende 4 etapas consecutivas conhecidas pela sigla:
A) DORA (Discover, Offer, Request, Acknowledge)
B) RARP (Request, ARP, Reply, Port)
C) SYN, SYN-ACK, ACK, FIN
D) PADI, PADO, PADR, PADS
E) UDP, TCP, IP, ICMP

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** As mensagens do processo **DORA** são:
1. **DHCP Discover:** O cliente envia um broadcast para localizar servidores DHCP ativos.
2. **DHCP Offer:** Os servidores respondem com uma proposta de IP disponível.
3. **DHCP Request:** O cliente envia um broadcast solicitando formalmente o IP oferecido.
4. **DHCP Acknowledge (ACK):** O servidor confirma a concessão (lease) e envia os parâmetros adicionais (máscara, gateway, DNS).
</details>

---

### Questão 24 (FCC - TRF - Analista)
Em relação às portas e ao protocolo de transporte utilizados pelo DHCP, assinale a alternativa correta:
A) O DHCP utiliza o protocolo TCP nas portas 80 e 443 para segurança dos dados corporativos.
B) O DHCP utiliza o protocolo de transporte UDP, com o servidor escutando na porta 67 e o cliente escutando na porta 68.
C) O cliente envia requisições na porta TCP 68 e o servidor responde via multicast na porta UDP 67.
D) O DHCP opera de forma descentralizada na camada física do modelo OSI, dispensando portas lógicas.
E) O protocolo de transporte utilizado é o ICMP (portas dinâmicas de 1 a 1024).

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O DHCP utiliza a arquitetura UDP para evitar o overhead de conexões TCP em redes sem IP configurado no cliente. Por padrão, o **servidor escuta na porta UDP 67** (recebendo requisições) e o **cliente escuta na porta UDP 68** (recebendo as respostas).
</details>

---

### Questão 25 (FCC - METRÔ)
Durante o ciclo de concessão de um endereço IP pelo DHCP, o cliente monitora temporizadores para renovar seu aluguel (lease time). O cliente tenta renovar a concessão pela primeira vez de forma automática enviando uma mensagem `DHCP Request` do tipo unicast diretamente ao servidor original quando atinge:
A) 87,5% do tempo total da concessão (Timer T2).
B) 100% do tempo total da concessão (Expiração).
C) 50% do tempo total da concessão (Timer T1).
D) 10% do tempo total da concessão.
E) Apenas se houver reinicialização física da placa de rede.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O temporizador **T1 (Renewal Timer)** é configurado por padrão em **50%** do tempo total de concessão do IP (lease time). Ao atingir T1, o cliente envia um `DHCP Request` unicast. Se não obtiver resposta do servidor original até atingir o temporizador **T2 (Rebinding Timer - 87,5%** do lease time), o cliente envia mensagens de request em broadcast para tentar renovar com qualquer servidor DHCP disponível na sub-rede.
</details>

---

### Questão 26 (FCC - TRT)
Um administrador de rede precisa conectar duas filiais do TJ-CE através de uma nuvem IP pública utilizando roteamento estático ou dinâmico. Se ele optar pelo roteamento dinâmico baseado em **Link State**, o protocolo mais adequado para gerenciar essa rede interna (IGP) de forma escalável e com rápida convergência é o:
A) RIPv1.
B) BGP-4.
C) OSPF.
D) RIPv2.
E) EGP.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O OSPF é o protocolo IGP de estado de enlace (Link State) mais utilizado do mercado. Diferente dos protocolos baseados em vetor de distância (como RIP), o OSPF mantém um mapa completo da topologia da rede em cada roteador (LSDB), permitindo uma convergência extremamente rápida e sem loops de roteamento.
</details>

---

### Questão 27 (FCC - TRT)
Considere a diferença operacional entre **IBGP (Internal BGP)** e **EBGP (External BGP)**. É correto afirmar que:
A) O EBGP é utilizado para estabelecer vizinhança entre roteadores BGP dentro do mesmo Sistema Autônomo (AS).
B) Roteadores executando IBGP assumem que todos os roteadores internos estão diretamente conectados e ignoram a tabela de rotas interna (IGP).
C) O IBGP é utilizado para roteadores BGP pertencentes ao mesmo AS, possuindo uma regra de "split horizon" que impede que um roteador encaminhe para vizinhos internos uma rota aprendida de outro vizinho interno (exigindo conexões em malha completa - Full Mesh - ou uso de Route Reflectors).
D) O EBGP altera o atributo `Next-Hop` das mensagens de rota, enquanto o IBGP altera a métrica baseada em hop count.
E) O IBGP exige cabos físicos dedicados para estabelecer sessões entre roteadores.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** Para evitar loops de roteamento dentro de um mesmo AS, o IBGP estabelece que uma rota aprendida de um vizinho IBGP **não** pode ser retransmitida para outro vizinho IBGP. Por isso, exige-se uma topologia lógica Full Mesh (onde todos os roteadores rodam sessões IBGP entre si) ou soluções escaláveis como **Route Reflectors (Refletores de Rota)** ou Confederations BGP.
</details>

---

### Questão 28 (FCC - TRF - Analista)
Em redes locais segmentadas por roteadores, os pacotes DHCP Discover (que utilizam o endereço IP de destino de broadcast `255.255.255.255`) são descartados por padrão pelos roteadores para evitar tempestades de broadcast. Para permitir que clientes de sub-redes remotas obtenham parâmetros IP de um servidor DHCP localizado em um segmento de rede central, o roteador da sub-rede local do cliente deve ser configurado com o recurso:
A) NAT (Network Address Translation).
B) DNS Forwarder.
C) DHCP Relay Agent (ou comando helper-address em roteadores Cisco).
D) Proxy reverso transparente.
E) VLAN Trunking (IEEE 802.1Q).

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O **DHCP Relay Agent** intercepta os pacotes de broadcast locais enviados pelo cliente (porta UDP 68), transforma-os em pacotes unicast direcionados ao endereço IP real do servidor DHCP remoto e encaminha-os de volta.
</details>

---

### Questão 29 (FCC - ARTESP)
Qual das seguintes alternativas descreve corretamente o funcionamento de uma consulta DNS do tipo **Recursiva** efetuada por um cliente de rede?
A) O cliente pergunta a um servidor DNS local, que assume a responsabilidade de consultar outros servidores de nomes na internet até obter a resposta final e retorná-la ao cliente.
B) O cliente deve consultar manualmente cada servidor de nomes root, TLD e autoritativo até obter a resposta.
C) O servidor DNS local responde imediatamente com a melhor resposta parcial que possui, instruindo o cliente sobre qual outro servidor consultar.
D) O servidor de nomes inverte o processo e tenta descobrir o IP do próprio host solicitante (DNS Reverso).
E) A consulta é bloqueada temporariamente para validação de certificados SSL.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** Na consulta **recursiva**, o servidor DNS consultado compromete-se a retornar a resposta definitiva ao cliente (ou uma mensagem de erro indicando que o nome não existe), realizando todas as buscas intermediárias em cascata em nome do solicitante. Na consulta **iterativa**, o servidor responde apenas com a indicação (referral) do próximo servidor da árvore hierárquica.
</details>

---

### Questão 30 (FCC - TRT)
Considere a métrica do RIP que limita as rotas a 15 saltos. O principal problema associado a esse limite e ao algoritmo de vetor de distância básico em caso de falhas em links físicos da rede é o:
A) Estouro de pilha de memória por pacotes excessivamente grandes.
B) Problema de Contagem até o Infinito (Count-to-Infinity) antes que a rota com falha seja descartada definitivamente.
C) Descarte imediato de todas as rotas válidas da rede.
D) Conflito de IPs idênticos duplicados por tabelas corrompidas.
E) Alinhamento incorreto de pacotes UDP na porta 179.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Como roteadores que rodam vetor de distância clássico (como RIP) propagam rotas baseados nas tabelas dos vizinhos sem conhecer a topologia completa, uma queda de link pode fazer com que dois roteadores fiquem trocando atualizações incrementando a métrica em loop. Esse problema de **Count-to-Infinity** é mitigado por mecanismos como *split horizon*, *route poisoning* e definição de métrica máxima de infinito igual a 16.
</details>

---

## 📝 TEMA 3: Legislação Previdenciária do Estado do Ceará — Sistema Único de Previdência (SUPSEC)

### Questão 31 (FCC - Adaptada)
O Sistema Único de Previdência Social dos Servidores Públicos Civis e Militares, dos Agentes Públicos e dos Membros de Poder do Estado do Ceará (SUPSEC) foi instituído pela Lei Complementar Estadual nº 12/1999. De acordo com a legislação estadual, o SUPSEC destina-se a gerenciar os regimes previdenciários de quais categorias?
A) Servidores exclusivamente comissionados e empregados públicos de empresas privadas do Ceará.
B) Servidores públicos estaduais titulares de cargos efetivos, membros de Poder, militares do Estado, ativos, inativos e respectivos pensionistas.
C) Prefeitos e vereadores de todos os municípios do Ceará sob regime do INSS.
D) Apenas servidores ativos da área de segurança pública e saúde estadual.
E) Empregados de concessionárias de serviços de saneamento e transporte público municipal.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O SUPSEC é o regime próprio de previdência social (RPPS) do Estado do Ceará. Ele abrange todos os servidores civis estáveis/efetivos (e membros de Poder) e militares estaduais, tanto em atividade quanto os aposentados/reserva/reforma e seus respectivos pensionistas (Art. 1º e 2º da LC 12/99).
</details>

---

### Questão 32 (FCC - TJ-CE - Juiz Substituto - Adaptada)
Nos termos da Lei Complementar Estadual nº 12/1999 (SUPSEC Ceará), os beneficiários do sistema previdenciário classificam-se em segurados e dependentes. Na categoria de dependentes previdenciários de **Classe I**, estão listados, entre outros:
A) O cônjuge, a companheira ou companheiro e os filhos de qualquer condição menores de 21 anos (ou inválidos/deficientes de qualquer idade).
B) Os pais do segurado, desde que comprovem dependência econômica.
C) Os irmãos de qualquer condição menores de 18 anos ou inválidos.
D) O enteado e o menor sob tutela, independentemente de declaração ou dependência econômica.
E) O ex-cônjuge divorciado que não receba pensão alimentícia judicial.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** A Classe I de dependentes do SUPSEC é a classe prioritária e inclui o cônjuge, companheiro(a) e os filhos não emancipados, de qualquer condição, menores de 21 anos ou inválidos/deficientes de qualquer idade (Art. 8º, I da LC 12/99).
</details>

---

### Questão 33 (FCC - TJ-CE)
Considere a regra de exclusão e concorrência de dependentes no âmbito do SUPSEC Ceará. Caso um segurado falecido possua dependentes ativos classificados na **Classe I** (ex: cônjuge e filho menor), o direito ao benefício de pensão por morte para os dependentes classificados na **Classe II** (pais) e **Classe III** (irmãos):
A) Será rateado de forma proporcional entre todos os membros de todas as classes envolvidas.
B) Ficará suspenso temporariamente até que o filho menor atinja a maioridade civil.
C) Fica totalmente excluído, pois a existência de dependentes de qualquer classe precedente exclui do direito às prestações previdenciárias os dependentes das classes seguintes.
D) Será concedido apenas se os pais comprovarem residir sob o mesmo teto do segurado falecido.
E) Exige autorização judicial em processo autônomo de jurisdição voluntária.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** Trata-se da regra de preferência previdenciária clássica disposta no Artigo 8º, § 1º da LC 12/1999: *"A existência de dependente de qualquer das classes deste artigo exclui do direito às prestações os das classes seguintes"*.
</details>

---

### Questão 34 (FCC - Concursos de Tribunais)
Em relação à comprovação de dependência econômica para fins de concessão de benefícios previdenciários no SUPSEC Ceará, assinale a alternativa correta:
A) A dependência econômica das pessoas classificadas na Classe I (cônjuge e filhos) deve ser provada anualmente por meio de certidões fiscais.
B) A dependência econômica das pessoas da Classe I é presumida, enquanto a das Classes II (pais) e III (irmãos) deve ser cabalmente comprovada.
C) Nenhuma classe possui presunção de dependência econômica, exigindo-se perícia social e financeira para todos os beneficiários.
D) Apenas o cônjuge tem presunção de dependência; os filhos menores de 21 anos devem provar que não possuem renda própria.
E) Pais e irmãos possuem presunção legal absoluta de dependência financeira por serem parentes consanguíneos diretos.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Conforme o Art. 8º, § 2º da LC 12/1999, os dependentes de Classe I gozam de **presunção legal de dependência econômica** (dispensando provas documentais de custeio diário). Os dependentes de Classe II (pais) e Classe III (irmãos) devem comprovar a dependência econômica real e exclusiva em relação ao segurado falecido.
</details>

---

### Questão 35 (FCC - Concursos Estaduais Ceará)
A Emenda Constitucional Federal nº 103/2019 alterou profundamente o regime de previdência social. Em harmonia com as diretrizes federais, a legislação previdenciária do Ceará restringe o rol de benefícios previdenciários concedidos pelo SUPSEC. Atualmente, constituem benefícios de natureza estritamente previdenciária de responsabilidade do SUPSEC:
A) Aposentadoria (ou reforma/reserva para militares) e Pensão por Morte.
B) Aposentadoria, auxílio-doença, salário-maternidade e auxílio-reclusão.
C) Licença para tratamento de saúde, salário-família e pensão por morte.
D) Apenas a Pensão por Morte (as aposentadorias passaram a ter natureza assistencial).
E) Licença-prêmio convertida em pecúnia e indenizações por invalidez.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** Após a Reforma da Previdência (EC 103/19) e a consequente adequação da legislação do Estado do Ceará, os regimes próprios (RPPS) ficaram proibidos de custear benefícios de natureza não previdenciária. Assim, o auxílio-doença (licença médica), o salário-maternidade e o auxílio-reclusão foram desconstitucionalizados como benefícios previdenciários e passaram a ser pagos diretamente pelo órgão de dotação orçamentária do servidor ativo (natureza estatutária/administrativa), restando ao SUPSEC apenas as **Aposentadorias/Reforma/Reserva e as Pensões por Morte**.
</details>

---

### Questão 36 (FCC - PGE-CE - Adaptada)
Considere as regras de cálculo para a concessão do benefício de Pensão por Morte estabelecidas na legislação previdenciária cearense após a reforma da previdência. O valor da pensão equivalente às cotas de dependentes será rateado da seguinte forma:
A) 100% do valor da base de cálculo para o cônjuge sobrevivente, acrescido de 10% por filho menor até o limite de 150%.
B) Uma cota familiar equivalente a 50% do valor da aposentadoria recebida pelo segurado (ou daquela a que teria direito), acrescida de cotas de 10% por dependente, até o limite máximo de 100%.
C) 70% fixos do subsídio do cargo efetivo do segurado em atividade.
D) Distribuição desigual baseada na idade do beneficiário mais jovem.
E) 100% integrais divididos igualmente, independentemente do número de dependentes.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Alinhado com o Artigo 23 da EC 103/2019 e incorporado às regras estaduais do Ceará, a pensão por morte é calculada por um sistema de cotas: **50% de cota familiar básica + 10% por dependente** alocado, até atingir o limite de 100%. Se houver perda da qualidade de um dos dependentes, a sua cota de 10% deixa de ser devida (regra de não reversibilidade automática da cota, salvo disposição específica).
</details>

---

### Questão 37 (FCC - TJ-CE)
De acordo com as regras de perda da qualidade de dependente no SUPSEC Ceará, o direito à cota-parte de pensão ou dependência previdenciária do filho do segurado cessa, por regra geral:
A) Ao completar 18 anos de idade, sem exceções.
B) Ao completar 21 anos de idade, salvo se inválido ou com deficiência intelectual, mental ou grave.
C) Ao concluir o curso de ensino superior em instituição credenciada pelo MEC.
D) Apenas ao completar 25 anos se comprovar matrícula em universidade.
E) Apenas em caso de casamento civil ou concurso público aprovado.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Conforme a legislação previdenciária estadual, a maioridade previdenciária para os filhos cessa aos **21 anos**, ocorrendo a extinção automática do benefício, **salvo** se o dependente for comprovadamente inválido ou possuir deficiência física, mental ou intelectual grave diagnosticada antes de atingir essa idade.
</details>

---

### Questão 38 (FCC - TJ-CE - Analista)
Um segurado ativo do TJ-CE falece deixando como dependentes habilitados de Classe I sua esposa e duas filhas menores de idade. A divisão do valor total do benefício previdenciário de pensão por morte será feita:
A) Destinando 50% do valor total à esposa e os outros 50% divididos em partes iguais entre as filhas.
B) Rateando o valor integral da pensão em partes rigorosamente iguais entre todos os dependentes habilitados da mesma classe (1/3 para cada).
C) Destinando o valor integral apenas à esposa por chefia de família.
D) Concedendo 100% do valor para a esposa e 10% de adicional assistencial não integrável para cada filha.
E) De forma decrescente por ordem de nascimento das filhas.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Conforme as diretrizes da LC 12/1999 (SUPSEC), os benefícios de pensão por morte destinados a dependentes de uma mesma classe habilitada são divididos e **rateados em partes iguais** entre todos os beneficiários daquela classe (Art. 35, § 1º).
</details>

---

### Questão 39 (FCC - PGE-CE)
Considere as contribuições previdenciárias destinadas ao custeio do SUPSEC Ceará. Os servidores inativos (aposentados) e pensionistas do Estado:
A) São totalmente isentos de qualquer contribuição previdenciária sob proteção do direito adquirido.
B) Contribuem com a mesma alíquota dos servidores ativos aplicada sobre o valor total de seus proventos de aposentadoria ou pensão, sem faixas de isenção.
C) Contribuem apenas sobre a parcela de seus proventos de aposentadoria e de pensão que supere o limite máximo (teto) estabelecido para os benefícios do Regime Geral de Previdência Social (RGPS), podendo incidir sobre o valor que supere o salário mínimo nacional caso seja constatado déficit atuarial no regime estadual.
D) Contribuem com uma taxa fixa anual equivalente a um salário mínimo vigente.
E) Contribuem apenas se retornarem ao serviço público em cargos de comissão.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** De acordo com as adequações previdenciárias cearenses alinhadas à EC 103/19: inativos e pensionistas contribuem sobre a parcela que ultrapassa o teto do RGPS. No entanto, em caso de **déficit atuarial comprovado**, a base de contribuição pode ser ampliada por lei estadual para incidir sobre o valor dos proventos que exceder o salário mínimo nacional.
</details>

---

### Questão 40 (FCC - Concursos Previdenciários)
A gestão, operacionalização, administração e governança dos regimes de previdência integrados ao SUPSEC Ceará são centralizadas e executadas por meio de uma fundação pública estadual específica criada para este fim. Esta entidade é a:
A) CEARAPREV (Fundação de Previdência Social do Estado do Ceará)
B) DETRAN-CE Previdenciário
C) COGERH Previdência
D) CEARAPREV-S/A (Empresa Privada de Previdência)
E) FUNPRESP-CE

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** A **CEARAPREV** (criada pela Lei Complementar Estadual nº 184/2018) é a fundação de previdência social responsável por gerenciar de forma unificada as aposentadorias e pensões de todos os Poderes e órgãos do Estado do Ceará associados ao SUPSEC.
</details>

---

### Questão 41 (FCC - Concursos de Tribunais)
Um servidor do Tribunal de Justiça do Ceará sofre um acidente grave fora do horário de trabalho que o incapacita de forma total e permanente para o serviço público. O laudo da equipe médica do tribunal atesta a impossibilidade de reabilitação para outro cargo. Nos termos do regime próprio do Ceará (SUPSEC), o servidor será submetido à:
A) Demissão sem justa causa com indenização de FGTS.
B) Licença médica sem vencimentos por tempo indeterminado.
C) Aposentadoria por incapacidade permanente para o trabalho (antiga aposentadoria por invalidez).
D) Readaptação obrigatória em funções administrativas de menor complexidade.
E) Disponibilidade remunerada com vencimentos proporcionais ao tempo de serviço militar.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** Constatada a incapacidade total e permanente de forma definitiva por perícia biopsicossocial/médica oficial da CEARAPREV/Tribunal, e sem possibilidade de readaptação (Art. 37 da Constituição e LC 12/99), o servidor é aposentado por incapacidade permanente para o trabalho.
</details>

---

### Questão 42 (FCC - TJ-CE)
Considere as regras do SUPSEC Ceará. A idade máxima permitida para a permanência de um servidor público civil ativo no exercício de suas funções, ponto em que ocorrerá a sua **aposentadoria compulsória** automática com proventos proporcionais ao tempo de contribuição, é de:
A) 65 anos de idade.
B) 70 anos de idade.
C) 75 anos de idade.
D) 80 anos de idade.
E) 60 anos de idade para homens e 55 anos para mulheres.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** Em conformidade com a Lei Complementar Federal nº 152/2015 e as disposições integradas à previdência do Ceará, a idade limite para a aposentadoria compulsória de servidores da União, Estados, DF e Municípios é de **75 anos** (tanto para homens quanto para mulheres).
</details>

---

### Questão 43 (FCC - TJ-CE - Analista)
Em relação ao regime previdenciário do SUPSEC Ceará, o vínculo previdenciário do servidor estatutário nomeado para cargo efetivo no TJ-CE é:
A) Facultativo, podendo o servidor optar por contribuir apenas para planos privados de previdência complementar.
B) Obrigatório e automático a partir do momento da entrada em exercício no cargo público efetivo.
C) Temporário, extinguindo-se após 5 anos se o servidor não solicitar renovação.
D) Restrito apenas aos servidores nascidos no Estado do Ceará.
E) Vinculado ao regime geral do INSS até a conclusão do estágio probatório.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Os regimes próprios de previdência social (RPPS) possuem natureza de filiação **obrigatória e automática**. O servidor ocupante de cargo efetivo torna-se segurado obrigatório do SUPSEC na data de início do exercício de suas funções (Art. 5º da LC 12/99).
</details>

---

### Questão 44 (FCC - Concursos de Tribunais)
Considere o acúmulo de benefícios previdenciários de pensão por morte previstos pela legislação previdenciária cearense em consonância com a Emenda Constitucional nº 103/2019. É permitido ao cônjuge sobrevivente acumular integralmente:
A) Duas pensões por morte deixadas por cônjuges diferentes no âmbito do mesmo regime próprio (SUPSEC).
B) Uma pensão por morte decorrente de cônjuge segurado do SUPSEC Ceará com uma pensão por morte decorrente de cônjuge segurado do Regime Geral (RGPS/INSS), aplicando-se redutor escalonado sobre o benefício de menor valor.
C) Três pensões por morte de filhos diferentes.
D) Aposentadoria por invalidez civil com proventos de reforma militar cumulada com auxílio-acidente.
E) Nenhuma das alternativas. Qualquer acúmulo de pensões é expressamente proibido pela legislação do Ceará.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** É proibida a acumulação de mais de uma pensão por morte deixada por cônjuge ou companheiro no âmbito do mesmo regime de previdência. Contudo, é permitida a acumulação de uma pensão por morte do SUPSEC com outra de regime distinto (RGPS ou outro RPPS), aplicando-se o limitador/redutor escalonado (conforme Art. 24 da EC 103/19) sobre a pensão de menor valor.
</details>

---

### Questão 45 (FCC - Concursos Estaduais Ceará)
A fundação de previdência social do Estado do Ceará (CEARAPREV) realiza periodicamente um procedimento obrigatório para atualização cadastral, validação de dados de segurados ativos, aposentados e pensionistas do SUPSEC, visando combater fraudes e garantir a sustentabilidade atuarial. Este procedimento de atualização cadastral de caráter obrigatório é denominado:
A) Censo Previdenciário (ou Recadastramento Previdenciário).
B) Avaliação Biopsicossocial Coletiva.
C) Audiência de Instrução Previdenciária.
D) Inquérito Administrativo de Frequência.
E) Homologação de Estágio Probatório de Benefício.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** O **Censo Previdenciário** é a atualização de dados cadastrais, funcionais e previdenciários dos servidores ativos, aposentados, inativos e pensionistas do Estado do Ceará, administrado pela CEARAPREV, sendo obrigatório sob pena de suspensão do pagamento dos proventos ou pensão.
</details>
