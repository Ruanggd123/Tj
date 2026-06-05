# Bateria de Questões FCC — Quinta-feira 04/06

## 📝 TEMA 1: Banco de Dados: Modelagem ER + Normalização de Dados

### Questão 1 (FCC - Questão Prática / Adaptada)
Um Engenheiro de Dados do Tribunal Regional do Trabalho da 12ª Região está encarregado de reestruturar o sistema legado de cadastro de estagiários. Na tabela atual, há uma coluna chamada `Telefones_Contato` que armazena os números do estagiário no formato '48999991111, 48999992222' separados por vírgula. Durante o processo de normalização do banco de dados relacional para adequação à Primeira Forma Normal (1FN), o procedimento arquitetural correto que o engenheiro deve adotar é:
A) Modificar a coluna para o tipo JSONB ou BLOB para que o banco reconheça formalmente os múltiplos números e mantenha a tabela como está.
B) Criar colunas fixas adjacentes denominadas `Telefone_1`, `Telefone_2` e `Telefone_3` na própria tabela de estagiários, garantindo assim a atomicidade na consulta SQL sem a necessidade de tabelas externas.
C) Eliminar a coluna `Telefones_Contato` da tabela principal e criar uma nova tabela associada (ex: `Telefone_Estagiario`), relacionando-a por chave estrangeira em um formato de 1 para N (1:N), garantindo a atomicidade e a ausência de grupos repetitivos.
D) Estabelecer uma chave primária composta na tabela de estagiários envolvendo o CPF e os Telefones em conjunto, o que automaticamente satisfaz os requisitos da 1FN.
E) Adotar o modelo relacional de herança, especializando o estagiário em múltiplas classes instanciáveis a depender da quantidade de telefones informados na triagem.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. A 1FN exige atomicidade (um valor por célula) e a eliminação de grupos/campos repetitivos ou multivalorados. A solução padrão em bancos relacionais é sempre criar uma nova tabela para armazenar os múltiplos telefones associados à chave primária do dono.
</details>

### Questão 2 (FCC - Questão Prática / Adaptada)
O setor de estatística e relatórios (BI) de um fórum solicitou ao DBA a geração de um relatório complexo que envolvia 8 cruzamentos (JOINs) pesados entre tabelas de processo e andamento que se encontravam na Terceira Forma Normal (3FN), o que estava estourando o tempo limite de resposta do servidor de banco de dados e travando a rede. Para solucionar esse problema visando exclusivamente o ganho de velocidade em leitura, o DBA decidiu fundir duas tabelas de histórico num único modelo, recriando campos redundantes e quebrando propositalmente as regras da 3FN. Essa técnica aplicada para ganho de performance é denominada:
A) Otimização Transacional Isolada.
B) Normalização de Boyce-Codd (BCNF).
C) Particionamento Horizontal em Hash.
D) Desnormalização.
E) Criação de Índice Árvore-B Físico.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. A Desnormalização é a prática deliberada e consciente de violar uma ou mais regras de normalização (inserindo redundância e agrupando tabelas) para evitar JOINs custosos e aumentar dramaticamente a velocidade de leitura (Data Warehouses e relatórios OLAP fazem muito isso).
</details>

### Questão 3 (FCC - Questão Prática / Adaptada)
Durante a construção do diagrama lógico de um banco de dados no padrão ER (Entidade-Relacionamento), um Analista Judiciário de TI precisou mapear um relacionamento lógico muitos-para-muitos (N:M) entre as entidades `Juiz` e `Vara`, afinal, um Juiz pode atuar em várias Varas ao longo da vida, e uma Vara pode ter múltiplos Juízes designados. Para mapear corretamente esse cenário no Banco de Dados Relacional físico (ex: PostgreSQL) garantindo a integridade sem perda de histórico, o analista deve obrigatoriamente:
A) Inserir a chave primária da entidade `Vara` como uma chave estrangeira na tabela `Juiz` contendo a restrição `ON DELETE CASCADE`.
B) Mesclar ambas as entidades em uma macro-tabela contendo colunas nulas, reduzindo anomalias de exclusão.
C) Criar uma terceira tabela (entidade associativa) que deve conter, no mínimo, as chaves estrangeiras que apontam para as chaves primárias de `Juiz` e `Vara`, formando muitas vezes a chave primária composta dessa nova tabela.
D) Utilizar o mecanismo de dependência transitiva cruzada no Oracle, eliminando a exigência física de chaves estrangeiras secundárias.
E) Criar um Array Binário Longo (BLOB) dentro da tabela `Juiz` para armazenar o ID das Varas sequencialmente.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Em bancos relacionais, não há forma direta de implementar um relacionamento N:M entre duas tabelas. A solução canônica é 'quebrar' o relacionamento criando uma terceira tabela (tabela associativa ou de junção) que conecta as chaves das duas tabelas originais e resolve o problema transformando em dois relacionamentos 1:N.
</details>

### Questão 4 (FCC - Questão Prática / Adaptada)
O Tribunal Regional está auditando a tabela `Processo_Audiencia` que possui uma chave primária composta formada por (`Numero_Processo`, `Data_Audiencia`). Além das colunas de chave, a tabela contém a coluna `Juiz_Designado` e a coluna `Classe_Judicial_Processo`. O auditor de dados identificou que o valor da coluna `Classe_Judicial_Processo` depende única e exclusivamente do `Numero_Processo`, sendo totalmente alheio à `Data_Audiencia`. Do ponto de vista acadêmico da normalização, a tabela apresenta um vício crônico por ferir diretamente a regra da:
A) Primeira Forma Normal (1FN).
B) Segunda Forma Normal (2FN).
C) Terceira Forma Normal (3FN).
D) Quarta Forma Normal (4FN).
E) Forma Normal de Boyce-Codd (FNBC).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. A Segunda Forma Normal (2FN) foca em chaves compostas e exige que todos os atributos não chave dependam INTEGRALMENTE da chave primária inteira (e não apenas de uma parte dela). Como a Classe do Processo depende apenas do Número do Processo (uma fração da chave), isso configura Dependência Parcial, ferindo a 2FN.
</details>

### Questão 5 (FCC - Questão Prática / Adaptada)
Um Desenvolvedor Júnior modelou a tabela `Servidor` com os seguintes atributos estruturais: (`Matricula` [PK], `Nome`, `Codigo_Departamento`, `Nome_Departamento`, `Local_Departamento`). Ao apresentar ao DBA Sênior, este reprovou o modelo indicando que os campos `Nome_Departamento` e `Local_Departamento` dependem de `Codigo_Departamento`, que por sua vez depende da `Matricula`. Essa relação na qual um atributo não-chave depende de outro atributo não-chave que finalmente depende da chave primária viola a regra máxima de normalização exigida na:
A) Primeira Forma Normal (1FN).
B) Segunda Forma Normal (2FN).
C) Terceira Forma Normal (3FN).
D) Quarta Forma Normal (4FN).
E) Dependência Multivalorada (DMV).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Esse é o clássico exemplo de 'Dependência Transitiva'. A 3FN dita que atributos não-chave devem ser mutuamente independentes entre si e depender DIRETAMENTE da chave primária. Como os dados do departamento dependem do código (e não diretamente da matrícula), deve-se criar uma tabela `Departamento`.
</details>

### Questão 6 (FCC - Questão Prática / Adaptada)
Considere o conceito do Modelo Entidade-Relacionamento original (Peter Chen). Ao projetar o sistema do plano de saúde do tribunal, o analista identificou uma entidade `Dependente`. Notou-se que um dependente (um filho) não possui atributo capaz de identificá-lo unicamente no sistema sem associar-se forçosamente ao seu `Servidor` responsável. Se o servidor for excluído do banco, seus dependentes perdem o sentido e também desaparecem em cascata. Na modelagem conceitual, o `Dependente` é tecnicamente modelado e caracterizado como uma:
A) Entidade Associativa Interseccional.
B) Entidade Generalista Base.
C) Entidade Forte Isolada.
D) Entidade Fraca.
E) Entidade Multivalorada Abstrata.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. Entidades que não possuem chave primária suficiente para existirem independentemente no sistema e dependem estritamente da existência de uma Entidade Forte (Pai) são chamadas de Entidades Fracas no modelo ER. Elas utilizam a chave do pai junto a um atributo discriminador próprio para formar sua chave.
</details>

### Questão 7 (FCC - Questão Prática / Adaptada)
No projeto conceitual do sistema criminal, a tabela `Veiculo` possui a coluna `Placa`, que identifica o carro unicamente, e também a coluna `Chassi`, que de igual maneira é única para cada carro fabricado e nunca se repete. O desenvolvedor escolheu `Placa` para atuar como a Chave Primária (Primary Key). Dessa forma, de acordo com a teoria de banco de dados, o campo `Chassi`, por também possuir a capacidade de identificação universal da tupla, é classificado como uma chave:
A) Estrangeira (Foreign Key).
B) Candidata (Candidate Key) ou Chave Alternativa.
C) Derivada (Derived Key).
D) Composta Natural (Composite Key).
E) Transitiva Secundária.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Qualquer conjunto de colunas que seja único e não nulo capaz de identificar a linha inteira é uma Chave Candidata. O analista escolhe apenas uma das candidatas para ser a Primária. As outras que 'sobraram' no processo e não foram escolhidas (como o Chassi) passam a ser chamadas de Chaves Alternativas.
</details>

### Questão 8 (FCC - Questão Prática / Adaptada)
Um Arquiteto de Sistemas desenhou um banco de dados relacional para o tribunal, focando-se em uma tabela chamada `Professor_Disciplina`. A tabela possui a chave composta (`ID_Professor`, `Materia`) e o atributo `ID_Area_Conhecimento`. Analisando os negócios, ele viu que o `ID_Professor` sozinho já determina o `ID_Area_Conhecimento` de forma absoluta (ex: Professor Joao é sempre da área de Exatas). O Arquiteto notou que isso geraria redundância na hora de atualizar a área. A qual anomalia de banco de dados esse cenário está primariamente suscetível devido à falta de normalização em 2FN?
A) Anomalia de Seleção, pois consultas de relatório trarão tabelas duplicadas sem índice.
B) Anomalia de Integridade Referencial Cíclica, gerando deadlock do banco SQL Server.
C) Anomalia de Atualização (Update Anomaly), visto que alterar a área de conhecimento do professor exigiria encontrar e modificar cada registro de disciplina que ele ministra.
D) Anomalia de Exclusão Cascata (Delete Anomaly), forçando o apagamento da tabela mãe de departamentos acadêmicos inteira.
E) Anomalia de Particionamento (Partition Anomaly), inviabilizando que o banco grave fisicamente o registro em clusters remotos da mesma nuvem.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Se você tem dependência parcial, o dado 'Área de Conhecimento' estará gravado redundante centenas de vezes (uma para cada disciplina que o professor der). Se a área mudar, você sofrerá uma 'Anomalia de Atualização', correndo o risco de atualizar o valor em 50 linhas e esquecer de atualizar em outras 50, corrompendo a verdade do dado.
</details>

### Questão 9 (FCC - Questão Prática / Adaptada)
A Norma Boyce-Codd (FNBC / BCNF) é muitas vezes tratada como uma versão mais rígida ou avançada da Terceira Forma Normal (3FN). Um analista argumentou tecnicamente em reunião que o banco de dados do Tribunal atingiu a FNBC. A definição formal correta que atesta que uma tabela em 3FN também satisfaz a Forma Normal de Boyce-Codd é:
A) Se e somente se todo determinante na relação for uma superchave candidata, eliminando casos onde partes de uma chave candidata dependem de atributos não-chave.
B) Se e somente se não existir nenhuma dependência multivalorada independente armazenada isoladamente.
C) Se a tabela estiver particionada horizontalmente com pelo menos um índice HASH ativado no sistema gerenciador.
D) Se todas as chaves estrangeiras da tabela principal apontarem para tabelas secundárias com cardinalidade restrita do tipo (1:1).
E) Se não houver campos vazios (NULL) na tabela e todos os atributos numéricos contiverem validações externas (CHECK Constraints).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- A) Correta. A FNBC foi criada por Codd e Boyce para corrigir um pequeno furo matemático da 3FN. A FNBC estabelece que 'todo determinante deve ser uma superchave' (ou chave candidata). Ela previne anomalias raras quando a tabela possui duas ou mais chaves compostas que se sobrepõem/cruzam entre si.
</details>

### Questão 10 (FCC - Questão Prática / Adaptada)
No modelo Entidade-Relacionamento Extendido (EER), um relacionamento do tipo Herança (Generalização e Especialização) é comum, como por exemplo: `Pessoa` (Pai) que pode ser especializadas em `Pessoa Física` (Filha) e `Pessoa Jurídica` (Filha). Ao transformar esse diagrama EER para o modelo Lógico (Tabelas Relacionais) visando aplicar restrições rígidas de controle sem gerar campos vazios e sem causar redundâncias severas, a melhor e mais recomendada abordagem de mapeamento clássica gerará:
A) Uma única e exclusiva tabela `Pessoa` agregando todos os atributos de física e jurídica, controlados por um tipo enumerado e resultando em inúmeras colunas nulas (NULL) obrigatoriamente (Single Table).
B) Apenas duas tabelas fisicamente dissociadas: `Pessoa Física` e `Pessoa Jurídica`, duplicando a coluna ID genérica de Pessoa e perdendo a indexação central da superclasse unificada (Concrete Table).
C) Três tabelas no banco de dados (`Pessoa`, `Pessoa Física`, `Pessoa Jurídica`), onde as filhas terão como chave primária o exato ID da tabela pai `Pessoa`, atuando simultaneamente como Chave Estrangeira (Class Table).
D) Nenhuma tabela no banco, e sim uma View (Visão) materializada no PostgreSQL baseada nos dados binários JSON do aplicativo.
E) Um banco de dados orientado a grafos isolado sem restrição referencial estrita e com nós dinâmicos polimórficos de acesso veloz em nuvem.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Para modelar herança no banco relacional de forma 'perfeita' e normalizada (Class Table ou Tabela-por-Tipo), criam-se as 3 tabelas. A tabela Pai guarda ID e Nome. A tabela Filha guarda apenas seus atributos específicos e usa o ID do Pai como Primária e Estrangeira ao mesmo tempo. Não há células NULL inúteis nem duplicação central.
</details>

### Questão 11 (FCC - Questão Prática / Adaptada)
Um banco de dados de um aplicativo governamental possui a tabela `Professor` com colunas `Materia_Lecionada` e `Hobby_Pessoal`. Sabemos que um professor pode lecionar várias matérias e, independentemente das matérias, pode ter vários hobbies esportivos. Armazenar esses dois conjuntos independentes de dados repetitivos (Múltiplas matérias X Múltiplos Hobbies) em uma mesma tabela base gera anomalias explosivas de cruzamento de dados vazios. Essa violação clássica envolvendo dependências independentes dentro da mesma entidade fere tecnicamente a regra da:
A) Primeira Forma Normal (1FN).
B) Segunda Forma Normal (2FN).
C) Terceira Forma Normal (3FN).
D) Quarta Forma Normal (4FN).
E) Quinta Forma Normal (5FN).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. A Quarta Forma Normal (4FN) é específica para combater e erradicar as 'Dependências Multivaloradas'. Se a tabela guarda mais de uma relação independente 1:N no mesmo local, ela violou a 4FN. A solução é extraí-las para duas novas tabelas (Professor_Materia e Professor_Hobby).
</details>

### Questão 12 (FCC - Questão Prática / Adaptada)
Um estagiário de TI no TRT gerou uma tabela `Contrato` e incluiu uma coluna chamada `Idade_do_Contrato_Em_Dias`, que deveria ser atualizada em um rotina noturna no cron do Linux subtraindo a `Data_Assinatura` da data atual. O Administrador de Dados sênior removeu a coluna argumentando que atributos cujo valor pode ser completamente deduzido a partir de outros campos já persistidos no banco não devem possuir armazenamento físico definitivo visando manter a integridade de normalização. No jargão de ER (Chen), esse tipo de campo é denominado Atributo:
A) Composto.
B) Multivalorado.
C) Derivado.
D) Cíclico Identificador.
E) Polimórfico Abstrato.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Um Atributo Derivado (representado por um círculo tracejado no ER clássico de Peter Chen) é aquele que pode ser calculado 'em tempo de execução' (on-the-fly) a partir de outras colunas base (como a Idade a partir da Data de Nascimento). Armazená-los quebra a consistência, pois requer atualizações diárias ou Triggers.
</details>

### Questão 13 (FCC - Questão Prática / Adaptada)
Para o design da nova aplicação web das varas cíveis, a equipe de desenvolvimento precisa mapear uma restrição lógica de cardinalidade. A regra de negócio afirma categoricamente: 'Uma Sala de Audiência PODE abrigar de ZERO a VÁRIOS processos durante um mês. Um Processo Judicial SOMENTE PODE acontecer OBRIGATORIAMENTE em UMA, e apenas uma, Sala de Audiência ao longo de sua vida ativa'. No padrão de diagramação clássica (Notação Min-Max), essa restrição (Sala X Processo) deve ser descrita corretamente como:
A) Sala (1,1) e Processo (0,N).
B) Sala (0,N) e Processo (1,1).
C) Sala (1,N) e Processo (0,1).
D) Sala (0,1) e Processo (1,N).
E) Sala (0,0) e Processo (N,N).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Sala -> abriga Processo. A Sala tem o mínimo de ZERO processos (pode estar vazia) e máximo de VÁRIOS (N). O Processo precisa OBRIGATORIAMENTE de uma sala (Mínimo 1) e APENAS de uma (Máximo 1). Logo, Processo é (1,1). Na notação comum, os parênteses ficam junto à entidade alvo.
</details>

### Questão 14 (FCC - Questão Prática / Adaptada)
Uma 'Constraint' (Restrição) de Integridade em bancos relacionais é a base que sustenta a confiança nos dados gravados. A restrição física que impede que você cadastre dois tribunais diferentes com o mesmíssimo número de CNPJ nacional na tabela, mesmo sabendo que o CNPJ não foi escolhido pelo arquiteto como a 'Chave Primária' (PK) na tabela, é implementada tecnicamente no SGBD pela constraint de:
A) FOREIGN KEY (Chave Estrangeira).
B) CHECK DOMAIN (Checagem de Domínio Restrito).
C) DEFAULT VALUE (Valor Padrão Automático).
D) UNIQUE (Unicidade).
E) CASCADE UPDATE (Atualização Cascata Remota).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. A restrição UNIQUE (Único) garante que não haverá valores duplicados naquela coluna (ideal para Chaves Candidatas Alternativas, como CPF e CNPJ). Ela age quase igual a uma Primary Key, mas aceita (na maioria dos SGBDs) que o campo seja preenchido com NULL, dependendo da configuração.
</details>

### Questão 15 (FCC - Questão Prática / Adaptada)
Um banco de dados de alto volume e transações rápidas (OLTP) de um Tribunal alcançou a Terceira Forma Normal e está modelado impecavelmente em tabelas estritas e altamente granulares. Contudo, devido a um vazamento de memória do servidor virtual, o DBA precisa garantir que todas as transações ACID do Tribunal envolvendo dados críticos tenham garantias absolutas contra panes elétricas no meio de uma gravação (COMMIT). O pilar do padrão ACID focado especificamente em assegurar que, após a transação ser concretizada no sistema, os dados persistirão de forma não volátil mesmo em caso de perda abrupta de energia ou incêndio no Data Center, é o pilar da:
A) Atomicidade (Atomicity).
B) Consistência (Consistency).
C) Isolamento (Isolation).
D) Durabilidade (Durability).
E) Agilidade Transacional (Agility).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. No ACID, D = Durabilidade. Ela garante tecnicamente (geralmente gravando os WAL logs no disco físico) que assim que o banco de dados confirma 'Transação Finalizada', ela está cimentada e não vai sumir se alguém puxar o fio da tomada no milissegundo seguinte.
</details>

## 📝 TEMA 2: Cloud Computing (AWS) e Virtualização de SO/Containers

### Questão 16 (FCC - Questão Prática / Adaptada)
O Arquiteto de Nuvem do Tribunal Eleitoral foi designado para criar uma infraestrutura altamente resiliente na AWS que garantisse o funcionamento do sistema de totalização de votos (monolítico no EC2) mesmo que um desastre natural ou corte de energia destruísse completamente um Data Center inteiro da região sudeste da AWS. Para garantir que o sistema não saia do ar se um prédio de data center inteiro ruir, o arquiteto deve projetar o Load Balancer roteando ativamente o tráfego de servidores EC2 espalhados por:
A) Múltiplas Contas da AWS da mesma agência.
B) Múltiplos Buckets do S3 configurados para armazenamento magnético de alta latência local.
C) Múltiplas Regiões da AWS isoladas e alocadas no formato Serverless.
D) Uma única Zona de Disponibilidade (AZ), desde que conte com proteção de Edge Computing local.
E) Múltiplas Zonas de Disponibilidade (Availability Zones - AZs) espalhadas dentro de uma mesma Região local.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**

- E) Correta. A AWS é dividida em Regiões geográficas globais. Cada Região (Ex: sa-east-1) é composta por múltiplas Zonas de Disponibilidade (AZs). Cada AZ é, de fato, um grupo de 1 ou mais prédios físicos de data centers isolados entre si contra enchentes, quedas de energia e desastres. Dividir entre AZs é a chave clássica da resiliência local.
</details>

### Questão 17 (FCC - Questão Prática / Adaptada)
Um órgão governamental de saúde executa o processamento pesado de arquivos .CSV todas as madrugadas usando instâncias na nuvem da AWS. O detalhe crucial desse negócio é que os scripts não têm pressa de começar e podem ser desligados repentinamente no meio da execução pela Amazon e reiniciados na próxima hora sem nenhum prejuízo ao negócio final. Sob a ótica restrita da extrema redução de OPEX, a AWS oferece um modelo computacional que aluga frotas ociosas com descontos agressivos de até 90% para esse tipo de carga de trabalho altamente flexível a interrupções. Esse modelo é conhecido como:
A) Amazon RDS Reservado Integral (Reserved All-Upfront).
B) Servidor EC2 Dedicado Exclusivo (Dedicated Host).
C) Instâncias Spot (Spot Instances).
D) Contêiner Fargate Escalonado Horizontalmente (Fargate Out).
E) Instâncias EC2 On-Demand de Tarifação Lenta Fixada (On-Demand Flat Rate).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Instâncias Spot (Instâncias de Spot) utilizam o poder ocioso que sobra nos datacenters da AWS. Como 'ninguém' está usando, a AWS aluga por migalhas. A 'pegadinha' ou risco é que, se alguém pagar mais ou a AWS precisar do servidor, ela mata a sua instância com um aviso de apenas 2 minutos.
</details>

### Questão 18 (FCC - Questão Prática / Adaptada)
O analista de infraestrutura explicou à equipe que, diferentemente das máquinas virtuais antigas (como VMware ESXi) que emulam o hardware por completo, a tecnologia Docker do projeto utiliza apenas os recursos do Kernel do Linux da máquina original de forma direta e ágil. Dentre as estruturas físicas de controle do Linux, qual tecnologia profunda e nativa de Kernel é responsável isoladamente por delimitar, cobrar e fatiar fisicamente a quantidade de hardware (ex: Máximo de 2GB de Memória RAM ou máximo de uso de ciclos da CPU) que um container Docker em específico do tribunal pode devorar?
A) cgroups (Control Groups).
B) Namespaces (Mount / PID Namespace).
C) Sistema Operacional Hospedeiro Gráfico.
D) Módulos DLLs injetados assincronamente pelo bash.
E) Sub-redes Lógicas Locais Internas em Overlay e NAT.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- A) Correta. A diferença clássica entre as duas bases de containers é: Namespaces lidam com ISOLAMENTO VISUAL lógico (para que o container só veja os processos e arquivos dele mesmo); e cgroups lidam com ISOLAMENTO DE HARDWARE FÍSICO (limitando a CPU, memória RAM e disco que ele pode comer).
</details>

### Questão 19 (FCC - Questão Prática / Adaptada)
A Diretoria do Tribunal necessita de um sistema relacional robusto e altamente monitorado na AWS sem depender de um administrador de banco de dados (DBA) provisionando patches e configurando RAID de disco em instâncias virtuais cruas na unha. O serviço de banco de dados nativo de arquitetura PaaS focado primariamente em gerenciar a instalação e a sustentação de SGBDs estritamente Relacionais conhecidos do mercado (como PostgreSQL, Oracle e MySQL) é o:
A) Amazon DynamoDB.
B) AWS Elastic Beanstalk (EB).
C) Amazon RDS (Relational Database Service).
D) Amazon S3 Storage Class.
E) Amazon EBS (Elastic Block Store) atrelado diretamente às pastas var/log.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Amazon RDS (Relational Database Service) é o carro-chefe de relacional gerenciado na AWS. Você foca nos queries, ele cuida dos patches de sistema operacional, dos backups automáticos cruciais, do RAID e do failover automático (Multi-AZ).
</details>

### Questão 20 (FCC - Questão Prática / Adaptada)
Ao arquivar registros confidenciais e imutáveis da sindicância oficial nos buckets do Amazon S3, um oficial de segurança do Tribunal observou que há o risco legal severo de um analista sênior da própria base apagar ou subscrever os logs de auditoria deliberadamente por má fé, já que o analista possui permissões nativas de superusuário na AWS. Para impedir ativamente alterações nesses objetos gravados, garantindo a proteção WORM (Write Once, Read Many) pelo tempo exigido em lei, deve-se aplicar nos objetos isolados a configuração protetiva denominada:
A) S3 Transfer Acceleration Global Fixo.
B) Amazon EC2 Security Group de Saída Focada.
C) S3 Object Lock (Bloqueio de Objeto).
D) S3 Versionamento Cruzado com Redirecionamento Assíncrono.
E) AWS IAM Policy baseada puramente na negação provisória do grupo restrito.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. O S3 Object Lock atua de modo físico/legal WORM ('Grave Uma Vez, Leia Muitas'). Uma vez configurado o período do bloqueio (ex: 5 anos de congelamento), nem mesmo o superusuário root dono principal da conta AWS consegue excluir ou subscrever o arquivo. Ele previne perfeitamente atos de exclusão criminosos ou ataques graves de exclusão de ransomwares de extorsão contra backups em nuvem.
</details>

### Questão 21 (FCC - Questão Prática / Adaptada)
A Diretoria deseja adotar a nuvem, porém, por limitações de confidencialidade governamental da nova base militar de apoio tático ligada ao Tribunal, é forçoso legalmente que toda a infraestrutura física virtualizada (os roteadores virtuais, os racks de servidores de dados processuais e os storages unificados) pertença restritamente de modo local a um único cluster gerenciado por um provedor interno fechado apenas na rede intranet física e isolada do país, sem o compartilhamento do aluguel físico com outras empresas civis (Multitenancy fora do ar). Trata-se do clássico e exato modelo acadêmico de implantação em nuvem de:
A) Nuvem Pública de Terceiros Alocada.
B) Nuvem Serverless Híbrida de Borda (Edge).
C) Nuvem Privada (Private Cloud) Física Dedicada Local.
D) Nuvem de Alta Elasticidade Interconectada Global Fechada.
E) SaaS Intermediado via Provedores em Malha de Redes Públicas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. No paradigma e nas documentações do NIST, a infraestrutura mantida, operada local ou alocada apenas e restritamente de modo privado local interno a uma única corporação no isolamento corporativo total focado sem uso do modo Multitenant (isolada do acesso de outros clientes na mesma máquina) é o modelo básico de Private Cloud (Nuvem Privada).
</details>

### Questão 22 (FCC - Questão Prática / Adaptada)
Um desenvolvedor escreveu uma pequena e ágil função em Python que emite um comprovante em PDF e o anexa em um e-mail para advogados em cada finalização local e manual de processos, gerando pequenos espasmos mensais eventuais e esparsos de tempo computacional (menos de 3 segundos esporádicos por evento processual). Qual é o serviço exato do paradigma arquitetural Serverless (Sem servidor) dentro do ecossistema Amazon AWS que foca eminentemente na execução dessa função reativa à ocorrência temporal impulsionada de eventos (FaaS)?
A) Amazon Virtual Private Cloud (VPC).
B) AWS Elastic Beanstalk C++ Core Integrator.
C) AWS Lambda.
D) Amazon RDS PostgreSQL Base Isolada.
E) Amazon EBS Snapshots Regulares Nativos Lógicos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. O AWS Lambda é a pura expressão comercial global do Serverless de Função FaaS. O desenvolvedor escreve a pequena rotina, manda pro Lambda e esquece o servidor, o sistema operacional ou as atualizações. Quando ocorre o evento, a AWS carrega, roda em 30 milissegundos e cobra só os 30 milissegundos pontuais do tribunal, morrendo a rotina em seguida.
</details>

### Questão 23 (FCC - Questão Prática / Adaptada)
Para escalar sua rede interna massiva de computação local para o estado total do Ceará conectando servidores robustos baseados num datacenter físico On-Premise, a coordenação de TI avaliou que o Hypervisor virtualizador de base a ser instalado debaixo dos sistemas operacionais e das aplicações dos tribunais precisava rodar sem o lastro pesado de um Sistema Operacional nativo tradicional completo (como Windows 11 base ou um Ubuntu pré-instalado clássico hospedado em tela). O Hypervisor precisava ser inserido de modo nu e cru nos equipamentos físicos (hardware metálico) recém adquiridos para o data center local. Esse tipo de técnica e estrutura nativa caracteriza fidedignamente os classificados academicamente Hypervisors virtuais do Tipo:
A) Tipo 2 (Hosted Hypervisor Local), devido ao acoplamento orgânico aos firmwares virtuais do banco SQL relacional fechado localmente na base restritiva.
B) Tipo 1 (Bare-Metal), onde o próprio hypervisor funciona intimamente e de modo primário como um pequeno sistema operacional super eficiente instalado em cima cru e colado ao hardware nédio principal sem intermediários lentos operacionais de tela.
C) Tipo FaaS, limitando isoladamente os ciclos do barramento TCP e executando lógicas e regras isoladas eventuais em memórias e roteadores USB secundários nativos.
D) Tipo 3 (Emulação Gráfica Pesada de Jogos de Borda), usado unicamente por virtualizadores abertos nativos como o VMware Player 10 Básico gratuito no país e focado no uso doméstico lúdico temporário e simples visual.
E) Tipo Docker/Contêiner Restrito Nativo de Hardware, em razão dos módulos visuais de acoplamento do Kernel físico da máquina de estado binária global e contínua.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. A diferença de base em arquitetura na virtualização e nuvem On-premise local é simples: O Tipo 1 (Bare-metal) se encarrega direto de encostar no hardware real da máquina. São os gigantes dos datacenters como VMware ESXi ou Microsoft Hyper-V. O Tipo 2 são programas hospedeiros simples rodados por você na tela visual básica instalada previamente na base Windows (Ex: VirtualBox).
</details>

### Questão 24 (FCC - Questão Prática / Adaptada)
Para empacotar todos os arquivos do site oficial antigo local em C# e o sistema interno de relatórios Java em unidades restritas portáveis visuais de contêiner e orquestrá-los simultaneamente (Subir os 2 blocos de contêiner juntos em desenvolvimento de código), o desenvolvedor instruiu uma ferramenta clássica oficial do Docker focado eminentemente em unir comandos no diretório em modo CLI. Qual a tecnologia padrão para rodar multi-containers orquestrados localmente na máquina desktop do desenvolvedor baseada na extensão declarativa de um modelo em texto limpo do tipo YAML oficial descritivo nativo base?
A) Kubernetes API Server Deployment File Unificado Lógico Dinâmico.
B) Script Base Nativo de BASH Shell de Linux puro e limpo restrito no ambiente.
C) Dockerfile Simples e Padrão Isolado da Rede Local Virtual.
D) Package.json Global Base Dinâmico Exclusivo Interno Isolado do Servidor Nginx.
E) Ferramenta nativa clássica local Docker Compose e o descritivo associado arquivo docker-compose.yml nativos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**

- E) Correta. O Dockerfile (C) só levanta 1 imagem isolada simples construtiva física na máquina base. Para orquestrar, configurar redes unificadas isoladas e gerenciar ao mesmo tempo vários contêineres interligados no teste do analista local (ex: rodar um Redis junto de um Node e do Banco Postgres todos unidos magicamente) na mesma máquina isolada local do desenvolvedor, usa-se o oficial utilitário ágil 'Docker Compose'.
</details>

### Questão 25 (FCC - Questão Prática / Adaptada)
Em um cenário hipotético em que a plataforma digital AWS da corte regional seja invadida, constatou-se que o invasor adquiriu os arquivos confidenciais alocados dentro de uma das VMs abertas alugadas no formato IaaS e instalou ransomwares que exploraram falhas não corrigidas pelos técnicos do estado nas bibliotecas abertas do sistema Ubuntu Linux 18.04 da máquina virtual em funcionamento interno. Sobre a lógica de segurança inerente à base teórica formal do documento oficial AWS, conhecido como 'Modelo de Responsabilidade Compartilhada', cabe atestar legalmente quem detém a obrigação direta de corrigir essas citadas brechas do sistema operacional Ubuntu em nuvem:
A) É obrigação final direta e estrita base central contratual puramente unificada do Provedor AWS, garantindo todo e qualquer ambiente remoto blindado nativamente na sua camada lógica independente de uso interno regional judicial alugado pela equipe técnica de TI local.
B) Fica de forma equânime dividida local e presencialmente em taxas físicas cobráveis e mensuráveis mensais baseadas num fundo comum logístico global entre as redes estáticas das 2 corporações envolvidas isoladas.
C) A obrigação final de gestão e reparo local lógico do próprio SO restringe-se e cabe à gestão do Tribunal Cliente Estadual Judicial, uma vez que o AWS assegura apenas e centralmente a segurança 'DA' Nuvem (Datacenters de base física, os roteadores da base física original global isolada e do maquinário estático hipervisor subjacente restritivo), mas não 'NA' nuvem em modelos fechados puramente IaaS lógicos abstratos de software básico interno emulados pelo usuário de máquina virtual virtualizado global aberto.
D) O provedor externo de auditoria internacional judicial central da justiça penal estadunidense e do governo nacional associado federal.
E) O AWS isoladamente se a infraestrutura for orientada remotamente a base contínua em modelo de plataforma SaaS estrito nativo das instâncias fechadas de código local sem isolamentos virtuais base e sem acesso irrestrito do SO logado na base.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. A AWS e os concorrentes globais usam a Responsabilidade Compartilhada base clássica de regras lógicas. A Amazon garante unicamente e fechado os data centers, resfriamento físico e os Hypervisores pesados ('Segurança DA nuvem física base central'). O tribunal de trabalho / cliente, ao rodar uma VM EC2 padrão em modelo de base IaaS (Security IN the cloud), tem obrigatoriamente a gerência completa em instalar atualizações de SO Linux local, antivírus lógicos fechados, configurar porta aberta SSH remota global restritiva nativa unificada presencial de forma prudencial unificada.
</details>

### Questão 26 (FCC - Questão Prática / Adaptada)
Qual é a tecnologia subjacente e basilar nativa empregada ativamente pelos orquestradores em rede aberta moderna, a exemplo lógico claro oficial das máquinas do Kubernetes unificadas, capaz de conceder magicamente e nativamente aos containers fisicamente e ativamente descentralizados em dezenas de servidores físicos heterogêneos ruidosos de empresas regionais distintas, uma abstração única global de conversarem unificados nativamente na rede fechada sem se preocuparem remotamente se o servidor número B se localiza em um prédio vizinho da empresa matriz restritiva regional isolada?
A) Redes exclusivas de Fibra Óptica locais em Topologia anel e central fechada puramente de Token Ring isolado centralizado e arcaico da base física restrita estrita nativa e sem uso de virtualização temporal assíncrona remota global unificada nas camadas de base do SO Lógico nativo da AWS isolado.
B) Comutadores (Switches) Baseados na norma Token Ethernet 802.1B estritamente alocados fisicamente nos Datacenters privados de nuvens híbridas globais locais.
C) Sistema de Rede e Comunicações de Topologia e NAT estrito simples em VPN via Firewall L7 Restrito da Plataforma local da borda fechada de Rede.
D) Redes baseadas na tecnologia de Sobreposição local isolada unificada digital (Overlay Networks), operantes através e por cima unicamente isolado dos pacotes reais do IP hospedeiro encapsulados de forma unificada lógica restrita.
E) Enlaces diretos abertos e limpos não roteáveis unificados isolados unicamente do protocolo NAT reverso e contínuo da base regional IPv4 de sub-rede.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. O milagre de orquestração de rede do Docker Swarm ou Kubernetes é criar as redes Overlays (Sobreposição fechada abstrata). Os containers pensam unificadamente e magicamente que conversam em um único grande switch invisível no mesmo datacenter na mesma sub-rede fechada isolada, sendo que fisicamente as máquinas base host estão distribuídas aleatoriamente. Ele empacota na base física subjacente pacotes de rede virtuais limpos abertos em pacotes reais para passar de forma invisível nos roteadores normais fechados nativos contínuos do datacenter oficial restrito regional.
</details>

### Questão 27 (FCC - Questão Prática / Adaptada)
O volume principal atrelado cru ao EC2 rodando o servidor PostgreSQL fechado regional precisa funcionar de modo clássico local com formatação ext4 isolada em discos virtuais independentes físicos puros regionais de bloco na região leste norte americana contínua sem formatação atrelada de arquivos abertos simples não baseados em buckets abstratos restritivos abertos contínuos no S3 focado local estrito de rede externa fechado contínua global base unificada relacional externa isolada virtualizada temporariamente e atrelado com os sistemas base de base rígida estrutural oficial. O nome descritivo básico deste tipo de serviço lógico de hardware local base isolada anexado de modo físico direto aberto é nomeado na AWS como:
A) Amazon RDS Base Remota Restritiva Local Lógica Fria.
B) Amazon Simple Storage Global Unificado Fixo Virtual (S3).
C) Amazon EFS Dinâmico Estrutural Base Assíncrona Fixada Global Aberta em Rede DFS Limitada Virtual Unificada Remota Assíncrona (EFS).
D) Amazon Elastic Block Store Unificado Local Central Rígido de Bloco Simples Clássico Contínuo e Direto Limitado (EBS).
E) Amazon CloudFront Regional Direto Lógico de CDN Aberto Restrito de Fronteira Virtual e Aberta Fixa Contínua Isolada Externa Regional Base Unificada Estrutural e Temporal Remoto (CDN).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. O Amazon Elastic Block Store (EBS) funciona exatamente de modo unificado puro como se fosse um Disco Rígido clássico vazio e independente (HD ou SDD alocado físico isolado em bloco na placa principal da rede unificada do host hypervisor EC2 isolado remota regional base). Diferentemente nativamente isolado de buckets (como a rede unificada global contínua abstrata do objeto S3), ele é puramente de bloco cru para colocar sistema unificado local de rede de partição formatada do sistema Linux.
</details>

### Questão 28 (FCC - Questão Prática / Adaptada)
Um banco na base lógica do tribunal estadual, visando estabilidade no tráfego, atrelou e acionou regras avançadas operativas baseadas no princípio técnico puramente funcional da rede de 'Auto Scaling Horizontal' oficial remoto AWS. O princípio teórico primário da ferramenta de serviço escalonado e monitoramento unificado regional base no AWS Auto Scaling age de maneira contínua unificada e independente regional operando reativamente e proativamente em prol da justiça para estritamente:
A) Escalar a frequência isolada de relógio base primária CPU dos servidores On-Demand unificados na própria placa do rack físico subjacente remoto base virtual sem aumento do banco base isolado central nativo (Vertical Up).
B) Adicionar (lancar / boot out) ou Retirar dinamicamente e automaticamente sob comando das métricas estritas os clones de Instâncias inteiras virtuais extras contínuas da base lógica por detrás e ocultas no Load Balancer base oficial local do tribunal ajustando perfeitamente estrito à demanda mutável da hora estrita contínua sem limites operacionais de recursos.
C) Clonar os roteadores físicos isolados unicamente do DNS no formato reverso BGP central contínuo virtual oficial da borda remota externa e distribuída unificada isolada global temporal.
D) Incrementar apenas a memória cache virtual estática do banco Amazon Redshift na base contínua de memória e no disco externo rígido base local virtual contínuo relacional oficial virtual local temporal fixo e central (Scale Vert).
E) Adicionar servidores SQL unificados lógicos relacionais contínuos temporários nas redes de borda global contínua do CloudFront CDN aberto isolado virtual contínua remota regional de bases temporárias (CDN Scale Base).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Auto Scaling (Auto Escalamento Horizontal puro base do Cloud-native oficial) lida de fato com a inserção e acoplamento contínuo virtual nativo ou fechamento de novos CLONES idênticos de instâncias lógicas virtuais inteiras de máquinas alocadas atrás atreladas do distribuidor contínuo de recursos balanceador contínuo virtual e oficial local (Load balancer local) seguindo de modo exato as métricas puras abertas unificadas isoladas e as necessidades pontuais do tráfego web. Esse modelo nativo atende contínua picos e corta gastos em baixas unificadas isoladas no sistema.
</details>

### Questão 29 (FCC - Questão Prática / Adaptada)
Na modelagem corporativa de acessos seguros, as credenciais e o papel estrito operacional oficial lógico base da plataforma AWS em que se foca eminentemente na autorização técnica baseada na criação rigorosa de grupos de acesso contínuo interno base, na validação unificada do modelo restritivo Múltiplo Fator e também em alocar as políticas rígidas granulares internas restritivas abstratas ('Policy') de leitura contínua e restrição ou negação remota baseada base de quem pode criar e quem deve apagar dados contínuos isolados remotos nativos unificados na nuvem sem acessar atrelamentos unificados oficiais isolados físicos nativos do tribunal corporativo fechado de forma nativa regional restrita isolada é gerido de forma integrada base global isolado na camada de segurança unificada de produto e recurso global AWS estritamente atrelado denominado tecnicamente base do(a):
A) Amazon RDS Base Isolada Lógica Fria.
B) Identity and Access Management Base Dinâmico Estrutural Base Assíncrona Fixada Global Aberta em Rede Regional Oficial Lógica Contínua Virtual Limitada Base Unificada IAM (AWS IAM).
C) Route 53 e Proxy Externo Lógico Base DNS Limitado Virtual Unificada Remota Assíncrona.
D) AWS Shield Global Central e Avançado Nativo Base Unificada Fechada Estrutural Firewall WAF.
E) Amazon CloudTrail Virtual Log Base Auditoria Isolada Lógica Virtual Auditoria Central.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. A IAM (Gerenciamento restrito unificado oficial de Identidade e Controle unificado contínuo remoto regional Acesso de Base Global Contínua Isolada) é o centro neural oficial aberto de proteção de autenticação. É lá na IAM que a regra local abstrata diz se o 'Analista Silva' atrelado de forma nativa isolada pode ler no bucket base de S3, mas não deletar tabelas relacionais contínuas unificadas de VMs lógicas do DynamoDB remota unificada ou na base remota global unificada oficial local regional.
</details>

### Questão 30 (FCC - Questão Prática / Adaptada)
Um cenário na arquitetura base e oficial governamental contínua de um sistema base de banco relacional e unificado central contínuo virtual oficial de Justiça determina expressamente que todas e únicas requisições pesadas em SQL contínuo virtual unificado oficial e base lógico unificado local e centralizado complexas voltadas especificamente ao uso contínuo puro da diretoria do Business Intelligence (Consultas OLAP Analíticas Extensas Unificadas Virtuais de Longa base Unificadas Oficiais) e aos painéis de painéis base unificados visuais estáticos, ocorram inteiramente fora do ambiente transacional principal virtual onde atuam juízes e processos nativos. Qual é o recurso oficial de base oficial isolada relacional AWS aplicável unicamente nos provedores relacionais Amazon RDS focado diretamente no alívio desse tipo estrito de carga na nuvem base oficial e regional de forma inteligente contínua?
A) Auto Scaling Híbrido Contínuo Externo Reduzido Base.
B) Réplicas Locais Unificadas Secundárias Oficiais Restritas Limitadas de Resiliência Isolada Lógica Virtual Básica.
C) Read Replicas ou Clones Regionais Abertos Unificados Nativos e Funcionais Limpos de Leitura Direcionados.
D) Multi-AZ Clusters Abstratos Virtuais Temporais Standby Nativo de Escrita Múltipla Lógica Paralela Isolada Regional.
E) Caches Abstratos Isolados Nativos e Relacionais em MongoDB Virtual Unificado Contínuo Sem Banco e sem base lógica.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Read Replicas (Instâncias oficiais exclusivas Unificadas Contínuas de pura Leitura Oficial e Assíncrona Regional Unificada Contínua Oficial) do provedor RDS têm por finalidade pura desafogar o mestre central transacional (a carga local unificada base e isolada nativa base e primária oficial e virtual contínua que processa todas as Gravações pesadas base contínua regionais). Desse modo natural abstrato e isolado local, você redireciona base unificada analítica relacional toda a horda centralizada local massiva global e lógica das complexas buscas relacionais dos analistas unificados contínuos de relatórios para as bases cópias oficiais de bases nativas (as puras réplicas virtuais limpas base unificada estritamente atrelada e alocada abstrata de relatório isolado oficial base unificada unicamente de leitoras).
</details>

## 📝 TEMA 3: Eng. de Software: APIs RESTful, Swagger, Paginação e JSON

### Questão 31 (FCC - Questão Prática / Adaptada)
Um Desenvolvedor Pleno do Tribunal desenhou a rota HTTP `POST /processos/123/arquivar` para mudar o status de um processo existente no banco de dados para a condição arquivada. Segundo os princípios arquiteturais rigorosos e semânticos do padrão REST (Representational State Transfer) definidos por Roy Fielding e aplicados ao desenvolvimento web contemporâneo, a modelagem dessa rota HTTP:
A) Está perfeita, pois o verbo POST é historicamente e restritamente obrigatório para alterar qualquer metadado que já exista de modo interno e persistido ativamente no servidor web lógico da base de controle estrito unificado RESTful em qualquer ocasião.
B) Fere a semântica RESTful, pois endpoints devem expor substantivos (os recursos) e não verbos de ação no próprio caminho da URL. O correto seria acessar o recurso `/processos/123` utilizando verbos HTTP apropriados para modificação (como PATCH ou PUT).
C) Atende ao nível máximo (Glory of REST) do Modelo de Maturidade de Richardson, já que a presença do verbo arquivar assegura a navegação nativa Hypermedia de base semântica livre HATEOAS estrita de transição local de status independente HTTP no sistema digital web.
D) Fere os requisitos de segurança da Camada 4 do modelo OSI, uma vez que requisições tipo POST expõem todos os dados da rota no log unificado de criptografia global SSL/TLS sem restrição base visual lógica remota unificada externa no log visual local.
E) Está correta e alinhada às melhores práticas, desde que o corpo da requisição POST esteja absolutamente vazio, servindo como sinalizador neutro estrito do comando base unificado isolado ao backend da base oficial judicial lógica temporal de estado de execução síncrona virtual estática.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Em REST, URIs não devem conter ações (verbos). A URI identifica o *Recurso* (um substantivo). A Ação é determinada pelo verbo HTTP (GET, POST, PUT, DELETE, PATCH). Uma rota como `/arquivar` foge do padrão. O ideal seria enviar um PATCH para `/processos/123` com o corpo `{"status": "arquivado"}`.
</details>

### Questão 32 (FCC - Questão Prática / Adaptada)
Uma API pública do TRT sofre intermitência na conexão (Timeout) porque a base de jurisprudência processual é massiva, contendo milhões de linhas. A equipe técnica optou por não utilizar o deslocamento clássico (Offset-based Pagination) `LIMIT 50 OFFSET 10000` em suas listagens virtuais via REST, optando ativamente pela implementação acadêmica da Paginação Baseada em Cursor (Cursor-based ou Keyset Pagination). O trunfo fundamental gerado por essa troca arquitetônica e temporal de consulta reflete-se na/no:
A) Eliminação forçada da exigência de se utilizar o formato JSON de comunicação unificada abstrata contínua base da API pública remota isolada lógica virtual nativa base de REST.
B) Carga de processamento pesada e exponencial nas páginas finais (Ex: Página 10.000) de base temporal estática que inviabiliza as buscas virtuais de índices.
C) Alto ganho de performance e escalabilidade estrutural da tabela relacional em bases enormes, uma vez que a paginação por cursor passa o valor da última linha lida e faz com que o banco pule dezenas de milhares de registros velozmente através de índices nativos, em vez de exigir a leitura ineficiente estrita sequencial e descarte de linhas executada pelo velho `OFFSET` unificado isolado de busca cega contínua SQL.
D) Prevenção autônoma contra a inserção maliciosa oculta de vírus SQL injetados nas variáveis ocultas restritas base unificadas virtuais lógicas remota oficiais locais temporais da web estrita fechada regional remota nacional.
E) Encriptação orgânica contínua de fluxo abstrato lógica regional do corpo principal estrito HTTPS atrelado globalmente de modo automático sem o uso certificado do OpenSSL.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. A paginação OFFSET diz ao banco: 'Leia 10.000 linhas, descarte-as e me dê as próximas 50'. Isso mata a CPU em tabelas grandes. Na paginação Keyset (Cursor), você usa o ID da última linha (ex: `WHERE ID > 980 LIMIT 50`). O banco usa o Índice B-Tree para pular instantaneamente pro ID 980 sem ler os anteriores, gerando uma busca ultrarrápida (O(log n)) que nunca sofre lentidão, independentemente da página em que você esteja.
</details>

### Questão 33 (FCC - Questão Prática / Adaptada)
No tocante ao uso avançado do OpenAPI Specification (anteriormente concebido como projeto Swagger) para o registro contratual digital contínuo virtual das pontes de comunicação lógica externa da plataforma REST do Tribunal de Justiça Eleitoral com as varas locais. Ao desenhar o contrato API, o uso restrito estrutural e nativo do OpenAPI versão 3.0 provê primariamente a capacidade de:
A) Omitir a obrigatoriedade lógica de segurança, garantindo autenticações fáceis abertas externas remotas não seguras baseadas no padrão SOAP legado base de dados restrito regional e unificado.
B) Criar exclusivamente modelos front-end interativos para designers UX nativos regionais de software mobile do Tribunal de Justiça sem acesso a código-fonte back-end de bancos paralelos e limitados em escala lógica aberta relacional externa.
C) Descrever de maneira padronizada em YAML ou JSON o contrato de interface exato (endpoints, métodos, parâmetros, schemas de corpo, tipos de resposta e segurança) para que tanto humanos entendam a documentação visual como máquinas consigam gerar código cliente/servidor base automáticos e automatizar os testes.
D) Criptografar magicamente todas as bases relacionais unificadas MySQL virtuais limpas sem atuar como interface restrita local de rede corporativa VPN global local abstrata temporal remota contínua física do usuário web de rede externa base fechada lógica isolada regional temporal da Justiça nacional remota.
E) Limitar severamente o uso contínuo de JSON na base e forçar puramente o XML em todos os tráfegos restritos nativos da internet local do órgão estatal nacional base de segurança abstrata emulada lógicos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. O OpenAPI (Swagger) é uma linguagem padrão em YAML/JSON para descrever 'O que essa API faz, o que entra e o que sai'. Esse formato padronizado permite que ferramentas leiam e gerem a bela página de documentação (Swagger UI), gerem código inicial para o programador (Codegen) ou gerem testes automáticos de segurança e integração.
</details>

### Questão 34 (FCC - Questão Prática / Adaptada)
O analista da integração judiciária formatou um arquivo de carga no formato texto padrão da notação oficial JSON. De acordo com a RFC 8259 que especifica tecnicamente o JSON nativo (JavaScript Object Notation), assinale a formatação correta de declaração textual válida em código para a representação universal oficial limpa e restritiva de um objeto neste modelo base digital estrutural lógico contínuo global para a web:
A) {'nome': 'Silva', 'idade': 40}
B) {"nome": "Silva", "idade": 40}
C) {nome: "Silva", idade: 40}
D) <json><nome>Silva</nome><idade>40</idade></json>
E) ["nome" => "Silva", "idade" => 40]

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Apesar de JavaScript ser flexível, o JSON possui regras rígidas estritas: Toda chave (nome da propriedade) TEM que estar cercada por aspas duplas (""). Valores do tipo string também exigem aspas duplas. Aspas simples (') não são válidas na especificação oficial do JSON. O formato A, C e E estão errados.
</details>

### Questão 35 (FCC - Questão Prática / Adaptada)
Uma das prerrogativas da arquitetura web baseada nos níveis mais estritos arquiteturais estabelecidos de Roy Fielding é atingir o nível 3 (Level 3) do tradicional Modelo de Maturidade de Richardson. Na aplicação prática de programação do desenvolvedor de APIs, esse degrau de maturidade de pico restrito base web alcançado na comunicação lógica local nativa abstrata de integração externa foca em:
A) Assegurar a criação restrita e exclusiva de comunicação web no padrão SOAP unificado e central corporativo regional fechado na camada RPC estrito nativo com SSL base.
B) Focar no uso único do verbo POST estrito emulando todos os demais na chamada local fechada regional em um único endpoint restrito `/api/v1/geral`.
C) Prover controles de Hipermídia (HATEOAS). A API, além de devolver o JSON contendo os dados brutos requeridos do recurso em si, também passa a enviar, de forma atrelada e anexada no corpo, múltiplos Links (URLs lógicos dinâmicos) orientando e descrevendo autonomamente os próximos estados e as próximas ações possíveis que o cliente pode realizar na aplicação a partir de agora sem consultar manuais fechados temporais.
D) Iniciar processos assíncronos base e contínuos globais rodando o Kafka restritivo interno temporal unificado contínuo da rede fechada.
E) Exigir que a autenticação passe de local estática para regional LDAP isolada virtual da VPN estrita corporativa nativa na sub-rede remota federal nacional unificada oficial emulada fechada básica isolada virtual lógica.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. O Modelo de Maturidade de Richardson tem passos (0, 1, 2, 3). O Nível 3 (Glory of REST) é caracterizado pelo uso prático da Hipermídia (HATEOAS). Em suma, a API não apenas envia os dados (ex: Nome do Paciente e ID), mas também envia no JSON uma lista de URLs que mostram o que o sistema cliente pode fazer a seguir com aquele recurso (ex: o link exato gerado para cancelar a consulta, ou o link atual para aprovar a alta no hospital). Isso gera total auto-descobrimento e reduz o acoplamento do sistema cliente.
</details>

### Questão 36 (FCC - Questão Prática / Adaptada)
O princípio fundamental de 'Idempotência' deve guiar o desenvolvimento do engenheiro na adoção do padrão REST e a escolha inteligente dos verbos nativos HTTP. Ao criar uma lógica de gravação e envio estrito virtual, qual dos métodos (verbos) listados abaixo não possui a garantia teórica nativa semântica oficial da idempotência, ou seja, submeter dez vezes idênticas e sucessivas essa mesma requisição web de base gerará, muitas vezes como efeito natural base lógico do servidor, a duplicação ou o processamento multiplicador contínuo de registros e eventos em vez de produzir invariavelmente e apenas o mesmo resultado exato único local após a primeira vez de envio?
A) PUT
B) DELETE
C) GET
D) POST
E) HEAD

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. O verbo POST em REST e no HTTP não é idempotente. Em suma, enviar dez vezes o POST de um formulário de novo usuário fatalmente e naturalmente criará (se o banco não possuir uma Constraint Unique na modelagem da placa do carro ou do e-mail) 10 novos usuários idênticos acumulados (ou fará 10 transferências financeiras somadas cumulativas iguais seguidas na conta, o que é desastroso). GET, PUT, PATCH e DELETE já são semanticamente (e devem ser implementados na base) de modo idempotente. Por exemplo: Enviar dez comandos PUT dizendo 'Mude a cor da placa do servidor para VERDE', mesmo chegando mil vezes seguidas, o resultado final prático isolado do servidor será sempre que a placa do veículo se encontra VERDE. Ocorreu zero multiplicação cumulativa desastrosa temporal no campo unificado final.
</details>

### Questão 37 (FCC - Questão Prática / Adaptada)
Se um Analista de Tribunal necessita e deseja informar explicitamente que o cliente móvel e a sua plataforma da justiça são e estão tecnicamente capacitados para lidar internamente na leitura isolada visual e receber a resposta oficial no padrão base limpo unificado JSON, o analista instrui e programa que a requisição de rede (Request) feita via HTTP deva ser despachada do celular contendo especificamente atrelada e configurada o cabeçalho base de negociação de conteúdo remoto focado nominado formalmente:
A) Content-Disposition: attachment
B) Content-Type: application/json
C) Authorization: Basic JSON
D) Accept: application/json
E) Access-Control-Allow-Origin: json

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. O cabeçalho 'Accept' serve exatamente e incisivamente para realizar a famosa negociação digital HTTP base de 'Content Negotiation'. Com o cabeçalho 'Accept: application/json', o browser/celular 'diz' abertamente ao servidor judiciário do tribunal 'Eu quero e aceito receber a resposta nesse formato de código de base de dados restrito'. O Content-Type serve pra outra funcionalidade (Diz o que está sendo ENVIADO pelo cliente no payload local isolado corpo oficial da requisição POST).
</details>

### Questão 38 (FCC - Questão Prática / Adaptada)
Um Desenvolvedor Sênior da Corte Superior Eleitoral determinou na aprovação arquitetural do sistema judiciário que as alterações do contrato da API que causam quebra e incompatibilidade na vida dos consumidores (Exemplo claro básico isolado regional remoto: Renomear bruscamente a coluna local `cpf` vital na web externa nativa fechada para `codigo_identificador` oficial sem aviso abstrato regional anterior temporal nativo) sejam geridas adequadamente. A ferramenta padrão do design de APIs adotada pelo desenvolvedor para gerir mudanças violentas ao longo dos anos de uso contínuo de produção é:
A) Habilitar ofuscação nativa restrita de código no frontend Vue oficial restrito isolado virtual da borda de modo contínuo regional na base e compilar binários.
B) Versionamento da API (ex: criando roteamento base unificado restrito lógico virtual `/v1/` e `/v2/` em endpoints), mantendo-se a versão antiga viva e ligada rodando de forma estrita isolada até os parceiros externos da justiça conseguirem ajustar remotamente os programas para consumirem a versão nova oficial atual virtual.
C) Desativar forçosamente o tráfego regional no Firewall AWS Shield WAF e enviar circulares escritas abertas exigindo o download local estrito nacional nativo temporário isolado na intranet virtual da rede corporativa do executável regional fechado base lógico do órgão.
D) Realizar encriptação massiva SSL nativa nos JSON e mudar senhas na raiz nativa local da máquina em modo diário global abstrato virtual unificado nacional isolado presencial no país.
E) Atualizar a máquina para HTTPS versão 3 regional oficial globalmente restritiva em TLS isolado físico remoto e desatualizar nativamente os logs de controle.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. A maneira recomendada e clássica de lidar com as inevitáveis quebras de contrato (Breaking Changes) nas APIs é o Versionamento. Cria-se o endpoint `api/v2/`. Os clientes novos usam a `v2` modernizada (com os nomes de colunas novos). Os clientes antigos continuam batendo e sobrevivendo na rota `api/v1/` até se ajustarem (evitando assim apagões digitais estritos de milhões de acessos governamentais diários na madrugada da virada técnica).
</details>

### Questão 39 (FCC - Questão Prática / Adaptada)
Ao utilizar Swagger para documentar uma nova API de petições digitais do fórum cível central trabalhista, o desenvolvedor nota que as anotações visuais abstratas geraram uma bela página oficial unificada interativa. Dentre os recursos centrais valiosos de uso do OpenAPI integrados na rotina de base nativa, o sistema possibilita no dia a dia técnico que o QA da equipe possa:
A) Criptografar magicamente todo banco em SQL temporal nativo relacional globalmente.
B) Fazer requisições HTTP e testes exploratórios na página web ao vivo e reais na plataforma REST oficial clicando no botão ('Try it out' - Tentar/Executar Agora) disponível dentro e diretamente da própria página limpa da documentação dinâmica Swagger UI.
C) Subir máquinas virtuais Linux completas hospedadas num servidor IaaS remoto AWS base.
D) Gerenciar fisicamente roteadores da rede do Governo de forma autônoma nas sub-redes temporais limitadas fechadas isoladas virtuais remotamente na rede base local.
E) Adicionar memória RAM ao serviço de banco local relacional nativo PostgreSQL remoto global isolado unificado na nuvem central e fechada local base oficial do órgão de TI presencial base unificada oficial.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. O Swagger UI é amplamente adotado não apenas porque exibe a estrutura da API (documentação estática chata isolada), mas principalmente porque as páginas geradas pelo Swagger são ativas. A equipe, clicando e usando a página no navegador de forma manual local isolada virtual contínua na borda regional local do sistema remoto, pode preencher as informações virtuais exigidas abertas da API (colocar um JSON, um número) e clicar em enviar requisição, testando ativamente e imediatamente a própria interface da API real.
</details>

### Questão 40 (FCC - Questão Prática / Adaptada)
Um processo contínuo de modernização de relatórios do TST requer a extração de dados do endpoint oficial da API do Tribunal Regional do Ceará. A equipe decidiu implementar o PATCH ao invés do tradicional PUT restrito para a ação oficial contínua temporal de mudar apenas e exclusivamente a pequena variável virtual contínua 'Ativo' de falso para verdadeiro (boolean), sem alterar os demais 50 campos cadastrais brutos preenchidos estáticos da base. A adoção técnica restritiva puramente intencional regional desse verbo HTTP base oficial específico obedeceu rigorosamente ao fundamento purista de arquitetura e lógica formal da REST no qual:
A) O PATCH elimina completamente qualquer registro físico oficial da máquina abstrata virtual oficial do usuário temporal na AWS regional isolada local fechada e externa e lógica oficial.
B) O PATCH não faz transações abertas e não criptografa nativamente no formato AES contínuo temporal unificado do Oracle remoto da corte de base unificada e estritamente nativa virtual oficial lógica local e externa da rede.
C) O PATCH, diferentemente do PUT puro, é formalmente e filosoficamente dedicado de modo exato às modificações ou alterações parciais abstratas contínuas cirúrgicas ('remendos' isolados em uma parcela do objeto sem forçar e requerer de modo rígido oficial o tráfego violento maciço temporal pela web remota do arquivo bruto e completo global estático de novo em cada alteração isolada local regional oficial virtual).
D) O PATCH garante e emula o isolamento global em Borda de Nuvem temporal das máquinas de servidor SQL injetado local em ambiente local virtual assíncrono fechado base nativa abstrata contínua restritivo unificado interno base do Tribunal oficial regional.
E) O PUT criptografa na base SSL todos os cabeçalhos, mas o PATCH utiliza SSH estático remoto isolado em Linux oficial da justiça estritamente virtual na plataforma restrita centralizada corporativa remota e oficial local na federação da união e nacional.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. O PATCH aplica-se teoricamente para atualizações parciais. PUT significa a substituição/regravação física teórica completa do documento e recurso. A economia de banda unificada isolada regional oficial e o respeito semântico tornam o PATCH ideal estrito em base para pequenas e limpas edições em um único atributo remoto contínuo isolado oficial básico na API.
</details>

## 📝 TEMA 4: Inglês Instrumental para TI

### Questão 41 (FCC - Questão Prática / Adaptada)
Um Desenvolvedor Sênior deixou o seguinte alerta num canal de chat técnico sobre o último pacote de atualizações de código e a manutenção da arquitetura:

'The new dependency we added yesterday causes a severe memory **leak** in the application. We need to **roll back** the latest commit immediately.'

Nesta comunicação asilada rápida de urgência virtual técnica de base do dia a dia, os termos em inglês '**leak**' e '**roll back**' correspondem estritamente e respectivamente aos seguintes equivalentes operacionais na área técnica regional unificada:
A) Injeção - Formatar tudo.
B) Desvio - Acoplar rápido.
C) Falha isolada Lógica - Rezar regionalmente.
D) Vazamento - Reverter/Retroceder/Desfazer.
E) Encriptação - Gravar em log nativo local aberto temporal remoto estrito contínuo fechado e seguro abstrato limpo virtual básico unificado contínuo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. A expressão 'Memory leak' quer dizer vazamento de memória (a memória enche e trava). 'Roll back' quer dizer reverter a alteração para a versão anterior ou regredir.
</details>

### Questão 42 (FCC - Questão Prática / Adaptada)
Em um contrato governamental da licitação do parque base da justiça regional de máquinas, lê-se nas especificações técnicas nativas contínuas abertas oficiais e isoladas lógicas e regionais abertas nativas contínuas base lógicas unificadas:

'All servers must feature **hot-swappable** hard drives to minimize unexpected **downtime**.'

Os vocábulos e os jargões grifados significam estritamente e diretamente no meio de infraestrutura:
A) Criptografados no HD de alta tensão regional básica temporal / Tempo longo visual temporário abstrato remoto nacional estático.
B) Troca à quente (Trocáveis sem precisar desligar a máquina) / Tempo inativo (Sistema fora do ar, indisponível).
C) Aquecidos nativamente / Rede unificada aberta.
D) Remotos Unificados Nativos Global e Temporal Isolado / Sistema isolado nativo temporal externo abstrato.
E) Fechados na rede local remota oficial virtual e baseada abstrata temporal fechado / Log restrito contínuo unificado em borda virtual lúdica aberta isolado regional e físico contínua base temporal e lúdica.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Um disco (HD) 'Hot-swappable' é aquele que você pode retirar e plugar um novo sem precisar interromper/desligar a energia do servidor. O 'Downtime' expressa inatividade (período em que o sistema ficou fora de ar ou parado).
</details>

### Questão 43 (FCC - Questão Prática / Adaptada)
Leia as notas oficiais lógicas na atualização temporal do banco de dados remoto isolado relacional contínua da web local oficial unificada virtual:

'The new query engine completely **bypasses** the traditional parser, **boosting** read performance by up to 40%.'

As palavras destacadas em negrito '**bypasses**' e '**boosting**' expressam, no contexto computacional:
A) Contorna / Impulsionando (Aumentando).
B) Oculta visualmente local base temporal aberta / Excluindo nativamente lógico virtual unificado contínua do banco regional isolada nativa base de relatórios regionais puros da web oficial regional isolada.
C) Apaga permanentemente e limpa a base unificada / Revertendo temporal assíncrona local contínua base de segurança externa regional.
D) Transmite para outros computadores contínuos isolados remotos lógicos / Isolando visual log contínuo base da web local oficial.
E) Encripta visual log restritivo regional puro base local fechada remota virtual unificada aberta e temporal isolada do estado civil oficial / Atualizando unificadas oficiais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- A) Correta. 'Bypasses' significa passar por cima, ignorar ou contornar um caminho ou restrição padrão lógica. 'Boosting' indica aumento explosivo de potência física impulsionando a carga ou melhorando radicalmente (boost) a performance.
</details>

### Questão 44 (FCC - Questão Prática / Adaptada)
Uma notificação automática regional gerada pela AWS do Tribunal Federal alertou para o sistema base restrito lógico:

'Instance xyz has reached its resource **threshold** and will be **rebooted**.'

As palavras '**threshold**' e '**rebooted**' indicam respectivamente e essencialmente a tradução de:
A) Cota de Impostos Oficiais Internos Limitados da União Nacional Fechada Isolada Remota Limite Base Regional / Renomeada isolada limpa unificada temporal isolada visual base.
B) Espaço Livre Físico Global Abstrato Limpo Virtual e Nativo / Apagada Lógica Aberta Limpa.
C) Limiar/Limite Máximo Crítico estático unificado contínuo da borda oficial unificada lógica nativo base contínua remoto fechado / Reiniciada.
D) Firewall Ativo Contínuo / Criptografada base local abstrata restritivo puro contínua e regional limpa virtual fechada global abstrato unificado e local virtual do servidor estático da nuvem.
E) Disco Lógico Virtual Base Nativa Contínuo Temporal Isolado Regional Unificada Oficial Básica / Congelada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. A palavra 'Threshold' é fundamental em TI para indicar o Limite (o limiar) crítico. O 'Rebooted' aponta o simples e popular 'reiniciada'.
</details>

### Questão 45 (FCC - Questão Prática / Adaptada)
Um manual de programação Java descreve uma boa prática base no desenvolvimento da interface remota relacional restritiva unificada lúdico virtual do projeto nativa e contínua unificada da aplicação base unificada judicial nacional na nuvem oficial isolada remota base abstrato fechado contínua:

'Variables should be initialized to avoid unexpected **behavior** and potential **crashes** during **runtime**.'

De acordo com esse aviso técnico base oficial do documento remota contínua global isolada nativa aberta contínua isolada relacional abstrata fechada local do tribunal base oficial, as palavras '**behavior**', '**crashes**' e '**runtime**' traduzem-se para o dia a dia:
A) Log regional nativo virtual oficial / Lentidão extrema estática de base oficial contínua temporal oficial isolado visual / Compilação.
B) Comportamento / Falhas Críticas/Travamentos Fatais da Base / Tempo de Execução.
C) Criptografia Base Visual Isolada Local Restrito Regional Abstrato Temporal Remoto Isolado / Apagamentos Temporais Lógicos do Disco Básico Unificado Nativa Base Restritiva Virtual Oficial Regional Contínua Fechada Base Global Unificado / Tempo Base Lógica Ocioso Oficial Judicial Unificada Local Restrita e Fechada Isolada Nativa Contínua.
D) Carga Temporal da Borda Relacional Regional Limite Unificada Virtual Isolada Lógica Base / Alterações Base Abstrata Unificada Contínua Oficial Lógica Aberta Limite Temporal Nacional da Base Regional / Armazenamento Abstrato do Oracle Unificada Remota Oficial Fechada Contínua Base Nacional Local Oficial Virtual.
E) Velocidade Base Oficial Nacional Lúdico Contínua Temporal Isolado Virtual Regional / Bugs Visuais Front-end Lógicos Nativos Restritos Regionais Oficiais Fechados Temporais Virtuais Lógicos Borda Contínuos Abertos Unificados Relacionais Limites Nacionais Nativos Locais Fechados / Desconexão Local Unificada Abstrata Borda Nativa Oficial e Temporal Contínua Global Local Base Nacional Virtual Lógica Aberta Regional Isolada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. 'Behavior' = comportamento da aplicação. 'Crashes' = Os clássicos travamentos fatais e súbitos (aplicativo fechou do nada ou morreu). 'Runtime' = No jargão da computação lúdico oficial restrita temporal nativo limpo base lógico oficial regional unificado contínuo da web remota isolado base nativo local abstrato contínua aberta, significa o tempo exato (ou período temporal em andamento e em andamento aberto contínuo regional na hora e durante) da máquina em andamento ligado contínua da borda local nacional nativa unificada lógica temporal regional local nacional unificado remota oficial: Tempo Real de Execução (quando o programa está efetivamente rodando e acordado limpo).
</details>

### Questão 46 (FCC - Questão Prática / Adaptada)
Um documento descritivo sobre o projeto front-end diz:
'We will use a modern framework to handle **DOM** manipulation and to ensure **seamless** transitions between views.'
Na expressão acima, o termo '**seamless**' pode ser traduzido tecnicamente como:
A) Complexas e manuais, que exigem reload total do servidor web.
B) Ininterruptas, transparentes ou sem emendas (suaves), indicando uma experiência contínua sem quebras de navegação.
C) Restritas apenas aos dispositivos móveis Apple.
D) Baseadas exclusivamente no backend, sem intervenção visual.
E) Encriptadas e lentas devido à carga de segurança alta no carregamento de telas isoladas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. A palavra 'seamless' no jargão técnico (e comum) significa algo que é feito sem interrupções sensíveis (sem emendas ou costuras). Transições 'seamless' no front-end são aquelas que fluem naturalmente (como num Single Page Application) sem o usuário perceber travamentos ou as velhas telas brancas de carregamento.
</details>

### Questão 47 (FCC - Questão Prática / Adaptada)
Durante a auditoria de um sistema de logs no TRT, identificou-se o seguinte trecho sobre as ocorrências de segurança:
'To prevent automated attacks, the system automatically **bans** any IP address that **triggers** the brute-force threshold.'
As palavras destacadas '**bans**' e '**triggers**' significam, respectivamente:
A) Bane (Bloqueia) e Aciona (Dispara).
B) Libera e Monitora.
C) Compacta e Ignora.
D) Redireciona e Evita.
E) Descriptografa e Alerta.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- A) Correta. 'Bans' quer dizer 'bane' ou 'bloqueia' de forma restrita (não deixar o IP acessar mais). 'Triggers' significa 'dispara', 'ativa', 'desencadeia' (ex: atingiu o limite de erros, então disparou/ativou a regra de defesa).
</details>

### Questão 48 (FCC - Questão Prática / Adaptada)
Ao ler a documentação do GitHub para submeter contribuições em um repositório corporativo Open Source, um estagiário de TI se deparou com a instrução:
'Please make sure your code does not contain any **hardcoded** secrets before you submit a **pull request**.'
O termo técnico '**hardcoded**' no jargão de engenharia de software significa:
A) Código compilado nativamente usando bibliotecas pesadas de Inteligência Artificial em C++.
B) Códigos que possuem algoritmos de ordenação e busca demorados, difíceis de interpretar pela máquina remota.
C) A prática de embutir valores (como senhas, IPs e chaves) diretamente e de forma fixa/chumbada no código-fonte, em vez de usar variáveis de ambiente ou arquivos de configuração externos.
D) A necessidade de aplicar criptografia assimétrica dupla nas chamadas HTTP realizadas pelo projeto restritivo.
E) Código protegido por direitos autorais que não pode ser legalmente auditado sem uma licença oficial comprada e homologada pelo órgão.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Hardcoded (ou 'chumbado' no jargão em português) quer dizer que o valor (ex: `password = "123456"`) foi digitado fisicamente no código. Isso é uma péssima prática de segurança, especialmente quando o código vai para um repositório como o Git, permitindo o vazamento global (data breach).
</details>

### Questão 49 (FCC - Questão Prática / Adaptada)
No planejamento ágil do projeto judicial, o Product Owner (PO) emite o seguinte alerta na ferramenta Jira:
'We must fix the critical bug on the payment module because it blocks the main **workflow** and creates a huge **bottleneck** for the administrative staff.'
Os termos '**workflow**' e '**bottleneck**' denotam, no contexto corporativo e de TI:
A) Ambiente de Servidor / Redundância Física.
B) Fluxo de Trabalho (processos/rotina) / Gargalo (ponto de estrangulamento ou lentidão).
C) Ferramenta de Suporte / Falha de Banco de Dados Crítica Externa.
D) Requisito Funcional Opcional / Aceleração de Processos de Negócio Externos e Virtuais.
E) Fluxo de Tela Visual Frontend / Segurança Avançada Contra Invasores.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. 'Workflow' é o fluxo de trabalho diário, ou seja, o passo a passo da esteira produtiva das varas da justiça. 'Bottleneck' significa 'gargalo de garrafa', e é muito usado na TI e na administração para indicar o ponto do processo onde tudo trava e fica lento ou empilha tarefas por ineficiência local.
</details>

### Questão 50 (FCC - Questão Prática / Adaptada)
A equipe de QA reportou o seguinte no relatório de finalização de testes semanais:
'The application works flawlessly under normal conditions, but we noticed performance **degradation** when the system is subjected to high **throughput**.'
Os termos destacadas '**degradation**' e '**throughput**' representam, nesse contexto:
A) Queda de qualidade (piora/lentidão) e Vazão (capacidade de transferência ou processamento contínuo).
B) Melhora automática do código / Restrição manual dos acessos externos.
C) Fragmentação de disco local / Interrupção (tempo inativo) gerado pelo data center fechado.
D) Otimização repentina / Latência alta de ping em requisições de rede restrita na intranet oficial.
E) Escalabilidade horizontal restritiva nativa da nuvem da AWS / Quantidade de erros gerados no sistema na base de uso virtual.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- A) Correta. 'Degradation' indica que algo degradou (ficou pior ou lento, geralmente atrelado a performance degradation). 'Throughput' é a taxa de vazão/transferência da rede (ex: o quanto de dados o sistema processa com sucesso por minuto). Muita vazão forçada gera degradação se o servidor for fraco.
</details>

### Questão 51 (FCC - Questão Prática / Adaptada)
O arquiteto da AWS do tribunal, ao planejar as instâncias EC2, descreveu o seguinte requisito no documento:
'In order to reduce costs, we can utilize instances that are highly **scalable** and can be **torn down** when the processing is complete.'
A expressão '**torn down**' no jargão de infraestrutura virtual remota e Cloud significa primariamente:
A) Migradas para provedores de nuvens internacionais de terceiros distantes remotamente de forma local.
B) Criptografadas severamente por políticas de rede unificadas abertas de forma nativa e estática base de roteador local do estado isolado físico contínuo e judicial.
C) Destruídas, desmontadas ou desligadas sumariamente após cumprirem o seu papel temporário, parando de gerar gastos na conta final do TRT.
D) Atualizadas nativamente base em patches unificados do Linux base isolado temporal virtual global corporativo limpo.
E) Congeladas visualmente local nativo e contínuo da interface web limpa da base temporal do Amazon Relational Database estrutural assíncrona.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. A expressão 'Tear down' (passado 'torn down') significa 'desmontar', 'derrubar' ou 'destruir' algo. Na nuvem, você sobe (spin up) recursos/máquinas virtuais e, quando não precisa mais, as 'destrói' (tear down) para que parem de cobrar por hora e liberem espaço abstrato.
</details>

### Questão 52 (FCC - Questão Prática / Adaptada)
Um desenvolvedor backend descreveu um erro inesperado e fatal para a equipe, avisando que o comportamento ocorria devido a condições raras e específicas do usuário:
'This problem only occurs in extreme **edge cases**, therefore we will not implement a **workaround** at this moment.'
As duas expressões no inglês corporativo, '**edge cases**' e '**workaround**', representam, de modo preciso e respectivo:
A) Casos centrais do negócio principal unificados e nativos oficiais / Rotina de exclusão massiva nativa da nuvem temporária relacional.
B) Casos limites/exceções raras (cenários muito peculiares) e Gambiarra/Solução de contorno provisória.
C) Cargas severas nativas base unificadas temporais de limite base remoto / Otimização profunda em núcleo Linux da AWS.
D) Cenários limpos oficiais testados globalmente nativos base / Rotina nativa de rede restritiva unificada e base central.
E) Falhas generalizadas básicas diárias virtuais / Cancelamento imediato regional oficial base abstrata restritiva.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. 'Edge cases' na TI significam os 'casos de borda' ou seja, situações raras (quando o usuário faz uma série de movimentos bizarros muito improváveis). 'Workaround' é a velha e famosa solução de contorno, improviso técnico momentâneo (uma 'gambiarra' oficial) para um problema que não possui uma correção estrutural e limpa definitiva.
</details>

### Questão 53 (FCC - Questão Prática / Adaptada)
Durante a reunião com a fornecedora do novo portal da justiça, o diretor da empresa contratada afirmou no roadmap do projeto oficial e comercial restrito a ser entregue remotamente na plataforma:
'We plan to **ship** the new platform by late December, as long as there are no major **setbacks** during the beta phase testing.'
As expressões '**ship**' e '**setbacks**' significam, em ambientes de entrega de software corporativo local:
A) Codificar limpo e rápido da nuvem fechada unificada local / Relatórios semanais isolados estáticos oficiais contínuos limpos de teste base judicial regional.
B) Lançar/Entregar (publicar o código e mandar pro cliente) e Contratempos/Atrasos imprevisíveis na vida de desenvolvimento de projeto real oficial e final abstrato virtual.
C) Descontinuar velhos projetos do servidor local estático fechado contínuo unificado virtual temporal básico / Reuniões remotas e visuais na intranet do TRT e do provedor corporativo isolado limpo temporal.
D) Exportar bases físicas locais em MySQL fechadas puramente / Códigos fonte livres de segurança AWS isolado virtual limpo.
E) Instalar no ambiente de desenvolvimento puro remoto local contínuo de TI / Melhorias incrementais rápidas temporárias lógicas abertas e nativas na federação isolada estrita.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. 'To ship' em engenharia e desenvolvimento de software não significa enviar algo pelo correio físico do mar. É jargão para 'Lançar' ou 'Publicar' para a produção (entregar o código rodando ao cliente ou ao público). 'Setbacks' quer dizer tropeços, percalços, imprevistos ou contratempos operacionais.
</details>

### Questão 54 (FCC - Questão Prática / Adaptada)
Um manual do Node.js, framework clássico e assíncrono nativo temporal unificado da borda web restrita virtual e rápida global isolada base local contínua judicial, descreve em sua documentação aberta:
'Node.js is highly effective for I/O bound tasks, but its single-threaded nature makes it completely **unsuitable** for CPU-intensive operations.'
A palavra destacada e essencial, '**unsuitable**', descreve, traduz e avisa para o analista e programador do Tribunal que:
A) O Node.js deve ser compulsoriamente imposto e usado isoladamente.
B) O framework é inapropriado, não adequado ou não recomendado unificadamente e formalmente na base de tarefas pesadas da máquina regional lógica virtual local limpa unificada temporal.
C) A linguagem possui velocidade máxima global limpa temporal oficial judicial restrita remota contínua da borda base lógica virtual isolada limpa e segura corporativa regional estática local em processos.
D) É obrigatório e perfeitamente ajustado e adaptável ao limite temporal restrito e base nativa virtual isolada base lúdica contínua nativa e isolada da área de uso contínuo lógico base judicial oficial local do CPU do Linux local.
E) Funciona exclusivamente para compilar de forma offline local restritiva virtual e base global contínua temporal oficial unificada da justiça local restritiva base e contínua do Kernel do computador servidor regional restrito da borda.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. A palavra 'suitable' significa apropriado/adequado. O prefixo 'un' nega a palavra ('unsuitable' = inadequado/inapropriado). Portanto, o manual diz: Node.js é inapropriado para tarefas pesadas que exijam uso violento intensivo da CPU devido à sua arquitetura de base de thread única original nativa de fábrica da Google (V8 JavaScript Engine).
</details>

### Questão 55 (FCC - Questão Prática / Adaptada)
Um erro no log do Linux do tribunal disparou na madrugada temporal unificada e virtual isolada da base remota contínua nacional base lógico oficial local regional restritivo oficial temporal da máquina corporativo temporal unificada lógica abstrato limpa judicial:
'Network connection was forcefully **dropped** due to high packet loss. Attempting to **resume** the secure download...' 
Os termos '**dropped**' e '**resume**' significam, na área de redes restritas unificadas globais locais remotas lógicas virtuais e base do analista corporativo oficial:
A) Conectada e Mantida estavelmente na rede contínua base unificada abstrata contínua local isolada limpa da rede / Ocultar de modo abstrato regional o arquivo limpo base temporal oficial local da intranet do país fechada emulada oficial temporal judicial nacional nativa de processos limpos contínuos remotos fechados de forma básica.
B) Finalizada de forma limpa orgânica na rede fechada / Deletar.
C) Perdida e Derrubada/Desconectada unificada / Retomar/Continuar remotamente.
D) Compartilhada regional e oficial limpa temporal / Substituir.
E) Armazenada e Roteada visual temporal e isolada virtual / Encerrar o processo global virtual da justiça nacional.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. 'Dropped' (em contexto de rede) significa conexão ou pacote de rede derrubado e descartado forçadamente ou perdido (exemplo limpo: frame drop num vídeo online é quando perde os quadros de vídeo temporais isolados contínuos nativos locais limpos nativos regionais de processos, a conexão foi perdida). 'Resume' significa continuar ou retomar o download (e não fazer um currículo de emprego temporal local fechado restrito remoto limpo global isolado virtual da borda, embora resume signifique currículo no RH). No contexto da rede judicial da justiça base corporativa nativa: O download parou, o sistema tenta 'retomar/resume' de onde isolou-se remoto.
</details>

