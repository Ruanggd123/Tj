# Bateria de Questões FCC — Quinta-feira 28/05
Este arquivo contém 45 questões altamente calibradas nos padrões da FCC, com alternativas de comprimento similar e distratores baseados em pegadinhas reais (mudanças sutis de palavras-chave, restrições e termos legais).

---
## 📝 TEMA 1: Banco de Dados — MongoDB, CTEs e Window Functions
### Questão 1 (FCC)
Considere que um analista precise definir a estrutura de dados para o novo sistema do tribunal no MongoDB. Sobre os conceitos de coleções (collections) e documentos (documents) neste banco de dados, é correto afirmar:
A) Uma coleção não exige definição prévia de esquema (schema-less), o que permite que documentos de uma mesma coleção possuam diferentes campos e estruturas.
B) Um documento do MongoDB possui estrutura tabular rígida, exigindo que todos os atributos sejam declarados no momento da criação da coleção correspondente.
C) Uma coleção no MongoDB é conceitualmente idêntica a uma linha de tabela de um banco de dados relacional tradicional, armazenando múltiplos registros simples.
D) Os documentos do MongoDB utilizam o formato XML nativo de armazenamento físico para assegurar a portabilidade e indexação rápida dos dados.
E) O MongoDB exige que todas as coleções tenham pelo menos um relacionamento físico pré-definido (Foreign Key) com outras coleções do banco de dados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 2 (FCC)
No MongoDB, o campo `_id` desempenha um papel fundamental na identificação única de documentos em uma coleção. Sobre o funcionamento e propriedades do campo `_id`, assinale a alternativa correta:
A) O valor do ObjectId gerado pelo MongoDB é um número sequencial simples de 32 bits iniciado em zero e incrementado a cada nova inserção na coleção.
B) O campo `_id` é opcional e, caso não seja fornecido ou gerado, a coleção aceitará múltiplos documentos sem qualquer chave primária interna.
C) Se o usuário não especificar o campo `_id` na inserção de um documento, o MongoDB gerará automaticamente um valor do tipo ObjectId para ele.
D) O campo `_id` pode ter valores duplicados dentro de uma mesma coleção, desde que esses documentos estejam em partições físicas (shards) distintas.
E) O MongoDB proíbe estritamente a utilização de tipos de dados personalizados, como strings ou números inteiros, no valor do campo `_id` informado pelo usuário.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 3 (FCC)
Deseja-se realizar uma busca no MongoDB para localizar todos os processos na coleção `processos` cuja `prioridade` seja maior ou igual a 3. Assinale a sintaxe correta para essa consulta:
A) db.processos.select({prioridade: {$gte: 3}})
B) db.processos.find({prioridade: {$gt: 3}})
C) db.processos.find({prioridade: {$eq: 3}})
D) db.processos.query({prioridade: {$ge: 3}})
E) db.processos.find({prioridade: {$gte: 3}})

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 4 (FCC)
Expressões de Tabela Comuns (CTEs) são recursos avançados do SQL. Sobre a utilização de CTEs em instruções SQL baseadas no padrão ANSI, é correto afirmar:
A) O uso de CTEs reduz a legibilidade do código SQL, pois exige a criação de subconsultas aninhadas redundantes dentro da cláusula WHERE.
B) Uma CTE é armazenada de forma física e permanente no disco do banco de dados, sendo visível para qualquer sessão do usuário até que seja descartada.
C) Uma CTE é criada utilizando a palavra-chave WITH e funciona como uma tabela temporária cujo escopo é restrito à execução de uma única consulta.
D) As CTEs não admitem a referência a si mesmas (recursividade), sendo restritas apenas a subconsultas lineares simples e agrupamentos.
E) Uma CTE só pode ser referenciada uma única vez dentro da instrução SQL principal, sendo vedada sua reutilização na mesma consulta.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 5 (FCC)
As Window Functions (funções analíticas) em SQL executam cálculos em um conjunto de linhas que estão relacionadas à linha atual. A cláusula obrigatória utilizada para identificar uma Window Function é:
A) ROWS BETWEEN
B) PARTITION
C) WINDOW
D) GROUP BY
E) OVER

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 6 (FCC)
Sobre a diferença fundamental entre as cláusulas PARTITION BY (usada em Window Functions) e GROUP BY em consultas SQL, assinale a alternativa correta:
A) O GROUP BY mantém todas as linhas individuais no resultado final, apenas aplicando ordenações secundárias e filtros baseados na cláusula HAVING.
B) O GROUP BY permite a utilização de funções analíticas como ROW_NUMBER(), enquanto o PARTITION BY restringe a consulta a funções de agregação clássicas.
C) O PARTITION BY exige que todas as colunas selecionadas no SELECT façam parte de sua cláusula, diferentemente do comportamento padrão do GROUP BY.
D) O PARTITION BY executa cálculos sobre a janela mantendo a individualidade das linhas, enquanto o GROUP BY colapsa o conjunto de linhas em uma única linha agregada.
E) O PARTITION BY é executado fisicamente antes da cláusula WHERE, enquanto o GROUP BY é processado na etapa final de renderização do result set.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 7 (FCC)
Em Window Functions SQL, as funções RANK() e DENSE_RANK() são utilizadas para classificar linhas de uma partição. A diferença técnica de comportamento entre elas é que:
A) A função RANK() é exclusiva para campos de texto, enquanto a função DENSE_RANK() é aplicada apenas a campos numéricos e datas.
B) A função DENSE_RANK() pula posições na classificação se houver empates, enquanto a função RANK() gera números contínuos sem pular valores.
C) A função RANK() exige a ordenação ascendente dos dados, enquanto a função DENSE_RANK() opera exclusivamente em ordenações decrescentes.
D) A função DENSE_RANK() calcula a classificação baseada no desvio padrão dos valores, enquanto a função RANK() realiza apenas uma contagem simples de linhas.
E) A função RANK() pula posições na sequência de classificação se houver empates, enquanto a função DENSE_RANK() gera números sequenciais contínuos sem lacunas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 8 (FCC)
Para analisar dados temporais no tribunal, um analista precisa acessar o valor de uma coluna na linha imediatamente anterior da janela atual de dados. A função analítica SQL adequada para essa operação é:
A) ROW_NUMBER()
B) LEAD()
C) FIRST_VALUE()
D) NTH_VALUE()
E) LAG()

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 9 (FCC)
Para implementar uma consulta SQL que percorra uma estrutura hierárquica de cargos no tribunal (como uma árvore organizacional), o desenvolvedor deve utilizar:
A) Um operador de junção externa (LEFT OUTER JOIN) aninhado recursivamente até o limite físico de dez níveis de profundidade de tabelas.
B) Uma subconsulta correlacionada simples associada à cláusula GROUP BY e filtrada com HAVING na instrução externa principal.
C) Uma Window Function utilizando a cláusula OVER combinada com a função analítica LEAD() e a partição baseada na chave primária.
D) Uma tabela temporária física criada com CREATE TEMP TABLE e indexada sequencialmente a cada iteração de um loop interno.
E) Uma CTE definida com a cláusula WITH RECURSIVE, combinando um caso base e um caso recursivo através do operador UNION ou UNION ALL.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 10 (FCC)
Para otimizar o desempenho das consultas de busca por nome de servidores na coleção `funcionarios` no MongoDB, deve-se criar um índice. O comando correto para criar um índice ascendente no campo `nome` é:
A) db.funcionarios.setIndex({nome: true})
B) db.funcionarios.createIndex({nome: -1})
C) db.funcionarios.createIndex({nome: 1})
D) db.funcionarios.addIndex({nome: 'asc'})
E) db.funcionarios.ensureIndex({nome: '*' })

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 11 (FCC)
Em relação à consistência e transações no MongoDB, a partir de suas versões modernas (4.0+), o banco de dados passou a oferecer suporte a:
A) Escritas síncronas obrigatórias em disco que impedem operações de leitura paralela.
B) Consistência estrita em tempo real sem suporte a qualquer isolamento transacional.
C) Transações relacionais baseadas na linguagem de programação PL/SQL do Oracle.
D) Transações ACID multi-documento em coleções na mesma partição ou em réplicas associadas.
E) Bloqueio exclusivo de tabelas inteiras durante qualquer operação de inserção de documentos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 12 (FCC)
Em uma Window Function, a cláusula que restringe o conjunto de linhas a serem consideradas no cálculo analítico a partir da linha atual (como calcular uma média móvel de 3 linhas anteriores e a atual) é:
A) ORDER BETWEEN 3 PRECEDING AND CURRENT ROW
B) RANGE BETWEEN 3 FOLLOWING AND CURRENT ROW
C) ROWS BETWEEN 3 FOLLOWING AND CURRENT ROW
D) PARTITION BETWEEN 3 PRECEDING AND CURRENT ROW
E) ROWS BETWEEN 3 PRECEDING AND CURRENT ROW

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 13 (FCC)
No MongoDB, para realizar operações de agregação complexas que envolvem filtragem, agrupamento e projeção de dados (similar ao GROUP BY, WHERE e SELECT do SQL), utiliza-se:
A) A linguagem SQL padrão enviada através de drivers JDBC compatíveis com o MongoDB.
B) O comando `db.colecao.group()` de forma exclusiva, pois o MongoDB não possui estágios de pipeline.
C) O framework de agregação (Aggregation Framework) através do método `db.colecao.aggregate()` recebendo uma lista de estágios (pipeline).
D) A execução de loops imperativos em JavaScript rodando exclusivamente no navegador do cliente.
E) O comando `db.colecao.find().groupBy()` associado a funções de redução do MapReduce clássico.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 14 (FCC)
O MongoDB possui um limite físico padrão de tamanho para um único documento BSON para garantir que o uso de memória e a latência de rede permaneçam otimizados. Esse limite máximo é de:
A) 8 MB
B) 16 MB
C) 32 MB
D) 64 MB
E) 4 MB

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 15 (FCC)
A função analítica de distribuição acumulada que calcula a posição relativa de um valor dentro de um grupo de valores em SQL é a:
A) PERCENT_RANK()
B) CUME_DIST()
C) NTILE()
D) DENSE_RANK()
E) RATIO_TO_REPORT()

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

## 📝 TEMA 2: Sistemas Operacionais — SO Linux (Red Hat/Oracle Linux, comandos, permissões, usuários)
### Questão 16 (FCC)
No Linux (distribuições Red Hat / Oracle Linux), o diretório no qual são guardados os arquivos de configuração locais específicos do sistema e de seus serviços é o:
A) /bin
B) /var
C) /usr/sbin
D) /etc
E) /home

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 17 (FCC)
Um analista de TI precisa configurar as permissões de um arquivo de script no Linux para que o dono tenha acesso total (leitura, escrita e execução), o grupo do arquivo tenha acesso de leitura e execução, e os outros usuários tenham apenas acesso de execução. A representação numérica octal correspondente a essa configuração é:
A) 750
B) 755
C) 644
D) 775
E) 751

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 18 (FCC)
Sobre o sistema de permissões de arquivos e diretórios no Linux, a permissão de execução (x) quando aplicada a um diretório específico determina que o usuário:
A) Pode compilar e rodar binários executáveis localizados exclusivamente na raiz do diretório.
B) Pode listar o nome dos arquivos contidos no diretório (executar o comando `ls`).
C) Pode criar, excluir e renomear arquivos dentro daquele diretório específico.
D) Pode acessar o diretório (entrar nele com o comando `cd`) e acessar seus arquivos internos.
E) Pode alterar o dono e o grupo do diretório usando o comando `chown` diretamente.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 19 (FCC)
Para buscar por linhas contendo o termo 'erro' dentro de todos os arquivos de log localizados no diretório `/var/log` no Linux, o comando adequado é:
A) locate /var/log/erro
B) find /var/log -name 'erro'
C) grep -r 'erro' /var/log
D) cat /var/log | grep 'erro'
E) awk -f 'erro' /var/log

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 20 (FCC)
Nas distribuições Linux da família Red Hat Enterprise Linux (RHEL) e Oracle Linux, o gerenciador de pacotes de baixo nível (que instala arquivos locais sem resolver dependências externas) e o gerenciador de pacotes de alto nível (que consulta repositórios remotos e resolve dependências automaticamente) são, respectivamente:
A) yum e rpm
B) dpkg e apt
C) rpm e dnf
D) dnf e yum
E) rpm e dpkg

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 21 (FCC)
Para alterar o dono de um arquivo `relatorio.txt` para o usuário `ruan` e o seu grupo associado para `ti` no Linux, utiliza-se o comando:
A) chattr ruan:ti relatorio.txt
B) chmod ruan:ti relatorio.txt
C) chgrp ruan:ti relatorio.txt
D) chown ruan:ti relatorio.txt
E) usermod ruan:ti relatorio.txt

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 22 (FCC)
O diretório `/var/log` no Linux é de suma importância para a administração do sistema. Sua função principal é:
A) Conter os arquivos binários essenciais de administração reservados exclusivamente ao usuário superusuário root.
B) Guardar arquivos temporários gerados pelo sistema operacional e removidos a cada reinicialização.
C) Armazenar arquivos de registros de eventos do sistema, mensagens de serviços e logs de aplicações em execução.
D) Armazenar arquivos executáveis de bibliotecas dinâmicas compartilhadas pelos programas do usuário.
E) Manter os arquivos de dados locais das contas dos usuários comuns criados no sistema.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 23 (FCC)
O comando `tar` é amplamente utilizado no Linux. Sobre as operações realizadas pelo comando `tar -cvf backup.tar /home/usuario`, assinale a alternativa correta:
A) Ele cria um novo arquivo de arquivo (`backup.tar`) contendo os arquivos do diretório `/home/usuario` empacotados, sem compactação nativa.
B) Ele extrai e descompacta o arquivo `backup.tar` dentro do diretório `/home/usuario` limpando a origem.
C) Ele realiza a compactação compacta utilizando o algoritmo gzip com taxa máxima de compressão.
D) Ele lista o conteúdo detalhado de permissões do arquivo `backup.tar` na saída padrão do terminal.
E) Ele remove os arquivos originais do diretório `/home/usuario` após concluir a cópia de segurança.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 24 (FCC)
O comando `chmod o+x script.sh` aplicado a um arquivo no Linux resulta em:
A) Tornar o arquivo `script.sh` propriedade exclusiva do grupo de usuários administradores.
B) Remover a permissão de execução de todos os usuários do sistema do arquivo `script.sh`.
C) Conceder permissão de escrita e leitura para o dono e o grupo associado ao arquivo `script.sh`.
D) Adicionar a permissão de execução (x) exclusivamente para os outros usuários (others) em relação ao arquivo `script.sh`.
E) Remover todas as permissões dos outros usuários (others) em relação ao arquivo `script.sh`.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 25 (FCC)
Uma vantagem técnica fundamental do gerenciador de pacotes `dnf` (ou `yum`) em relação ao utilitário `rpm` no Oracle Linux é:
A) A capacidade de calcular, baixar e instalar de forma automática todas as dependências requeridas por um pacote.
B) A dispensa do acesso privilegiado de root para a instalação de softwares no sistema operacional.
C) A compilação local dos arquivos de código-fonte durante a instalação dos pacotes.
D) O funcionamento offline obrigatório que dispensa a existência de repositórios baseados em rede.
E) O suporte exclusivo à instalação de pacotes baseados na extensão Debian (`.deb`).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 26 (FCC)
Para visualizar a documentação oficial detalhada e o manual de utilização do comando `iptables` no Linux, utiliza-se o comando:
A) iptables --manual
B) help iptables
C) info -f iptables
D) doc iptables
E) man iptables

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 27 (FCC)
O comando `pwd` na linha de comando do terminal do Linux tem a finalidade de:
A) Alterar a senha (password) do usuário logado no sistema operacional.
B) Exibir o caminho absoluto do diretório de trabalho atual do usuário no terminal.
C) Listar todos os processos em execução que pertencem ao usuário atual.
D) Exibir a quantidade de espaço em disco utilizado em cada partição física.
E) Configurar as permissões de acesso físico de arquivos em lote.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 28 (FCC)
Em relação à hierarquia de diretórios padrão no Linux (FHS), no diretório `/sbin` encontram-se tipicamente:
A) Os arquivos de bibliotecas dinâmicas do sistema essenciais para a inicialização e execução de comandos do `/bin`.
B) Os arquivos binários executáveis essenciais usados para a administração do sistema e manutenção, reservados ao root.
C) Os arquivos de cabeçalho C e códigos-fonte do kernel necessários para desenvolvimento.
D) Os arquivos binários executáveis de uso geral de todos os usuários comuns sem privilégios.
E) Os arquivos de dados de configurações globais de rede e hosts do sistema.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 29 (FCC)
Para redirecionar a saída padrão (stdout) de um comando para um arquivo de texto, sobrescrevendo qualquer conteúdo existente nesse arquivo, utiliza-se o caractere:
A) <
B) >>
C) >
D) |
E) &

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 30 (FCC)
O caractere `|` (pipe) é utilizado no terminal Linux com o objetivo de:
A) Redirecionar a saída padrão (stdout) de um comando para servir como entrada padrão (stdin) de outro comando subsequente.
B) Executar dois comandos de forma paralela e em segundo plano (background) no terminal.
C) Enviar a saída de erro padrão (stderr) de um processo para a partição física nula `/dev/null`.
D) Pausar temporariamente a execução de um processo até receber o sinal de interrupção SIGCONT.
E) Criar um link simbólico físico entre dois arquivos de dados na tabela de inodes.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

## 📝 TEMA 3: Legislação Previdenciária do Estado do Ceará
### Questão 31 (FCC)
De acordo com a Lei Complementar Estadual nº 12/1999, que trata do Regime Próprio de Previdência Social (RPPS) do Estado do Ceará, a filiação ao regime é classificada como:
A) Obrigatória para todos os servidores ocupantes de cargo de provimento efetivo do Estado.
B) Facultativa para novos servidores efetivos nomeados após a aprovação de reformas.
C) Obrigatória para cargos exclusivamente em comissão e empregos públicos temporários.
D) Facultativa para membros do Poder Judiciário e do Ministério Público Estadual.
E) Obrigatória apenas para servidores ativos com remuneração acima do teto do RGPS.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 32 (FCC)
O financiamento e custeio do Regime Próprio de Previdência Social dos servidores do Ceará baseia-se em contribuições de:
A) Caráter contributivo e solidário, mediante contribuições do Estado, dos servidores ativos, aposentados e pensionistas.
B) Caráter exclusivamente patronal, sendo custeado integralmente pelo tesouro estadual sem descontos na folha do servidor.
C) Caráter voluntário dos servidores efetivos associados à capitalização individual em fundos abertos de previdência.
D) Repasses federais do Fundo de Participação dos Estados (FPE) de forma exclusiva e vinculada ao INSS.
E) Contribuições incidentes apenas sobre a remuneração de servidores ativos de nível superior do Poder Executivo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 33 (FCC)
Em relação à contribuição previdenciária devida por servidores aposentados e pensionistas sob o RPPS do Ceará, assinale a regra de incidência correta:
A) A alíquota é reduzida pela metade e incide apenas se o aposentado retornar ao serviço público em cargo em comissão.
B) Aposentados e pensionistas são totalmente isentos de contribuição previdenciária em qualquer hipótese constitucional.
C) A contribuição incidirá sobre o valor integral dos proventos, independentemente do teto fixado para o regime geral.
D) Incidirá sobre a parcela dos proventos de aposentadoria e de pensão que supere o limite máximo estabelecido para os benefícios do RGPS.
E) Incidirá sobre os proventos de aposentadoria apenas se o beneficiário residir fora do território do Estado do Ceará.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 34 (FCC)
O sistema previdenciário público brasileiro assenta-se sobre o princípio da solidariedade. Nesse sentido, a solidariedade significa que:
A) Os benefícios concedidos pelo RPPS dependem da rentabilidade financeira dos investimentos individuais de cada segurado.
B) O financiamento do regime é um dever coletivo de toda a sociedade, incluindo ativos, inativos e o próprio ente público patronal.
C) O Estado está autorizado a não repassar a cota patronal se houver crise fiscal temporária nas contas do tesouro estadual.
D) Os servidores inativos possuem direito adquirido de não contribuir para o custeio do déficit atuarial do sistema público.
E) As alíquotas de contribuição previdenciária devem ser idênticas para todos os entes federados e servidores do Brasil.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 35 (FCC)
Na relação de custeio e financiamento do SUPSEC (Sistema Único de Previdência Social dos Servidores do Ceará), o Estado do Ceará figura como:
A) Ente público patrocinador, responsável pelo repasse das contribuições de cota patronal e pelo equilíbrio atuarial do regime.
B) Segurado obrigatório do regime de previdência, respondendo com suas receitas próprias de impostos residuais.
C) Agente financeiro intermediário privado com fins lucrativos de exploração de fundos mobiliários.
D) Beneficiário direto dos proventos acumulados nas contas de previdência complementar fechada.
E) Encarregado exclusivo da fiscalização de autarquias previdenciárias de outros Estados da federação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 36 (FCC)
A base de cálculo sobre a qual incide a alíquota da contribuição previdenciária mensal do servidor ativo para o RPPS do Ceará é:
A) Apenas o vencimento-base do servidor, excluindo-se qualquer adicional por tempo de serviço ou gratificação de caráter permanente.
B) A remuneração de contribuição do servidor, composta pelo vencimento do cargo efetivo acrescido das vantagens pecuniárias permanentes estabelecidas em lei.
C) A remuneração integral do servidor ativo incluindo parcelas indenizatórias, diárias de viagem e terço de férias.
D) O valor correspondente ao salário-mínimo nacional vigente acrescido de abonos de produtividade da comarca.
E) O limite correspondente a metade do teto estabelecido para os benefícios do Regime Geral de Previdência Social (RGPS).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 37 (FCC)
O regime de previdência pública básica (RPPS) estruturado pelo Estado do Ceará funciona sob o regime financeiro de:
A) Poupança programada compulsória exclusiva de servidores com proventos inferiores a cinco salários-mínimos.
B) Capitalização individual, em que as contribuições de cada servidor são acumuladas em uma conta individual e rentabilizadas em mercado.
C) Repartição capitalizada fechada, que veda a contribuição do ente público patronal e exige investimentos em títulos internacionais.
D) Contas nocionais abertas, baseadas no valor de reposição inflacionária calculado pelo Banco Central do Brasil.
E) Repartição simples, em que as contribuições dos servidores ativos financiam diretamente os benefícios dos aposentados e pensionistas atuais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 38 (FCC)
Quando o beneficiário de aposentadoria sob o RPPS do Ceará for portador de doença incapacitante, a contribuição previdenciária incidirá sobre as parcelas de proventos que superem:
A) O dobro do limite máximo estabelecido para os benefícios do RGPS de forma obrigatória e permanente.
B) O limite máximo estabelecido para os benefícios do RGPS, nos termos das normas gerais federais aplicáveis.
C) Três vezes o valor do salário-mínimo nacional estabelecido pelo Governo Federal.
D) O valor correspondente a 80% do último vencimento recebido em atividade pelo servidor.
E) Qualquer valor, isentando totalmente o aposentado do recolhimento de contribuições previdenciárias.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 39 (FCC)
A gestão, administração e operacionalização do Regime Próprio de Previdência Social (RPPS) dos servidores do Ceará competem à fundação pública de direito público denominada:
A) Prev-Ceará (Instituto Estadual de Seguros de Saúde e Previdência)
B) INSS-CE
C) SUPSEC-Autarquia
D) Cearáprev (Fundação de Previdência Social do Estado do Ceará)
E) Secretaria de Planejamento e Gestão Previdenciária do Ceará

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 40 (FCC)
Se o servidor efetivo ativo do Estado do Ceará possuir remuneração de contribuição inferior ao limite máximo do RGPS (teto do INSS), a sua contribuição previdenciária:
A) Ficará totalmente suspensa, passando o servidor à condição de isento temporário de custeio.
B) Incidirá normalmente sobre a totalidade de sua remuneração de contribuição, aplicando-se a alíquota definida em lei.
C) Deverá ser recolhida diretamente ao INSS por tratar-se de faixa salarial vinculada ao RGPS.
D) Terá sua alíquota reduzida pela metade para evitar o confisco de renda de servidores de baixa remuneração.
E) Será revertida integralmente para fundos privados de previdência complementar aberta.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 41 (FCC)
A contribuição do Estado do Ceará (cota patronal) para o custeio do RPPS dos servidores não poderá ser:
A) Inferior ao valor da contribuição do segurado, nem superior ao dobro desta contribuição.
B) Superior a 10% da receita corrente líquida estadual em nenhuma hipótese atuarial.
C) Recolhida em atraso após o quinto dia útil do mês de competência da folha de pagamento.
D) Inferior a duas vezes o valor da contribuição de servidores inativos e pensionistas acumulados.
E) Destinada a fins de pagamento de despesas de assistência médica ou benefícios de natureza assistencial.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 42 (FCC)
Para garantir a higidez, a solvência e o equilíbrio financeiro e atuarial do RPPS do Estado do Ceará ao longo do tempo, a legislação exige a realização periódica de:
A) Aumentos automáticos e semestrais nas alíquotas de contribuição de todos os segurados ativos.
B) Sorteios de prêmios de incentivo à permanência na ativa para servidores aptos a se aposentar.
C) Emissões compulsórias de títulos da dívida pública estadual vinculados à previdência privada.
D) Avaliações atuariais anuais para dimensionar os compromissos futuros do regime e propor ajustes necessários de custeio.
E) Auditorias externas trimestrais executadas por bancos comerciais privados de fomento econômico.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 43 (FCC)
Os recursos obtidos através da taxa de administração cobrada pelo órgão gestor do RPPS do Ceará devem ser destinados exclusivamente a:
A) Custear as despesas de funcionamento, manutenção e modernização administrativa do próprio órgão gestor da previdência.
B) Financiar obras de infraestrutura urbana nas comarcas do Poder Judiciário do Estado do Ceará.
C) Efetuar o pagamento de precatórios alimentares de servidores inativos com doenças graves.
D) Complementar a remuneração funcional de servidores ativos da Secretaria de Fazenda Estadual.
E) Amortizar de forma extraordinária a dívida líquida consolidada do Estado perante a União.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 44 (FCC)
O abono de permanência é um benefício pecuniário garantido ao servidor que preenche todos os requisitos para a aposentadoria voluntária, mas opta por permanecer em atividade. Esse benefício corresponde ao valor de:
A) Uma remuneração integral adicional paga anualmente no mês de aniversário do servidor efetivo.
B) 10% de seu vencimento básico de cargo efetivo a título de gratificação de permanência extraordinária.
C) Sua contribuição previdenciária mensal, funcionando como um reembolso de mesmo valor enquanto permanecer em atividade.
D) Isenção total do recolhimento mensal de Imposto de Renda Retido na Fonte (IRRF) em folha.
E) Promoção funcional automática para a classe e padrão imediatamente superiores de sua carreira.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 45 (FCC)
A segregação de massas é uma técnica de estruturação de planos de custeio aplicada ao RPPS. O objetivo principal da segregação de massas no Ceará é:
A) Separar os servidores públicos do Estado do Ceará de acordo com o Poder em que atuam (Judiciário, Executivo ou Legislativo).
B) Dividir os segurados do regime em grupos distintos (como Fundo Financeiro e Fundo Previdenciário) para buscar o equilíbrio atuarial a longo prazo.
C) Diferenciar servidores civis e militares para aplicar alíquotas de imposto de renda regressivas especiais.
D) Promover a transferência dos inativos e pensionistas para fundos de previdência de bancos comerciais privados.
E) Permitir a fusão temporária das contas de receitas de impostos do Estado com os recursos de contribuições previdenciárias.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---
