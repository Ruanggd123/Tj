import os

filepath = r"c:\Users\Ruan Gomes\Downloads\TJC\03_Baterias_Questoes_FCC\dia_28_05_questoes.md"

with open(filepath, "w", encoding="utf-8") as f:
    f.write("# Bateria de Questões - 28/05/2026\n\n")
    
    q_num = 1
    # Topic 1: Banco de Dados (15 questions)
    db_topics = [
        ("MongoDB é classificado como um banco de dados NoSQL do tipo orientado a:", "Documentos.", "Colunas.", "Grafos.", "Chave-valor.", "Objetos."),
        ("No MongoDB, uma coleção (collection) é conceitualmente equivalente, em bancos relacionais, a uma:", "Tabela.", "Linha.", "Coluna.", "Chave Primária.", "Visão."),
        ("O formato interno de armazenamento de documentos no MongoDB é conhecido como:", "BSON.", "JSON.", "XML.", "YAML.", "CSV."),
        ("Para buscar documentos em uma coleção `usuarios` onde a `idade` é maior que 20 no MongoDB, o comando correto é:", "db.usuarios.find({idade: {$gt: 20}})", "db.usuarios.select(idade > 20)", "db.usuarios.find(idade > 20)", "db.usuarios.query({idade: {$greater: 20}})", "db.usuarios.search({idade: > 20})"),
        ("A cláusula SQL utilizada para criar Expressões de Tabela Comuns (CTEs) é:", "WITH", "CREATE CTE", "SELECT AS", "DECLARE", "TEMP TABLE"),
        ("Para criar uma CTE recursiva em SQL, a palavra-chave utilizada em conjunto com a cláusula CTE é:", "RECURSIVE", "LOOP", "REPEAT", "WHILE", "ITERATE"),
        ("Qual das alternativas a seguir representa uma Window Function em SQL?", "ROW_NUMBER()", "MAX_GROUP()", "HAVING()", "GROUP_CONCAT()", "DISTINCT()"),
        ("A cláusula que define a \"janela\" sobre a qual uma Window Function operará é:", "OVER", "PARTITION", "WINDOW_SIZE", "RANGE", "FRAME"),
        ("A principal diferença entre RANK() e DENSE_RANK() em Window Functions é que:", "DENSE_RANK() não pula números após empates.", "RANK() não pula números após empates.", "DENSE_RANK() não permite empates.", "RANK() é exclusivo para dados numéricos.", "DENSE_RANK() ordena decrescentemente por padrão."),
        ("Para agregar dados no MongoDB de forma semelhante ao GROUP BY do SQL, utiliza-se o método:", "aggregate()", "group()", "reduce()", "mapReduce()", "summarize()"),
        ("Em bancos orientados a documentos, o schema-less significa que:", "Documentos na mesma coleção podem ter estruturas diferentes.", "Não há suporte a índices.", "O banco de dados não exige autenticação.", "Não é possível realizar joins.", "O esquema é definido apenas no momento da consulta."),
        ("No SQL, para calcular uma média móvel usando Window Functions, qual cláusula complementar é comumente usada no OVER()?", "ORDER BY", "GROUP BY", "WHERE", "HAVING", "LIMIT"),
        ("O comando para criar um índice no campo `nome` em uma coleção `clientes` no MongoDB é:", "db.clientes.createIndex({nome: 1})", "db.clientes.index(nome)", "db.clientes.addIndex('nome')", "CREATE INDEX ON clientes(nome)", "db.clientes.setIndex({nome: true})"),
        ("Um benefício do uso de CTEs em relação a subconsultas aninhadas é:", "Melhor legibilidade e possibilidade de reuso na mesma consulta.", "Execução sempre mais rápida que as subconsultas.", "As CTEs são materializadas permanentemente no disco.", "As CTEs não exigem permissão de SELECT.", "As CTEs dispensam o uso de JOINs."),
        ("A função LAG() em SQL Avançado é utilizada para:", "Acessar dados da linha anterior na janela especificada.", "Acessar dados da linha seguinte na janela especificada.", "Calcular o tempo de atraso de uma query.", "Mover a linha atual para o final do result set.", "Somar valores de colunas defasadas.")
    ]
    
    for q in db_topics:
        f.write(f"### Questão {q_num} (FCC - Adaptada)\n")
        f.write(f"{q[0]}\n\n")
        f.write(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}\nE) {q[5]}\n\n")
        f.write(f"<details><summary>Comentários da Questão {q_num}</summary>\n\n")
        f.write(f"**Gabarito: A**\n\nExplicação: A alternativa A está correta conforme os princípios técnicos cobrados pela FCC para Banco de Dados.\n</details>\n\n")
        f.write("---\n\n")
        q_num += 1

    # Topic 2: Linux (15 questions)
    linux_topics = [
        ("No Linux, o diretório padrão onde são armazenados os arquivos de configuração do sistema é o:", "/etc", "/var", "/bin", "/home", "/usr/sbin"),
        ("A representação octal da permissão `rwxr-xr-x` é:", "755", "644", "777", "750", "775"),
        ("Para que um usuário possa entrar em um diretório no Linux usando o comando `cd`, ele precisa da permissão de:", "Execução (x)", "Leitura (r)", "Gravação (w)", "Leitura e Gravação (rw)", "Total (rwx)"),
        ("O comando utilizado para buscar padrões de texto em arquivos no Linux é o:", "grep", "find", "locate", "awk", "sed"),
        ("Nas distribuições Red Hat/Oracle Linux, o gerenciador de pacotes de baixo nível é o:", "rpm", "yum", "apt", "dnf", "dpkg"),
        ("Qual comando é utilizado para alterar o dono e o grupo de um arquivo no Linux?", "chown", "chmod", "chgrp", "usermod", "chattr"),
        ("O diretório `/var/log` no Linux é tipicamente utilizado para armazenar:", "Arquivos de registro de eventos (logs).", "Binários de usuários.", "Arquivos temporários do sistema.", "Configurações de rede.", "Variáveis de ambiente globais."),
        ("O utilitário padrão para empacotamento de arquivos (sem compressão nativa) no Linux é o:", "tar", "gzip", "zip", "bzip2", "rar"),
        ("O comando `chmod o+x arquivo` resulta em:", "Adicionar permissão de execução para os outros usuários (others).", "Remover a permissão de execução do dono.", "Conceder todas as permissões para o grupo.", "Tornar o arquivo executável para todos os usuários.", "Remover todas as permissões dos outros usuários."),
        ("O gerenciador de pacotes de alto nível `yum` possui como uma de suas vantagens em relação ao `rpm`:", "A resolução automática de dependências.", "A execução mais rápida na linha de comando.", "Não necessitar de acesso root para instalar pacotes.", "Não utilizar repositórios na rede.", "Compilar o código-fonte durante a instalação."),
        ("Para visualizar o manual de um comando no Linux, utiliza-se o comando:", "man", "help", "info", "doc", "?"),
        ("O comando `pwd` no Linux é usado para:", "Exibir o diretório de trabalho atual.", "Mudar a senha do usuário.", "Listar os processos em execução.", "Testar a conectividade de rede.", "Exibir o uso de disco particionado."),
        ("Em qual diretório do Linux normalmente encontram-se os executáveis de administração do sistema (reservados ao root)?", "/sbin", "/bin", "/opt", "/home", "/tmp"),
        ("Qual caractere é utilizado para redirecionar a saída padrão de um comando para um arquivo, sobrescrevendo seu conteúdo?", ">", ">>", "<", "|", "&"),
        ("O sinalizador `|` (pipe) no Linux serve para:", "Conectar a saída padrão de um comando à entrada padrão de outro.", "Executar dois comandos simultaneamente.", "Redirecionar a saída de erro para um arquivo.", "Pausar a execução do comando atual.", "Anular a saída de um comando.")
    ]

    for q in linux_topics:
        f.write(f"### Questão {q_num} (FCC - Adaptada)\n")
        f.write(f"{q[0]}\n\n")
        f.write(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}\nE) {q[5]}\n\n")
        f.write(f"<details><summary>Comentários da Questão {q_num}</summary>\n\n")
        f.write(f"**Gabarito: A**\n\nExplicação: A alternativa A está correta com base na arquitetura Linux e distribuições Red Hat.\n</details>\n\n")
        f.write("---\n\n")
        q_num += 1

    # Topic 3: Legislacao Previdenciaria (15 questions)
    legis_topics = [
        ("O Regime Próprio de Previdência Social (RPPS) dos servidores do Estado do Ceará é caracterizado por ser:", "De filiação obrigatória para os ocupantes de cargo efetivo.", "Facultativo para novos servidores.", "Aberto à participação da iniciativa privada.", "Administrado exclusivamente pelo INSS.", "Isento de contribuição para servidores ativos."),
        ("O financiamento do RPPS estadual ocorre por meio de:", "Contribuições dos segurados e do próprio ente público (Estado).", "Exclusivamente pelas contribuições dos segurados.", "Apenas com recursos do tesouro estadual, sem desconto em folha.", "Doações e repasses federais do FPM.", "Impostos arrecadados especificamente para esse fim."),
        ("Sobre a contribuição previdenciária de aposentados e pensionistas no RPPS, é correto afirmar:", "Incide apenas sobre a parcela dos proventos que supere o limite máximo do RGPS.", "Não existe contribuição para aposentados e pensionistas.", "A alíquota é aplicada sobre o valor integral do benefício recebido.", "É cobrada apenas nos primeiros cinco anos de aposentadoria.", "Aplica-se apenas em caso de déficit atuarial no sistema."),
        ("O princípio previdenciário que determina que todos contribuam para o financiamento do sistema é o da:", "Solidariedade.", "Igualdade material.", "Universalidade irrestrita.", "Seletividade e distributividade.", "Irredutibilidade do valor dos benefícios."),
        ("O ente federativo (Estado) figura, na relação previdenciária de custeio, como:", "Ente patronal ou patrocinador.", "Segurado especial.", "Administrador único dos recursos de terceiros.", "Beneficiário indireto.", "Agente financeiro autônomo."),
        ("A base de cálculo da contribuição do servidor ativo para o RPPS incide sobre:", "A totalidade da sua remuneração de contribuição, fixada em lei.", "Apenas o seu vencimento base, excluindo gratificações.", "O valor correspondente ao salário-mínimo nacional.", "Metade do teto do RGPS.", "Sua remuneração subtraída do imposto de renda."),
        ("No modelo de previdência pública, o Fundo Financeiro baseia-se no sistema de:", "Repartição simples.", "Capitalização individual.", "Contas nocionais plurais.", "Títulos públicos intransferíveis.", "Poupança programada autônoma."),
        ("Em caso de deficiência ou doença incapacitante do aposentado, a Constituição Federal estabelece que a contribuição incidirá sobre parcelas que superem:", "O dobro do limite máximo estabelecido para o RGPS.", "O limite máximo do RGPS.", "Três salários-mínimos.", "A remuneração integral da ativa.", "Qualquer valor, isentando totalmente de contribuição."),
        ("A administração e gestão do RPPS do Estado do Ceará cabe, geralmente, a uma autarquia denominada:", "Cearáprev (Fundação de Previdência Social do Estado do Ceará).", "INSS-CE.", "Secretaria de Fazenda Exclusiva.", "Instituto Nacional do Seguro Social.", "Departamento Estadual de Trânsito Previdenciário."),
        ("Se a remuneração de um servidor ativo estiver abaixo do teto do RGPS, ele:", "Contribui normalmente para o RPPS com base na sua remuneração.", "Fica isento de contribuição.", "Contribui para o RGPS e não para o RPPS.", "Paga apenas metade da alíquota estabelecida.", "Aplica sua contribuição no sistema de previdência complementar fechado."),
        ("A contribuição do ente público (Estado) ao RPPS não pode ser:", "Inferior ao valor da contribuição do servidor ativo.", "Superior ao dobro da contribuição do servidor ativo.", "Repassada até o dia 10 do mês subsequente.", "Calculada sobre a folha de pagamento bruta.", "Destinada ao fundo financeiro de repartição."),
        ("Para a manutenção do equilíbrio financeiro e atuarial do RPPS, o Estado realiza periodicamente:", "Avaliações atuariais anuais.", "Sorteios de prêmios aos servidores ativos.", "Emissão de títulos da dívida pública previdenciária.", "Aumento linear de alíquotas a cada semestre.", "Empréstimos compulsórios sobre os proventos."),
        ("A taxa de administração cobrada pelo órgão gestor do RPPS visa custear as despesas de:", "Manutenção e funcionamento do próprio regime.", "Pagamento de precatórios estaduais.", "Investimentos em saúde pública no Estado.", "Educação básica de dependentes dos servidores.", "Amortização da dívida consolidada do ente."),
        ("O abono de permanência é um benefício que consiste:", "No reembolso do valor equivalente à contribuição previdenciária ao servidor que já pode se aposentar mas decide permanecer na ativa.", "Na isenção total do imposto de renda retido na fonte.", "Em férias em dobro para o servidor que adia a sua aposentadoria.", "No pagamento antecipado do décimo terceiro.", "Em uma promoção funcional automática na carreira."),
        ("No que tange aos fundos, a segregação de massas tem como objetivo principal:", "Separar servidores de diferentes regimes de custeio para buscar o reequilíbrio a longo prazo.", "Misturar os recursos de impostos com as contribuições previdenciárias.", "Transferir os servidores civis para o regime militar.", "Diminuir o valor das aposentadorias já concedidas.", "Privatizar a previdência dos servidores públicos estaduais.")
    ]

    for q in legis_topics:
        f.write(f"### Questão {q_num} (FCC - Adaptada)\n")
        f.write(f"{q[0]}\n\n")
        f.write(f"A) {q[1]}\nB) {q[2]}\nC) {q[3]}\nD) {q[4]}\nE) {q[5]}\n\n")
        f.write(f"<details><summary>Comentários da Questão {q_num}</summary>\n\n")
        f.write(f"**Gabarito: A**\n\nExplicação: A alternativa A está correta de acordo com as normas constitucionais e estaduais sobre o RPPS e Custeio.\n</details>\n\n")
        f.write("---\n\n")
        q_num += 1

print(f"Bateria de questões gerada em: {filepath}")
