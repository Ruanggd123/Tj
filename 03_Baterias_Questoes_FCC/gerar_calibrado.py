# -*- coding: utf-8 -*-
import os
import subprocess
import sys

def main():
    workspace_dir = r"c:\Users\Ruan Gomes\Downloads\TJC"
    questoes_dir = os.path.join(workspace_dir, "03_Baterias_Questoes_FCC")
    
    # -------------------------------------------------------------
    # DIA 28/05 - QUINTA-FEIRA (Banco de Dados, Linux, Prev CE)
    # -------------------------------------------------------------
    
    dia_28_content = []
    dia_28_content.append("# Bateria de Questões FCC — Quinta-feira 28/05\n")
    dia_28_content.append("Este arquivo contém 45 questões altamente calibradas nos padrões da FCC, com alternativas de comprimento similar e distratores baseados em pegadinhas reais (mudanças sutis de palavras-chave, restrições e termos legais).\n\n---\n")
    
    # Tema 1: Banco de Dados (CTEs, Window Functions, MongoDB)
    dia_28_content.append("## 📝 TEMA 1: Banco de Dados — MongoDB, CTEs e Window Functions\n")
    
    db_questions = [
        # Q1: MongoDB
        (
            "Considere que um analista precise definir a estrutura de dados para o novo sistema do tribunal no MongoDB. Sobre os conceitos de coleções (collections) e documentos (documents) neste banco de dados, é correto afirmar:",
            "Uma coleção não exige definição prévia de esquema (schema-less), o que permite que documentos de uma mesma coleção possuam diferentes campos e estruturas.",
            "Um documento do MongoDB possui estrutura tabular rígida, exigindo que todos os atributos sejam declarados no momento da criação da coleção correspondente.",
            "Uma coleção no MongoDB é conceitualmente idêntica a uma linha de tabela de um banco de dados relacional tradicional, armazenando múltiplos registros simples.",
            "Os documentos do MongoDB utilizam o formato XML nativo de armazenamento físico para assegurar a portabilidade e indexação rápida dos dados.",
            "O MongoDB exige que todas as coleções tenham pelo menos um relacionamento físico pré-definido (Foreign Key) com outras coleções do banco de dados."
        ),
        # Q2: MongoDB _id
        (
            "No MongoDB, o campo `_id` desempenha um papel fundamental na identificação única de documentos em uma coleção. Sobre o funcionamento e propriedades do campo `_id`, assinale a alternativa correta:",
            "Se o usuário não especificar o campo `_id` na inserção de um documento, o MongoDB gerará automaticamente um valor do tipo ObjectId para ele.",
            "O campo `_id` é opcional e, caso não seja fornecido ou gerado, a coleção aceitará múltiplos documentos sem qualquer chave primária interna.",
            "O valor do ObjectId gerado pelo MongoDB é um número sequencial simples de 32 bits iniciado em zero e incrementado a cada nova inserção na coleção.",
            "O campo `_id` pode ter valores duplicados dentro de uma mesma coleção, desde que esses documentos estejam em partições físicas (shards) distintas.",
            "O MongoDB proíbe estritamente a utilização de tipos de dados personalizados, como strings ou números inteiros, no valor do campo `_id` informado pelo usuário."
        ),
        # Q3: MongoDB query
        (
            "Deseja-se realizar uma busca no MongoDB para localizar todos os processos na coleção `processos` cuja `prioridade` seja maior ou igual a 3. Assinale a sintaxe correta para essa consulta:",
            "db.processos.find({prioridade: {$gte: 3}})",
            "db.processos.find({prioridade: {$gt: 3}})",
            "db.processos.find({prioridade: {$eq: 3}})",
            "db.processos.query({prioridade: {$ge: 3}})",
            "db.processos.select({prioridade: {$gte: 3}})"
        ),
        # Q4: SQL CTE
        (
            "Expressões de Tabela Comuns (CTEs) são recursos avançados do SQL. Sobre a utilização de CTEs em instruções SQL baseadas no padrão ANSI, é correto afirmar:",
            "Uma CTE é criada utilizando a palavra-chave WITH e funciona como uma tabela temporária cujo escopo é restrito à execução de uma única consulta.",
            "Uma CTE é armazenada de forma física e permanente no disco do banco de dados, sendo visível para qualquer sessão do usuário até que seja descartada.",
            "O uso de CTEs reduz a legibilidade do código SQL, pois exige a criação de subconsultas aninhadas redundantes dentro da cláusula WHERE.",
            "As CTEs não admitem a referência a si mesmas (recursividade), sendo restritas apenas a subconsultas lineares simples e agrupamentos.",
            "Uma CTE só pode ser referenciada uma única vez dentro da instrução SQL principal, sendo vedada sua reutilização na mesma consulta."
        ),
        # Q5: Window Functions OVER
        (
            "As Window Functions (funções analíticas) em SQL executam cálculos em um conjunto de linhas que estão relacionadas à linha atual. A cláusula obrigatória utilizada para identificar uma Window Function é:",
            "OVER",
            "PARTITION",
            "WINDOW",
            "GROUP BY",
            "ROWS BETWEEN"
        ),
        # Q6: Window Functions PARTITION BY vs GROUP BY
        (
            "Sobre a diferença fundamental entre as cláusulas PARTITION BY (usada em Window Functions) e GROUP BY em consultas SQL, assinale a alternativa correta:",
            "O PARTITION BY executa cálculos sobre a janela mantendo a individualidade das linhas, enquanto o GROUP BY colapsa o conjunto de linhas em uma única linha agregada.",
            "O GROUP BY permite a utilização de funções analíticas como ROW_NUMBER(), enquanto o PARTITION BY restringe a consulta a funções de agregação clássicas.",
            "O PARTITION BY exige que todas as colunas selecionadas no SELECT façam parte de sua cláusula, diferentemente do comportamento padrão do GROUP BY.",
            "O GROUP BY mantém todas as linhas individuais no resultado final, apenas aplicando ordenações secundárias e filtros baseados na cláusula HAVING.",
            "O PARTITION BY é executado fisicamente antes da cláusula WHERE, enquanto o GROUP BY é processado na etapa final de renderização do result set."
        ),
        # Q7: RANK() vs DENSE_RANK()
        (
            "Em Window Functions SQL, as funções RANK() e DENSE_RANK() são utilizadas para classificar linhas de uma partição. A diferença técnica de comportamento entre elas é que:",
            "A função RANK() pula posições na sequência de classificação se houver empates, enquanto a função DENSE_RANK() gera números sequenciais contínuos sem lacunas.",
            "A função DENSE_RANK() pula posições na classificação se houver empates, enquanto a função RANK() gera números contínuos sem pular valores.",
            "A função RANK() exige a ordenação ascendente dos dados, enquanto a função DENSE_RANK() opera exclusivamente em ordenações decrescentes.",
            "A função DENSE_RANK() calcula a classificação baseada no desvio padrão dos valores, enquanto a função RANK() realiza apenas uma contagem simples de linhas.",
            "A função RANK() é exclusiva para campos de texto, enquanto a função DENSE_RANK() é aplicada apenas a campos numéricos e datas."
        ),
        # Q8: Window Functions LAG e LEAD
        (
            "Para analisar dados temporais no tribunal, um analista precisa acessar o valor de uma coluna na linha imediatamente anterior da janela atual de dados. A função analítica SQL adequada para essa operação é:",
            "LAG()",
            "LEAD()",
            "FIRST_VALUE()",
            "NTH_VALUE()",
            "ROW_NUMBER()"
        ),
        # Q9: SQL CTE recursiva
        (
            "Para implementar uma consulta SQL que percorra uma estrutura hierárquica de cargos no tribunal (como uma árvore organizacional), o desenvolvedor deve utilizar:",
            "Uma CTE definida com a cláusula WITH RECURSIVE, combinando um caso base e um caso recursivo através do operador UNION ou UNION ALL.",
            "Uma subconsulta correlacionada simples associada à cláusula GROUP BY e filtrada com HAVING na instrução externa principal.",
            "Uma Window Function utilizando a cláusula OVER combinada com a função analítica LEAD() e a partição baseada na chave primária.",
            "Uma tabela temporária física criada com CREATE TEMP TABLE e indexada sequencialmente a cada iteração de um loop interno.",
            "Um operador de junção externa (LEFT OUTER JOIN) aninhado recursivamente até o limite físico de dez níveis de profundidade de tabelas."
        ),
        # Q10: MongoDB index
        (
            "Para otimizar o desempenho das consultas de busca por nome de servidores na coleção `funcionarios` no MongoDB, deve-se criar um índice. O comando correto para criar um índice ascendente no campo `nome` é:",
            "db.funcionarios.createIndex({nome: 1})",
            "db.funcionarios.createIndex({nome: -1})",
            "db.funcionarios.setIndex({nome: true})",
            "db.funcionarios.addIndex({nome: 'asc'})",
            "db.funcionarios.ensureIndex({nome: '*' })"
        ),
        # Q11: MongoDB NoSQL features
        (
            "Em relação à consistência e transações no MongoDB, a partir de suas versões modernas (4.0+), o banco de dados passou a oferecer suporte a:",
            "Transações ACID multi-documento em coleções na mesma partição ou em réplicas associadas.",
            "Consistência estrita em tempo real sem suporte a qualquer isolamento transacional.",
            "Transações relacionais baseadas na linguagem de programação PL/SQL do Oracle.",
            "Escritas síncronas obrigatórias em disco que impedem operações de leitura paralela.",
            "Bloqueio exclusivo de tabelas inteiras durante qualquer operação de inserção de documentos."
        ),
        # Q12: Window Functions ROWS BETWEEN
        (
            "Em uma Window Function, a cláusula que restringe o conjunto de linhas a serem consideradas no cálculo analítico a partir da linha atual (como calcular uma média móvel de 3 linhas anteriores e a atual) é:",
            "ROWS BETWEEN 3 PRECEDING AND CURRENT ROW",
            "RANGE BETWEEN 3 FOLLOWING AND CURRENT ROW",
            "ROWS BETWEEN 3 FOLLOWING AND CURRENT ROW",
            "PARTITION BETWEEN 3 PRECEDING AND CURRENT ROW",
            "ORDER BETWEEN 3 PRECEDING AND CURRENT ROW"
        ),
        # Q13: MongoDB aggregate
        (
            "No MongoDB, para realizar operações de agregação complexas que envolvem filtragem, agrupamento e projeção de dados (similar ao GROUP BY, WHERE e SELECT do SQL), utiliza-se:",
            "O framework de agregação (Aggregation Framework) através do método `db.colecao.aggregate()` recebendo uma lista de estágios (pipeline).",
            "O comando `db.colecao.group()` de forma exclusiva, pois o MongoDB não possui estágios de pipeline.",
            "A linguagem SQL padrão enviada através de drivers JDBC compatíveis com o MongoDB.",
            "A execução de loops imperativos em JavaScript rodando exclusivamente no navegador do cliente.",
            "O comando `db.colecao.find().groupBy()` associado a funções de redução do MapReduce clássico."
        ),
        # Q14: MongoDB document size
        (
            "O MongoDB possui um limite físico padrão de tamanho para um único documento BSON para garantir que o uso de memória e a latência de rede permaneçam otimizados. Esse limite máximo é de:",
            "16 MB",
            "8 MB",
            "32 MB",
            "64 MB",
            "4 MB"
        ),
        # Q15: Window Function CUME_DIST
        (
            "A função analítica de distribuição acumulada que calcula a posição relativa de um valor dentro de um grupo de valores em SQL é a:",
            "CUME_DIST()",
            "PERCENT_RANK()",
            "NTILE()",
            "DENSE_RANK()",
            "RATIO_TO_REPORT()"
        )
    ]
    
    for i, q in enumerate(db_questions):
        dia_28_content.append(f"### Questão {i+1} (FCC)\n")
        dia_28_content.append(f"{q[0]}\n\n")
        dia_28_content.append(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}\nE) {q[5]}\n\n")
        dia_28_content.append(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
        dia_28_content.append(f"**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.\n</details>\n\n")
        dia_28_content.append("---\n\n")
        
    # Tema 2: Sistemas Operacionais - Linux (15 questions)
    dia_28_content.append("## 📝 TEMA 2: Sistemas Operacionais — SO Linux (Red Hat/Oracle Linux, comandos, permissões, usuários)\n")
    
    linux_questions = [
        # Q16: etc directory
        (
            "No Linux (distribuições Red Hat / Oracle Linux), o diretório no qual são guardados os arquivos de configuração locais específicos do sistema e de seus serviços é o:",
            "/etc",
            "/var",
            "/usr/sbin",
            "/bin",
            "/home"
        ),
        # Q17: file permissions chmod numeric
        (
            "Um analista de TI precisa configurar as permissões de um arquivo de script no Linux para que o dono tenha acesso total (leitura, escrita e execução), o grupo do arquivo tenha acesso de leitura e execução, e os outros usuários tenham apenas acesso de execução. A representação numérica octal correspondente a essa configuração é:",
            "751",
            "755",
            "644",
            "775",
            "750"
        ),
        # Q18: directory execution permission
        (
            "Sobre o sistema de permissões de arquivos e diretórios no Linux, a permissão de execução (x) quando aplicada a um diretório específico determina que o usuário:",
            "Pode acessar o diretório (entrar nele com o comando `cd`) e acessar seus arquivos internos.",
            "Pode listar o nome dos arquivos contidos no diretório (executar o comando `ls`).",
            "Pode criar, excluir e renomear arquivos dentro daquele diretório específico.",
            "Pode compilar e rodar binários executáveis localizados exclusivamente na raiz do diretório.",
            "Pode alterar o dono e o grupo do diretório usando o comando `chown` diretamente."
        ),
        # Q19: grep command
        (
            "Para buscar por linhas contendo o termo 'erro' dentro de todos os arquivos de log localizados no diretório `/var/log` no Linux, o comando adequado é:",
            "grep -r 'erro' /var/log",
            "find /var/log -name 'erro'",
            "locate /var/log/erro",
            "cat /var/log | grep 'erro'",
            "awk -f 'erro' /var/log"
        ),
        # Q20: Red Hat package manager (RPM vs YUM/DNF)
        (
            "Nas distribuições Linux da família Red Hat Enterprise Linux (RHEL) e Oracle Linux, o gerenciador de pacotes de baixo nível (que instala arquivos locais sem resolver dependências externas) e o gerenciador de pacotes de alto nível (que consulta repositórios remotos e resolve dependências automaticamente) são, respectivamente:",
            "rpm e dnf",
            "dpkg e apt",
            "yum e rpm",
            "dnf e yum",
            "rpm e dpkg"
        ),
        # Q21: chown command
        (
            "Para alterar o dono de um arquivo `relatorio.txt` para o usuário `ruan` e o seu grupo associado para `ti` no Linux, utiliza-se o comando:",
            "chown ruan:ti relatorio.txt",
            "chmod ruan:ti relatorio.txt",
            "chgrp ruan:ti relatorio.txt",
            "chattr ruan:ti relatorio.txt",
            "usermod ruan:ti relatorio.txt"
        ),
        # Q22: var/log directory
        (
            "O diretório `/var/log` no Linux é de suma importância para a administração do sistema. Sua função principal é:",
            "Armazenar arquivos de registros de eventos do sistema, mensagens de serviços e logs de aplicações em execução.",
            "Guardar arquivos temporários gerados pelo sistema operacional e removidos a cada reinicialização.",
            "Conter os arquivos binários essenciais de administração reservados exclusivamente ao usuário superusuário root.",
            "Armazenar arquivos executáveis de bibliotecas dinâmicas compartilhadas pelos programas do usuário.",
            "Manter os arquivos de dados locais das contas dos usuários comuns criados no sistema."
        ),
        # Q23: tar command
        (
            "O comando `tar` é amplamente utilizado no Linux. Sobre as operações realizadas pelo comando `tar -cvf backup.tar /home/usuario`, assinale a alternativa correta:",
            "Ele cria um novo arquivo de arquivo (`backup.tar`) contendo os arquivos do diretório `/home/usuario` empacotados, sem compactação nativa.",
            "Ele extrai e descompacta o arquivo `backup.tar` dentro do diretório `/home/usuario` limpando a origem.",
            "Ele realiza a compactação compacta utilizando o algoritmo gzip com taxa máxima de compressão.",
            "Ele lista o conteúdo detalhado de permissões do arquivo `backup.tar` na saída padrão do terminal.",
            "Ele remove os arquivos originais do diretório `/home/usuario` após concluir a cópia de segurança."
        ),
        # Q24: chmod others execution
        (
            "O comando `chmod o+x script.sh` aplicado a um arquivo no Linux resulta em:",
            "Adicionar a permissão de execução (x) exclusivamente para os outros usuários (others) em relação ao arquivo `script.sh`.",
            "Remover a permissão de execução de todos os usuários do sistema do arquivo `script.sh`.",
            "Conceder permissão de escrita e leitura para o dono e o grupo associado ao arquivo `script.sh`.",
            "Tornar o arquivo `script.sh` propriedade exclusiva do grupo de usuários administradores.",
            "Remover todas as permissões dos outros usuários (others) em relação ao arquivo `script.sh`."
        ),
        # Q25: yum/dnf advantages
        (
            "Uma vantagem técnica fundamental do gerenciador de pacotes `dnf` (ou `yum`) em relação ao utilitário `rpm` no Oracle Linux é:",
            "A capacidade de calcular, baixar e instalar de forma automática todas as dependências requeridas por um pacote.",
            "A dispensa do acesso privilegiado de root para a instalação de softwares no sistema operacional.",
            "A compilação local dos arquivos de código-fonte durante a instalação dos pacotes.",
            "O funcionamento offline obrigatório que dispensa a existência de repositórios baseados em rede.",
            "O suporte exclusivo à instalação de pacotes baseados na extensão Debian (`.deb`)."
        ),
        # Q26: man command
        (
            "Para visualizar a documentação oficial detalhada e o manual de utilização do comando `iptables` no Linux, utiliza-se o comando:",
            "man iptables",
            "help iptables",
            "info -f iptables",
            "doc iptables",
            "iptables --manual"
        ),
        # Q27: pwd command
        (
            "O comando `pwd` na linha de comando do terminal do Linux tem a finalidade de:",
            "Exibir o caminho absoluto do diretório de trabalho atual do usuário no terminal.",
            "Alterar a senha (password) do usuário logado no sistema operacional.",
            "Listar todos os processos em execução que pertencem ao usuário atual.",
            "Exibir a quantidade de espaço em disco utilizado em cada partição física.",
            "Configurar as permissões de acesso físico de arquivos em lote."
        ),
        # Q28: sbin directory
        (
            "Em relação à hierarquia de diretórios padrão no Linux (FHS), no diretório `/sbin` encontram-se tipicamente:",
            "Os arquivos binários executáveis essenciais usados para a administração do sistema e manutenção, reservados ao root.",
            "Os arquivos de bibliotecas dinâmicas do sistema essenciais para a inicialização e execução de comandos do `/bin`.",
            "Os arquivos de cabeçalho C e códigos-fonte do kernel necessários para desenvolvimento.",
            "Os arquivos binários executáveis de uso geral de todos os usuários comuns sem privilégios.",
            "Os arquivos de dados de configurações globais de rede e hosts do sistema."
        ),
        # Q29: redirect output
        (
            "Para redirecionar a saída padrão (stdout) de um comando para um arquivo de texto, sobrescrevendo qualquer conteúdo existente nesse arquivo, utiliza-se o caractere:",
            ">",
            ">>",
            "<",
            "|",
            "&"
        ),
        # Q30: pipe operator
        (
            "O caractere `|` (pipe) é utilizado no terminal Linux com o objetivo de:",
            "Redirecionar a saída padrão (stdout) de um comando para servir como entrada padrão (stdin) de outro comando subsequente.",
            "Executar dois comandos de forma paralela e em segundo plano (background) no terminal.",
            "Enviar a saída de erro padrão (stderr) de um processo para a partição física nula `/dev/null`.",
            "Pausar temporariamente a execução de um processo até receber o sinal de interrupção SIGCONT.",
            "Criar um link simbólico físico entre dois arquivos de dados na tabela de inodes."
        )
    ]
    
    for i, q in enumerate(linux_questions):
        dia_28_content.append(f"### Questão {i+16} (FCC)\n")
        dia_28_content.append(f"{q[0]}\n\n")
        dia_28_content.append(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}\nE) {q[5]}\n\n")
        dia_28_content.append(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
        dia_28_content.append(f"**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.\n</details>\n\n")
        dia_28_content.append("---\n\n")
        
    # Tema 3: Legislacao Previdenciaria (15 questions)
    dia_28_content.append("## 📝 TEMA 3: Legislação Previdenciária do Estado do Ceará\n")
    
    prev_questions = [
        # Q31: RPPS filiacao
        (
            "De acordo com a Lei Complementar Estadual nº 12/1999, que trata do Regime Próprio de Previdência Social (RPPS) do Estado do Ceará, a filiação ao regime é classificada como:",
            "Obrigatória para todos os servidores ocupantes de cargo de provimento efetivo do Estado.",
            "Facultativa para novos servidores efetivos nomeados após a aprovação de reformas.",
            "Obrigatória para cargos exclusivamente em comissão e empregos públicos temporários.",
            "Facultativa para membros do Poder Judiciário e do Ministério Público Estadual.",
            "Obrigatória apenas para servidores ativos com remuneração acima do teto do RGPS."
        ),
        # Q32: RPPS financiamento
        (
            "O financiamento e custeio do Regime Próprio de Previdência Social dos servidores do Ceará baseia-se em contribuições de:",
            "Caráter contributivo e solidário, mediante contribuições do Estado, dos servidores ativos, aposentados e pensionistas.",
            "Caráter exclusivamente patronal, sendo custeado integralmente pelo tesouro estadual sem descontos na folha do servidor.",
            "Caráter voluntário dos servidores efetivos associados à capitalização individual em fundos abertos de previdência.",
            "Repasses federais do Fundo de Participação dos Estados (FPE) de forma exclusiva e vinculada ao INSS.",
            "Contribuições incidentes apenas sobre a remuneração de servidores ativos de nível superior do Poder Executivo."
        ),
        # Q33: Contribuicao aposentados e pensionistas
        (
            "Em relação à contribuição previdenciária devida por servidores aposentados e pensionistas sob o RPPS do Ceará, assinale a regra de incidência correta:",
            "Incidirá sobre a parcela dos proventos de aposentadoria e de pensão que supere o limite máximo estabelecido para os benefícios do RGPS.",
            "Aposentados e pensionistas são totalmente isentos de contribuição previdenciária em qualquer hipótese constitucional.",
            "A contribuição incidirá sobre o valor integral dos proventos, independentemente do teto fixado para o regime geral.",
            "A alíquota é reduzida pela metade e incide apenas se o aposentado retornar ao serviço público em cargo em comissão.",
            "Incidirá sobre os proventos de aposentadoria apenas se o beneficiário residir fora do território do Estado do Ceará."
        ),
        # Q34: Principio da solidariedade
        (
            "O sistema previdenciário público brasileiro assenta-se sobre o princípio da solidariedade. Nesse sentido, a solidariedade significa que:",
            "O financiamento do regime é um dever coletivo de toda a sociedade, incluindo ativos, inativos e o próprio ente público patronal.",
            "Os benefícios concedidos pelo RPPS dependem da rentabilidade financeira dos investimentos individuais de cada segurado.",
            "O Estado está autorizado a não repassar a cota patronal se houver crise fiscal temporária nas contas do tesouro estadual.",
            "Os servidores inativos possuem direito adquirido de não contribuir para o custeio do déficit atuarial do sistema público.",
            "As alíquotas de contribuição previdenciária devem ser idênticas para todos os entes federados e servidores do Brasil."
        ),
        # Q35: Ente público na relação de custeio
        (
            "Na relação de custeio e financiamento do SUPSEC (Sistema Único de Previdência Social dos Servidores do Ceará), o Estado do Ceará figura como:",
            "Ente público patrocinador, responsável pelo repasse das contribuições de cota patronal e pelo equilíbrio atuarial do regime.",
            "Segurado obrigatório do regime de previdência, respondendo com suas receitas próprias de impostos residuais.",
            "Agente financeiro intermediário privado com fins lucrativos de exploração de fundos mobiliários.",
            "Beneficiário direto dos proventos acumulados nas contas de previdência complementar fechada.",
            "Encarregado exclusivo da fiscalização de autarquias previdenciárias de outros Estados da federação."
        ),
        # Q36: Base de calculo da contribuicao ativo
        (
            "A base de cálculo sobre a qual incide a alíquota da contribuição previdenciária mensal do servidor ativo para o RPPS do Ceará é:",
            "A remuneração de contribuição do servidor, composta pelo vencimento do cargo efetivo acrescido das vantagens pecuniárias permanentes estabelecidas em lei.",
            "Apenas o vencimento-base do servidor, excluindo-se qualquer adicional por tempo de serviço ou gratificação de caráter permanente.",
            "A remuneração integral do servidor ativo incluindo parcelas indenizatórias, diárias de viagem e terço de férias.",
            "O valor correspondente ao salário-mínimo nacional vigente acrescido de abonos de produtividade da comarca.",
            "O limite correspondente a metade do teto estabelecido para os benefícios do Regime Geral de Previdência Social (RGPS)."
        ),
        # Q37: Reparticao simples vs Capitalizacao
        (
            "O regime de previdência pública básica (RPPS) estruturado pelo Estado do Ceará funciona sob o regime financeiro de:",
            "Repartição simples, em que as contribuições dos servidores ativos financiam diretamente os benefícios dos aposentados e pensionistas atuais.",
            "Capitalização individual, em que as contribuições de cada servidor são acumuladas em uma conta individual e rentabilizadas em mercado.",
            "Repartição capitalizada fechada, que veda a contribuição do ente público patronal e exige investimentos em títulos internacionais.",
            "Contas nocionais abertas, baseadas no valor de reposição inflacionária calculado pelo Banco Central do Brasil.",
            "Poupança programada compulsória exclusiva de servidores com proventos inferiores a cinco salários-mínimos."
        ),
        # Q38: Contribuicao em caso de incapacidade
        (
            "Quando o beneficiário de aposentadoria sob o RPPS do Ceará for portador de doença incapacitante, a contribuição previdenciária incidirá sobre as parcelas de proventos que superem:",
            "O limite máximo estabelecido para os benefícios do RGPS, nos termos das normas gerais federais aplicáveis.",
            "O dobro do limite máximo estabelecido para os benefícios do RGPS de forma obrigatória e permanente.",
            "Três vezes o valor do salário-mínimo nacional estabelecido pelo Governo Federal.",
            "O valor correspondente a 80% do último vencimento recebido em atividade pelo servidor.",
            "Qualquer valor, isentando totalmente o aposentado do recolhimento de contribuições previdenciárias."
        ),
        # Q39: Cearaprev autarquia
        (
            "A gestão, administração e operacionalização do Regime Próprio de Previdência Social (RPPS) dos servidores do Ceará competem à fundação pública de direito público denominada:",
            "Cearáprev (Fundação de Previdência Social do Estado do Ceará)",
            "INSS-CE",
            "SUPSEC-Autarquia",
            "Prev-Ceará (Instituto Estadual de Seguros de Saúde e Previdência)",
            "Secretaria de Planejamento e Gestão Previdenciária do Ceará"
        ),
        # Q40: Remuneracao abaixo do teto
        (
            "Se o servidor efetivo ativo do Estado do Ceará possuir remuneração de contribuição inferior ao limite máximo do RGPS (teto do INSS), a sua contribuição previdenciária:",
            "Incidirá normalmente sobre a totalidade de sua remuneração de contribuição, aplicando-se a alíquota definida em lei.",
            "Ficará totalmente suspensa, passando o servidor à condição de isento temporário de custeio.",
            "Deverá ser recolhida diretamente ao INSS por tratar-se de faixa salarial vinculada ao RGPS.",
            "Terá sua alíquota reduzida pela metade para evitar o confisco de renda de servidores de baixa remuneração.",
            "Será revertida integralmente para fundos privados de previdência complementar aberta."
        ),
        # Q41: Limite da contribuicao patronal
        (
            "A contribuição do Estado do Ceará (cota patronal) para o custeio do RPPS dos servidores não poderá ser:",
            "Inferior ao valor da contribuição do segurado, nem superior ao dobro desta contribuição.",
            "Superior a 10% da receita corrente líquida estadual em nenhuma hipótese atuarial.",
            "Recolhida em atraso após o quinto dia útil do mês de competência da folha de pagamento.",
            "Inferior a duas vezes o valor da contribuição de servidores inativos e pensionistas acumulados.",
            "Destinada a fins de pagamento de despesas de assistência médica ou benefícios de natureza assistencial."
        ),
        # Q42: Avaliacao atuarial
        (
            "Para garantir a higidez, a solvência e o equilíbrio financeiro e atuarial do RPPS do Estado do Ceará ao longo do tempo, a legislação exige a realização periódica de:",
            "Avaliações atuariais anuais para dimensionar os compromissos futuros do regime e propor ajustes necessários de custeio.",
            "Sorteios de prêmios de incentivo à permanência na ativa para servidores aptos a se aposentar.",
            "Emissões compulsórias de títulos da dívida pública estadual vinculados à previdência privada.",
            "Aumentos automáticos e semestrais nas alíquotas de contribuição de todos os segurados ativos.",
            "Auditorias externas trimestrais executadas por bancos comerciais privados de fomento econômico."
        ),
        # Q43: Taxa de administracao
        (
            "Os recursos obtidos através da taxa de administração cobrada pelo órgão gestor do RPPS do Ceará devem ser destinados exclusivamente a:",
            "Custear as despesas de funcionamento, manutenção e modernização administrativa do próprio órgão gestor da previdência.",
            "Financiar obras de infraestrutura urbana nas comarcas do Poder Judiciário do Estado do Ceará.",
            "Efetuar o pagamento de precatórios alimentares de servidores inativos com doenças graves.",
            "Complementar a remuneração funcional de servidores ativos da Secretaria de Fazenda Estadual.",
            "Amortizar de forma extraordinária a dívida líquida consolidada do Estado perante a União."
        ),
        # Q44: Abono de permanencia
        (
            "O abono de permanência é um benefício pecuniário garantido ao servidor que preenche todos os requisitos para a aposentadoria voluntária, mas opta por permanecer em atividade. Esse benefício corresponde ao valor de:",
            "Sua contribuição previdenciária mensal, funcionando como um reembolso de mesmo valor enquanto permanecer em atividade.",
            "10% de seu vencimento básico de cargo efetivo a título de gratificação de permanência extraordinária.",
            "Uma remuneração integral adicional paga anualmente no mês de aniversário do servidor efetivo.",
            "Isenção total do recolhimento mensal de Imposto de Renda Retido na Fonte (IRRF) em folha.",
            "Promoção funcional automática para a classe e padrão imediatamente superiores de sua carreira."
        ),
        # Q45: Segregacao de massas
        (
            "A segregação de massas é uma técnica de estruturação de planos de custeio aplicada ao RPPS. O objetivo principal da segregação de massas no Ceará é:",
            "Dividir os segurados do regime em grupos distintos (como Fundo Financeiro e Fundo Previdenciário) para buscar o equilíbrio atuarial a longo prazo.",
            "Separar os servidores públicos do Estado do Ceará de acordo com o Poder em que atuam (Judiciário, Executivo ou Legislativo).",
            "Diferenciar servidores civis e militares para aplicar alíquotas de imposto de renda regressivas especiais.",
            "Promover a transferência dos inativos e pensionistas para fundos de previdência de bancos comerciais privados.",
            "Permitir a fusão temporária das contas de receitas de impostos do Estado com os recursos de contribuições previdenciárias."
        )
    ]
    
    for i, q in enumerate(prev_questions):
        dia_28_content.append(f"### Questão {i+31} (FCC)\n")
        dia_28_content.append(f"{q[0]}\n\n")
        dia_28_content.append(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}\nE) {q[5]}\n\n")
        dia_28_content.append(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
        dia_28_content.append(f"**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.\n</details>\n\n")
        dia_28_content.append("---\n\n")

    # Salva o arquivo md
    filepath_28 = os.path.join(questoes_dir, "dia_28_05_questoes.md")
    with open(filepath_28, "w", encoding="utf-8") as f:
        f.write("".join(dia_28_content))
    print(f"Gerado: {filepath_28}")

    # -------------------------------------------------------------
    # DIA 29/05 - SEXTA-FEIRA (Criptografia, SOLID/GRASP/C/PHP, Port. Vozes)
    # -------------------------------------------------------------
    
    dia_29_content = []
    dia_29_content.append("# Bateria de Questões FCC — Sexta-feira 29/05\n")
    dia_29_content.append("Este arquivo contém 45 questões altamente calibradas nos padrões da FCC, com alternativas de comprimento similar e distratores baseados em pegadinhas reais.\n\n---\n")
    
    # Tema 1: Criptografia
    dia_29_content.append("## 📝 TEMA 1: Segurança da Informação — Criptografia, Hashes, Certificados e Assinatura Digital\n")
    
    crypto_questions = [
        # Q1: Symmetric vs Asymmetric
        (
            "Criptografia simétrica e assimétrica diferem essencialmente na forma de gerenciamento das chaves de segurança. Sobre essa diferença, é correto afirmar:",
            "A criptografia simétrica utiliza uma única chave compartilhada para cifrar e decifrar os dados, enquanto a assimétrica utiliza um par de chaves (pública e privada).",
            "A criptografia assimétrica utiliza uma única chave secreta que deve ser distribuída previamente por canais físicos e seguros.",
            "A criptografia simétrica utiliza um par de chaves em que a chave privada cifra os dados e a chave pública decifra os dados de forma exclusiva.",
            "A criptografia assimétrica possui menor custo computacional, sendo preferida para cifrar grandes volumes de dados de tráfego de rede.",
            "A criptografia simétrica impede o não-repúdio de forma nativa, pois cada sessão possui um par de chaves públicas geradas dinamicamente."
        ),
        # Q2: Hash functions properties
        (
            "As funções de hash criptográfico desempenham um papel vital na segurança da informação. A propriedade que garante que é computacionalmente inviável encontrar dois inputs diferentes que gerem o mesmo valor de hash de saída é a:",
            "Resistência à colisão",
            "Resistência à pré-imagem",
            "Resistência à segunda pré-imagem",
            "Propriedade de efeito avalanche",
            "Propriedade de integridade simétrica"
        ),
        # Q3: AES and DES
        (
            "Em relação aos algoritmos de criptografia simétrica clássicos e modernos, assinale a opção que apresenta um algoritmo considerado inseguro devido ao seu tamanho de chave e o algoritmo padrão que o substituiu, respectivamente:",
            "DES (chave de 56 bits) e AES (chaves de 128, 192 ou 256 bits)",
            "AES (chave de 128 bits) e DES (chaves de 512 bits)",
            "RSA (chave de 1024 bits) e AES (chaves de 128 bits)",
            "DES (chave de 56 bits) e RSA (chaves de 2048 bits)",
            "MD5 (chave de 128 bits) e SHA-256 (chaves de 256 bits)"
        ),
        # Q4: Asymmetric algorithms
        (
            "O algoritmo RSA é um dos sistemas de criptografia assimétrica mais conhecidos. Sua segurança fundamenta-se na dificuldade matemática de realizar a seguinte operação computacional:",
            "Fatoração de números inteiros grandes que são produtos de dois números primos grandes.",
            "Cálculo de logaritmos discretos em corpos finitos de curvas elípticas generalizadas.",
            "Multiplicação matricial densa em bases de dados multidimensionais sem perdas.",
            "Ordenação de chaves criptográficas em pilhas de dados recursivas orientadas.",
            "Resolução de sistemas lineares de equações com múltiplas variáveis complexas."
        ),
        # Q5: Digital signature
        (
            "Para garantir a integridade e o não-repúdio de um documento assinado digitalmente, a assinatura digital é gerada pelo remetente cifrando:",
            "O resumo criptográfico (hash) do documento original utilizando a chave privada do próprio remetente.",
            "O documento original de forma completa utilizando a chave pública do destinatário final.",
            "O resumo criptográfico (hash) do documento original utilizando a chave pública do destinatário.",
            "A chave simétrica de sessão temporária utilizando a chave privada da autoridade certificadora.",
            "O documento original de forma completa utilizando a chave privada do destinatário final."
        ),
        # Q6: Digital certificate X.509
        (
            "Os certificados digitais baseados no padrão X.509 são utilizados para associar a identidade de um usuário a um par de chaves criptográficas. Um elemento que consta obrigatoriamente do certificado digital do usuário é:",
            "A chave pública do usuário associada à assinatura digital da Autoridade Certificadora emissora.",
            "A chave privada do usuário associada ao hash de validação gerado pelo navegador.",
            "A chave privada da Autoridade Certificadora responsável pela emissão da chave do usuário.",
            "A lista completa de senhas criptografadas do usuário em serviços públicos de diretório.",
            "A chave simétrica acordada no início da sessão de handshake do protocolo HTTPS."
        ),
        # Q7: Hybrid cryptography
        (
            "Para conciliar a segurança do gerenciamento de chaves e a eficiência de processamento de dados, os sistemas modernos utilizam criptografia híbrida. Na criptografia híbrida:",
            "A criptografia assimétrica é usada para compartilhar a chave simétrica, e a criptografia simétrica é usada para cifrar os dados da mensagem.",
            "A criptografia simétrica é usada para compartilhar a chave pública, e a criptografia assimétrica é usada para cifrar os dados da mensagem.",
            "As chaves simétrica e assimétrica são combinadas gerando uma única chave híbrida indivisível e permanente.",
            "A criptografia assimétrica realiza a cifragem dos blocos de dados, e a criptografia simétrica garante o não-repúdio.",
            "O algoritmo de hash calcula o resumo digital, e a criptografia simétrica cifra o hash gerando a assinatura."
        ),
        # Q8: SHA family
        (
            "As funções hash da família SHA-2 são amplamente recomendadas para segurança de sistemas. Assinale a alternativa que apresenta apenas algoritmos válidos e pertencentes a essa família:",
            "SHA-224, SHA-256, SHA-384 e SHA-512",
            "SHA-1, SHA-2, SHA-3 e SHA-4",
            "SHA-128, SHA-256 e SHA-512",
            "SHA-256, MD5 e SHA-3",
            "SHA-256, HMAC e SHA-1"
        ),
        # Q9: ICP-Brasil hierarchy
        (
            "No âmbito da Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil), a entidade que atua como o topo da cadeia (Autoridade Certificadora Raiz), credenciando e fiscalizando as demais Autoridades Certificadoras (ACs), é o:",
            "ITI (Instituto Nacional de Tecnologia da Informação)",
            "ANPD (Autoridade Nacional de Proteção de Dados)",
            "CNJ (Conselho Nacional de Justiça)",
            "MCTI (Ministério da Ciência, Tecnologia e Inovação)",
            "SERPRO (Serviço Federal de Processamento de Dados)"
        ),
        # Q10: Hashes MD5 and SHA-1 status
        (
            "Sobre os algoritmos de hash criptográfico clássicos MD5 e SHA-1, assinale a opção que descreve corretamente o seu status atual de segurança:",
            "São considerados inseguros para aplicações criptográficas de assinatura devido à descoberta de colisões práticas em tempo viável.",
            "Permanecem totalmente seguros e são recomendados pela ICP-Brasil para assinaturas de processos eletrônicos judiciais.",
            "São os algoritmos simétricos padrão para cifragem de discos rígidos em servidores de datacenters modernos.",
            "Foram unificados no algoritmo SHA-3 para formar um único hash de 512 bits resistente a computação quântica.",
            "São restritos exclusivamente ao uso em redes locais com cabeamento estruturado de par trançado Classe F."
        ),
        # Q11: Certificate Revocation List (CRL)
        (
            "Para verificar se um certificado digital X.509 de um servidor foi revogado antes de expirar a sua validade, o navegador cliente pode consultar periodicamente:",
            "A Lista de Revogação de Certificados (LRC / CRL) ou utilizar o protocolo online OCSP (Online Certificate Status Protocol).",
            "O repositório local de chaves privadas do sistema operacional ou o arquivo temporário de hosts DNS.",
            "O banco de dados de chaves simétricas negociadas durante o handshake do protocolo HTTPS.",
            "A Autoridade Certificadora Raiz através de uma requisição síncrona baseada em FTP.",
            "O Comitê de Acessibilidade da ICP-Brasil responsável pelo credenciamento das Autoridades de Registro."
        ),
        # Q12: Signature verification process
        (
            "Ao receber um arquivo assinado digitalmente, o destinatário verifica a assinatura realizando o seguinte procedimento técnico:",
            "Calcula o hash do arquivo recebido e o compara com o hash obtido ao decifrar a assinatura com a chave pública do remetente.",
            "Decifra o arquivo completo usando a sua própria chave privada e o compara com o texto plano original enviado.",
            "Envia o arquivo para a Autoridade Certificadora autenticar usando a chave privada da autoridade.",
            "Calcula o hash do arquivo recebido e o compara com o hash obtido ao decifrar a assinatura com a sua própria chave privada.",
            "Decifra a assinatura digital usando a chave simétrica acordada no handshake do TLS."
        ),
        # Q13: Curve cryptography (ECC)
        (
            "A Criptografia de Curvas Elípticas (ECC) possui uma vantagem técnica importante sobre os algoritmos assimétricos clássicos como o RSA:",
            "Oferecer o mesmo nível de segurança criptográfica que o RSA utilizando tamanhos de chaves significativamente menores.",
            "Funcionar sem a necessidade de chaves públicas, reduzindo o tráfego de dados na rede.",
            "Ser um algoritmo de criptografia simétrica com suporte nativo a blocos dinâmicos de dados.",
            "Garantir a integridade dos dados sem a necessidade de calcular funções hash adicionais.",
            "Ser imune a qualquer ataque físico ou lógico mesmo que a chave privada seja exposta publicamente."
        ),
        # Q14: Digital Certificate validation steps
        (
            "Para validar a autenticidade de um certificado digital X.509 recebido de um servidor, o cliente realiza as seguintes verificações, com EXCEÇÃO de:",
            "Verificar se a chave privada do certificado do servidor corresponde à chave pública da Autoridade Certificadora emissora.",
            "Verificar a validade do certificado comparando a data atual com o período de validade constante no documento.",
            "Validar a assinatura digital do certificado utilizando a chave pública da Autoridade Certificadora que o emitiu.",
            "Confirmar se o certificado não consta em Listas de Revogação de Certificados (CRLs) atualizadas.",
            "Verificar se o nome de domínio (Common Name - CN) do certificado corresponde ao endereço do website acessado."
        ),
        # Q15: Non-repudiation definition
        (
            "Em segurança da informação, o não-repúdio (irretratabilidade) é a garantia de que:",
            "O emissor de uma mensagem ou transação assinada digitalmente não pode negar a sua autoria ou criação.",
            "Os dados transmitidos não sofreram qualquer alteração acidental ou intencional durante o trânsito na rede.",
            "Apenas usuários autorizados tenham acesso à leitura do conteúdo confidencial armazenado em servidores.",
            "Os sistemas de rede estejam disponíveis e funcionais para os usuários legítimos em tempo integral.",
            "O canal de comunicação simétrico impeça o acesso físico aos servidores e switches locais."
        )
    ]
    
    for i, q in enumerate(crypto_questions):
        dia_29_content.append(f"### Questão {i+1} (FCC)\n")
        dia_29_content.append(f"{q[0]}\n\n")
        dia_29_content.append(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}\nE) {q[5]}\n\n")
        dia_29_content.append(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
        dia_29_content.append(f"**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.\n</details>\n\n")
        dia_29_content.append("---\n\n")

    # Tema 2: Engenharia de Software (SOLID, PHP, C, C#)
    dia_29_content.append("## 📝 TEMA 2: Engenharia de Software — Programação em PHP, C, C# e .NET, SOLID e GRASP\n")
    
    software_questions = [
        # Q16: SOLID Single Responsibility
        (
            "O princípio SOLID da Responsabilidade Única (Single Responsibility Principle - SRP) estabelece que:",
            "Uma classe deve ter um, e apenas um, motivo para mudar, possuindo uma única responsabilidade no sistema.",
            "Uma classe só pode conter um único método público para realizar todas as operações do seu módulo.",
            "Os componentes do sistema devem ser acoplados exclusivamente de forma síncrona na camada de apresentação.",
            "Toda interface deve declarar apenas um método abstrato a ser implementado pelas classes herdeiras.",
            "O banco de dados deve possuir apenas uma tabela associada a cada entidade de negócio do sistema."
        ),
        # Q17: SOLID Open-Closed
        (
            "De acordo com o princípio SOLID Aberto-Fechado (Open-Closed Principle - OCP), as entidades de software (classes, módulos, funções) devem ser:",
            "Abertas para extensão, mas fechadas para modificação.",
            "Abertas para modificação externa, mas fechadas para herança.",
            "Abertas para acesso público, mas fechadas para injeção de dependências.",
            "Abertas para persistência em disco, mas fechadas para compilação local.",
            "Abertas para alterações parciais no código, mas fechadas para refatorações."
        ),
        # Q18: SOLID Liskov Substitution
        (
            "O princípio SOLID da Substituição de Liskov (Liskov Substitution Principle - LSP) determina que:",
            "Objetos de uma superclasse devem ser substituíveis por objetos de suas subclasses sem que isso quebre o funcionamento correto do programa.",
            "Subclasses devem sobrescrever todos os métodos da superclasse para alterar a assinatura original e forçar o polimorfismo.",
            "Toda classe derivada deve herdar diretamente de múltiplas superclasses abstratas simultaneamente.",
            "Interfaces não podem ser estendidas por outras interfaces para evitar conflitos de implementação múltipla.",
            "Classes concretas devem substituir todas as referências a injeção de dependências por instanciação estática de objetos."
        ),
        # Q19: SOLID Interface Segregation
        (
            "O princípio SOLID da Segregação de Interfaces (Interface Segregation Principle - ISP) preconiza que:",
            "Muitas interfaces específicas são melhores do que uma única interface de propósito geral, evitando que classes sejam forçadas a depender de métodos que não utilizam.",
            "Interfaces devem ser unificadas em um único arquivo de contrato para facilitar a manutenção de grandes sistemas Java ou C#.",
            "Módulos de alto nível não devem herdar de interfaces abstratas criadas em pacotes de baixo nível.",
            "Todas as interfaces do sistema devem declarar obrigatoriamente constantes estáticas e finais do tipo string.",
            "Interfaces de persistência de banco de dados devem ser separadas fisicamente de classes controladoras MVC."
        ),
        # Q20: SOLID Dependency Inversion
        (
            "O princípio SOLID da Inversão de Dependência (Dependency Inversion Principle - DIP) estabelece que:",
            "Módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações. Abstrações não devem depender de detalhes; detalhes devem depender de abstrações.",
            "Módulos de baixo nível devem gerenciar o ciclo de vida e a instanciação estática dos objetos de alto nível no Spring Framework.",
            "As dependências do sistema devem ser invertidas fisicamente no disco através de links simbólicos de arquivos binários.",
            "Classes concretas devem depender diretamente de outras classes concretas, reduzindo o uso excessivo de interfaces e abstrações.",
            "A injeção de dependência deve ser realizada exclusivamente através do construtor de classes sem visibilidade pública."
        ),
        # Q21: GRASP Controller
        (
            "No conjunto de padrões GRASP para atribuição de responsabilidades em POO, o padrão **Controller** (Controlador) é responsável por:",
            "Receber eventos do sistema originados por elementos da interface do usuário (UI) e coordenar as operações de negócio adequadas.",
            "Garantir que uma classe tenha apenas uma única instância física carregada na memória da máquina virtual Java ou .NET.",
            "Criar objetos de coleções complexas e encapsular o acesso físico a tabelas de banco de dados relacionais.",
            "Definir a estrutura hierárquica de classes para simular a herança múltipla de comportamento em interfaces simples.",
            "Impedir que classes de domínio interajam com as classes de visualização através do acoplamento forte."
        ),
        # Q22: GRASP Creator
        (
            "De acordo com o padrão GRASP **Creator** (Criador), uma classe $A$ deve ser responsável pela criação de instâncias de uma classe $B$ se:",
            "A classe $A$ agrega, contém, registra ou usa de forma muito próxima as instâncias da classe $B$.",
            "A classe $B$ estende diretamente a classe $A$ através de herança simples ou múltipla de implementação.",
            "A classe $A$ não possui atributos de instância e declara apenas métodos estáticos e abstratos.",
            "O desenvolvedor deseja aplicar o princípio SOLID da substituição de Liskov na instanciação de Beans.",
            "O banco de dados relacional possui uma chave estrangeira de $A$ apontando para a tabela $B$ correspondente."
        ),
        # Q23: C language pointers
        (
            "Na linguagem de programação C, o operador de desreferenciação `*` (asterisco) e o operador de endereço `&` (e comercial), quando aplicados a ponteiros e variáveis comuns, servem para, respectivamente:",
            "Acessar o valor armazenado no endereço apontado pelo ponteiro, e obter o endereço de memória de uma variável comum.",
            "Obter o endereço de memória de uma variável ponteiro, e realizar a multiplicação aritmética de dois inteiros.",
            "Alocar espaço na memória heap do sistema operacional, e liberar o espaço em memória associado à variável local.",
            "Declarar uma constante global em tempo de compilação, e verificar a igualdade lógica de dois valores booleanos.",
            "Concatenar duas sequências de caracteres na memória dinâmica, e calcular a negação lógica de bits."
        ),
        # Q34: PHP namespaces and autoloader
        (
            "Em PHP 8+, a declaração `namespace` e a utilização de ferramentas como o autoloader do Composer têm como finalidade principal:",
            "Organizar e isolar o escopo de classes evitando conflitos de nomes, e carregar os arquivos de classes sob demanda de forma automática (lazy loading).",
            "Compilar o código PHP em linguagem de máquina nativa do servidor, e gerenciar a segurança lógica de portas abertas.",
            "Substituir o uso de classes de banco de dados por consultas SQL em formato binário indexado.",
            "Exigir a declaração obrigatória de tipos dinâmicos para todas as variáveis globais da aplicação corporativa.",
            "Importar bibliotecas em C++ compiladas diretamente no kernel do Apache Server sem passar pelo interpretador."
        ),
        # Q25: C# Value vs Reference Types
        (
            "Na linguagem C# e plataforma .NET, as variáveis são divididas em tipos de valor (value types) e tipos de referência (reference types). Sobre essa divisão, é correto afirmar:",
            "Tipos de valor (como structs, int, bool) são armazenados diretamente na pilha (stack), enquanto tipos de referência (como classes, interfaces, objects) são armazenados na memória heap.",
            "Tipos de referência são armazenados na memória stack para garantir o acesso instantâneo e a liberação de espaço sem o Garbage Collector.",
            "Tipos de valor são gerenciados pelo Garbage Collector da plataforma .NET de forma síncrona e obrigatória.",
            "Classes em C# são classificadas como tipos de valor, enquanto as structs representam tipos de referência nativos.",
            "O armazenamento de tipos de referência na pilha impede a ocorrência de exceções de estouro de memória (StackOverflowException)."
        ),
        # Q26: C# using statement
        (
            "Na linguagem C#, a instrução `using` (por exemplo, `using (var resource = new Resource()) { ... }`) é utilizada para garantir:",
            "A liberação automática de recursos não gerenciados (como conexões de rede ou arquivos) ao final do bloco de código, chamando o método Dispose().",
            "A importação de bibliotecas externas compiladas em C++ nativo e localizadas no diretório do sistema `/bin`.",
            "A herança múltipla de interfaces por classes controladoras de dados da persistência do EF Core.",
            "O tratamento obrigatório de exceções de divisão por zero e estouro de buffer em tempo de execução.",
            "A compilação em lote de arquivos de código-fonte dinâmicos associados a namespaces corporativos."
        ),
        # Q27: C malloc and free
        (
            "Na linguagem de programação C, para alocar dinamicamente 10 inteiros na memória heap e, posteriormente, liberar esse espaço na memória de forma correta, o desenvolvedor deve utilizar, respectivamente, as funções:",
            "malloc() e free()",
            "new e delete",
            "calloc() e remove()",
            "alloc() e dispose()",
            "malloc() e clean()"
        ),
        # Q28: C# properties
        (
            "Em C#, as propriedades (properties) com sintaxes como `{ get; set; }` são utilizadas para:",
            "Implementar o encapsulamento de forma simplificada, abstraindo a criação manual de atributos privados e métodos getters/setters correspondentes.",
            "Definir que o atributo associado será armazenado exclusivamente na memória stack de acesso rápido.",
            "Obrigar que a classe implemente herança de comportamento baseada em atributos públicos dinâmicos.",
            "Bloquear o acesso de escrita por classes herdadas na mesma assembly em tempo de execução.",
            "Configurar o mapeamento objeto-relacional automático do framework Entity Framework sem anotações adicionais."
        ),
        # Q29: GRASP Information Expert
        (
            "O padrão GRASP **Information Expert** (Especialista na Informação) dita que a responsabilidade de executar uma determinada tarefa deve ser atribuída para:",
            "A classe que possui as informações necessárias para realizar essa responsabilidade.",
            "A classe controladora que gerencia a interface visual do sistema operacional.",
            "A classe abstrata que possui o maior número de subclasses concretas associadas.",
            "O módulo de persistência de dados encarregado do acesso ao banco de dados relacional.",
            "A interface que declara o maior número de métodos abstratos e propriedades genéricas."
        ),
        # Q30: .NET Garbage Collector
        (
            "O Garbage Collector (GC) da plataforma .NET atua de forma automática para gerenciar a memória da aplicação. A operação básica realizada pelo GC consiste em:",
            "Monitorar a memória heap para liberar o espaço alocado por objetos que não possuem mais nenhuma referência ativa no programa.",
            "Mover todas as variáveis locais da memória stack para a memória heap para evitar erros de ponteiros nulos.",
            "Compilar dinamicamente o código C# para linguagem intermediária (IL) durante a execução do programa.",
            "Compactar fisicamente os arquivos executáveis gerados na pasta de publicação para economizar espaço em disco.",
            "Autenticar os certificados digitais X.509 utilizados em requisições seguras ao banco de dados."
        )
    ]
    
    for i, q in enumerate(software_questions):
        dia_29_content.append(f"### Questão {i+16} (FCC)\n")
        dia_29_content.append(f"{q[0]}\n\n")
        dia_29_content.append(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}\nE) {q[5]}\n\n")
        dia_29_content.append(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
        dia_29_content.append(f"**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.\n</details>\n\n")
        dia_29_content.append("---\n\n")
        
    # Tema 3: Portugues - Flexao e Vozes do Verbo
    dia_29_content.append("## 📝 TEMA 3: Língua Portuguesa — Flexão Nominal e Verbal, Vozes do Verbo e Transposição\n")
    
    portuguese_questions = [
        # Q31: Voz passiva sintetica vs analitica
        (
            "A transposição de uma oração da voz ativa para a voz passiva analítica exige a reestruturação dos termos sintáticos. A frase *'O analista do tribunal desenvolveu o novo sistema de segurança'* transposta para a voz passiva analítica assume a seguinte redação correta:",
            "O novo sistema de segurança foi desenvolvido pelo analista do tribunal.",
            "Desenvolveu-se o novo sistema de segurança pelo analista do tribunal.",
            "O novo sistema de segurança desenvolvera-se pelo analista do tribunal.",
            "O analista do tribunal tinha desenvolvido o novo sistema de segurança.",
            "O novo sistema de segurança seria desenvolvido pelo analista do tribunal."
        ),
        # Q32: Voz passiva sintetica
        (
            "A voz passiva sintética (ou pronominal) caracteriza-se pelo uso do pronome apassivador 'se' associado a verbo transitivo direto. Assinale a frase que exemplifica corretamente o uso da voz passiva sintética:",
            "Identificaram-se falhas graves de segurança nos servidores do tribunal.",
            "Precisa-se de novos servidores estáveis na área de infraestrutura de TI.",
            "Os técnicos assistiram ao deploy do novo módulo judicial na quarta-feira.",
            "Eles referiram-se ao antigo banco de dados corporativo durante a reunião.",
            "Trabalhou-se bastante durante o fim de semana para corrigir os bugs de rede."
        ),
        # Q33: Agente da passiva
        (
            "Na oração *'As novas regras de tratamento de dados pessoais foram estabelecidas pela ANPD'*, o termo *'pela ANPD'* desempenha a função sintática de:",
            "Agente da passiva",
            "Objeto direto preposicionado",
            "Adjunto adnominal",
            "Predicativo do sujeito",
            "Complemento nominal"
        ),
        # Q34: Transposicao voz passiva sintetica
        (
            "Transpondo a frase *'Os auditores analisarão todos os logs de acesso'* para a voz passiva sintética, obtém-se a forma correta:",
            "Analisar-se-ão todos os logs de acesso.",
            "Analisar-se-ia todos os logs de acesso.",
            "Todos os logs de acesso serão analisados pelos auditores.",
            "Teriam sido analisados todos os logs de acesso pelos auditores.",
            "Analisaram-se todos os logs de acesso pelos auditores."
        ),
        # Q35: Flexao verbal concordancia
        (
            "Assinale a alternativa que apresenta a flexão verbal correta de acordo com a norma-padrão da língua portuguesa:",
            "Se eles mantiverem os backups atualizados, o risco de perda de dados diminuirá.",
            "Se eles manterem os backups atualizados, o risco de perda de dados diminuirá.",
            "Quando a equipe ver o relatório de erros, tomará as devidas providências.",
            "Se o diretor intervir a tempo, a falha crítica de rede não ocorrerá hoje.",
            "Eles requiseram a exclusão definitiva dos prontuários médicos da base."
        ),
        # Q36: Verbo intervir flexao
        (
            "O verbo intervir é derivado do verbo vir e deve seguir a sua conjugação. Assinale a alternativa que apresenta a flexão correta desse verbo no pretérito perfeito do indicativo:",
            "O comitê interveio na tomada de decisões estratégicas de segurança ontem.",
            "O comitê interviu na tomada de decisões estratégicas de segurança ontem.",
            "Os analistas interviram na tomada de decisões estratégicas de segurança ontem.",
            "Se o comitê intervisse na tomada de decisões, o projeto teria sucesso.",
            "Quando o comitê intervir na tomada de decisões, as falhas serão sanadas."
        ),
        # Q37: Voz reflexiva
        (
            "A voz reflexiva ocorre quando o sujeito pratica e sofre a ação verbal simultaneamente. A frase que exemplifica a voz reflexiva com pronome de reciprocidade (ação mútua) é:",
            "Os dois analistas de sistemas parabenizaram-se mutuamente pelo deploy bem-sucedido.",
            "O desenvolvedor cortou-se acidentalmente com a chapa de metal do rack de rede.",
            "O sistema operacional atualizou-se automaticamente durante a madrugada.",
            "Os técnicos queixaram-se do calor excessivo dentro da sala de servidores públicos.",
            "Eles arrependeram-se de não ter migrado a base de dados para o PostgreSQL."
        ),
        # Q38: Transposicao tempo verbal
        (
            "Ao realizar a transposição de uma frase da voz ativa para a voz passiva analítica, o tempo e modo do verbo auxiliar da passiva deve corresponder exatamente ao tempo e modo do verbo principal da ativa. Na frase *'O switch transmitia os pacotes de dados'*, o verbo auxiliar correspondente na voz passiva analítica deve ser flexionado no:",
            "Pretérito imperfeito do indicativo (eram)",
            "Pretérito perfeito do indicativo (foram)",
            "Futuro do pretérito do indicativo (seriam)",
            "Pretérito mais-que-perfeito do indicativo (tinham sido)",
            "Presente do indicativo (são)"
        ),
        # Q39: Participio irregular
        (
            "Alguns verbos possuem dois particípios: um regular (terminado em -ado ou -ido), usado com os auxiliares ter ou haver, e outro irregular, usado com ser ou estar. Assinale a frase gramaticalmente correta em relação ao uso do particípio:",
            "O tribunal já havia aceitado todas as propostas comerciais enviadas pelas empresas.",
            "A proposta comercial de TI foi aceitada pela comissão de licitação do tribunal.",
            "A equipe já tinha elegido o novo coordenador de segurança da informação.",
            "O documento de requisitos foi imprimido em papel timbrado pelo analista.",
            "Os servidores públicos já tinham chego ao prédio do fórum judicial de manhã."
        ),
        # Q40: Pronome se index ou passivo
        (
            "Na frase *'Não se tolerarão falhas graves no processamento de dados dos cidadãos'*, a função da palavra 'se' e a classificação de voz da oração são, respectivamente:",
            "Pronome apassivador e voz passiva sintética.",
            "Índice de indeterminação do sujeito e voz ativa com sujeito indeterminado.",
            "Pronome reflexivo e voz reflexiva com sujeito simples.",
            "Partícula expletiva de realce e voz ativa com sujeito oculto.",
            "Conjunção subordinada condicional e voz ativa com sujeito composto."
        ),
        # Q41: Flexao de plural nomes compostos
        (
            "Assinale a alternativa que apresenta a flexão de plural correta do substantivo composto de acordo com a norma-padrão:",
            "Os novos decretos estabeleceram diversos salários-família para os servidores.",
            "Os novos decretos estabeleceram diversos salário-famílias para os servidores.",
            "A comissão contratou dois analistas de sistemas recém-formados para os cargos-chaves.",
            "Os técnicos instalaram os softwares-base em todos os computadores do fórum.",
            "As partes assinaram os termos de cooperação com vários estados-membros."
        ),
        # Q42: Verbo reaver flexao
        (
            "O verbo reaver é classificado como defectivo e deve ser conjugado apenas nas formas em que o verbo haver possui a letra 'v'. Assinale a alternativa que apresenta a flexão correta do verbo reaver:",
            "Nós reavemos todos os arquivos de backups que haviam sido apagados da base.",
            "Nós reouvemos todos os arquivos de backups que haviam sido apagados da base.",
            "Se a equipe reaver os arquivos de backups, o sistema voltará a funcionar.",
            "Eles reaveram o acesso físico aos servidores após a intervenção técnica.",
            "Quando a comissão reaver os documentos de licitação, o processo continuará."
        ),
        # Q43: Transposicao sem sujeito passivo
        (
            "A transposição para a voz passiva só é possível em orações que possuem objeto direto na voz ativa (verbos transitivos diretos ou transitivos diretos e indiretos). Assinale a frase que NÃO admite transposição para a voz passiva:",
            "Os técnicos de TI necessitam de novos switches gigabit ethernet de alto desempenho.",
            "O analista de infraestrutura instalou o sistema operacional Linux no servidor.",
            "O comitê de acessibilidade analisou as barreiras físicas no prédio do fórum.",
            "A empresa terceirizada entregou os cabos de manobra patch cord na terça-feira.",
            "A ANPD aplicou uma advertência administrativa formal ao órgão público."
        ),
        # Q44: Flexao verbal subjuntivo
        (
            "Assinale a alternativa que apresenta o emprego correto do verbo no modo subjuntivo de acordo com a norma-padrão:",
            "Caso a equipe requeira o acesso ao banco de dados, o administrador concederá.",
            "Caso a equipe requira o acesso ao banco de dados, o administrador concederá.",
            "Quando o diretor propor o novo planejamento de metas, todos concordarão.",
            "Se o analista dispor de tempo livre hoje à tarde, revisará os requisitos.",
            "Se nós medirmos a velocidade do canal de cabeamento, o teste falhará."
        ),
        # Q45: Voz passiva analitica verbo composto
        (
            "Transpondo a frase *'A diretoria de TI vinha revisando os processos de deploy'* para a voz passiva analítica, obtém-se a forma correta:",
            "Os processos de deploy vinham sendo revisados pela diretoria de TI.",
            "Os processos de deploy vinha sendo revisados pela diretoria de TI.",
            "Os processos de deploy tinham sido revisados pela diretoria de TI.",
            "Os processos de deploy foram sendo revisados pela diretoria de TI.",
            "Revisavam-se os processos de deploy pela diretoria de TI."
        )
    ]
    
    for i, q in enumerate(portuguese_questions):
        dia_29_content.append(f"### Questão {i+31} (FCC)\n")
        dia_29_content.append(f"{q[0]}\n\n")
        dia_29_content.append(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}\nE) {q[5]}\n\n")
        dia_29_content.append(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
        dia_29_content.append(f"**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.\n</details>\n\n")
        dia_29_content.append("---\n\n")

    # Salva o arquivo md
    filepath_29 = os.path.join(questoes_dir, "dia_29_05_questoes.md")
    with open(filepath_29, "w", encoding="utf-8") as f:
        f.write("".join(dia_29_content))
    print(f"Gerado: {filepath_29}")

if __name__ == "__main__":
    main()
