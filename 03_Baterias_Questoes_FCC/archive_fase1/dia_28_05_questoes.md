# Bateria de Questões FCC — Quinta-feira 28/05

## 📝 TEMA 1: Banco de Dados, MongoDB e SQL

### Questão 1 (FCC - 2022 - TRT 22ª Região - Analista Judiciário - Tecnologia da Informação)
Na linguagem SQL, para combinar registros de duas tabelas, retornando todas as linhas da tabela da esquerda e as linhas correspondentes da tabela da direita, e preenchendo com nulos caso não haja correspondência, utiliza-se a junção do tipo:

A) INNER JOIN
B) FULL OUTER JOIN
C) RIGHT OUTER JOIN
D) LEFT OUTER JOIN
E) CROSS JOIN

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A) Incorreta. O INNER JOIN retorna exclusivamente os registros que possuem correspondência nas duas tabelas envolvidas na junção.
B) Incorreta. O FULL OUTER JOIN retorna todos os registros de ambas as tabelas (esquerda e direita), preenchendo com nulos os lados que não apresentarem correspondência.
C) Incorreta. O RIGHT OUTER JOIN prioriza a tabela da direita, retornando todas as suas linhas, e preenche com nulos as colunas da tabela da esquerda onde não houver vínculo.
D) Correta. O LEFT OUTER JOIN retorna todas as linhas da tabela declarada à esquerda da junção, além das linhas correspondentes da tabela da direita. Caso uma linha da esquerda não tenha par na direita, os campos desta última serão nulos na saída.
E) Incorreta. O CROSS JOIN não busca correspondências lógicas, ele realiza um produto cartesiano absoluto entre as tabelas, combinando cada linha de uma com todas as linhas da outra.
</details>

---

### Questão 2 (FCC - 2023 - TRT 18ª Região - Analista Judiciário - Tecnologia da Informação)
No MongoDB, um banco de dados NoSQL orientado a documentos, os dados são armazenados em um formato binário, permitindo maior eficiência de busca e armazenamento, que se assemelha ao JSON. Esse formato é conhecido como:

A) XML
B) BSON
C) YAML
D) Parquet
E) Avro

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) Incorreta. XML (eXtensible Markup Language) é uma linguagem de marcação baseada em tags, não sendo o formato de armazenamento padrão adotado nativamente pelo MongoDB.
B) Correta. O formato BSON (Binary JSON) é uma serialização de documentos semelhante ao JSON, utilizada nativamente pelo MongoDB para representar estruturas de dados e documentos de forma binária e altamente eficiente, otimizando velocidade e espaço.
C) Incorreta. YAML é um formato de serialização de dados focado em fácil leitura humana, muito comum em arquivos de configuração, mas não utilizado para o armazenamento interno no Mongo.
D) Incorreta. Parquet é um formato de armazenamento de dados colunar, mais comum em ecossistemas de Big Data (como Hadoop e Spark) para otimizar processamento analítico.
E) Incorreta. Avro é outro framework e formato de serialização de dados criado para o Apache Hadoop, não representando a estrutura interna básica do MongoDB.
</details>

---

### Questão 3 (FCC - 2023 - TRT 11ª Região - Analista Judiciário - Tecnologia da Informação)
Em uma consulta SQL, a cláusula utilizada para filtrar os resultados de uma função de agregação (como SUM, COUNT, AVG), operando nos grupos formados pela cláusula GROUP BY, é:

A) WHERE
B) ORDER BY
C) HAVING
D) DISTINCT
E) FILTER

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. A cláusula WHERE realiza o filtro a nível de linha, antes que os dados sejam agrupados. Ela não suporta avaliar funções de agregação, o que causaria erro de sintaxe.
B) Incorreta. A cláusula ORDER BY serve exclusivamente para a ordenação ascendente ou descendente do conjunto final de resultados, não para filtrar agrupamentos.
C) Correta. A cláusula HAVING foi desenhada para atuar em conjunto com o GROUP BY. Ela filtra os grupos após a sumarização das funções de agregação, descartando os agrupamentos que não passam no teste imposto.
D) Incorreta. A cláusula DISTINCT serve para suprimir valores duplicados da listagem resultante da projeção de campos, sem capacidade de fazer filtros lógicos.
E) Incorreta. A palavra-chave FILTER até possui utilidade para agregações específicas no padrão SQL moderno, mas a filtragem universal baseada em agregações para o GROUP BY dá-se via HAVING.
</details>

---

### Questão 4 (FCC - 2022 - TRT 23ª Região - Analista Judiciário - Tecnologia da Informação)
No contexto de projeto de banco de dados relacional, uma tabela encontra-se na Terceira Forma Normal (3FN) se, e somente se, estiver na Segunda Forma Normal (2FN) e:

A) contiver atributos multivalorados em colunas distintas.
B) todas as colunas não chaves forem mutuamente independentes e dependerem integralmente da chave primária.
C) não possuir dependências funcionais parciais em relação a uma chave primária composta.
D) não possuir atributos atômicos em sua estrutura.
E) todas as chaves estrangeiras forem também chaves primárias.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) Incorreta. O fato de não conter atributos multivalorados e estar contido apenas em colunas atômicas satisfaz apenas a Primeira Forma Normal (1FN).
B) Correta. Para uma tabela alcançar a Terceira Forma Normal (3FN), ela primeiramente deve estar na Segunda Forma Normal (2FN). Além disso, não pode haver dependência funcional transitiva de atributos não-chaves com a chave primária. Em outras palavras, todos os atributos não chave devem depender inteiramente e apenas da chave primária, e devem ser mutuamente independentes entre si.
C) Incorreta. Não possuir dependências funcionais parciais com relação a chaves compostas é o critério de normalização utilizado para elevar a relação à Segunda Forma Normal (2FN).
D) Incorreta. Pelo contrário, para satisfazer já as formas iniciais, como a 1FN, deve-se possuir unicamente atributos atômicos em sua estrutura.
E) Incorreta. Esta exigência não possui qualquer amparo nas formas normais de modelagem relacional. As chaves estrangeiras apenas referenciam chaves primárias de outras relações, independentemente da forma normal.
</details>

---

### Questão 5 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - Tecnologia da Informação)
Em relação ao MongoDB, os agrupamentos de documentos dentro de um banco de dados, que são equivalentes às tabelas de um banco de dados relacional, são denominados:

A) Tabelas
B) Grafos
C) Coleções
D) Chaves
E) Agregados

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. O termo "tabelas" provém unicamente do mundo dos bancos de dados relacionais e em SQL não é utilizado para representar os grupos no MongoDB.
B) Incorreta. Bancos baseados em grafos representam dados em nós e arestas (ex.: Neo4j). O MongoDB é focado em documentos.
C) Correta. No MongoDB, a analogia direta com as tabelas relacionais é a estrutura chamada de Coleção (Collection), que armazena múltiplos documentos BSON não necessariamente de mesmo formato.
D) Incorreta. As chaves são importantes na formação das estruturas relacionais e NoSQL de chave-valor (Key-Value), que formam outro segmento de bancos não relacionais.
E) Incorreta. O framework de "Agregação" (Aggregation) existe no MongoDB para processamento de dados e pipelines, porém não é a estrutura persistente que estoca os dados, como as coleções.
</details>

---

### Questão 6 (FCC - 2021 - TCE-SC - Auditor Fiscal de Controle Externo - Ciência da Computação)
A linguagem SQL é dividida em subconjuntos de comandos, de acordo com a sua finalidade. Os comandos GRANT e REVOKE pertencem a qual subconjunto?

A) DML (Data Manipulation Language)
B) DDL (Data Definition Language)
C) DCL (Data Control Language)
D) DQL (Data Query Language)
E) TCL (Transaction Control Language)

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. A DML (Data Manipulation Language) abrange comandos operacionais sobre os dados, que são a Inserção, Atualização e Exclusão (INSERT, UPDATE, DELETE).
B) Incorreta. A DDL (Data Definition Language) envolve comandos que desenham a estrutura dos objetos no esquema: criação, alteração ou exclusão do modelo (CREATE, ALTER, DROP).
C) Correta. A DCL (Data Control Language) compreende justamente as instruções usadas na governança e segurança do banco de dados, ditando quem tem permissões ou retirando privilégios, como o GRANT (conceder) e o REVOKE (revogar).
D) Incorreta. A DQL (Data Query Language) consiste no comando utilizado para consultar informações (o SELECT), sem mexer na estrutura ou no conteúdo persistido.
E) Incorreta. A TCL (Transaction Control Language) engloba os comandos que finalizam, confirmam ou cancelam as transações correntes (COMMIT e ROLLBACK).
</details>

---

### Questão 7 (FCC - 2019 - TRF 3ª Região - Analista Judiciário - Informática)
O conceito de Transação em Bancos de Dados garante a execução segura e confiável das operações. A propriedade que garante que, uma vez que uma transação seja confirmada, seus efeitos permaneçam no banco de dados mesmo após falhas no sistema, é denominada:

A) Atomicidade
B) Consistência
C) Isolamento
D) Durabilidade
E) Integridade

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A) Incorreta. A Atomicidade garante que uma transação ocorra como uma unidade completa — todas as partes executam sucesso, ou a transação falha inteira (tudo ou nada), não tratando diretamente da sobrevivência pós-falha de disco após estar finalizada.
B) Incorreta. A Consistência garante que as transações operem seguindo as restrições lógicas e regras de negócio de integridade implementadas no banco, deixando a base num estado coerente.
C) Incorreta. O Isolamento refere-se ao mecanismo que previne que duas ou mais transações executadas concorrentemente interfiram umas nas outras ou gerem anomalias visuais durante sua duração.
D) Correta. A Durabilidade é a propriedade que certifica que, no instante em que o sistema relatar o término seguro de um `COMMIT`, aqueles dados estejam em repouso confiável e não se percam, sequer perante falhas súbitas de energia ou travamentos do SGBD.
E) Incorreta. Integridade é um macro-conceito aplicado dentro da propriedade da Consistência, regido pelo cumprimento das constraints e referências e não a uma sigla ACID estrita.
</details>

---

### Questão 8 (FCC - 2023 - TRE-PB - Analista Judiciário - Tecnologia da Informação)
Considere a instrução SQL: SELECT nome FROM Empregados WHERE salario BETWEEN 2000 AND 3000;
Esta consulta pode ser reescrita de forma equivalente sem o operador BETWEEN utilizando:

A) WHERE salario > 2000 OR salario < 3000
B) WHERE salario >= 2000 AND salario <= 3000
C) WHERE salario > 2000 AND salario < 3000
D) WHERE salario IN (2000, 3000)
E) WHERE salario >= 2000 OR salario <= 3000

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) Incorreta. A reescrita utilizando `>` ou `<` ignora os extremos numéricos definidos e o operador lógico `OR` permitiria a aceitação de quaisquer salários maiores que 2000 ou menores que 3000, abrangendo todos os registros existentes no mundo.
B) Correta. O operador `BETWEEN A AND B` tem caráter semântico inclusivo, significando que engloba o limite inferior até o limite superior, matematicamente traduzível para uma união restrita com maior igual (>=) para a base combinada com a restrição de menor igual (<=) para o topo via a conjunção lógia `AND`.
C) Incorreta. A sintaxe de uso está equivocada porque os limitadores estritos sem o sinal de igual excluem exatamente os valores que delimitam as fronteiras (2000 e 3000), o que não era feito pela instrução original.
D) Incorreta. A verificação feita pelo filtro `IN (...)` busca unicamente os valores absolutos digitados internamente, ou seja, recuperaria somente os que recebem exatamente 2000 cravados ou 3000 cravados.
E) Incorreta. O uso do condicional lógico `OR` faria as faixas de filtro expandirem ao invés de convergir. A expressão sempre avaliaria como verdadeira, independentemente do salário do empregado ser 1500 ou 4000.
</details>

---

### Questão 9 (FCC - 2018 - TRT 6ª Região - Analista Judiciário - Tecnologia da Informação)
O Teorema CAP é frequentemente aplicado no estudo de sistemas de bancos de dados distribuídos. Segundo este teorema, é impossível prover simultaneamente mais de duas de três garantias essenciais. Estas três garantias são:

A) Consistência, Atomicidade e Performance.
B) Consistência, Disponibilidade e Tolerância a Particionamento.
C) Confiabilidade, Acessibilidade e Performance.
D) Controle, Atomicidade e Particionamento.
E) Consistência, Assincronicidade e Paralelismo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) Incorreta. A Atomicidade e a Performance não são variáveis que entram na premissa e equacionamento direto do teorema de Brewer (Teorema CAP).
B) Correta. O Teorema CAP baseia sua premissa na impossibilidade teórica de provar que em um sistema computacional de dados distribuídos consigamos manter os três itens a seguir de forma simultânea durante eventos problemáticos: Consistency (Consistência - mesmos dados simultâneos), Availability (Disponibilidade - sistema sempre pronto para aceitar reads/writes) e Partition Tolerance (Tolerância a particionamento de rede).
C) Incorreta. Confiabilidade, acessibilidade e performance são aspectos vitais de engenharia de software, porém o acrônimo CAP dita especificamente propriedades de rede e sincronismo.
D) Incorreta. O C significa consistência em vez de controle e o A simboliza a disponibilidade, divergindo totalmente de transações atômicas de forma restrita (ACID).
E) Incorreta. O teorema enfatiza as barreiras em bancos em rede e a resiliência à ruptura dessa rede e não estritamente as tarefas assíncronas do núcleo processador.
</details>

---

### Questão 10 (FCC - 2022 - TRT 5ª Região - Analista Judiciário - Tecnologia da Informação)
No Modelo Entidade-Relacionamento, um relacionamento em que uma instância de uma entidade A pode estar associada a várias instâncias da entidade B, mas uma instância da entidade B só pode estar associada a, no máximo, uma instância da entidade A, é classificado quanto à sua cardinalidade como:

A) Um para Um (1:1)
B) Muitos para Muitos (N:N)
C) Um para Muitos (1:N)
D) Auto-relacionamento
E) Relacionamento Ternário

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. Se o relacionamento indicasse que um pode se ligar no máximo a um, e vice-versa, a representação dar-se-ia pela cardinalidade "1 para 1" (1:1).
B) Incorreta. Se na associação fosse dito que a entidade A vincula-se a diversos B e cada um dos indivíduos da entidade B pudessem se ligar de volta a múltiplas entidades de A, seria "Muitos para Muitos" (N:N).
C) Correta. A questão demonstra uma relação clássica da modelagem: A pode chegar a várias instâncias de B (o lado "N"), porém se você olha a partir da perspectiva de uma instância na entidade B, ela enxerga no máximo uma em A (o lado "1"). Daí configura-se a proporção "Um para Muitos" (1:N).
D) Incorreta. Auto-relacionamento ou relacionamento unário acontece quando os elos ocorrem entre dados ou registros de uma mesma e única entidade interna.
E) Incorreta. O modelo citado conta com a interação envolvendo meramente duas pontas ou entidades distintas, não sendo cabível a indicação matemática que liga de forma simultânea três atores semânticos no grafo.
</details>

---

### Questão 11 (FCC - 2017 - TST - Analista Judiciário - Tecnologia da Informação)
No SQL, a restrição que garante referencial cruzado válido entre duas tabelas, exigindo que os valores em uma coluna existam em uma coluna correspondente de outra tabela, é denominada:

A) PRIMARY KEY
B) UNIQUE
C) FOREIGN KEY
D) CHECK
E) NOT NULL

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. A propriedade `PRIMARY KEY` apenas certifica que não ocorra repetição de dados em uma tabela em si e impede dados nulos, garantindo identificação única para suas tuplas e instâncias. Não trata de referências inter-tabelas.
B) Incorreta. A chave `UNIQUE` certifica que uma determinada coluna preenchida não poderá deter um dado repetido em suas linhas, sem impor relação de consistência com outra tabela.
C) Correta. A constraint `FOREIGN KEY` (Chave Estrangeira) tem por missão implementar e manter a integridade referencial. Ela amarra e restringe o conjunto de dados da coluna filha aceitando apenas valores que genuinamente existam lá na coluna que fora apontada como destino principal.
D) Incorreta. A regra imposta pelo `CHECK` consiste em barrar a entrada de dados nas tuplas que não satisfaçam uma expressão de domínio genérica ou booleana (como não aceitar idades inferiores a 18 anos).
E) Incorreta. O limitador `NOT NULL` atesta singularmente que em nenhum momento aquela coluna, mesmo sem dependências, poderá omitir uma informação se transformando em vazia.
</details>

---

### Questão 12 (FCC - 2019 - TRF 4ª Região - Analista Judiciário - Tecnologia da Informação)
No MongoDB, para realizar uma consulta (query) e encontrar os documentos onde o valor do campo "idade" seja maior ou igual a 18, utiliza-se a seguinte sintaxe do operador de comparação:

A) db.usuarios.find({idade: { $gt: 18 }})
B) db.usuarios.find({idade: { >= : 18 }})
C) db.usuarios.find({idade: { $gte: 18 }})
D) db.usuarios.find({idade: { $ge: 18 }})
E) db.usuarios.find({idade: { $eq: 18 }})

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. O comando `$gt` serve apenas para ditar estritamente a relação de "maior do que" (Greater Than), o que faria as buscas excluírem os usuários contendo exatos 18.
B) Incorreta. Ao contrário dos sistemas de SQL Tradicionais, o uso de símbolos matemáticos puros na forma de operadores `>` ou `>=` não é parte da sintaxe interpretada validamente pelo Mongo.
C) Correta. Para compilar a lógica semântica solicitada, as requisições em BSON/JSON nos sistemas do MongoDB utilizam operadores que iniciam com o caractere do cifrão (`$`). Para significar de maneira abreviada o termo "Greater Than or Equal", traduzido para Maior Ou Igual, utiliza-se a junção abreviada e o acrônimo oficial `$gte`.
D) Incorreta. A grafia `$ge` destoa do padrão implementado e aceito na linguagem de filtragem. Falta o T do "Than".
E) Incorreta. A inserção do parâmetro condicional `$eq` faria a filtragem achar restrita e cirurgicamente aqueles dados que possuam exatos 18 (Equal), deixando de fora qualquer idade superior.
</details>

---

### Questão 13 (FCC - 2016 - TRT 20ª Região - Analista Judiciário - Tecnologia da Informação)
Para otimizar consultas em banco de dados relacionais, criam-se índices. Um índice cujas entradas ditam a ordem física (armazenamento) dos registros na tabela é conhecido como:

A) Índice Denso
B) Índice Hash
C) Índice Secundário
D) Índice Clusterizado (Clustered)
E) Índice Espacial

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A) Incorreta. O Índice Denso indica uma estrutura que mapeia entradas para todos os registros que ocorrem nos dados; ele, per si, não manipula o endereçamento físico base do disco (apesar de comumente ser feito usando outro índice por trás).
B) Incorreta. Um Índice Hash emprega função de dispersão em baldes e slots para resolver as consultas exatas, não armazenando ordenamento crescente, decrescente ou linear.
C) Incorreta. O Índice Secundário dita uma rota alternativa lógica que não interage nem espelha a sequência física em que a base persistiu o arranjo original contíguo das tuplas.
D) Correta. Conhecido também como Índice Agrupado (Clustered Index), os dados subjacentes da própria tabela são forçados e organizados na sequência exata ditada pela chave desse índice no momento em que é armazenado na mídia física. Portanto, só poderá haver um deste por tabela.
E) Incorreta. Índices espaciais provêm meios de gerir geometrias ou dados baseados em coordenadas geográficas multidimensionais, não cabendo para ordenação univalorada convencional no cluster físico.
</details>

---

### Questão 14 (FCC - 2018 - TRT 2ª Região - Analista Judiciário - Tecnologia da Informação)
Qual comando DML (Data Manipulation Language) do SQL é responsável por remover um ou mais registros de uma tabela existente?

A) DROP
B) TRUNCATE
C) DELETE
D) REMOVE
E) ALTER

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. O `DROP` não age removendo registros isoladamente. Ele apaga objetos de forma total, incluindo a própria estrutura e definição e seu comando enquadra-se na classificação de linguagem DDL.
B) Incorreta. O comando `TRUNCATE` destrói massivamente todos os valores em todos os registros zerando as marcações sem possuir sintaxe voltada a seleção individual com `WHERE`. Além disso, usualmente é alocado como instrução DDL, pois não gera histórico em logs DML na teoria relacional.
C) Correta. Dentro das rotinas de alteração de dados propriamente (DML), o comando específico providenciado que conta também com o suporte opcional do filtro `WHERE` para restringir registros e apagá-los pontualmente ou integralmente sem afetar a estrutura, chama-se `DELETE`.
D) Incorreta. A diretiva `REMOVE` não se faz valer como um comando oficial para o ANSI SQL voltado e desenhado para limpeza e expurgo em entidades.
E) Incorreta. Como integrante de classificação da classe DDL, a função da palavra chave `ALTER` baseia-se unicamente em atualizar, somar ou abater características morfológicas, tamanhos e os metadados dos contêineres e colunas.
</details>

---

### Questão 15 (FCC - 2021 - DPE-RR - Analista de Sistemas)
O fenômeno em bancos de dados que ocorre quando uma transação T1 lê um dado que foi modificado por uma transação T2 que ainda não efetuou o commit, e T2 acaba sendo abortada (rollback), fazendo com que T1 tenha lido um dado que "nunca existiu" oficialmente no banco, é chamado de:

A) Leitura Fantasma (Phantom Read)
B) Leitura Suja (Dirty Read)
C) Leitura Não Repetível (Non-Repeatable Read)
D) Atualização Perdida (Lost Update)
E) Deadlock

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) Incorreta. A leitura fantasma relata um quadro de transação onde num cenário de repetidas buscas amplas (geralmente por range), um item novo aparece ou some após outra ação ter provocado uma inserção/exclusão comitada que afetou aquele grupo.
B) Correta. A falha descrita trata-se diretamente da anomalia de "Dirty Read" ou leitura suja. Ela se manifesta devido a isolamentos baixos demais (como o Read Uncommitted) liberarem acesso e visibilidade em itens que estão em estado temporário não comprometidos pela transação modificadora.
C) Incorreta. A leitura não repetível decorre das situações onde o componente A executa leitura num registro e obtém X; a transação componente B valida um UPDATE sobre esse valor fazendo virar Y (e faz commit); e A, ao refazer a mesma leitura, recebe valores desiguais em queries onde os dados não deveriam flutuar.
D) Incorreta. O cenário que retrata atualizações perdidas demonstra múltiplas sobreposições cegas, onde dois saves sobrescrevem inadvertidamente edições concorrentes de escritas validadas, o que remete ao controle transacional de update, não sendo anomalia de leitura suja.
E) Incorreta. Deadlock ilustra um impasse em estado fatal entre instâncias competindo, uma exigindo o lock travado por outra enquanto os recursos tornam os pares reciprocamente inacessíveis, parando e bloqueando a continuação.
</details>

---


## 📝 TEMA 2: SO Linux (Red Hat/Oracle)

### Questão 1 (FCC - 2018 - TRT 2 - Analista de TI)
No sistema operacional Linux (distribuição Red Hat ou CentOS), o comando utilizado para exibir informações detalhadas sobre a memória RAM, como total, usada e livre, em megabytes, é:
A) free -m
B) meminfo -m
C) df -m
D) top -m
E) ps -m

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- **A) free -m**: Correta. O comando `free` é utilizado para exibir a quantidade de memória RAM livre, usada, além dos buffers, cache e swap no sistema. A flag `-m` especifica que a exibição deve ser no formato de megabytes.
- **B) meminfo -m**: Incorreta. Não existe um comando executável padrão chamado `meminfo`. As informações detalhadas da memória são gerenciadas pelo kernel e armazenadas no arquivo virtual `/proc/meminfo`.
- **C) df -m**: Incorreta. O utilitário `df` (disk free) exibe o espaço livre e ocupado no sistema de arquivos das partições de disco rígido, e não informa a utilização da memória RAM.
- **D) top -m**: Incorreta. O comando `top` exibe os processos em execução e recursos do sistema dinamicamente, mas a sintaxe `-m` para simplesmente exibir memória não é válida.
- **E) ps -m**: Incorreta. O comando `ps` lista os processos no sistema de forma estática (snapshot). A opção `m` exibe as threads do processo e não sumariza a memória do SO.
</details>

---

### Questão 2 (FCC - 2017 - TST - Analista Judiciário - Suporte em TI)
Considere um sistema operacional Linux. O arquivo de configuração onde as partições são listadas para serem montadas automaticamente durante a inicialização do sistema é o:
A) /etc/mtab
B) /etc/fstab
C) /etc/inittab
D) /etc/partitions
E) /etc/mounts

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **A) /etc/mtab**: Incorreta. O arquivo `mtab` (Mounted Table) mantém uma lista dinâmica dos sistemas de arquivos que já estão *atualmente* montados no sistema. Ele é atualizado pela execução dos comandos mount e umount.
- **B) /etc/fstab**: Correta. O arquivo `fstab` (File System Table) é um arquivo de configuração estática lido no momento do boot. Ele dita os pontos de montagem, UUIDs ou labels das partições, formato do sistema de arquivos e como eles devem ser montados automaticamente pelo SO.
- **C) /etc/inittab**: Incorreta. Historicamente usado no processo `SysVinit` para configurar os níveis de execução (runlevels) e a inicialização de scripts de boot. Não é o arquivo para montar partições.
- **D) /etc/partitions**: Incorreta. Este arquivo não existe. O equivalente virtual reconhecido diretamente pelo kernel para listar partições em disco é `/proc/partitions`.
- **E) /etc/mounts**: Incorreta. Esse arquivo com este nome no diretório `/etc` não existe. O Linux mantém as montagens detectadas pelo kernel no arquivo `/proc/mounts`.
</details>

---

### Questão 3 (FCC - 2016 - TRT 23 - Analista Judiciário - Tecnologia da Informação)
No Linux (Red Hat/CentOS/Oracle Linux), o gerenciador de pacotes YUM é amplamente utilizado. O comando correto para atualizar todos os pacotes instalados no sistema para suas versões mais recentes, mantendo as configurações padrão, é:
A) yum upgrade-all
B) yum update all
C) yum update
D) yum install updates
E) yum refresh

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **A) yum upgrade-all**: Incorreta. Este não é um comando válido reconhecido pelo YUM para atualização. 
- **B) yum update all**: Incorreta. A sintaxe é inválida, pois a palavra "all" ao fim informaria falsamente ao YUM para procurar um pacote específico chamado "all", o que gera erro.
- **C) yum update**: Correta. O comando solitário `yum update` pesquisa nos repositórios, resolve as dependências e atualiza simultaneamente *todos* os pacotes atualmente instalados que tenham atualizações disponíveis.
- **D) yum install updates**: Incorreta. O comando `yum install` tenta instalar pacotes novos que não estão no sistema. Colocar "updates" fará com que o utilitário procure erroneamente por um pacote literal chamado "updates".
- **E) yum refresh**: Incorreta. Ao contrário de gerenciadores como zypper (`zypper refresh`) ou apt (`apt update`), no YUM não existe a flag direta "refresh" para atualização de pacotes (existe apenas `yum makecache` para os metadados).
</details>

---

### Questão 4 (FCC - 2015 - TRT 3 - Analista Judiciário - Tecnologia da Informação)
No sistema operacional Linux, o comando utilizado para alterar a senha de um usuário existente é:
A) pwd
B) chpasswd
C) passwd
D) usermod -p
E) change

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **A) pwd**: Incorreta. A sigla significa Print Working Directory e é usada para exibir o caminho completo do diretório atual onde o usuário se encontra.
- **B) chpasswd**: Incorreta. Embora permita a alteração de senhas, não é utilizado no uso interativo dia a dia, pois este utilitário lê blocos de formato "usuario:senha" de uma entrada padrão para aplicar trocas de senha em lote (larga escala).
- **C) passwd**: Correta. O `passwd` é o comando principal interativo utilizado para que o usuário altere a própria senha ou que o root altere a de qualquer outro usuário.
- **D) usermod -p**: Incorreta. O `usermod -p` recebe a senha *já criptografada*, não em texto puro. O uso interativo padrão deve ser feito pelo `passwd`.
- **E) change**: Incorreta. Este comando sequer existe por padrão no Linux. Há o `chage`, que é usado para gerenciar informações de expiração e validade da senha de um usuário, não para alterar a senha propriamente dita.
</details>

---

### Questão 5 (FCC - 2014 - TRT 19 - Analista Judiciário - Tecnologia da Informação)
No sistema operacional Linux, o comando capaz de exibir as linhas finais de um arquivo texto e que possui um parâmetro para manter o arquivo aberto monitorando novas linhas inseridas em tempo real é:
A) head
B) tail
C) cat
D) more
E) less

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **A) head**: Incorreta. Usado para exibir as primeiras linhas de um arquivo (por padrão, as 10 iniciais).
- **B) tail**: Correta. O comando `tail` exibe o final de um arquivo. Ao utilizarmos o parâmetro `-f` (`tail -f arquivo`), ele mantém o arquivo aberto (follow) e joga na saída padrão qualquer nova linha inserida dinamicamente. Muito usado em monitoramento de logs.
- **C) cat**: Incorreta. O `cat` (concatenate) simplesmente joga todo o conteúdo do arquivo na tela de uma só vez, encerrando o processo imediatamente após a leitura.
- **D) more**: Incorreta. É um paginador clássico e estático para rolar a tela, não servindo para monitorar a injeção contínua de linhas num arquivo em crescimento.
- **E) less**: Incorreta. Paginador interativo e avançado. Embora ofereça um comando (Shift+F) semelhante ao `tail -f`, a questão descreve com exatidão o utilitário nativo e focado nisso, que é o `tail`.
</details>

---

### Questão 6 (FCC - 2018 - TRT 6 - Analista Judiciário - Suporte em TI)
Em uma distribuição baseada em Red Hat Enterprise Linux, como o Oracle Linux, o sistema de inicialização e gerenciamento de serviços padrão nas versões mais recentes (ex: versão 7 e 8) é o:
A) SysV init
B) Upstart
C) systemd
D) initrc
E) xinetd

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **A) SysV init**: Incorreta. Este era o sistema clássico de inicialização adotado no RHEL/CentOS 5 e 6, baseado em scripts sequenciais no `/etc/rc.d/`. Foi obsoleto por ser mais lento e rígido.
- **B) Upstart**: Incorreta. Desenvolvido para lidar com eventos, foi mais popular no Ubuntu e usado brevemente em conjunto no RHEL 6, mas abandonado a favor do systemd no ecossistema Red Hat.
- **C) systemd**: Correta. A partir das versões RHEL 7, Oracle Linux 7, CentOS 7, o `systemd` tornou-se o padrão. Seu grande trunfo é a paralelização na inicialização de daemons, controle robusto via cgroups e comandos geridos pelo `systemctl`.
- **D) initrc**: Incorreta. `rc` refere-se tradicionalmente a "run commands", nomes de arquivos ou diretórios que controlavam o boot em ambientes SysV, e não um sistema principal próprio.
- **E) xinetd**: Incorreta. Trata-se de um "super-daemon" de serviços de rede antigos (como telnet ou ftp) que ativava serviços sob demanda quando recebiam conexões de porta, não controlando o boot geral do SO.
</details>

---

### Questão 7 (FCC - 2017 - TRF 5 - Analista Judiciário - Informática)
No Linux, para conceder permissão de leitura, gravação e execução para o dono do arquivo, leitura e execução para o grupo, e apenas execução para os outros usuários do arquivo `script.sh`, utiliza-se o comando:
A) chmod 751 script.sh
B) chmod 761 script.sh
C) chmod 771 script.sh
D) chmod 754 script.sh
E) chmod 777 script.sh

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- **A) chmod 751 script.sh**: Correta. Em formato octal, o cálculo ocorre por: Leitura (r=4), Gravação (w=2), Execução (x=1). 
   - Dono: leitura (4) + gravação (2) + execução (1) = 7.
   - Grupo: leitura (4) + execução (1) = 5.
   - Outros: execução (1) = 1. Resultado = 751.
- **B) chmod 761 script.sh**: Incorreta. O valor numérico 6 para o grupo significa (4 + 2) Leitura e Gravação, sendo que o enunciado pede Leitura e Execução.
- **C) chmod 771 script.sh**: Incorreta. O 7 no grupo permitiria gravação completa aos membros do grupo, o que difere da necessidade da questão.
- **D) chmod 754 script.sh**: Incorreta. O 4 para "outros" significa apenas permissão de Leitura, e a questão exige apenas Execução (que seria 1).
- **E) chmod 777 script.sh**: Incorreta. Permissão máxima, liberando Leitura, Gravação e Execução de modo irrestrito para todas as classes de usuários.
</details>

---

### Questão 8 (FCC - 2014 - TRF 4 - Analista Judiciário - Suporte em TI)
No SO Linux, para compactar e descompactar arquivos, além de agrupar vários arquivos em um único, são utilizados, respectivamente, os utilitários de compressão e arquivamento. O comando `tar` com as opções corretas para extrair o conteúdo de um arquivo agrupado e compactado com `gzip` (ex: arquivo.tar.gz) é:
A) tar -cvf arquivo.tar.gz
B) tar -xvf arquivo.tar.gz
C) tar -zxvf arquivo.tar.gz
D) tar -jxvf arquivo.tar.gz
E) tar -cxvf arquivo.tar.gz

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **A) tar -cvf**: Incorreta. Os parâmetros significam: `-c` (create / criar), `-v` (verbose / modo detalhado) e `-f` (file). Juntos criam um arquivo não compactado, não servem para extrair.
- **B) tar -xvf**: Incorreta para o contexto ideal, apesar de versões modernas do GNU tar conseguirem autodetectar a compressão sem a flag explícita, a banca historicamente cobra a notação clássica com o algoritmo discriminado. Sem o descompactador definido explicitamente, esta não é a resposta mais adequada em questões de concurso perante a letra C.
- **C) tar -zxvf**: Correta. As flags são: `-z` (usa o descompressor gzip), `-x` (extract / extrair o conteúdo), `-v` (verbose / ver arquivos na tela) e `-f` (direciona o arquivo). Essa é a junção perfeita para um arquivo `.tar.gz`.
- **D) tar -jxvf**: Incorreta. A opção `-j` é destinada a trabalhar com a compressão através do algoritmo `bzip2` (arquivos `.tar.bz2`), diferente da estrutura gzip especificada na questão.
- **E) tar -cxvf**: Incorreta. Há total incompatibilidade, uma vez que as flags `-c` (criar) e `-x` (extrair) entram em conflito quando utilizadas ao mesmo tempo num processo do tar.
</details>

---

### Questão 9 (FCC - 2016 - TRE PB - Analista Judiciário - Tecnologia da Informação)
Em um sistema Linux, para listar os processos em execução e verificar o consumo de CPU e Memória em tempo real, um Analista deve utilizar o comando:
A) ps aux
B) top
C) vmstat
D) iostat
E) netstat

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **A) ps aux**: Incorreta. Embora exiba o consumo de CPU, Memória e os processos, sua abordagem fornece apenas um instantâneo (snapshot) no exato segundo em que é executado. Ele não acompanha as mudanças de consumo *em tempo real*.
- **B) top**: Correta. O utilitário `top` atualiza periodicamente a tela, mantendo uma visão contínua, orgânica e em tempo real dos processos ativos do sistema e quantificando o estado do hardware (CPU e RAM).
- **C) vmstat**: Incorreta. Informa relatórios resumidos e intermitentes da memória virtual (Virtual Memory Statistics), paginação e threads de CPU, mas não exibe e nem gerencia processos individuais de forma visual.
- **D) iostat**: Incorreta. Ferramenta voltada principalmente para a amostragem de Input/Output (leitura e escrita nos discos) e estatísticas de carga da CPU; ele não elenca os processos do sistema operacional.
- **E) netstat**: Incorreta. Comando antigo de gerenciamento e mapeamento das conexões de rede ativas (Network Statistics), portas de escuta e interfaces, não sendo pertinente ao monitoramento global da CPU e consumo por processos.
</details>

---

### Questão 10 (FCC - 2013 - TRT 1 - Analista Judiciário - Tecnologia da Informação)
O comando do Linux que permite pesquisar palavras ou padrões dentro de arquivos de texto é o:
A) find
B) awk
C) grep
D) sed
E) locate

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **A) find**: Incorreta. Comando destinado a localizar arquivos na hierarquia do sistema de arquivos baseado nos metadados (nome, tamanho, data de modificação, inode). Não se destina intrinsecamente a extrair textos do conteúdo.
- **B) awk**: Incorreta. É uma poderosa linguagem de script focada em manipulação estruturada de colunas, formatação de saída e cálculo em textos, excedendo o simples objetivo de pesquisar uma palavra isolada em um arquivo.
- **C) grep**: Correta. O `grep` (Global Regular Expression Print) varre os arquivos de texto e imprime no terminal as linhas que coincidam (façam "match") com um termo de pesquisa ou padrão de expressão regular.
- **D) sed**: Incorreta. O `sed` (Stream Editor) é usado majoritariamente para encontrar e *substituir* ou realizar modificações automáticas no texto ao longo de um fluxo, e não para pesquisa padrão de strings para exibição local pura (embora tecnicamente possa).
- **E) locate**: Incorreta. Localiza caminhos e arquivos no sistema muito velozmente consultando uma base de dados previamente indexada (updatedb), mas não investiga o conteúdo escrito *dentro* do arquivo em si.
</details>

---

### Questão 11 (FCC - 2015 - TRE RS - Analista Judiciário - Apoio Especializado)
No gerenciamento de volumes lógicos (LVM) em sistemas Oracle Linux / Red Hat, o comando utilizado para criar um Grupo de Volumes (Volume Group) a partir de Volumes Físicos (Physical Volumes) é o:
A) pvcreate
B) vgcreate
C) lvcreate
D) vgextend
E) mkfs.vg

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **A) pvcreate**: Incorreta. Este comando formata e reconhece previamente as partições ou os discos brutos no sistema do LVM para que passem a ser considerados Physical Volumes (PV). Ele é o passo anterior na esteira de criação.
- **B) vgcreate**: Correta. Este é o comando chave que agrupa múltiplos Physical Volumes (PVs) para montar um repositório conjunto de blocos unificado, o "Volume Group" (VG).
- **C) lvcreate**: Incorreta. Este é o último passo da abstração do LVM: pegar o espaço livre consolidado no Volume Group e convertê-lo em fatias prontas, que se tornam os Logical Volumes (LVs).
- **D) vgextend**: Incorreta. Comando usado para a manutenção rotineira (extensão). É feito para acrescentar novos discos físicos a um Volume Group que já tenha sido criado no passado.
- **E) mkfs.vg**: Incorreta. Este comando não é válido no pacote LVM. Utilitários iniciados por `mkfs.` formatam volumes com sistemas de arquivos convencionais (como ext4 e xfs), não operando na abstração estrutural do Volume Group.
</details>

---

### Questão 12 (FCC - 2012 - TST - Analista Judiciário - Suporte em TI)
Para alterar o dono (owner) e o grupo de um arquivo chamado `dados.txt` para o usuário `joao` e o grupo `admin` no Linux, utiliza-se o comando:
A) chown joao.admin dados.txt
B) chown joao:admin dados.txt
C) chmod joao:admin dados.txt
D) chgrp joao:admin dados.txt
E) usermod -g admin -u joao dados.txt

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **A) chown joao.admin dados.txt**: Incorreta. Em versões antigas do UNIX utilizava-se o caractere `.` para separar o usuário e o grupo. Com a adoção de usuários com ponto no nome (ex: nome.sobrenome), o padrão oficial em POSIX Linux passou a ser obrigatoriamente os dois-pontos.
- **B) chown joao:admin dados.txt**: Correta. O comando `chown` (change owner) utiliza a sintaxe recomendada `usuario:grupo` para alterar eficientemente ambas as propriedades de uma só vez para o alvo selecionado.
- **C) chmod joao:admin dados.txt**: Incorreta. O `chmod` apenas permite mudar o mapeamento das matrizes de permissão de leitura, gravação e execução (rwx), mas não transfere a posse e a titularidade dos arquivos.
- **D) chgrp joao:admin dados.txt**: Incorreta. O comando `chgrp` altera unicamente o grupo, não processando também nomes de usuários de posse. A sintaxe apresentada falharia se rodada no chgrp.
- **E) usermod -g admin -u joao dados.txt**: Incorreta. O utilitário `usermod` modifica as diretrizes de gerenciamento central do próprio usuário (ex: pasta /home, login shell, grupo base em `/etc/passwd`). Ele interage com o sistema de identidades da máquina e não interage com permissões em arquivos aleatórios no sistema.
</details>

---

### Questão 13 (FCC - 2014 - TRT 13 - Analista Judiciário - Tecnologia da Informação)
Para exibir o espaço livre e ocupado das partições montadas no sistema de arquivos de um sistema Linux, em um formato legível por humanos (como MB, GB), utiliza-se o comando:
A) df -h
B) du -h
C) fdisk -l
D) mount -l
E) lsblk -h

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- **A) df -h**: Correta. O `df` (disk free) inspeciona e exibe a totalidade de blocos consumidos e o espaço disponível nas partições montadas do sistema de arquivos. A flag `-h` (human-readable) imprime as estatísticas em bytes arredondados com notações fáceis (KB, MB, GB).
- **B) du -h**: Incorreta. O `du` (disk usage) faz recursão interna numa árvore de diretórios apontados e soma o peso final (em bytes) dos arquivos alocados nele, ao invés de listar todo o estado de armazenamento livre da partição montada.
- **C) fdisk -l**: Incorreta. O `fdisk` lista a tabela bruta de blocos, cilindros, setores de partições lógicas e seus tamanhos físicos de formatação, sem reportar quanto de dados já preencheu a formatação localmente.
- **D) mount -l**: Incorreta. Mostra no terminal quais dispositivos virtuais ou hardware estão montados nos respectivos diretórios do Linux, informando opções de mount (rw, ro, sync), sem reportar capacidade de disco livre em bytes.
- **E) lsblk -h**: Incorreta. Embora o `lsblk` mostre a árvore de blocos no disco, no utilitário lsblk o parâmetro `-h` geralmente representa help, invocando o manual. Os bytes e tamanhos das partições são mostrados sem o `-h`.
</details>

---

### Questão 14 (FCC - 2017 - TRT 24 - Analista Judiciário - Tecnologia da Informação)
Em um servidor Linux (como o Red Hat Enterprise), qual comando clássico é utilizado para configurar temporariamente um endereço IP `192.168.1.10` na interface de rede `eth0`?
A) ipconfig eth0 192.168.1.10
B) ifconfig eth0 192.168.1.10
C) netstat -i eth0 192.168.1.10
D) ifup eth0 192.168.1.10
E) route add eth0 192.168.1.10

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **A) ipconfig eth0 192.168.1.10**: Incorreta. A ferramenta `ipconfig` é de domínio exclusivo das plataformas e sistemas operacionais da Microsoft Windows (no terminal DOS).
- **B) ifconfig eth0 192.168.1.10**: Correta. Ferramenta consolidada oriunda do pacote `net-tools`, cuja sintaxe vincula de imediato um endereço IP para a interface `eth0`. A ressalva é que essa via não mantém o IP salvo permanentemente nos próximos reboots.
- **C) netstat -i eth0 192.168.1.10**: Incorreta. `netstat -i` tem viés observador, mostrando contagens de pacotes e tráfego estatístico por placas de rede sem permitir input de novos IPs.
- **D) ifup eth0 192.168.1.10**: Incorreta. O comando `ifup eth0` invoca o link em subida (UP) baseando-se no preenchimento de IP contido unicamente no arquivo `/etc/sysconfig/network-scripts/ifcfg-eth0`, ignorando entradas arbitrárias digitadas em sua frente.
- **E) route add eth0 192.168.1.10**: Incorreta. O comando route serve estritamente para adicionar roteamento e estabelecer o gateway para o tráfego chegar ao mundo exterior; não injeta IPs diretos para uso primário na interface de rede da máquina.
</details>

---

### Questão 15 (FCC - 2018 - TRT 15 - Analista Judiciário - Infraestrutura de TI)
No Red Hat Enterprise Linux 7 ou Oracle Linux 7, para iniciar um serviço (por exemplo, `httpd`) e configurá-lo para que inicie automaticamente durante o boot (inicialização) do sistema operacional, os comandos do `systemctl` que devem ser utilizados são, respectivamente:
A) systemctl start httpd e systemctl on httpd
B) systemctl run httpd e systemctl boot httpd
C) systemctl start httpd e systemctl enable httpd
D) systemctl up httpd e systemctl chkconfig httpd
E) systemctl init httpd e systemctl auto httpd

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **A) systemctl start httpd e systemctl on httpd**: Incorreta. A sintaxe "on" operava no utilitário anterior chkconfig (ex: `chkconfig httpd on`), não sendo uma ação reconhecida nativamente pelo interpretador `systemctl`.
- **B) systemctl run httpd e systemctl boot httpd**: Incorreta. Não existe sintaxe `run` para ligar unidades ou comandos de gerência chamados `boot` num servidor Linux com systemd.
- **C) systemctl start httpd e systemctl enable httpd**: Correta. O primeiro comando (`start`) lança e carrega imediatamente o processo do servidor web no runtime atual. O segundo (`enable`) constrói os links simbólicos para alocar o serviço nos "targets" de ativação, garantindo sua volta no boot.
- **D) systemctl up httpd e systemctl chkconfig httpd**: Incorreta. "Up" é uma expressão de serviço inexistente no systemd e "chkconfig" é um software descontinuado por ele (SysVinit).
- **E) systemctl init httpd e systemctl auto httpd**: Incorreta. Nenhuma das diretivas de operação "init" (fazer setup) e "auto" pertencem às tabelas de sintaxe oficial para ativação de persistência no boot.
</details>

---


## 📝 TEMA 3: Previdência CE

### Questão 1 (FCC - 2021 - SEFAZ-CE - Auditor Fiscal)
Sobre o Regime Próprio de Previdência Social (RPPS) dos servidores do Estado do Ceará, assinale a opção correta à luz do texto constitucional e das recentes reformas previdenciárias.
A) O servidor público estadual será aposentado compulsoriamente aos setenta e cinco anos de idade, com proventos integrais, independentemente do tempo de contribuição.
B) É garantido o direito à aposentadoria por incapacidade permanente para o trabalho, sendo os proventos sempre calculados de forma proporcional ao tempo de contribuição, sem qualquer exceção de integralidade.
C) É vedada a percepção de mais de uma aposentadoria à conta do regime próprio de previdência social, ressalvadas as aposentadorias decorrentes dos cargos acumuláveis na forma da Constituição Federal.
D) O tempo de contribuição nos regimes geral e próprio será contado reciprocamente para fins de aposentadoria, dispensando-se a compensação financeira caso não haja impacto atuarial imediato.
E) Os proventos de aposentadoria e as pensões por morte poderão ser pagos em valor inferior ao salário mínimo nacional, caso o segurado tenha se aposentado proporcionalmente.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Análise das Alternativas:**
- **A) Incorreta.** A aposentadoria compulsória ocorre aos 70 anos de idade, ou aos 75 anos na forma de lei complementar, mas sempre com proventos **proporcionais** ao tempo de contribuição, conforme o art. 40, § 1º, II, da CF. A integralidade não se aplica a este caso.
- **B) Incorreta.** Há exceção. A regra atual estipula que a aposentadoria por incapacidade permanente terá proventos proporcionais, contudo, o cálculo corresponderá a 100% da média (assemelhando-se à "integralidade" do valor base) quando a incapacidade decorrer de **acidente de trabalho, de doença profissional ou de doença do trabalho** (art. 40, § 1º, I, CF c/c regras de cálculo da EC 103/19 e legislação estadual correlata).
- **C) Correta.** Trata-se da exata dicção do art. 40, § 6º, da Constituição Federal. A acumulação de benefícios de aposentadoria no âmbito do RPPS é proibida, exceto para os cargos acumuláveis (ex: dois cargos de professor; um de professor com outro técnico/científico; dois de profissionais da saúde).
- **D) Incorreta.** A contagem recíproca do tempo de contribuição (entre RGPS e RPPS ou entre RPPS de entes diferentes) exige **obrigatoriamente** a respectiva compensação financeira, não havendo hipótese de dispensa atuarial (art. 201, § 9º, CF).
- **E) Incorreta.** Os benefícios de aposentadoria e pensão (o valor global, não necessariamente a cota-parte, mas o benefício em si) concedidos pelo regime próprio **não poderão ser inferiores ao valor mínimo** a que se refere o art. 201, § 2º (salário mínimo), por expressa disposição constitucional (art. 40, § 7º, CF).

</details>

---

### Questão 2 (FCC - 2019 - TRF 4 - Analista Judiciário - Área Administrativa)
No que diz respeito à Previdência Complementar no âmbito do Estado do Ceará, instituída nos moldes da Constituição Federal e legislação estadual respectiva, é correto afirmar que:
A) a adesão ao Regime de Previdência Complementar (RPC) é obrigatória para todos os novos servidores estaduais, independentemente de sua remuneração superar o teto do INSS.
B) o Estado patrocinará o plano de benefícios com uma contribuição superior à do servidor, para garantir a viabilidade financeira do fundo estadual.
C) a adesão é facultativa ao servidor, e a contribuição patronal (do Estado) será paritária à do servidor, não podendo exceder o percentual estabelecido sobre a parcela que ultrapassar o teto do RGPS.
D) somente os servidores ocupantes exclusivamente de cargos em comissão podem aderir à previdência complementar estadual, uma vez que são regidos pelo RGPS.
E) a administração dos recursos da previdência complementar estadual é de competência exclusiva de instituições financeiras privadas, não se permitindo a criação de fundação pública de direito privado.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Análise das Alternativas:**
- **A) Incorreta.** A adesão à previdência complementar é **facultativa**. O servidor pode optar por não contribuir, mas seus proventos pelo RPPS ficarão limitados ao teto do RGPS. Em alguns entes existe a adesão automática (mas com o direito de desistência em prazo legal), porém nunca é obrigatória sem direito à desvinculação.
- **B) Incorreta.** A contribuição do Estado (patrocinador) deve ser, no máximo, **paritária** à contribuição do segurado (art. 40, § 15, CF). O Estado não pode contribuir com valor superior ao do servidor.
- **C) Correta.** É o desenho clássico do RPC. A adesão definitiva ao fundo é facultativa. Se o servidor ganha acima do teto do RGPS e decide aderir para ter benefício suplementar, a contribuição do patrocinador incidirá sobre o que passar do teto e será igual (paritária) à do servidor.
- **D) Incorreta.** Servidores exclusivamente em comissão não estão amparados pelo RPPS, mas pelo RGPS. O regime de previdência complementar do Ente destina-se aos servidores titulares de cargo efetivo.
- **E) Incorreta.** Os regimes de previdência complementar dos entes federativos podem ser administrados por entidade fechada de previdência complementar de natureza pública (fundação pública de direito privado) ou através de entidade aberta ou fechada privada devidamente selecionada por licitação (art. 40, § 15).

</details>

---

### Questão 3 (FCC - 2021 - SEFAZ-CE - Auditor Fiscal)
O servidor público efetivo do Estado do Ceará que tenha completado todos os requisitos exigidos para a aposentadoria voluntária e que opte por permanecer em atividade no cargo público:
A) fará jus a um abono de permanência equivalente ao dobro do valor da sua contribuição previdenciária.
B) ficará isento da incidência de imposto de renda retido na fonte sobre a totalidade de sua remuneração, como forma de incentivo.
C) fará jus a um abono de permanência equivalente, no máximo, ao valor da sua contribuição previdenciária, até completar a idade para aposentadoria compulsória.
D) deverá requerer obrigatoriamente a suspensão de seu desconto previdenciário, pois o abono não possui caráter remuneratório, mas sim indenizatório.
E) terá o seu tempo de contribuição averbado em dobro a partir da aquisição do direito, para fins de recálculo dos proventos futuros.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Análise das Alternativas:**
- **A) Incorreta.** O abono de permanência corresponde a, no máximo, o valor da própria contribuição previdenciária do servidor (100% da contribuição), e não ao dobro. Na prática, ele neutraliza o desconto previdenciário.
- **B) Incorreta.** O abono de permanência não confere isenção de imposto de renda sobre a remuneração do servidor. Ademais, o STJ pacificou entendimento de que incide imposto de renda sobre o abono de permanência.
- **C) Correta.** Segundo o art. 40, § 19, da CF, o servidor que tenha completado os requisitos para aposentadoria voluntária e opte por permanecer em atividade fará jus a um abono de permanência equivalente, no máximo, ao valor da sua contribuição previdenciária, até que atinja a idade para a aposentadoria compulsória.
- **D) Incorreta.** O desconto da contribuição previdenciária continua ocorrendo no contracheque. O que ocorre é que o servidor recebe uma rubrica adicional (o abono) no mesmo valor, neutralizando o efeito financeiro. O desconto previdenciário não é "suspenso".
- **E) Incorreta.** A Constituição Federal veda expressamente a contagem de tempo de contribuição fictício (art. 40, § 10). Não há hipótese de contagem em dobro de tempo de serviço sob o regime constitucional atual para aumentar proventos.

</details>

---

### Questão 4 (FCC - 2018 - ALESE - Analista Legislativo - Adaptada para a realidade da EC 103 e do Estado)
Considerando as regras atuais sobre o benefício de pensão por morte aplicáveis ao Regime Próprio de Previdência Social, é correto afirmar que:
A) o valor da pensão por morte será invariavelmente equivalente a 100% do valor da aposentadoria que o servidor recebia ou a que teria direito, independentemente da quantidade de dependentes.
B) a pensão por morte concedida a cônjuge ou companheiro será sempre vitalícia, sendo vedado estipular prazos decadenciais em relação à duração do casamento ou idade do beneficiário.
C) o pagamento da cota individual da pensão por morte cessa com a perda da qualidade de dependente e, em regra, não se reverte aos demais dependentes remanescentes.
D) é expressamente permitida a cumulação integral de mais de uma pensão por morte deixada por cônjuge ou companheiro no âmbito do mesmo regime de previdência.
E) o benefício não se sujeitará ao teto do Regime Geral de Previdência Social em nenhuma hipótese, uma vez que decorre do serviço público efetivo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Análise das Alternativas:**
- **A) Incorreta.** Com as reformas, a pensão por morte consiste numa cota familiar de 50%, acrescida de cotas de 10% por dependente, até o limite de 100%. Só será 100% se houver, por exemplo, 5 dependentes ou se houver dependente inválido ou com deficiência intelectual, mental ou grave.
- **B) Incorreta.** A vitaliciedade da pensão ao cônjuge/companheiro depende da idade do pensionista na data do óbito e do tempo de união (no mínimo 2 anos de casamento/união estável e mínimo de contribuições). Há prazos de duração para pensionistas jovens.
- **C) Correta.** Conforme a EC 103/2019, que padronizou a regra para a União e que foi reproduzida nos Estados, as cotas por dependente que perdem a qualidade de beneficiário (ex: filho completou 21 anos) não são mais revertidas (redistribuídas) aos demais dependentes, sendo extintas daquele grupo familiar, ressalvado se o total do benefício original já estivesse no teto de 100%.
- **D) Incorreta.** É vedada a cumulação de mais de uma pensão por morte de cônjuge/companheiro no mesmo regime de previdência (CF, art. 201, e EC 103). Se forem em regimes diferentes, haverá redução no valor do benefício menos vantajoso.
- **E) Incorreta.** Se o Estado instituiu o Regime de Previdência Complementar (RPC), os servidores que ingressarem a partir da instituição estarão sujeitos, em suas aposentadorias e pensões, ao teto dos benefícios do RGPS.

</details>

---

### Questão 5 (FCC - 2015 - TCE-CE - Auditor de Controle Externo)
Em relação ao custeio do Regime Próprio de Previdência Social, no que tange aos servidores aposentados e pensionistas, a Constituição Federal estabelece que a contribuição previdenciária:
A) não pode incidir sobre inativos e pensionistas, sob pena de configurar bitributação e ofensa ao direito adquirido.
B) incide sobre o valor total dos proventos e pensões que exceder o limite máximo estabelecido para os benefícios do Regime Geral de Previdência Social (RGPS), em situação de normalidade atuarial.
C) será igual à dos servidores ativos, incidindo desde o primeiro centavo dos proventos, independentemente de se observar teto do RGPS.
D) possui alíquota progressiva que varia exclusivamente conforme a idade do inativo, visando compensar a maior longevidade no sistema.
E) deverá ser isenta integralmente caso o aposentado comprove doença grave, independentemente do valor que recebe de aposentadoria.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Análise das Alternativas:**
- **A) Incorreta.** Desde a EC 41/2003, inativos e pensionistas contribuem para o RPPS, não configurando direito adquirido nem bitributação (súmulas e jurisprudência do STF confirmam a validade da cobrança).
- **B) Correta.** A regra de matriz constitucional (art. 40, § 18, CF) é que a contribuição de inativos e pensionistas incide apenas sobre a parcela dos proventos de aposentadorias e de pensões que **supere o limite máximo estabelecido para os benefícios do RGPS** (teto do INSS). (Ressalta-se que a EC 103/2019 autoriza baixar esse limite isento até o salário mínimo apenas em caso de déficit atuarial, mas a regra geral aplicável permanece a do teto do RGPS).
- **C) Incorreta.** Diferente dos servidores ativos que contribuem sobre toda a remuneração de contribuição, inativos e pensionistas possuem a faixa de isenção descrita na alternativa B.
- **D) Incorreta.** Se houver alíquota progressiva (o que é permitido pós-EC 103), ela varia de acordo com as faixas do **valor da base de contribuição/remuneração**, e não com base na idade do inativo.
- **E) Incorreta.** Antes da EC 103/2019, portadores de doença grave tinham direito a que a contribuição só incidisse sobre o que superasse o dobro do teto do RGPS (art. 40, §21). No entanto, a EC 103 revogou esse parágrafo, não existindo mais essa isenção ampliada a nível constitucional, muito menos "isenção integral automática" independente de valor.

</details>

---

### Questão 6 (FCC - 2021 - PGE-PB - Procurador do Estado - Adaptada a nível estadual)
À luz da Constituição Federal, com as inovações introduzidas pela Emenda Constitucional nº 103/2019 acerca das regras do Regime Próprio de Previdência Social (RPPS), analise as afirmativas:
A) O tempo de contribuição de servidor cedido ou afastado para o exercício de mandato eletivo só será contado para fins de aposentadoria caso haja recolhimento em dobro, como forma de compensação.
B) As idades mínimas para a aposentadoria voluntária do servidor estadual são fixadas exclusivamente pela Constituição Federal em 65 anos para homens e 62 para mulheres, sem que o Estado possua autonomia para definir, mediante sua própria Constituição ou Lei Complementar, idades divergentes.
C) Aos Estados, o Distrito Federal e os Municípios não se aplica a obrigatoriedade de instituição de Regime de Previdência Complementar.
D) É lícita a adoção de requisitos e critérios diferenciados para aposentadoria de servidores cujas atividades sejam exercidas com efetiva exposição a agentes químicos, físicos e biológicos prejudiciais à saúde, por meio de lei complementar do ente respectivo.
E) O cálculo dos proventos de aposentadoria deve garantir sempre a paridade e a integralidade àqueles que ingressaram no serviço público após a edição da EC 41/2003.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Análise das Alternativas:**
- **A) Incorreta.** O servidor em exercício de mandato eletivo permanece vinculado ao seu regime de origem e recolhe a contribuição de forma normal, não havendo previsão legal ou constitucional de recolhimento "em dobro".
- **B) Incorreta.** Com a EC 103/2019, a competência para fixar as idades mínimas e os tempos de contribuição dos servidores estaduais, distritais e municipais passou a ser dos próprios entes, que o farão mediante **emenda às suas respectivas constituições estaduais ou leis orgânicas** (art. 40, § 1º, III, CF). As idades de 65 e 62 aplicam-se apenas à União, a menos que o Estado decida replicar a regra em sua constituição local.
- **C) Incorreta.** A EC 103 tornou **obrigatória** a instituição do Regime de Previdência Complementar por todos os Estados, DF e Municípios que possuam RPPS (art. 40, § 14, CF).
- **D) Correta.** Exceção clássica à vedação de critérios diferenciados. O art. 40, § 4º-C, da CF autoriza que os entes federativos, mediante lei complementar, estabeleçam idade e tempo de contribuição diferenciados para aposentadoria especial decorrente de exposição a agentes nocivos (atividades insalubres).
- **E) Incorreta.** Servidores que ingressaram após 31/12/2003 (data da EC 41) já não têm direito automático à integralidade e à paridade. Seus proventos são calculados com base na média aritmética de remunerações e sofrem reajustes anuais para preservação do valor real.

</details>

---

### Questão 7 (FCC - 2011 - TRE-CE - Analista Judiciário - Área Administrativa)
No que se refere às regras de aposentadoria do servidor público estadual com deficiência, de acordo com o texto constitucional pertinente ao Regime Próprio de Previdência Social, é correto afirmar que:
A) a concessão de aposentadoria ao servidor com deficiência garante invariavelmente proventos integrais correspondentes à última remuneração, independentemente da data de ingresso.
B) dependem de edição de lei complementar do respectivo ente federativo para que sejam estabelecidos requisitos e critérios diferenciados para a concessão da aposentadoria.
C) não pode haver qualquer estipulação de idade ou tempo de contribuição reduzidos para esses servidores, sob pena de afrontar o princípio do equilíbrio financeiro e atuarial do regime.
D) a aposentadoria será garantida exclusivamente sob a modalidade de incapacidade permanente, impossibilitando a aposentadoria voluntária do deficiente no serviço público.
E) a fixação de tempo de contribuição diferenciado dispensa comprovação do grau de deficiência (leve, moderada ou grave), por se tratar de direito humano incondicionado.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Análise das Alternativas:**
- **A) Incorreta.** A aposentadoria do servidor com deficiência não atrai, de modo automático e absoluto, o instituto da integralidade (última remuneração). Seu cálculo obedece à sistemática da média, a não ser que haja previsão específica ou que o servidor tenha ingressado antes das reformas de 2003, conforme regras de transição.
- **B) Correta.** O art. 40, § 4º-A, da Constituição Federal dispõe que "Poderão ser estabelecidos por **lei complementar do respectivo ente federativo** idade e tempo de contribuição diferenciados para aposentadoria de servidores com deficiência, previamente submetidos a avaliação biopsicossocial".
- **C) Incorreta.** A própria Constituição cria a exceção. É permitida a estipulação de requisitos diferenciados para a pessoa com deficiência.
- **D) Incorreta.** Ter uma deficiência não significa ser permanentemente incapaz para o trabalho. A pessoa com deficiência exerce suas atribuições, contribuindo com a previdência, e apenas usufrui de requisitos etários/temporais mais brandos para a aposentadoria voluntária.
- **E) Incorreta.** A lei deve fixar critérios diferenciados estritamente atrelados à gradação da deficiência (leve, moderada, grave), conforme modelo da LC 142/2013 (União) aplicável por simetria enquanto os Estados não editam as suas próprias. Logo, a comprovação e o grau são essenciais.

</details>

---

### Questão 8 (FCC - 2021 - SEFAZ-CE - Auditor)
A instituição do Regime de Previdência Complementar (RPC) para os servidores do Estado do Ceará impõe algumas modificações profundas na sistemática protetiva destes. Sobre este tema, é correto afirmar:
A) Com a criação do RPC estadual, todos os servidores estaduais já em efetivo exercício têm seus proventos imediatamente limitados ao teto do RGPS, sendo inscritos no fundo de capitalização de ofício.
B) A previdência complementar dos servidores estaduais deverá ser instituída por meio de lei de iniciativa do Poder Executivo, que observará os requisitos de instituição aplicáveis às estatais.
C) Uma vez instituído o RPC, os servidores que ingressarem no serviço público a partir de então estarão obrigatoriamente sujeitos ao limite máximo dos benefícios do RGPS (teto) na percepção de sua aposentadoria e pensão pelo regime próprio.
D) A natureza pública das fundações de direito privado criadas para administrar o RPC inviabiliza que estas invistam seus ativos no mercado financeiro aberto.
E) O patrocínio da previdência complementar estadual aos servidores estende-se sem limite aos proventos decorrentes da cumulação lícita de três cargos públicos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Análise das Alternativas:**
- **A) Incorreta.** A submissão ao teto do RGPS não atinge os servidores que **já estavam no serviço público** antes da instituição do RPC, a menos que eles **optem de forma prévia e expressa** por migrar de regime. O ato não é de ofício nem compulsório para os antigos.
- **B) Incorreta.** Embora a lei seja de iniciativa do Poder Executivo, a natureza da previdência complementar obedece ao art. 202 da CF e às Leis Complementares 108 e 109/2001, possuindo gestão privada e requisitos próprios, não se confundindo com as regras puras de criação de estatais comuns (L. 13.303).
- **C) Correta.** É o mecanismo central do RPC. Conforme a CF (art. 40, § 14 e § 15), instituído o regime de previdência complementar por ente federativo, o teto do RGPS aplicar-se-á aos limites das aposentadorias e pensões do RPPS concedidos aos **servidores que ingressarem a partir da data de publicação** do ato de sua instituição.
- **D) Incorreta.** As fundações de previdência complementar (como a CE-PREV/PREVINORDESTE, Funpresp, etc.) possuem justamente o propósito de formar reservas (capitalização). Suas diretrizes de aplicação autorizam fortes e complexos investimentos no mercado financeiro aberto para rentabilizar os recursos.
- **E) Incorreta.** A cumulação de cargos públicos está limitada a dois, e não a três, nas estritas hipóteses previstas no art. 37, XVI, da CF.

</details>

---

### Questão 9 (FCC - 2018 - SEFAZ-SC - Auditor Fiscal da Receita Estadual)
Com relação ao custeio extraordinário do Regime Próprio de Previdência Social, inserido na Constituição Federal, caso seja demonstrada a insuficiência da adoção das medidas ordinárias para equacionar grave déficit atuarial, é lícito ao Estado do Ceará:
A) suspender o pagamento das aposentadorias cujo valor esteja situado acima do teto do RGPS, até que as reservas atuariais se estabilizem.
B) extinguir o Regime Próprio de Previdência e transferir compulsoriamente os inativos para o Regime Geral, reduzindo os proventos.
C) instituir contribuição extraordinária exclusiva para os servidores ativos, preservando-se a segurança jurídica de inativos e pensionistas.
D) instituir contribuição extraordinária aplicável a servidores ativos, aposentados e pensionistas, de forma temporária e por prazo determinado.
E) determinar o confisco da parcela dos salários dos servidores vinculados ao RPC para sanear as contas do RPPS estadual.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Análise das Alternativas:**
- **A) Incorreta.** A Constituição garante o direito ao recebimento dos benefícios previdenciários. A supressão de pagamentos já concedidos ofende o direito adquirido, a dignidade humana e a proteção constitucional ao idoso e aposentado.
- **B) Incorreta.** É vedada a extinção do RPPS sem garantias. Além disso, embora a EC 103 permita a extinção e a ida ao RGPS no futuro, isso não afetará direitos adquiridos nem autoriza a redução irrestrita de proventos já estabilizados, existindo regras severas de transição e assunção passiva do Ente.
- **C) Incorreta.** A EC 103/2019 incluiu o art. 149, § 1º-B, prevendo que a contribuição extraordinária, quando houver déficit grave, poderá ser instituída não apenas para os ativos, mas também para aposentados e pensionistas.
- **D) Correta.** O art. 149, § 1º-B, da Constituição Federal, autoriza que "demonstrada a insuficiência da medida prevista no § 1º-A para equacionar o déficit atuarial, é facultada a instituição de **contribuição extraordinária**, no âmbito da União, **dos Estados**, do Distrito Federal e dos Municípios, no prazo máximo de 20 (vinte) anos, **nos termos de lei, e de forma temporária e aplicável aos servidores ativos, aposentados e pensionistas**".
- **E) Incorreta.** A Constituição Federal repudia o confisco (art. 150, IV). As contribuições devem pautar-se por leis estritas, garantindo as reservas da Previdência Complementar, que pertencem às contas individuais dos segurados e são apartadas do caixa do RPPS.

</details>

---

### Questão 10 (FCC - 2012 - TRT 11 - Juiz do Trabalho - Adaptada a conceitos previdenciários estaduais)
No que diz respeito às regras de contagem de tempo de serviço e contribuição, assinale a alternativa que consagra um preceito constitucional exigível do Regime Próprio de Previdência Social estadual.
A) Será computado integralmente, sem limite, o tempo de trabalho exercido de forma fictícia (por cômputo matemático em dobro), caso o servidor tenha exercido suas funções em área de fronteira e mediante legislação estadual específica.
B) As aposentadorias concedidas a ex-ocupantes de cargo em comissão não vinculados a cargo efetivo correrão obrigatoriamente por conta do RPPS estadual.
C) O tempo de contribuição averbado do serviço militar nas Forças Armadas deverá ser computado para efeitos de aposentadoria no serviço público estadual.
D) É lícita a exigência de idade mínima mais severa para servidores que optaram pelo regime de transição do que para aqueles submetidos à regra permanente de aposentadoria.
E) A averbação do tempo de serviço de empresa pública regida pela CLT gera, de imediato, o recebimento de acréscimo de 5% sobre os vencimentos a título de adicional por tempo de serviço.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Análise das Alternativas:**
- **A) Incorreta.** O art. 40, § 10, da CF é taxativo: **A lei não poderá estabelecer qualquer forma de contagem de tempo de contribuição fictício**. Portanto, veda-se tempo averbado em dobro, seja na fronteira ou em qualquer outra localidade.
- **B) Incorreta.** Conforme art. 40, § 13, da CF, aplica-se o Regime Geral de Previdência Social (RGPS / INSS) ao ocupante exclusivamente de cargo em comissão declarado em lei de livre nomeação e exoneração. Logo, ele não pertence ao RPPS.
- **C) Correta.** O tempo de contribuição militar e civil prestado sob a égide da União, Estados e Municípios é assegurado e computado para a aposentadoria recíproca no regime estatutário do Estado (CF, art. 40, § 9º c/c o antigo art. 201, § 9º). A legislação previdenciária de todos os entes absorve e averba o tempo de Forças Armadas (com a devida compensação).
- **D) Incorreta.** A essência jurídica de uma regra de transição é, logicamente, atenuar as regras novas para os servidores mais antigos. É ilógico e violador do preceito de confiança que o regime de transição crie requisitos mais gravosos que a regra permanente.
- **E) Incorreta.** A averbação tem fins **previdenciários** (aposentadoria, contagem de contribuição), conforme dita o art. 201, § 9º. Ela não assegura benefícios puramente estatutários (anuênios, quinquênios, vantagens financeiras locais), pois estes se referem estritamente ao serviço público do Ente (no caso o Estado), e não ao tempo celetista prévio.

</details>

---

### Questão 11 (FCC - 2021 - SEFAZ-CE)
O cálculo dos proventos de aposentadoria no âmbito do Regime Próprio de Previdência Social (RPPS), para os servidores estaduais não amparados por direito adquirido ou regras antigas de paridade/integralidade, basear-se-á:
A) na última remuneração recebida pelo servidor no momento do requerimento da aposentadoria, adicionando-se vantagens de caráter indenizatório.
B) na média aritmética de 80% dos maiores salários de contribuição de todo o período contributivo do segurado, desprezando-se os 20% menores salários.
C) na média aritmética simples de 100% (cem por cento) dos salários de contribuição desde a competência julho de 1994, com a aplicação subsequente de alíquotas que iniciam, em regra, em 60% dessa média.
D) no valor fixo correspondente a 10 salários mínimos para categorias de nível superior, e 5 salários para categorias de nível médio.
E) integralmente na capitalização dos rendimentos do Fundo Estadual de Previdência, que definirá o valor conforme oscilação das bolsas de valores.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Análise das Alternativas:**
- **A) Incorreta.** A regra para servidores não amparados por paridade e integralidade aboliu o uso exclusivo da "última remuneração". Vantagens indenizatórias (como diárias, auxílio-alimentação) sequer compõem a base previdenciária.
- **B) Incorreta.** Essa era a regra antiga, anterior à Reforma da Previdência (Lei 10.887/04). O cálculo considerava os 80% maiores salários. Esta forma foi revogada pela EC 103/2019 e legislações correlatas, que instituíram o uso de todos os salários.
- **C) Correta.** Após a Reforma da Previdência da EC 103/2019 (regra absorvida pelas reformas estaduais em obediência à simetria de cálculos gerais ou norma expressa), o cálculo parte da média de **100% de todo o histórico contributivo (desde 07/1994)**. O valor do benefício corresponderá, na regra geral da aposentadoria voluntária, a 60% dessa média, acrescido de 2% para cada ano de contribuição que exceder os 20 anos (ou outra regra equivalente a depender de sexo e estado).
- **D) Incorreta.** Nenhum regime público brasileiro adota valores fixos em salários mínimos como método de provento baseado em nível de escolaridade, pois fere o caráter contributivo e solidário que deve ser estritamente pautado na contribuição efetivamente vertida.
- **E) Incorreta.** O RPPS funciona primariamente sob o regime de **repartição simples** ou capitais de cobertura atuarial para benefícios definidos. A renda previdenciária decorre da lei e da matemática atuarial baseada em salários de contribuição, e não do puro risco de oscilação do mercado (capitalização pura), como ocorre nos planos abertos de risco puro.

</details>

---

### Questão 12 (FCC - 2018 - TRT 6 - Analista Judiciário)
Em conformidade com as restrições e vedações constitucionais afetas aos Regimes Próprios de Previdência Social, os proventos de aposentadoria e as pensões:
A) não poderão sofrer o desconto da contribuição previdenciária mensal, tendo em vista que os fatos geradores são extintos no momento da jubilação.
B) por ocasião de sua concessão, não poderão exceder a remuneração do respectivo servidor, no cargo efetivo em que se deu a aposentadoria ou que serviu de referência para a concessão da pensão.
C) são passíveis de redução atuarial automática caso o Estado aponte decréscimo de arrecadação do ICMS em período superior a um semestre civil.
D) estão sujeitos ao teto remuneratório do funcionalismo estadual, que, segundo a Constituição, limita-se sem qualquer exceção ao subsídio do Governador do Estado para os membros do Judiciário estadual.
E) serão obrigatoriamente reajustados de modo a espelhar perfeitamente qualquer elevação remuneratória dos servidores ativos, sendo proibido o reajuste apenas pela inflação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Análise das Alternativas:**
- **A) Incorreta.** Inativos e pensionistas sofrem descontos de contribuição previdenciária sobre o valor que excede o limite estipulado na CF, sendo essa cobrança plenamente válida e constitucional (art. 40, § 18).
- **B) Correta.** Disposição literal do art. 40, § 2º, da Constituição Federal. O limite imposto pelo texto constitucional dita que a soma do benefício não pode ultrapassar a remuneração do servidor do respectivo cargo efetivo em que ocorreu o fato que gerou o benefício. Trata-se do "teto interno da remuneração original".
- **C) Incorreta.** A redução autônoma, repentina e administrativa de proventos já estabilizados é inadmissível em face do princípio constitucional da irredutibilidade do valor dos benefícios previdenciários e do direito adquirido. O remédio para desequilíbrio passa por ajustes de alíquotas (contribuições), não por esmagamento dos benefícios concedidos.
- **D) Incorreta.** O teto do funcionalismo estadual possui um limite multifacetado: Desembargadores do TJ para o Judiciário (e também aplicável a todos caso o Estado aprove subteto único), e para o Executivo é o subsídio do Governador. Membros do Judiciário não se limitam ao teto do Governador.
- **E) Incorreta.** Ao contrário, a regra matriz hoje (para quem não tem o direito assegurado de paridade) é que o benefício previdenciário possui apenas o direito ao "reajustamento periódico para preservação de seu valor real" (reajuste inflacionário - art. 40, § 8º). A paridade não é mais obrigatória.

</details>

---

### Questão 13 (FCC - 2017 - DPE-RS - Analista)
Sobre a concessão de pensão por morte, caso ocorra a morte do servidor do Estado do Ceará e este possua como dependentes seu filho de 15 anos de idade e seu cônjuge de 45 anos de idade:
A) a cota-parte destinada ao filho de 15 anos, quando este atingir a idade limite de invalidez (21 anos ou fim da faculdade aos 24), se reverterá automaticamente à viúva, ampliando a cota dela, independentemente de quando o óbito tiver ocorrido.
B) a pensão deverá ser dividida em partes iguais; no entanto, em razão da regra da EC 103/2019, as cotas individuais caídas não são reversíveis aos demais dependentes, findando sua parcela respectiva na obrigação previdenciária.
C) a viúva receberá 100% da pensão correspondente ao marido e repassará, sob forma de pensão alimentícia judicial, uma quota-parte para o filho, por ser este menor impúbere.
D) a concessão de pensão ao cônjuge só será devida caso este comprove que não detém renda própria advinda de qualquer vínculo formal no serviço público ou iniciativa privada.
E) o filho, por ser dependente previdenciário, receberá sua parte de forma vitalícia, protegendo a formação e continuidade acadêmica.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Análise das Alternativas:**
- **A) Incorreta.** Após a EC 103/2019, foi abolido o mecanismo de reversão/redistribuição de cotas caídas (quando um dependente perde essa qualidade) para o dependente remanescente. Com o fim do benefício do filho aos 21 anos, a sua quota extingue-se, barateando a despesa estatal.
- **B) Correta.** É o novo figurino constitucional previdenciário. As cotas por dependente (cada dependente garante 10% do valor da base de cálculo e tem sua fatia) não reversíveis em caso de perda da qualidade, extingue-se assim a sua fatia sobre o montante (art. 23, § 1º, da EC 103).
- **C) Incorreta.** A previdência social concede e paga a pensão por morte na forma de **cotas-partes** diretamente nominais aos dependentes habilitados. A administração divide e paga aos titulares/representantes legais, não existindo isso da viúva ter o poder de "repassar como pensão alimentícia".
- **D) Incorreta.** O cônjuge possui **dependência econômica presumida**. Ele faz jus à pensão por morte independentemente de deter trabalho ou outra fonte de renda no setor público ou privado, podendo apenas a lei estipular redutores em caso de cumulação de aposentadoria e pensão.
- **E) Incorreta.** O filho não inválido/não deficiente tem sua qualidade de dependente previdenciário encerrada ao completar 21 anos. Não há extensão vitalícia ou até os 24 anos (para universitários) em regimes previdenciários (há vasta jurisprudência do STJ afastando a extensão previdenciária universitária).

</details>

---

### Questão 14 (FCC - 2014 - AL-PE - Analista Legislativo - Adaptada)
A gestão da Previdência Social no âmbito do Estado requer rigorosos critérios técnicos. No que tange à caracterização do Regime Próprio de Previdência Social, assinale a assertiva que traduz o modelo constitucional de equilíbrio:
A) O RPPS dos entes estaduais organiza-se sob o método financeiro de capitalização pura, de forma idêntica à das seguradoras bancárias privadas.
B) As contribuições vertidas para o RPPS pelos servidores poderão ser livremente transpostas para financiar despesas de saúde pública estaduais e obras do Executivo que atendam à coletividade.
C) A observância dos critérios que preservem o equilíbrio financeiro e atuarial é premissa obrigatória e incontornável do Regime Próprio de Previdência Social.
D) É lícito que o regime crie benefícios sociais assistenciais, a exemplo do programa "bolsa-família estadual", valendo-se dos recursos arrecadados previdenciariamente.
E) A responsabilidade pela cobertura de insuficiência financeira do RPPS dos servidores estaduais transfere-se supletivamente à União Federal, por força do pacto federativo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Análise das Alternativas:**
- **A) Incorreta.** O RPPS tem organização predominantemente embasada no pilar do **regime de repartição simples** e da solidariedade intergeracional (o ativo paga os benefícios do inativo atual), e não em mera conta de capitalização individualizada ("conta poupança") de risco mercantil.
- **B) Incorreta.** Vigora no RPPS a afetação absoluta dos recursos: é vedada a aplicação de recursos de regimes de previdência para o custeio de despesas de assistência à saúde e despesas gerais do Estado (art. 167, XI, da CF). O recurso previdenciário serve unicamente para benefícios previdenciários.
- **C) Correta.** Trata-se da pedra basilar insculpida no art. 40, caput, da CF: O regime próprio terá "caráter contributivo e solidário, mediante contribuição do respectivo ente federativo, de servidores ativos, de aposentados e de pensionistas, observados critérios que preservem o **equilíbrio financeiro e atuarial**".
- **D) Incorreta.** Despesas de Assistência Social não integram o caixa da Previdência. O recurso dos inativos do RPPS não financia bolsas e projetos da seara assistencialista geral.
- **E) Incorreta.** Cada Ente federativo (no caso, o Estado) garante solitariamente a liquidez, solidez e as obrigações previdenciárias de seus servidores, não havendo assunção supletiva do déficit atuarial pela União Federal.

</details>

---

### Questão 15 (FCC - 2021 - TCE-SC - Auditor Fiscal de Controle Externo)
Imagine que a Assembleia Legislativa do Estado do Ceará avalie Projeto de Emenda Constitucional para tratar da previdência dos servidores. Analisando as limitações da competência concorrente e das regras gerais previdenciárias em nível nacional, assinale o que o Estado **ESTÁ VEDADO** (impedido) de fazer, sob pena de inconstitucionalidade.
A) Criar abono de permanência mais vantajoso que o previsto em âmbito federal, a fim de reter seus servidores estaduais experientes nas carreiras da Educação.
B) Extinguir os adicionais por tempo de serviço (quinquênios) para o futuro dos servidores estaduais.
C) Estabelecer alíquota de contribuição previdenciária de servidores ativos inferior à alíquota de contribuição exigida dos servidores da União, exceto se comprovado que o regime estadual não possui déficit atuarial a equacionar.
D) Fixar idades mínimas diferentes para aposentadoria voluntária daquelas adotadas pela União, adequando a matriz demográfica do servidor público local.
E) Estabelecer, por lei complementar própria, tempo de contribuição especial para seus servidores ocupantes do cargo de Policial Civil, distintos das regras dos demais servidores estaduais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Análise das Alternativas:**
- **A) Incorreta.** O Estado tem certa margem para disciplinar sua política remuneratória, desde que respeite os princípios constitucionais. O abono de permanência estadual pode ter peculiaridades estritas aos limites máximos da CF, contudo, é a alíquota abaixo do exigido que é cabalmente proibida.
- **B) Incorreta.** O Estado possui competência plena para reestruturar suas carreiras estatutárias e suprimir gratificações e adicionais por tempo de serviço (respeitado o direito adquirido do passado).
- **C) Correta.** É o que prevê o art. 149, § 1º, da CF: A alíquota de contribuição não será inferior à da contribuição dos servidores da União, exceto se demonstrado que o respectivo regime próprio de previdência social não possui déficit atuarial a ser equacionado (se tem déficit, a alíquota estadual não pode ser menor que os 14% aplicados na base federal, devendo adotar alíquotas ordinárias iguais ou maiores).
- **D) Incorreta.** Com a EC 103/2019, o art. 40 autorizou que os Estados fixem as idades mínimas por meio de suas Constituições Estaduais, logo não é vedado, é expressamente permitido pelo constituinte federal.
- **E) Incorreta.** A Constituição assegura textualmente aos entes federativos competência para criar lei complementar estipulando critérios diferenciados de aposentadoria para carreiras como as da polícia civil, agentes penitenciários e socioeducativos (§ 4º-B, art. 40, CF).

</details>

---


