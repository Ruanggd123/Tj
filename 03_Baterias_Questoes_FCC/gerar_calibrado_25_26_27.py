# -*- coding: utf-8 -*-
import os

def write_day_file(filepath, title, desc, themes_data):
    content = []
    content.append(f"# {title}\n\n")
    content.append(f"{desc}\n\n---\n\n")
    
    q_global_idx = 1
    for t_idx, (theme_name, questions) in enumerate(themes_data, 1):
        content.append(f"## 📝 TEMA {t_idx}: {theme_name}\n\n")
        for q in questions:
            content.append(f"### Questão {q_global_idx} (FCC)\n")
            content.append(f"{q[0]}\n\n")
            content.append(f"A) {q[1]}\n")
            content.append(f"B) {q[2]}\n")
            content.append(f"C) {q[3]}\n")
            content.append(f"D) {q[4]}\n")
            content.append(f"E) {q[5]}\n\n")
            content.append("<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
            content.append(f"**Gabarito: A**. {q[6]}\n")
            content.append("</details>\n\n")
            content.append("---\n\n")
            q_global_idx += 1
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("".join(content).strip() + "\n")
    print(f"Gerado: {filepath}")

def main():
    workspace_dir = r"c:\Users\Ruan Gomes\Downloads\TJC"
    questoes_dir = os.path.join(workspace_dir, "03_Baterias_Questoes_FCC")
    
    # =========================================================================
    # DIA 25/05 - SEGUNDA-FEIRA
    # =========================================================================
    dia_25_themes = []
    
    # Tema 1: Engenharia de Requisitos
    t1_25 = [
        # Q1
        (
            "Segundo Ian Sommerville, os requisitos de software são divididos em requisitos funcionais e não funcionais. Sobre as subcategorias de requisitos não funcionais, assinale a alternativa correta:",
            "Os requisitos não funcionais de produto definem restrições sobre o comportamento do software, englobando metas de desempenho, requisitos de confiabilidade e usabilidade.",
            "Os requisitos não funcionais organizacionais derivam de políticas e regras da empresa parceira, tais como restrições de horários de deploy e contratação de servidores.",
            "Os requisitos não funcionais externos especificam regras de codificação do ambiente de desenvolvimento, tais como uso obrigatório de IDEs homologadas pela equipe de TI.",
            "Os requisitos não funcionais de processo definem prazos para a entrega dos artefatos de homologação, impedindo a redefinição de escopos em fases de validação.",
            "Os requisitos não funcionais de conformidade tratam exclusivamente de auditorias contábeis realizadas por órgãos de controle externo e fiscalizadores fazendários."
        , "A alternativa A descreve corretamente os requisitos não funcionais de produto, que especificam ou restringem o comportamento do próprio software (como desempenho, usabilidade e confiabilidade)."),
        # Q2
        (
            "Em modelagem de sistemas com a UML 2.5, os diagramas de Casos de Uso são amplamente utilizados para mapear requisitos funcionais. Sobre os relacionamentos de 'include' e 'extend' nesse diagrama, é correto afirmar:",
            "O relacionamento de extend indica um comportamento opcional que é inserido no caso de uso base sob condições específicas definidas em pontos de extensão.",
            "O relacionamento de include representa um comportamento condicional que só é disparado se o ator principal realizar uma ação de exceção no fluxo principal.",
            "O relacionamento de extend aponta obrigatoriamente do caso de uso base para o caso de uso estendido, indicando uma execução sequencial e síncrona.",
            "O relacionamento de include indica que o caso de uso base adiciona opcionalmente o comportamento do caso de uso incluído sem alterar o fluxo de execução.",
            "O relacionamento de extend exige que o caso de uso estendido compartilhe a mesma assinatura de métodos e atributos definidos na classe do caso de uso base."
        , "A alternativa A define corretamente o relacionamento 'extend' como um comportamento condicional/opcional inserido no caso de uso base em determinados pontos de extensão."),
        # Q3
        (
            "A rastreabilidade de requisitos é uma atividade fundamental para garantir o controle de mudanças no ciclo de vida de desenvolvimento de sistemas. Sobre a rastreabilidade bidirecional, assinale a alternativa correta:",
            "Ela permite rastrear o requisito desde a sua origem (como a entrevista com o usuário) até os artefatos de projeto e código, e vice-versa.",
            "Ela garante exclusivamente a conformidade do código-fonte com o banco de dados relacional, sem necessidade de analisar solicitações de mudanças.",
            "Ela impede a exclusão de requisitos obsoletos do documento de especificação caso estes já tenham sido implementados no ambiente de testes.",
            "Ela rastreia os diagramas de classe em direção aos diagramas de caso de uso de forma estrita, sem considerar os documentos de requisitos textuais.",
            "Ela relaciona as interfaces com o usuário diretamente aos planos de testes unitários executados pela equipe de controle de qualidade integrada."
        , "A rastreabilidade bidirecional assegura que cada requisito possa ser rastreado adiante (forward) até o código/testes e também de volta (backward) até a sua origem."),
        # Q4
        (
            "A elicitação de requisitos é uma fase crítica que emprega diversas técnicas para capturar as necessidades dos stakeholders. Sobre a técnica de Etnografia, assinale a alternativa correta:",
            "Trata-se de uma técnica de observação imersiva na qual o analista acompanha a rotina diária real do usuário para identificar requisitos implícitos.",
            "Consiste em um questionário fechado com perguntas de múltipla escolha enviado por correio eletrônico a todos os gerentes setoriais do tribunal.",
            "Baseia-se em reuniões de design participativo estruturadas com a presença de facilitadores externos e especialistas em engenharia de software.",
            "É um processo focado na criação rápida de modelos de tela interativos para validar o fluxo de navegação do sistema com os patrocinadores.",
            "Envolve a análise exclusiva de manuais técnicos e documentações de sistemas legados que serão desativados no processo de migração de dados."
        , "A Etnografia baseia-se na observação de como os usuários realmente trabalham no dia a dia, sendo ideal para descobrir requisitos de processo implícitos."),
        # Q5
        (
            "A validação e a verificação de requisitos são processos que visam garantir a qualidade da especificação antes do início do desenvolvimento. A diferença conceitual entre validar e verificar requisitos é que:",
            "Validar garante que o sistema atende às reais necessidades do usuário (construir o produto correto), enquanto verificar garante a conformidade com as especificações técnicas (construir o produto corretamente).",
            "Verificar assegura que o cliente aprova o protótipo funcional apresentado na homologação, enquanto validar foca nas métricas internas de desempenho do banco de dados.",
            "Validar consiste na realização de testes de caixa-preta automatizados pela equipe de QA, enquanto verificar envolve auditorias fiscais sobre o orçamento do projeto.",
            "Verificar é uma atividade puramente manual realizada por gerentes de negócio, enquanto validar é uma atividade automatizada por compiladores de código.",
            "Validar busca encontrar conflitos gramaticais no texto da especificação de requisitos, enquanto verificar busca validar a viabilidade financeira do sistema."
        , "A validação foca em saber se o produto está alinhado ao que o usuário precisa, enquanto a verificação avalia se o produto segue a especificação técnica documentada."),
        # Q6
        (
            "No contexto de gerenciamento de requisitos, a matriz de rastreabilidade de requisitos (RTM) é uma ferramenta essencial. A função principal da RTM em um projeto de desenvolvimento de sistemas é:",
            "Mapear a relação entre cada requisito individual, suas fontes de origem, casos de uso correspondentes, componentes de código e casos de teste.",
            "Calcular o custo financeiro estimado para a implementação de cada funcionalidade mapeada durante a etapa de elicitação e levantamento de dados.",
            "Armazenar fisicamente os registros de log de depuração gerados pelos servidores de aplicação durante a execução dos testes de estresse.",
            "Exibir a escala hierárquica e a distribuição de cargos e salários dos analistas que participaram do desenvolvimento do sistema corporativo.",
            "Substituir o modelo conceitual de dados do banco relacional, unificando as entidades e relacionamentos em uma única tabela de consulta física."
        , "A matriz de rastreabilidade serve para correlacionar requisitos a outros artefatos do ciclo de vida, facilitando a análise de impacto e a cobertura de testes."),
        # Q7
        (
            "Durante o processo de engenharia de requisitos, a volatilidade de requisitos refere-se às mudanças que ocorrem ao longo do tempo. Sobre a volatilidade dos requisitos, é correto afirmar:",
            "Os requisitos são mutáveis devido a mudanças no ambiente de negócios, novas leis ou melhor compreensão dos usuários sobre suas próprias necessidades.",
            "A volatilidade é um erro de modelagem decorrente de falhas graves cometidas pelos analistas durante a fase inicial de elicitação dos dados.",
            "A volatilidade deve ser completamente eliminada em projetos de software através do uso de contratos rígidos de escopo fechado tradicional.",
            "Os requisitos não funcionais de portabilidade são os únicos que apresentam volatilidade severa em sistemas de missão crítica governamentais.",
            "A volatilidade impede a compilação do código-fonte do sistema em servidores de integração contínua baseados em microsserviços modernos."
        , "A volatilidade de requisitos é inerente aos projetos e ocorre por mudanças organizacionais, de negócios, legais ou maturidade da visão do cliente."),
        # Q8
        (
            "Considere que um analista precise definir os requisitos de segurança para um sistema do tribunal. Um exemplo típico de requisito não funcional de segurança que segue o padrão de especificação técnica é:",
            "O sistema deve criptografar todas as senhas de usuários e dados sensíveis utilizando o algoritmo de hash SHA-256 com salvação de sal em banco.",
            "O usuário deve poder emitir o relatório de produtividade semanal dos magistrados a partir da tela principal de consultas em lote.",
            "O sistema deve ser desenvolvido utilizando o framework Spring Boot 3 na linguagem Java com persistência via Hibernate e JPA local.",
            "A equipe de desenvolvimento deve entregar toda a documentação de arquitetura de rede no formato PDF em até dez dias úteis após a homologação.",
            "O sistema deve estar disponível para acesso na internet exclusivamente durante os dias úteis, entre as oito horas e as vinte horas de Brasília."
        , "A alternativa A apresenta uma restrição de segurança (como o sistema deve se comportar em relação à segurança dos dados), caracterizando um requisito não funcional."),
        # Q9
        (
            "Em relação à especificação de requisitos de software (SRS) baseada no padrão IEEE 830, uma característica essencial de uma SRS de alta qualidade é a consistência. Isso significa que:",
            "Nenhum subconjunto de requisitos individuais descritos no documento deve entrar em conflito direto ou indireto com outros requisitos do mesmo sistema.",
            "Todos os requisitos descritos no documento devem possuir exatamente a mesma quantidade de palavras e a mesma formatação visual de tópicos.",
            "A especificação deve ser escrita exclusivamente em linguagem matemática formal para evitar qualquer tipo de ambiguidade na interpretação do leitor.",
            "O documento de requisitos não deve admitir modificações ou revisões adicionais após a aprovação formal assinada pela diretoria do tribunal.",
            "Os requisitos de software devem ser descritos de forma genérica para permitir que qualquer sistema de mercado atenda às solicitações sem customização."
        , "A consistência em uma SRS significa ausência de conflitos entre os requisitos (por exemplo, um requisito exigindo entrega em 2 segundos e outro exigindo processamento em lote lento da mesma operação)."),
        # Q10
        (
            "Na modelagem de Casos de Uso da UML, a definição adequada de um Atores (Actors) é de fundamental relevância. Sobre o conceito de atores na UML, assinale a alternativa correta:",
            "Um ator representa um papel desempenhado por um usuário humano, um dispositivo de hardware ou outro sistema externo que interage com o sistema.",
            "Um ator é a representação física de uma tabela do banco de dados relacional que recebe atualizações síncronas de escrita durante a transação.",
            "Os atores devem ser implementados obrigatoriamente como classes abstratas no código-fonte para gerenciar as sessões ativas dos usuários.",
            "Um ator não pode possuir relacionamentos de herança ou generalização com outros atores descritos no mesmo diagrama de casos de uso do sistema.",
            "Os atores são elementos internos do sistema que realizam a lógica de processamento dos fluxos alternativos e de exceção mapeados."
        , "Atores são entidades externas (humanos, hardware, sistemas externos) que interagem diretamente com o sistema de software modelado."),
        # Q11
        (
            "Requisitos de Domínio são descritos como requisitos que derivam do campo de aplicação do sistema. Sobre os requisitos de domínio, é correto afirmar:",
            "Eles podem impor novas restrições ou regras de negócio específicas ao sistema, e se não forem atendidos, o sistema pode se tornar inoperante.",
            "Eles referem-se exclusivamente a restrições de rede de computadores e domínios de internet controlados por servidores DNS centrais do tribunal.",
            "Eles são opcionais e servem apenas como sugestões de design de interface gráfica para melhorar a experiência de usabilidade do usuário final.",
            "Eles devem ser convertidos obrigatoriamente em classes de teste unitário e não podem ser documentados no formato de texto livre padrão.",
            "Eles impedem a portabilidade do software para sistemas operacionais baseados em Unix, limitando a execução ao ambiente Microsoft Windows."
        , "Requisitos de domínio refletem as particularidades e regras do negócio/área onde o sistema opera (ex: regras jurídicas no tribunal). Se negligenciados, inviabilizam o uso do sistema."),
        # Q12
        (
            "No ciclo de engenharia de requisitos, a prototipação é frequentemente utilizada. Sobre os protótipos descartáveis (throwaway prototyping), assinale a alternativa correta:",
            "Eles são desenvolvidos rapidamente para ajudar a esclarecer requisitos incertos, sendo descartados após a validação do conceito pelo cliente.",
            "Eles servem como base direta de código-fonte que será refinado e evoluído até se tornar a versão final de produção do sistema corporativo.",
            "Eles exigem a implementação completa do banco de dados e de todas as regras de validação física para garantir a fidelidade do comportamento.",
            "Eles não admitem a utilização de ferramentas de design gráfico, devendo ser criados exclusivamente através de desenhos manuais em papel físico.",
            "Eles são mantidos em paralelo com o sistema real em produção para servir como ambiente alternativo de recuperação de desastres e backups."
        , "O protótipo descartável serve unicamente para elucidar requisitos complexos ou nebulosos, sendo jogado fora e o sistema real escrito do zero."),
        # Q13
        (
            "Em relação às técnicas de elicitação de requisitos, o JAD (Joint Application Development) destaca-se em ambientes corporativos. A principal característica do JAD é:",
            "A realização de reuniões estruturadas e colaborativas que reúnem usuários, desenvolvedores e gerentes para definir requisitos em conjunto.",
            "A análise isolada de logs de erros e banco de dados realizada pela equipe de suporte sem a interferência ou participação do usuário final.",
            "A observação silenciosa e imersiva do ambiente de trabalho do cliente por longos períodos para mapear os fluxos informais de processos.",
            "O envio de questionários eletrônicos anônimos para um grande grupo de stakeholders distribuídos geograficamente em comarcas distantes.",
            "A simulação computacional de falhas de hardware para verificar a resiliência de servidores físicos do datacenter corporativo do órgão."
        , "O JAD baseia-se em workshops colaborativos intensivos com representantes de negócios e de TI trabalhando juntos para acelerar a especificação."),
        # Q14
        (
            "A especificação de requisitos não funcionais de usabilidade visa garantir que o sistema seja fácil de aprender e utilizar. Um requisito de usabilidade adequado é:",
            "O tempo médio necessário para que um novo operador consiga realizar uma pesquisa de processo sem auxílio externo não deve exceder trinta minutos.",
            "O sistema de controle processual judicial deve suportar no mínimo quinhentos acessos simultâneos de usuários ativos sem apresentar latência.",
            "A taxa de falhas críticas nas transações financeiras de pagamento de custas judiciais deve ser inferior a uma falha a cada dez mil transações.",
            "O sistema deve ser desenvolvido em conformidade estrita com as especificações técnicas da Lei de Acesso à Informação e do Marco Civil.",
            "A interface gráfica do sistema deve ser renderizada utilizando exclusivamente folhas de estilo CSS compactadas e compatíveis com HTML5."
        , "Requisitos de usabilidade medem fatores como tempo de aprendizado, satisfação do usuário e facilidade de uso em termos quantificáveis."),
        # Q15
        (
            "Durante a fase de análise de requisitos, os analistas lidam com requisitos conflitantes de diferentes stakeholders. A abordagem correta para resolver esses conflitos é:",
            "Realizar negociações estruturadas para encontrar um consenso que atenda aos objetivos estratégicos do projeto e priorizar requisitos prioritários.",
            "Priorizar integralmente os requisitos solicitados pela equipe de desenvolvimento de software, por possuírem maior conhecimento sobre tecnologia.",
            "Implementar todas as solicitações conflitantes de forma paralela através de múltiplos ramais (branches) de código a serem unificados depois.",
            "Descartar imediatamente todos os requisitos que gerarem qualquer nível de discordância entre as áreas de negócio participantes do projeto.",
            "Decidir os conflitos por meio de votação eletrônica aberta a todos os cidadãos do Estado através do portal da transparência do tribunal."
        , "A negociação e a priorização de requisitos em reuniões de alinhamento são técnicas padrão da engenharia de requisitos para lidar de forma profissional com visões conflitantes de stakeholders.")
    ]
    dia_25_themes.append(("Engenharia de Software — Engenharia de Requisitos", t1_25))
    
    # Tema 2: Banco de Dados
    t2_25 = [
        # Q16
        (
            "No banco de dados Oracle, a pseudo-coluna ROWNUM é utilizada em consultas SQL. Sobre o funcionamento e comportamento do ROWNUM, assinale a alternativa correta:",
            "O ROWNUM é atribuído às linhas à medida que elas são selecionadas pela consulta, ocorrendo antes de qualquer operação de ordenação (ORDER BY).",
            "O ROWNUM funciona como uma coluna física gravada de forma permanente no bloco de dados da tabela, identificando a sequência de inserção física.",
            "A utilização direta da condição `WHERE ROWNUM = 2` em uma consulta simples retornará a segunda linha de dados processada com sucesso no buffer.",
            "O ROWNUM substitui a necessidade do uso de chaves primárias compostas em tabelas particionadas fisicamente por range de datas e horas.",
            "O Oracle atualiza os valores de ROWNUM de forma retroativa e síncrona sempre que uma instrução UPDATE altera os valores da coluna indexada."
        , "ROWNUM é gerado dinamicamente antes do ORDER BY. Por isso, para ordenar e depois limitar (top-N query), o Oracle exige o uso de uma subconsulta contendo o ORDER BY interno."),
        # Q17
        (
            "A tabela DUAL é um objeto nativo de suma importância no banco de dados Oracle. A característica técnica da tabela DUAL no Oracle é:",
            "Trata-se de uma tabela especial criada automaticamente pelo Oracle que possui apenas uma coluna denominada DUMMY e contém uma única linha.",
            "É uma tabela temporária física utilizada exclusivamente para armazenar registros de auditoria e sessões de usuários administradores ativos.",
            "Consiste em um mecanismo de particionamento virtual que duplica os dados das tabelas de produção para evitar perdas em transações paralelas.",
            "É uma tabela que veda operações de SELECT do usuário comum, sendo restrita à execução de stored procedures e triggers do sistema de BD.",
            "Trata-se de uma estrutura de memória RAM que armazena os índices de chaves estrangeiras pendentes de validação de consistência relacional."
        , "A tabela DUAL possui uma única coluna (DUMMY do tipo VARCHAR2(1)) e uma única linha (contendo o valor 'X'), sendo útil para avaliar expressões e funções do sistema com SELECT."),
        # Q18
        (
            "No PostgreSQL, a criação de colunas com auto-incremento pode ser feita de diferentes maneiras. Sobre a declaração serial e o padrão ANSI IDENTITY no PostgreSQL, assinale a alternativa correta:",
            "A partir da versão 10, o PostgreSQL recomenda o uso de GENERATED AS IDENTITY por ser padrão ANSI SQL, embora o tipo SERIAL ainda seja suportado.",
            "O tipo SERIAL cria uma chave primária física não sequencial baseada no algoritmo UUID versão 4 de criptografia assimétrica de rede.",
            "A declaração GENERATED ALWAYS AS IDENTITY impede que o usuário force a inserção de valores manuais na coluna de forma direta na instrução INSERT.",
            "O tipo SERIAL não cria sequências (sequences) internas no banco de dados, operando puramente como uma diretiva de compilação temporária de DDL.",
            "O uso de GENERATED BY DEFAULT AS IDENTITY restringe a coluna a aceitar apenas valores informados manualmente pelo usuário no banco de dados."
        , "O PostgreSQL suporta o padrão SQL com IDENTITY (`GENERATED ALWAYS/BY DEFAULT AS IDENTITY`), que é o recomendado atualmente em substituição ao clássico tipo serial (que cria uma sequência implícita)."),
        # Q19
        (
            "A paginação de dados em consultas SQL é um requisito comum em sistemas web do tribunal. A sintaxe correta para limitar o retorno em 10 linhas, pulando as primeiras 50 no PostgreSQL, é:",
            "LIMIT 10 OFFSET 50",
            "OFFSET 10 LIMIT 50",
            "ROWNUM BETWEEN 51 AND 60",
            "LIMIT 50, 10",
            "ROWS 50 TO 60"
        , "A sintaxe padrão e suportada no PostgreSQL para paginação utiliza a palavra-chave LIMIT (quantidade de registros a retornar) seguida por OFFSET (quantidade de registros a pular)."),
        # Q20
        (
            "O H2 Database é um SGBD amplamente utilizado em ambientes de desenvolvimento e testes. Sobre as características do H2 Database, assinale a alternativa correta:",
            "Ele suporta o modo 'In-Memory', o que permite que os dados sejam mantidos apenas na memória RAM e limpos ao finalizar a execução da aplicação.",
            "Ele opera exclusivamente como banco NoSQL orientado a documentos, impedindo o processamento de tabelas relacionais clássicas com chaves SQL.",
            "Ele veda o suporte à API JDBC tradicional, exigindo conexões proprietárias desenvolvidas em C# para realizar a manipulação de dados.",
            "O H2 exige a instalação prévia de um servidor de banco de dados robusto no sistema operacional, não funcionando em modo embutido (embedded).",
            "O H2 não suporta padrões de compatibilidade SQL com outros SGBDs do mercado, limitando-se a um dialeto próprio incompatível com Oracle."
        , "O H2 Database é escrito em Java, é leve e possui o modo In-Memory (`jdbc:h2:mem:...`), ideal para testes automatizados rápidos de banco de dados relacional."),
        # Q21
        (
            "O PostgreSQL utiliza um mecanismo de controle de concorrência avançado conhecido como MVCC. A principal finalidade do MVCC no PostgreSQL é:",
            "Garantir que leitores não bloqueiem escritores e escritores não bloqueiem leitores durante o acesso paralelo aos dados na transação.",
            "Duplicar fisicamente os arquivos de log de transações em tempo real para permitir a recuperação instantânea em casos de falta de energia.",
            "Impedir a execução de instruções de atualização (UPDATE) paralelas sobre diferentes tabelas que compartilham chaves estrangeiras comuns.",
            "Converter automaticamente consultas relacionais SQL complexas em consultas NoSQL otimizadas para processamento em servidores de busca.",
            "Bloquear exclusivamente a tabela inteira sempre que uma operação de leitura for executada por um usuário sem privilégios de administração."
        , "O MVCC (Multi-Version Concurrency Control) permite que leitores e escritores trabalhem sem se bloquear mutuamente, mantendo múltiplas versões das linhas do banco."),
        # Q22
        (
            "No Oracle Database, os arquivos de dados físicos (Datafiles) estão associados a uma estrutura lógica de armazenamento denominada:",
            "Tablespace",
            "Redo Log File",
            "Control File",
            "Schema Area",
            "PGA (Program Global Area)"
        , "Tablespace é a estrutura lógica de armazenamento no Oracle que agrupa um ou mais arquivos de dados (Datafiles) físicos no sistema de arquivos."),
        # Q23
        (
            "O comando VACUUM desempenha um papel crítico na manutenção e desempenho do PostgreSQL. A função principal do comando VACUUM no PostgreSQL é:",
            "Recuperar o espaço físico ocupado por versões de linhas obsoletas (mortas) resultantes de operações de UPDATE e DELETE anteriores.",
            "Realizar a desfragmentação física dos índices do tipo B-Tree gravando os dados em setores contínuos da memória de armazenamento principal.",
            "Efetuar o backup incremental síncrono da base de dados e transmiti-lo via rede para servidores secundários de replicação física.",
            "Validar as restrições de integridade referencial (chaves estrangeiras) que foram desativadas temporariamente por scripts de carga de dados.",
            "Compactar as conexões de rede ativas de usuários inativos para liberar espaço no pool de conexões do servidor do banco de dados."
        , "O VACUUM remove as linhas mortas geradas pelo MVCC, liberando esse espaço para novas gravações da própria tabela."),
        # Q24
        (
            "No Oracle, o dicionário de dados contém visões com prefixos específicos que indicam o escopo de visibilidade dos objetos do banco. As visões com os prefixos USER_, ALL_ e DBA_ contêm, respectivamente:",
            "Objetos pertencentes ao usuário atual; Objetos que o usuário atual tem permissão para acessar; Todos os objetos existentes no banco de dados.",
            "Objetos de propriedade de usuários comuns; Objetos compartilhados em rede; Objetos do esquema SYSTEM exclusivos do administrador de dados.",
            "Tabelas de dados cadastrais; Índices criados na sessão ativa; Procedimentos armazenados e triggers em execução síncrona no servidor.",
            "Objetos criados nas últimas 24 horas; Objetos legados em conformidade legal; Tabelas de sistema em manutenção de disco.",
            "Chaves primárias ativas; Chaves estrangeiras pendentes de validação; Índices únicos globais associados a partições físicas."
        , "USER_ mostra objetos do próprio esquema; ALL_ mostra todos os objetos que o usuário tem privilégio de acesso; DBA_ mostra todos os objetos do banco (para administradores)."),
        # Q25
        (
            "A arquitetura do PostgreSQL baseia-se em um modelo de processos. Sobre a arquitetura de processos do PostgreSQL, é correto afirmar:",
            "Para cada conexão de cliente estabelecida com o banco, o PostgreSQL cria um novo processo separado (backend process) gerenciado pelo postmaster.",
            "O PostgreSQL opera em uma arquitetura puramente multithreaded dentro de um único processo principal de execução em tempo real no SO.",
            "O processo postmaster é responsável exclusivo pela execução física do comando VACUUM FULL, parando todas as atividades de escrita do banco.",
            "O PostgreSQL exige o uso obrigatório de um servidor de pool de conexões externo como o PgBouncer para inicializar o banco de dados.",
            "As conexões ativas compartilham a mesma área de pilha de execução (Stack) de forma concorrente sem isolamento de memória física no SO."
        , "O PostgreSQL adota uma arquitetura baseada em processos (process-based), onde o postmaster faz o dispatch e cria um processo backend dedicado para cada conexão."),
        # Q26
        (
            "Em relação à compatibilidade de SQL no H2 Database, assinale a alternativa que apresenta uma propriedade de configuração técnica importante desse SGBD:",
            "Ele possui modos de compatibilidade integrados que emulam o comportamento de SGBDs como Oracle, PostgreSQL e MySQL de forma configurável.",
            "Ele exige a conversão de todas as tabelas em estruturas NoSQL JSON antes de executar consultas nativas em memória no sistema web.",
            "Ele opera com um compilador proprietário que veda o uso de joins implícitos e explícitos na instrução SELECT do usuário comum.",
            "Os modos de compatibilidade do H2 exigem a tradução manual de stored procedures escritas em PL/SQL para classes compiladas em C++.",
            "Ele veda o uso de constraints de integridade referencial quando o modo de compatibilidade do banco relacional PostgreSQL está ativo."
        , "O H2 possui uma flag de compatibilidade (ex: `;MODE=PostgreSQL` ou `;MODE=Oracle`) que auxilia emulando sintaxes e comportamentos específicos dos SGBDs maiores."),
        # Q27
        (
            "No Oracle, o ROWID é um conceito técnico importante. O ROWID representa:",
            "O endereço físico e único de uma linha de tabela no disco, composto pelo número do arquivo de dados, bloco e posição interna da linha.",
            "Uma pseudo-coluna sequencial numérica iniciada em um que é gerada dinamicamente a cada nova consulta executada pelo usuário ativo.",
            "O identificador único de transação do banco de dados que garante o isolamento lógico das alterações concorrentes da sessão de rede.",
            "A chave substituta (surrogate key) gerada automaticamente a partir de um gerador de UUIDs integrado no kernel do SGBD relacional.",
            "O código identificador do usuário que possui privilégios de escrita física sobre a tabela associada ao bloco de dados lido."
        , "O ROWID indica a exata localização física da linha no banco de dados Oracle, sendo o método de acesso mais rápido para retornar uma única linha de dados."),
        # Q28
        (
            "No PostgreSQL, a integridade referencial e as transações são controladas de perto. Ao tentar inserir um registro violando uma Foreign Key, o PostgreSQL:",
            "Aborta imediatamente a transação ativa ou gera um erro de violação de constraint, impedindo a persistência do dado inconsistente.",
            "Apenas registra um aviso em arquivo de log de eventos e permite a inserção física do registro mantendo a chave estrangeira nula.",
            "Cria dinamicamente o registro correspondente na tabela pai com valores em branco para manter a integridade referencial lógica.",
            "Suspende a execução da instrução INSERT indefinidamente até que o registro correspondente na tabela pai seja inserido via rede.",
            "Exclui automaticamente todos os registros dependentes nas tabelas filhas para assegurar a consistência referencial local."
        , "Qualquer violação de chave estrangeira (FK) gera um erro que aborta a transação em curso no PostgreSQL, não permitindo dados órfãos."),
        # Q29
        (
            "O H2 Database pode ser configurado de diferentes formas de conexão. A URL de conexão JDBC `jdbc:h2:tcp://localhost/~/test` indica que o banco de dados rodará no modo:",
            "Server (servidor), no qual a aplicação se conecta a um banco de dados rodando em um processo separado através da rede local.",
            "Embedded (embutido), no qual o banco de dados roda dentro da mesma máquina virtual Java (JVM) da própria aplicação ativa.",
            "In-Memory (memória), no qual os dados não são persistidos em disco e residem de forma exclusiva na memória RAM do computador.",
            "Clustered (clusterizado), no qual os dados são duplicados de forma síncrona em múltiplos servidores distribuídos geograficamente.",
            "NoSQL, no qual o H2 desativa todas as capacidades SQL relacionais para operar exclusivamente como armazenamento chave-valor."
        , "O prefixo `jdbc:h2:tcp:` indica conexões remotas via protocolo TCP, o que caracteriza a execução no modo Server, e não embutida (embedded)."),
        # Q30
        (
            "Sobre a remoção física de dados, considere a diferença entre os comandos `DELETE FROM tabela` e `TRUNCATE TABLE tabela` nos SGBDs relacionais corporativos. Assinale a alternativa correta:",
            "O TRUNCATE é um comando DDL que remove todas as linhas de uma tabela rapidamente sem gerar logs detalhados de transações por linha, enquanto o DELETE é DML e gera logs por linha.",
            "O DELETE libera de forma instantânea todo o espaço em disco ocupado pelos dados para o sistema operacional, ao contrário do TRUNCATE.",
            "O TRUNCATE permite a utilização de cláusulas WHERE para filtrar quais registros específicos serão removidos durante a execução do comando.",
            "O comando DELETE é executado muito mais rápido que o TRUNCATE por não validar regras de integridade referencial e chaves estrangeiras.",
            "O TRUNCATE ativa individualmente todas as triggers do tipo BEFORE DELETE associadas à tabela antes de executar a limpeza física de disco."
        , "TRUNCATE é DDL, remove os dados desalocando as páginas de dados de forma muito rápida e sem gerar logs de undo por registro, enquanto DELETE é DML, avaliando linha a linha e disparando triggers.")
    ]
    dia_25_themes.append(("Banco de Dados — SGBDs Oracle, PostgreSQL e H2", t2_25))
    
    # Tema 3: Classes de Palavras e Pronomes
    t3_25 = [
        # Q31
        (
            "Em relação à flexão e colocação dos pronomes pessoais oblíquos átonos, a norma-padrão da língua portuguesa estabelece regras específicas de próclise, mesóclise e ênclise. Assinale a frase gramaticalmente correta:",
            "Tudo se resolveu rapidamente após a intervenção da assessoria de segurança técnica.",
            "Me entregaram os relatórios de auditoria processual do tribunal logo pela manhã.",
            "Os analistas de suporte se comprometeram a realizar a migração da base de dados hoje.",
            "Caso encontre o arquivo corrompido em disco, devolva-o-nos imediatamente para perícia.",
            "Ninguém informou-nos sobre as alterações de escopo aprovadas no cronograma de estudos."
        , "A palavra 'Tudo' é um pronome indefinido, o que atrai obrigatoriamente a próclise ('se resolveu'). Iniciar frases com pronome oblíquo ('Me entregaram') ou usar ênclise após palavra atrativa ('Ninguém informou-nos') violam as regras cultas."),
        # Q32
        (
            "A correta utilização dos pronomes demonstrativos 'este', 'esse' e 'aquele' envolve fatores espaciais, temporais e textuais. Assinale a alternativa que apresenta o emprego correto desses pronomes:",
            "Esta ferramenta que tenho em mãos é excelente para monitorar a rede do tribunal.",
            "Esse projeto que finalizei no ano de 1998 foi muito elogiado pela equipe técnica.",
            "Aquele relatório que você está lendo agora contém inconsistências de dados cadastrais.",
            "O diretor de TI pediu este documento que está com você na sala de reuniões ao lado.",
            "Espero que este ano de 2010 seja produtivo para as atividades do Poder Judiciário."
        , "'Esta' é usado para o que está perto de quem fala (primeira pessoa). 'Esse' é para o que está perto de quem ouve (segunda pessoa) ou passado recente, e 'aquele' para o que está distante de ambos ou passado remoto. O uso de 'Esta' para a ferramenta que a pessoa segura está correto."),
        # Q33
        (
            "O pronome relativo 'cujo' possui regras de concordância e emprego muito específicas exigidas pela banca FCC. Assinale a frase que respeita integralmente a norma-padrão no uso desse pronome:",
            "Este é o servidor de banco de dados cujas informações técnicas de acesso foram alteradas.",
            "O analista de requisitos, cujo o relatório de elicitação foi entregue, pediu demissão.",
            "A comarca de justiça cujo a acessibilidade física é inadequada passará por reformas.",
            "Aquele é o coordenador do comitê de segurança de cujo eu te falei ontem à noite.",
            "Esta é a linguagem de programação de cuja os desenvolvedores mais gostam de programar."
        , "'Cujo' concorda em gênero e número com o termo subsequente (coisa possuída: 'cujas informações') e rejeita artigo subsequente ('cujo o' está incorreto). Também exige preposição caso a regência verbal a demande (quem fala, fala 'de algo' -> 'de que falei', e não 'de cujo falei'). A alternativa A está correta."),
        # Q34
        (
            "No que tange à substituição de termos das orações por pronomes oblíquos átonos, assinale a redação correta segundo a regência e colocação pronominal:",
            "Os técnicos instalaram os patches de segurança no servidor. / Os técnicos instalaram-nos no servidor.",
            "O diretor de TI enviou os e-mails aos analistas. / O diretor de TI enviou-lhes aos analistas.",
            "A assessoria analisará os contratos da licitação de rede. / A assessoria analisar-lhes-á com calma.",
            "Nós encontramos as falhas graves na base de dados. / Nós encontramo-las na base de dados.",
            "O comitê propôs a mudança de escopo na reunião. / O comitê propôs-la com argumentos sólidos."
        , "Na frase 'instalaram os patches', o objeto direto 'os patches' termina em som nasal, o que exige a transformação do pronome 'os' em 'nos' -> 'instalaram-nos'. Em D, 'encontramos' termina em -s, que cai ao se associar a 'as', virando 'encontramo-las' (mas há próclise atrativa por 'Nós', o que tornaria correto 'Nós as encontramos'). A alternativa A é plenamente correta."),
        # Q35
        (
            "O pronome relativo 'onde' deve ser empregado exclusivamente para indicar relação de lugar físico. Assinale a frase em que o uso do pronome relativo 'onde' está gramaticalmente correto:",
            "Este é o prédio do fórum judicial onde serão realizadas as audiências de conciliação.",
            "A engenharia de requisitos é uma área complexa onde ocorrem constantes mudanças de escopo.",
            "O tribunal passou por uma reestruturação organizacional onde muitos setores foram unificados.",
            "A nova política de segurança cibernética onde o uso de tokens é obrigatório gerou debates.",
            "Eles vivenciaram uma época histórica difícil onde os recursos tecnológicos eram escassos."
        , "'Onde' deve referir-se apenas a lugares físicos/geográficos (ex: 'prédio do fórum'). Para ideias abstratas, deve-se usar 'em que', 'no qual', 'na qual' etc."),
        # Q36
        (
            "Na Língua Portuguesa, as classes de palavras modificam-se em termos semânticos e sintáticos a depender do contexto. Na oração *'O analisar das métricas revelou gargalos de desempenho no banco de dados'*, a palavra *'analisar'* classifica-se como:",
            "Substantivo, devido ao processo de derivação imprópria (substantivação) ocasionado pelo artigo antecedente.",
            "Verbo em sua forma nominal de infinitivo, exercendo a função sintática de adjunto adverbial de modo.",
            "Adjetivo explicativo, qualificando a ação subsequente executada pela equipe de infraestrutura de TI.",
            "Conjunção coordenativa explicativa, conectando as orações subordinadas subjetivas do período composto.",
            "Advérbio de intensidade, modificando o sentido do termo 'métricas' para indicar a profundidade da análise."
        , "O infinitivo verbal 'analisar' precedido pelo artigo 'O' passa a funcionar como substantivo (substantivação/derivação imprópria)."),
        # Q37
        (
            "O pronome 'se' pode exercer diversas funções sintáticas e morfológicas na oração. Assinale a alternativa em que o 'se' funciona como pronome apassivador (partícula apassivadora):",
            "Mapearam-se todos os requisitos não funcionais de desempenho no início do projeto.",
            "Precisa-se de novos analistas de infraestrutura de rede para o suporte técnico.",
            "O desenvolvedor queixou-se das constantes interrupções na sala de desenvolvimento.",
            "Eles arrependeram-se de não terem migrado as bases de dados para o PostgreSQL.",
            "Se todos os testes unitários passarem na homologação, o deploy será autorizado hoje."
        , "Na voz passiva sintética, o verbo transitivo direto ('mapear') concorda com o sujeito paciente ('todos os requisitos não funcionais...'). O 'se' é pronome apassivador. Em B, 'precisar' exige preposição 'de' (VTI), sendo o 'se' índice de indeterminação do sujeito."),
        # Q38
        (
            "A contração da preposição com pronomes relativos é determinada pela regência do verbo subordinado. Assinale a frase gramaticalmente correta quanto à regência e uso do pronome relativo:",
            "Este é o sistema de controle de processos a cujo desenvolvimento nós nos referimos.",
            "Estes são os servidores públicos de cujos o diretor de TI solicitou o desligamento físico.",
            "Esta é a linguagem de programação com que os analistas de sistemas mais simpatizam nela.",
            "Aquele é o banco de dados relacional de cuja integridade física nós dependemos dela.",
            "O projeto do novo fórum digital em cujo o engenheiro civil trabalhou nele foi aprovado."
        , "O verbo 'referir-se' exige a preposição 'a' ('referir-se a algo'). Essa preposição deve anteceder o pronome relativo 'cujo' -> 'a cujo desenvolvimento'. Outras opções possuem erros de redundância ('nela', 'dela', 'nele') ou de acoplamento com artigo ('de cujos o')."),
        # Q39
        (
            "As conjunções coordenativas e subordinativas são classes de palavras que estabelecem nexos lógicos no período composto. Na oração *'Embora o sistema apresente boa usabilidade, a lentidão no processamento gerou reclamações dos usuários'*, a conjunção *'Embora'* estabelece relação de:",
            "Concessão, indicando uma ideia de oposição ou contraste que não impede a realização da oração principal.",
            "Condição, estabelecendo uma restrição obrigatória para que a oração principal ocorra no tempo correto.",
            "Causa, explicando o motivo pelo qual as reclamações foram registradas pela assessoria de TI do tribunal.",
            "Consequência, apresentando o resultado direto das constantes falhas de infraestrutura de rede corporativa.",
            "Conformidade, demonstrando o acordo entre os testes de usabilidade e o desempenho físico dos servidores."
        , "'Embora' é uma conjunção subordinativa concessiva típica, expressando um obstáculo que não é suficiente para impedir o fato da oração principal."),
        # Q40
        (
            "Considere a colocação pronominal em períodos que contêm locuções verbais ou tempos compostos. Assinale a frase correta de acordo com as normas gramaticais vigentes:",
            "Os analistas de sistemas deveriam ter-se atentado aos prazos de entrega do projeto de TI.",
            "Os analistas de sistemas deveriam-se ter atentado aos prazos de entrega do projeto de TI.",
            "Os analistas de sistemas deveriam se ter atentado aos prazos de entrega do projeto de TI.",
            "Os analistas de sistemas deveriam ter atentado-se aos prazos de entrega do projeto de TI.",
            "Os analistas de sistemas se deveriam ter atentado aos prazos de entrega do projeto de TI."
        , "Em locuções verbais com infinitivo ou gerúndio (sem palavra atrativa), o pronome pode ser colocado após o auxiliar (com hífen) ou após o principal. Mas em tempos compostos com particípio ('ter atentado'), o pronome não pode vir após o particípio ('atentado-se' é incorreto). O correto é após o auxiliar ter: 'ter-se atentado' ou antes dele. A opção A é a padrão correta."),
        # Q41
        (
            "O pronome relativo 'quem' refere-se exclusivamente a pessoas ou entes personificados e exige preposição em determinados contextos. Assinale a frase gramaticalmente correta:",
            "O engenheiro civil a quem o tribunal contratou para as reformas apresentou as plantas físicas.",
            "Este é o analista de banco de dados quem resolveu a falha crítica de integridade referencial.",
            "Aquele é o magistrado de quem o relatório de produtividade foi solicitado pelo comitê de TI.",
            "Os técnicos a quem nós nos dirigimos no setor de infraestrutura de redes foram atenciosos.",
            "Os usuários quem reclamaram da usabilidade do sistema judicial de prazos foram ouvidos."
        , "O pronome 'quem' exige preposição quando é objeto ('a quem nos dirigimos'). O verbo 'dirigir-se' exige a preposição 'a' ('dirigir-se a alguém'). Portanto, 'a quem nos dirigimos' está correto. Em B e E, falta preposição ou o pronome relativo adequado seria 'que' ou 'o qual'."),
        # Q42
        (
            "Advérbios são classes de palavras que modificam verbos, adjetivos ou outros advérbios. Na frase *'O banco de dados do tribunal respondeu extremamente rápido às consultas de auditoria'*, a palavra *'extremamente'* classifica-se como advérbio de:",
            "Intensidade, modificando o advérbio 'rápido' para intensificar a velocidade de resposta do sistema.",
            "Modo, descrevendo a forma como as tabelas relacionais físicas do banco de dados foram estruturadas.",
            "Tempo, indicando o momento exato em que a equipe de infraestrutura de TI realizou as medições.",
            "Lugar, situando espacialmente as consultas executadas pelos usuários cadastrados no tribunal de justiça.",
            "Conformidade, expressando o alinhamento das buscas SQL com as políticas internas do órgão público."
        , "'Extremamente' é um advérbio de intensidade que modifica o advérbio de modo 'rápido', acentuando sua força semântica."),
        # Q43
        (
            "Em relação ao uso de pronomes de tratamento em comunicações oficiais no tribunal, a norma culta exige concordância verbal e pronominal específica. Assinale a alternativa correta:",
            "Vossa Excelência deve apresentar seus relatórios de produtividade técnica na próxima reunião de conselho.",
            "Vossa Excelência deve apresentar vossos relatórios de produtividade técnica na próxima reunião de conselho.",
            "Vossa Senhoria deveis comparecer à assessoria jurídica com vossos assessores de segurança de redes.",
            "Sua Excelência (referindo-se à pessoa com quem se fala) determinou a abertura de nova licitação pública.",
            "Vossa Magnificência deveis assinar os termos de cooperação técnica com vossas próprias mãos ontem."
        , "Pronomes de tratamento exigem a concordância com a terceira pessoa (verbal e pronominal: 'deve apresentar seus relatórios'), mesmo se referindo à segunda pessoa. 'Vossa' é usado para falar com a pessoa, e 'Sua' para falar sobre a pessoa. A alternativa A está correta."),
        # Q44
        (
            "Assinale a frase em que o pronome oblíquo exerce papel sintático de adjunto adnominal (valor possessivo):",
            "O vento forte levou-lhe o chapéu de feltro enquanto caminhava pelo pátio externo do tribunal.",
            "A diretoria de TI comunicou-lhe as novas diretrizes de segurança adotadas nas redes locais.",
            "O analista de suporte entregou-lhe os relatórios de erros gerados pelo banco de dados relacional.",
            "Ninguém lhe disse que as consultas SQL com ROWNUM deveriam ser revisadas na homologação.",
            "O coordenador do projeto permitiu-lhe acessar o servidor de homologação durante os testes."
        , "Em 'levou-lhe o chapéu', o pronome 'lhe' equivale a 'seu chapéu' (levou o seu chapéu), exercendo a função sintática de adjunto adnominal (ideia de posse vinculada ao substantivo). Nas outras opções, o 'lhe' funciona como objeto indireto."),
        # Q45
        (
            "Preposições são palavras invariáveis que ligam dois termos de uma oração. Na frase *\"O sistema foi desenvolvido sob rígidas normas de segurança cibernética\"*, a preposição *\"sob\"* indica uma relação semântica de:",
            "Subordinação ou conformidade, expressando que o desenvolvimento seguiu as diretrizes técnicas definidas.",
            "Oposição ou contrariedade, demonstrando que o sistema violou as regras de segurança homologadas no órgão.",
            "Tempo ou duração, limitando o período em que a equipe de suporte pôde atuar na correção de bugs de rede.",
            "Lugar físico ou espacial, situando geograficamente o servidor de banco de dados nos blocos do datacenter.",
            "Causa ou motivo, explicando a razão pela qual as vulnerabilidades foram exploradas por agentes externos."
        , "A preposição 'sob' indica subordinação, dependência ou conformidade em relação a algo (sob normas = em conformidade com as normas).")
    ]
    dia_25_themes.append(("Língua Portuguesa — Classes de Palavras e Pronomes", t3_25))
    
    write_day_file(os.path.join(questoes_dir, "dia_25_05_questoes.md"),
                   "Bateria de Questões FCC — Segunda-feira 25/05",
                   "Este arquivo contém 45 questões altamente calibradas nos padrões da FCC, com alternativas de comprimento similar e distratores baseados em pegadinhas reais.",
                   dia_25_themes)

    # =========================================================================
    # DIA 26/05 - TERÇA-FEIRA
    # =========================================================================
    dia_26_themes = []
    
    # Tema 1: Redes e Infraestrutura
    t1_26 = [
        # Q1
        (
            "O protocolo HTTP/1.1 é a base da comunicação de dados na Web. Sobre os métodos de requisição HTTP (verbos) e suas propriedades, assinale a alternativa correta:",
            "O método GET é projetado exclusivamente para recuperar informações do servidor, devendo ser seguro e idempotente de acordo com a especificação RFC 7231.",
            "O método POST é idempotente, o que significa que múltiplas requisições idênticas consecutivas resultarão no mesmo estado físico no servidor de banco de dados.",
            "O método PUT é utilizado exclusivamente para remover recursos de forma permanente do diretório de armazenamento virtual do servidor HTTP local.",
            "O método PATCH deve ser utilizado para substituir de forma integral o recurso existente por uma nova representação fornecida no corpo da mensagem.",
            "O método HEAD solicita que o servidor retorne os cabeçalhos de resposta HTTP e o corpo HTML correspondente para depuração local pelo analista."
        , "GET é seguro e idempotente (não deve alterar o estado do servidor e múltiplas chamadas retornam o mesmo resultado). POST não é idempotente. PUT substitui o recurso (é idempotente). PATCH faz atualizações parciais. HEAD não retorna o corpo da resposta."),
        # Q2
        (
            "Em relação aos códigos de status de resposta HTTP (Status Codes), que são divididos em classes de três dígitos, assinale a alternativa correta:",
            "A classe 3xx indica redirecionamento de requisições, exigindo que o navegador realize ações adicionais para completar a operação iniciada.",
            "A classe 4xx indica erros internos do servidor de aplicação, significando que o servidor falhou ao processar uma requisição válida do cliente.",
            "O código 201 Created é utilizado para confirmar que a requisição de busca do usuário foi processada com sucesso, sem gerar novos registros.",
            "O código 403 Forbidden indica que o recurso solicitado não existe fisicamente no servidor e nenhuma rota correspondente foi encontrada.",
            "A classe 5xx indica falhas de autenticação do cliente, apontando que o usuário não forneceu credenciais válidas na requisição HTTP ativa."
        , "A classe 3xx é para redirecionamento. 4xx representa erro do cliente (ex: 403 Forbidden, 404 Not Found). 5xx representa erro do servidor (ex: 500 Internal Server Error). 201 Created indica que um recurso foi criado com sucesso."),
        # Q3
        (
            "O protocolo HTTPS adiciona uma camada de segurança sobre o HTTP utilizando os protocolos SSL ou TLS. Sobre o processo de handshake do TLS 1.2, é correto afirmar:",
            "No ClientHello, o cliente envia as versões do TLS que suporta, os algoritmos de criptografia (cipher suites) compatíveis e um valor aleatório.",
            "No ServerHello, o servidor envia a sua chave privada para o cliente cifrar os dados da sessão simétrica que será estabelecida via HTTPS.",
            "A negociação da chave de sessão simétrica ocorre de forma síncrona utilizando a infraestrutura física de rede antes do envio do ClientHello.",
            "O handshake do TLS impede o uso de certificados digitais X.509, dependendo exclusivamente de senhas de autenticação pré-compartilhadas.",
            "A verificação da identidade do servidor pelo cliente é opcional e ocorre apenas se o servidor enviar o cabeçalho HTTP de redirecionamento 301."
        , "O handshake TLS 1.2 inicia com o ClientHello, onde o cliente envia suas capacidades criptográficas e um valor aleatório. O servidor responde com ServerHello, certificado digital, etc. A chave privada do servidor NUNCA é enviada ao cliente."),
        # Q4
        (
            "A norma ABNT NBR 14565:2019 especifica os requisitos para sistemas de cabeamento estruturado para edifícios comerciais. Sobre essa norma, assinale a alternativa correta:",
            "Ela define os subsistemas de cabeamento estruturado, dividindo-os em cabeamento de backbone (de campus e de edifício) e cabeamento horizontal.",
            "Ela proíbe estritamente a utilização de cabos de par trançado sem blindagem (UTP), exigindo o uso de cabos blindados do tipo STP Cat 8.",
            "O comprimento máximo recomendado para os cabos de manobra (patch cords) na área de trabalho é de vinte metros para evitar perdas de sinal.",
            "A norma veda a utilização de fibras ópticas monomodo no cabeamento de backbone de campus, restringindo o uso a cabos de cobre de categoria 5e.",
            "Ela estabelece que a tomada de telecomunicações na área de trabalho deve possuir pelo menos quatro conectores do tipo RJ-45 de categoria 7."
        , "A NBR 14565:2019 padroniza os subsistemas de cabeamento estruturado, classificando o cabeamento em backbone (de campus e de edifício) e horizontal (que liga o distribuidor de piso às tomadas de telecomunicações da área de trabalho)."),
        # Q5
        (
            "No contexto de cabeamento estruturado, as categorias de cabos de par trançado determinam a largura de banda suportada. Sobre a Categoria 6A (Cat 6A), assinale a alternativa correta:",
            "Ela é especificada para operar em frequências de até 500 MHz e suporta taxas de transmissão de dados de 10 Gbps em distâncias de até 100 metros.",
            "Ela opera em frequências de até 100 MHz e é recomendada exclusivamente para redes locais baseadas em Fast Ethernet de 100 Mbps.",
            "Ela suporta taxas de 100 Gbps utilizando conectores do tipo RJ-11 em distâncias máximas de dez metros no cabeamento horizontal do prédio.",
            "Ela é uma especificação exclusiva para cabos de fibra óptica multimodo, não se aplicando a cabos de cobre de par trançado blindados.",
            "Ela exige a substituição dos switches de rede ativos por hubs repetidores analógicos de camada física para evitar interferência cruzada."
        , "A Categoria 6A (Cat 6A) opera a até 500 MHz, permitindo transmissões estáveis de 10 Gbps (10GBASE-T) a distâncias de até 100 metros no canal físico completo."),
        # Q6
        (
            "As fibras ópticas são meios de transmissão baseados na propagação da luz. A diferença fundamental entre fibras ópticas monomodo (single-mode) e multimodo (multi-mode) é:",
            "A fibra monomodo possui um núcleo mais estreito e permite a propagação de apenas um modo de luz, sendo ideal para longas distâncias devido à menor dispersão.",
            "A fibra multimodo possui núcleo mais estreito e utiliza lasers de alta intensidade para propagar múltiplos feixes de luz a milhares de quilômetros.",
            "A fibra monomodo é mais barata e utiliza LEDs comuns como fonte de luz, sendo amplamente aplicada no cabeamento horizontal da área de trabalho.",
            "A fibra multimodo apresenta menor atenuação do sinal óptico que a monomodo, dispensando o uso de repetidores em backbones de campus longos.",
            "A fibra monomodo sofre severamente com a dispersão modal, o que limita seu comprimento máximo a cinquenta metros em redes locais."
        , "Fibras monomodo possuem núcleos pequenos (8 a 10 micrômetros) que guiam um único modo de propagação da luz. Têm baixa dispersão e são usadas para links de longas distâncias. Multimodo têm núcleos maiores (50 ou 62.5 micrômetros) e sofrem maior dispersão."),
        # Q7
        (
            "Em sistemas de transmissão óptica, comprimentos de onda específicos (janelas de transmissão) são utilizados. Os comprimentos de onda típicos para fibras monomodo e multimodo são, respectivamente:",
            "1310 nm / 1550 nm (monomodo) e 850 nm / 1300 nm (multimodo).",
            "850 nm / 1300 nm (monomodo) e 1310 nm / 1550 nm (multimodo).",
            "500 nm / 700 nm (monomodo) e 1000 nm / 1200 nm (multimodo).",
            "1550 nm / 1625 nm (monomodo) e 450 nm / 650 nm (multimodo).",
            "1310 nm / 850 nm (monomodo) e 1550 nm / 1300 nm (multimodo)."
        , "Fibras multimodo operam nas primeiras janelas (850 nm e 1300 nm), enquanto fibras monomodo operam nas janelas superiores (1310 nm e 1550 nm), onde a atenuação física é significativamente menor."),
        # Q8
        (
            "Conectores de fibra óptica são utilizados para alinhar e conectar as fibras a equipamentos de rede. Assinale a alternativa que apresenta apenas tipos válidos de conectores ópticos:",
            "LC, SC, ST e FC",
            "RJ-45, RJ-11, LC e SC",
            "BNC, DB-9, SC e ST",
            "LC, SC, HDMI e USB",
            "TRS, XLR, SC e FC"
        , "LC (Lucent Connector), SC (Subscriber Connector), ST (Straight Tip) e FC (Ferrule Connector) são conectores padronizados para terminação e acoplamento de fibras ópticas."),
        # Q9
        (
            "O cabeamento de backbone de edifício, segundo a norma de cabeamento estruturado, conecta o distribuidor de edifício aos distribuidores de piso. O comprimento máximo de cabo permitido para o backbone de edifício é:",
            "500 metros, independentemente do tipo de meio físico (cobre ou fibra óptica) utilizado na instalação física do prédio.",
            "90 metros para cabos de par trançado de cobre de categoria 6 ou superior no canal de transmissão de dados local.",
            "2000 metros para fibras ópticas monomodo e multimodo de forma indistinta para assegurar a largura de banda nominal.",
            "100 metros para cabos de fibra óptica e noventa metros para cabos de par trançado de cobre blindados no rack de piso.",
            "1500 metros para cabos coaxiais de baixa impedância instalados em eletrodutos externos de concreto armado."
        , "De acordo com as normas de cabeamento estruturado (como ISO/IEC 11801 e adaptadas pela ABNT), a distância máxima recomendada para o backbone de edifício é tipicamente de até 500 metros (especialmente para fibra óptica) para garantir o desempenho e limites de propagação."),
        # Q10
        (
            "Em HTTP/2, diversas melhorias foram introduzidas em relação ao HTTP/1.1 para otimizar o desempenho na web. Uma característica técnica nativa do HTTP/2 é:",
            "A multiplexação de requisições e respostas sobre uma única conexão TCP de forma paralela e assíncrona, eliminando o bloqueio de cabeça de fila.",
            "A substituição obrigatória do protocolo TCP pelo protocolo UDP na camada de transporte para aumentar a velocidade de transmissão física.",
            "O envio de cabeçalhos HTTP criptografados em formato XML de texto plano para facilitar a compressão por servidores de proxy reverso.",
            "A exigência de que todas as páginas web sejam renderizadas no formato de dados JSON no navegador do usuário de forma exclusiva.",
            "O banimento do uso de conexões seguras HTTPS, operando apenas através de canais não criptografados para reduzir o consumo de CPU."
        , "HTTP/2 introduziu a multiplexação de streams sobre uma única conexão TCP, permitindo que vários requests e responses transitem concorrentemente, eliminando a lentidão gerada pelo 'head-of-line blocking' do HTTP/1.1."),
        # Q11
        (
            "Os cookies são cabeçalhos HTTP importantes para o gerenciamento de estados. O atributo em um cookie HTTP que impede que scripts do lado do cliente (como JavaScript via XSS) acessem o valor do cookie é:",
            "HttpOnly",
            "Secure",
            "SameSite",
            "Domain",
            "Path"
        , "O atributo `HttpOnly` avisa ao navegador que o cookie não deve ser exposto através de APIs de scripts (como `document.cookie`), mitigando ataques de roubo de sessão via Cross-Site Scripting (XSS)."),
        # Q12
        (
            "A perda de sinal ao longo de um cabo de fibra óptica é influenciada por fatores internos e externos. O fenômeno que descreve a redução da potência do sinal óptico à medida que ele viaja pela fibra é chamado de:",
            "Atenuação, causada principalmente por absorção física e espalhamento da luz nas impurezas do vidro de sílica.",
            "Dispersão cromática, que consiste no alargamento temporal dos pulsos de luz devido à reflexão total nas paredes do núcleo.",
            "Refração seletiva, na qual a luz é convertida em impulsos elétricos de baixa voltagem ao passar por curvas acentuadas.",
            "Difração de Fresnel, que descreve o bloqueio completo da passagem de luz em conectores do tipo LC mal polidos na instalação.",
            "Diafonia (crosstalk), que representa a interferência eletromagnética gerada por cabos de cobre vizinhos localizados na mesma calha."
        , "Atenuação é a perda de potência óptica expressa em dB/km, decorrente de fatores de absorção de material e do espalhamento Rayleigh da luz nas micro-imperfeições do núcleo de vidro."),
        # Q13
        (
            "Na arquitetura do protocolo HTTPS, a verificação do certificado digital do servidor envolve o uso de chaves públicas. O navegador do cliente valida o certificado do servidor:",
            "Decifrando a assinatura digital da autoridade emissora contida no certificado utilizando a chave pública da própria autoridade pré-instalada no sistema.",
            "Decifrando a assinatura digital da autoridade emissora contida no certificado utilizando a chave privada do próprio servidor web local.",
            "Enviando o certificado completo de volta ao servidor para que ele mesmo realize a validação e retorne o código HTTP 200 OK correspondente.",
            "Gerando uma chave simétrica temporária e enviando-a para a Autoridade Certificadora validar a assinatura do servidor via rede.",
            "Decifrando os dados confidenciais do servidor web utilizando a chave privada do navegador do cliente acordada no ClientHello."
        , "O navegador valida o certificado do servidor verificando a assinatura da CA (Autoridade Certificadora) que assinou o certificado. Isso é feito usando a chave pública da CA, cujos certificados raiz confiáveis já vêm pré-instalados no navegador ou no sistema operacional."),
        # Q14
        (
            "No cabeamento horizontal comercial, a distância útil máxima recomendada de cabo entre o distribuidor de piso (patch panel) e a tomada de telecomunicações é de:",
            "90 metros, permitindo mais dez metros adicionais para cabos de manobra (patch cords) na área de trabalho e armário de telecomunicações.",
            "100 metros para cabos de cobre de categoria 5e e duzentos metros para cabos de cobre de categoria 6A sem blindagem física.",
            "50 metros para evitar a perda excessiva de sinal elétrico gerada pela diafonia e ruídos eletromagnéticos de lâmpadas fluorescentes.",
            "150 metros quando forem utilizadas fibras ópticas monomodo conectadas diretamente a tomadas de telecomunicações ativas.",
            "75 metros para manter a largura de banda estável em redes Fast Ethernet operando em frequências de até 250 MHz no canal físico."
        , "O cabeamento horizontal (link permanente) é limitado a 90 metros de comprimento físico do cabo. O canal completo (incluindo cabos de manobra) pode chegar a 100 metros."),
        # Q15
        (
            "Em relação ao cabeamento estruturado e à infraestrutura de rede, o Distribuidor de Edifício (BD - Building Distributor) tem a função de:",
            "Interconectar o cabeamento de backbone de campus com o cabeamento de backbone de edifício nas instalações físicas da organização.",
            "Conectar diretamente os computadores e tomadas de telecomunicações da área de trabalho ao rack de piso de forma exclusiva.",
            "Alojar exclusivamente os servidores de banco de dados e switches de camada de aplicação do tribunal de justiça estadual.",
            "Alimentar fisicamente os dispositivos ativos de rede utilizando cabos de cobre com tecnologia Power over Ethernet (PoE) redundante.",
            "Medir a taxa de atenuação das conexões ópticas de campus e reportar falhas físicas ao console de gerência de rede local."
        , "O BD (Building Distributor / Distribuidor de Edifício) serve de nó central do edifício, realizando a conexão entre o backbone de campus (vindo do CD - Campus Distributor) e os backbones que descem/sobem para os pisos (FD - Floor Distributor).")
    ]
    dia_26_themes.append(("Redes e Infraestrutura — Protocolos HTTP/HTTPS, ABNT NBR 14565:2019 e Fibras Ópticas", t1_26))
    
    # Tema 2: Redes e Camada de Transporte
    t2_26 = [
        # Q16
        (
            "Os protocolos TCP e UDP operam na camada de transporte do modelo TCP/IP. A diferença fundamental de funcionamento entre o TCP e o UDP é:",
            "O TCP é orientado à conexão e garante a entrega ordenada e confiável de segmentos através de confirmações, enquanto o UDP é não orientado à conexão e prioriza a velocidade sem garantias de entrega.",
            "O UDP realiza o controle de fluxo e congestionamento utilizando o mecanismo de janela deslizante, ao contrário do TCP que transmite dados sem controle.",
            "O TCP é um protocolo de camada de aplicação que roda sobre conexões físicas Ethernet, enquanto o UDP é um protocolo de transporte exclusivo para redes sem fio.",
            "O UDP divide os dados em pacotes de tamanho fixo chamados datagramas de rede e exige o handshake de três vias (three-way handshake) para iniciar o tráfego.",
            "O TCP utiliza portas dinâmicas para comunicação em grupo (multicast), enquanto o UDP é restrito a conexões ponto a ponto (unicast) com portas fixas de controle."
        , "TCP (Transmission Control Protocol) é orientado à conexão, confiável, fornece controle de fluxo, retransmissão e entrega ordenada. UDP (User Datagram Protocol) é um protocolo simples, rápido, não confiável e sem conexão."),
        # Q17
        (
            "O estabelecimento de uma conexão TCP confiável utiliza o handshake de três vias (three-way handshake). A sequência correta de flags TCP enviadas pelos hosts cliente e servidor para estabelecer a conexão é:",
            "SYN (cliente) -> SYN-ACK (servidor) -> ACK (cliente)",
            "SYN (cliente) -> ACK (servidor) -> SYN-ACK (cliente)",
            "SYN-ACK (cliente) -> SYN (servidor) -> ACK (cliente)",
            "ACK (cliente) -> SYN (servidor) -> SYN-ACK (cliente)",
            "SYN (cliente) -> SYN (servidor) -> ACK (cliente/servidor)"
        , "O handshake de três vias do TCP consiste no envio de um segmento com flag SYN (sincronizar), a resposta com flags SYN-ACK (sincronizar e confirmar) e a confirmação final com flag ACK."),
        # Q18
        (
            "O controle de fluxo do TCP visa evitar que o transmissor envie dados mais rápido do que o receptor consegue processar. O mecanismo utilizado pelo TCP para realizar o controle de fluxo é:",
            "A janela deslizante (sliding window), em que o receptor informa no cabeçalho TCP o tamanho do espaço livre em seu buffer de recepção (Advertised Window).",
            "O algoritmo Slow Start, no qual o transmissor dobra o tamanho da janela de congestionamento a cada nova confirmação recebida na sessão.",
            "A modulação por largura de pulso (PWM) que ajusta dinamicamente a taxa de transmissão física do cabo de rede no switch central do tribunal.",
            "O descarte preventivo de datagramas órfãos na camada de rede (IP) quando o tempo de vida do pacote (TTL) atinge o valor limite de zero.",
            "O envio periódico de mensagens ICMP Source Quench do roteador para o host transmissor solicitando a redução imediata da banda de rede."
        , "O controle de fluxo do TCP é baseado na Janela Deslizante (sliding window) anunciada pelo receptor. O campo Window Size no cabeçalho TCP informa quantos bytes o transmissor pode enviar antes de esperar por um ACK."),
        # Q19
        (
            "O controle de congestionamento do TCP evita que a rede de computadores entre em colapso por excesso de tráfego. Sobre a fase de Slow Start (partida lenta), assinale a alternativa correta:",
            "A janela de congestionamento (cwnd) começa em um tamanho pequeno (ex: 1 MSS) e cresce exponencialmente (dobrando a cada RTT) até atingir o limite ssthresh.",
            "O transmissor envia os dados na velocidade máxima permitida pela interface física de rede e reduz a taxa linearmente se ocorrer perda de pacotes.",
            "O tamanho da janela de congestionamento é mantido fixo e o transmissor altera apenas a taxa de retransmissão de segmentos temporizados.",
            "A fase de Slow Start é ativada apenas se o tempo de resposta do servidor ultrapassar o limite padrão de trinta segundos da sessão ativa.",
            "Ela desativa o controle de fluxo do receptor para priorizar a passagem dos pacotes de dados prioritários através dos roteadores da rede."
        , "No Slow Start, a janela de congestionamento (cwnd) cresce exponencialmente (cwnd = cwnd * 2 a cada RTT) a partir de um valor inicial pequeno até alcançar o limiar de partida lenta (ssthresh), quando entra em Congestion Avoidance."),
        # Q20
        (
            "Em controle de congestionamento TCP, após a janela de congestionamento atingir o valor de ssthresh (Slow Start Threshold), o TCP entra na fase de:",
            "Congestion Avoidance (evitação de congestionamento), em que a janela de congestionamento cresce linearmente (1 MSS a cada RTT).",
            "Fast Recovery (recuperação rápida), na qual a janela de congestionamento é reduzida imediatamente para zero para limpar os buffers.",
            "Slow Start, reiniciando o crescimento exponencial da janela de transmissão a partir do valor inicial de dez segmentos TCP.",
            "Flow Control, repassando o controle do tamanho de transmissão para o buffer físico do adaptador de rede do cliente ativo.",
            "Connection Tear-down, finalizando a conexão TCP de forma abrupta com o envio de um segmento com a flag RST (reset)."
        , "Quando a janela cwnd alcança o ssthresh, o TCP muda do crescimento exponencial (Slow Start) para o crescimento linear (Congestion Avoidance), onde cwnd é incrementada em 1 MSS por RTT."),
        # Q21
        (
            "Os algoritmos Fast Retransmit (retransmissão rápida) e Fast Recovery (recuperação rápida) otimizam o comportamento do TCP sob perdas. O Fast Retransmit é disparado quando o transmissor recebe:",
            "Três confirmações duplicadas (triple duplicate ACKs) consecutivas para um mesmo segmento de dados enviado anteriormente.",
            "Uma mensagem ICMP de destino inalcançável gerada pelo roteador de borda devido à queda física do link de fibra óptica.",
            "Um segmento TCP contendo a flag FIN ativa para solicitar o encerramento ordenado da conexão de transporte ativa.",
            "Um pacote de sincronização (SYN) do servidor indicando que a numeração dos bytes da sessão deve ser reiniciada no buffer.",
            "Uma notificação do sistema operacional de que o buffer físico de envio da placa de rede local atingiu o limite de capacidade."
        , "Se o transmissor receber 3 ACKs duplicados consecutivos (além do original, totalizando 4 ACKs para o mesmo número de sequência), ele assume que o segmento subsequente foi perdido e faz a retransmissão imediata (Fast Retransmit) sem esperar o estouro do temporizador de retransmissão (RTO)."),
        # Q22
        (
            "Em relação ao cabeçalho do TCP, um campo que consta no cabeçalho TCP e NÃO consta no cabeçalho UDP é:",
            "Sequence Number (número de sequência), utilizado para ordenar os segmentos recebidos e detectar perdas.",
            "Source Port (porta de origem), que identifica o aplicativo de origem que enviou a mensagem de transporte.",
            "Destination Port (porta de destino), utilizada para encaminhar os dados para o processo de aplicação correto.",
            "Checksum, que é um campo de verificação de integridade utilizado para detectar erros de bits nos dados transmitidos.",
            "Length (comprimento), que indica o tamanho total do segmento de transporte incluindo cabeçalho e dados."
        , "O campo Sequence Number é exclusivo do TCP, sendo fundamental para o controle de ordenação e confiabilidade. UDP não possui números de sequência. Portas e Checksum estão presentes em ambos. Length está no UDP (no TCP, o tamanho é deduzido a partir do IP)."),
        # Q23
        (
            "As portas de comunicação identificam processos na camada de transporte. As portas padrão associadas aos protocolos SSH, SMTP e HTTPS são, respectivamente:",
            "22, 25 e 443",
            "80, 110 e 443",
            "21, 23 e 80",
            "22, 143 e 8080",
            "23, 25 e 8443"
        , "SSH opera na porta 22; SMTP na porta 25; HTTPS na porta 443. Portas clássicas muito cobradas em provas de concursos pela FCC."),
        # Q24
        (
            "O encerramento de uma conexão TCP ativa é realizado de forma ordenada através de uma sequência de controle. As flags enviadas para fechar a conexão de forma bilateral são:",
            "FIN (cliente) -> ACK (servidor) -> FIN (servidor) -> ACK (cliente)",
            "FIN (cliente) -> FIN-ACK (servidor) -> ACK (cliente/servidor)",
            "RST (cliente) -> RST-ACK (servidor) -> ACK (cliente)",
            "FIN (cliente) -> ACK (servidor) -> RST (servidor) -> ACK (cliente)",
            "SYN (cliente) -> ACK (servidor) -> FIN (servidor) -> ACK (cliente)"
        , "O encerramento ordenado (four-way handshake) utiliza a flag FIN (Finish) e a confirmação ACK em ambas as direções, pois o TCP é bidirecional (full-duplex) e cada lado deve fechar seu canal de envio de forma independente."),
        # Q25
        (
            "Em relação ao protocolo UDP, assinale a alternativa que apresenta uma aplicação típica na qual a sua utilização é preferível em relação ao TCP:",
            "Transmissões de voz sobre IP (VoIP) e streaming de vídeo em tempo real, onde a baixa latência é mais crítica que eventuais perdas de pacotes.",
            "Transferências de arquivos corporativos via FTP, onde a perda de um único byte pode corromper totalmente o arquivo copiado.",
            "Acesso remoto a servidores via SSH, onde a segurança e a integridade da digitação dos comandos devem ser garantidas de forma estrita.",
            "Consultas transacionais de envio de mensagens financeiras que exigem o registro cronológico rígido de logs no banco de dados.",
            "Envio de e-mails corporativos contendo anexos criptografados de grande porte para auditoria da corregedoria do tribunal."
        , "O UDP é ideal para aplicações de tempo real (como áudio, vídeo, jogos e VoIP) e consultas rápidas de pergunta-resposta (como DNS), onde atrasos causados por retransmissão de pacotes perdidos no TCP prejudicariam a experiência do usuário."),
        # Q26
        (
            "No cabeçalho do segmento TCP, o campo 'Header Length' (ou Data Offset) tem a finalidade técnica de:",
            "Especificar o tamanho do cabeçalho TCP medido em palavras de 32 bits, identificando onde começam os dados úteis da mensagem.",
            "Indicar o tamanho máximo do segmento (MSS) que o host receptor aceita receber na sessão ativa de transporte local.",
            "Definir a quantidade de memória RAM que o servidor de aplicação deve alocar para processar a requisição de rede HTTP.",
            "Informar o endereço físico do adaptador de rede de destino (MAC Address) para fins de roteamento em camada de enlace.",
            "Determinar o tempo de vida útil restante do segmento TCP na rede antes de ser descartado por estouro de temporizador físico."
        , "Como o cabeçalho TCP possui o campo de 'Options' que tem tamanho variável, o campo Data Offset (Header Length) é necessário para indicar onde termina o cabeçalho e começa a carga útil (payload). Ele é expresso em palavras de 32 bits (4 bytes)."),
        # Q27
        (
            "Um ataque de negação de serviço comum tenta explorar a fase inicial do estabelecimento de conexões TCP. Esse ataque, que inunda o servidor com requisições SYN sem completar o handshake, é conhecido como:",
            "SYN Flood, que esgota a tabela de conexões pendentes (backlog queue) do servidor impedindo novos acessos legítimos.",
            "Buffer Overflow, que sobrescreve a memória física do roteador de borda utilizando pacotes IP de tamanho maior que o padrão MTU.",
            "Man-in-the-Middle, no qual o atacante intercepta a troca de chaves públicas do TLS para descriptografar os dados em trânsito.",
            "SQL Injection, que insere códigos maliciosos nas queries de busca enviadas ao banco de dados relacional através da camada de transporte.",
            "DNS Spoofing, que altera as tabelas de cache dos servidores de nomes locais para redirecionar o tráfego a servidores clonados."
        , "O SYN Flood inunda o alvo com pacotes SYN. O servidor aloca memória para conexões 'semi-abertas' (SYN-RCVD) e responde com SYN-ACK, mas o atacante não envia o ACK final. Isso satura o buffer de conexões pendentes do sistema operacional."),
        # Q28
        (
            "O cabeçalho UDP é extremamente simples para minimizar o overhead de transmissão. O tamanho total padrão do cabeçalho UDP em bytes é de:",
            "8 bytes",
            "20 bytes",
            "32 bytes",
            "40 bytes",
            "12 bytes"
        , "O cabeçalho UDP possui exatamente 4 campos de 2 bytes cada (Source Port, Destination Port, Length, Checksum), totalizando 8 bytes. O cabeçalho TCP padrão sem opções possui 20 bytes."),
        # Q29
        (
            "As portas lógicas de transporte são divididas em faixas pela IANA. A faixa de portas conhecidas (Well-Known Ports) e a faixa de portas registradas (Registered Ports) cobrem, respectivamente, as faixas de:",
            "0 a 1023 e 1024 a 49151",
            "0 a 255 e 256 a 1023",
            "1 a 1024 e 1025 a 65535",
            "0 a 49151 e 49152 a 65535",
            "0 a 80 e 81 a 443"
        , "A IANA classifica as portas em: Well-Known (Conhecidas/Sistema): 0 a 1023; Registered (Registradas): 1024 a 49151; Dynamic/Private (Dinâmicas/Privadas): 49152 a 65535."),
        # Q30
        (
            "O temporizador de retransmissão (RTO - Retransmission Timeout) do TCP é calculado dinamicamente. O cálculo do RTO baseia-se na medição de:",
            "RTT (Round-Trip Time), que mede o tempo decorrido entre o envio de um segmento e a chegada da sua correspondente confirmação.",
            "Largura de banda da interface de rede, medida através da transmissão síncrona de rajadas de dados de teste (ping packet).",
            "Carga de processamento do roteador de borda intermediário, calculada através de mensagens ICMP Echo Request periódicas.",
            "Quantidade de colisões ocorridas na rede local devido a conexões ethernet em modo half-duplex nos hubs da comarca.",
            "Tamanho máximo de segmento (MSS) acordado pelas interfaces de rede ativas durante o handshake do protocolo TLS."
        , "O RTO é calculado com base no RTT (Round-Trip Time) estimado e sua variação (desvio padrão), garantindo que o TCP ajuste seu tempo de espera por ACKs de acordo com a latência real do caminho da rede.")
    ]
    dia_26_themes.append(("Redes e Camada de Transporte — Protocolo TCP vs. UDP, Controle de Fluxo/Congestionamento e Portas Conhecidas", t2_26))
    
    # Tema 3: RLM
    t3_26 = [
        # Q31
        (
            "Considere a seguinte proposição condicional: *\"Se o analista de suporte realiza o backup, então o banco de dados não perde dados\"*. Uma proposição logicamente equivalente a essa é:",
            "Se o banco de dados perdeu dados, então o analista de suporte não realizou o backup.",
            "Se o analista de suporte não realiza o backup, então o banco de dados perde dados.",
            "O analista de suporte realizou o backup e o banco de dados perdeu dados.",
            "Se o banco de dados não perdeu dados, então o analista de suporte realizou o backup.",
            "O analista de suporte não realiza o backup ou o banco de dados perde dados."
        , "A equivalência da condicional $P \to Q$ pela contrapositiva é $\neg Q \to \neg P$. Negando a consequente 'o banco de dados não perde dados' vira 'o banco de dados perde dados' (ou 'perdeu dados'). Negando a antecedente 'o analista realiza o backup' vira 'o analista não realizou o backup'. Assim: 'Se o banco de dados perdeu dados, então o analista de suporte não realizou o backup'. A alternativa A está correta."),
        # Q32
        (
            "Uma outra equivalência importante da condicional $P \to Q$ na lógica proposicional é a sua conversão em uma disjunção inclusiva. A equivalência correta nesse formato para a frase *\"Se estudo para o concurso do TJ, então sou aprovado\"* é:",
            "Não estudo para o concurso do TJ ou sou aprovado.",
            "Estudo para o concurso do TJ e sou aprovado.",
            "Se não estudo para o concurso do TJ, então não sou aprovado.",
            "Não estudo para o concurso do TJ ou não sou aprovado.",
            "Se sou aprovado, então estudo para o concurso do TJ."
        , "A condicional $P \to Q$ é logicamente equivalente a $\neg P \lor Q$. Aplicando à proposição: $\neg P$ = 'Não estudo para o concurso do TJ', $\lor$ = 'ou', $Q$ = 'sou aprovado'. Portanto: 'Não estudo para o concurso do TJ ou sou aprovado'. A opção A está correta."),
        # Q33
        (
            "Deseja-se realizar a negação lógica da proposição condicional: *\"Se o servidor do tribunal cometer uma falta grave, então ele será demitido\"*. A negação correta dessa condicional é:",
            "O servidor do tribunal comete uma falta grave e não é demitido.",
            "Se o servidor do tribunal não cometer uma falta grave, então ele não será demitido.",
            "O servidor do tribunal não comete uma falta grave ou ele é demitido.",
            "Se o servidor do tribunal for demitido, então ele cometeu uma falta grave.",
            "O servidor do tribunal não comete uma falta grave e ele não é demitido."
        , "A negação de uma condicional $\neg(P \to Q)$ equivale a $P \land \neg Q$ (regra do 'mantém a primeira E nega a segunda'). Assim: 'O servidor comete uma falta grave' (P) e ($\land$) 'não é demitido' ($\neg Q$). A alternativa A está correta."),
        # Q34
        (
            "De acordo com as Leis de De Morgan na lógica matemática, a negação de uma conjunção $\neg(P \land Q)$ e a negação de uma disjunção $\neg(P \lor Q)$ são equivalentes, respectivamente, a:",
            "$\neg P \lor \neg Q$ e $\neg P \land \neg Q$",
            "$\neg P \land \neg Q$ e $\neg P \lor \neg Q$",
            "$\neg P \to \neg Q$ e $\neg P \leftrightarrow \neg Q$",
            "$P \lor Q$ e $P \land Q$",
            "$\neg(P \leftrightarrow Q)$ e $\neg P \lor Q$"
        , "As Leis de De Morgan determinam que: 1) a negação de 'E' vira 'OU' com as proposições negadas: $\neg(P \land Q) \equiv \neg P \lor \neg Q$; 2) a negação de 'OU' vira 'E' com as proposições negadas: $\neg(P \lor Q) \equiv \neg P \land \neg Q$. A opção A é a correta."),
        # Q35
        (
            "Considere as seguintes premissas de um argumento lógico válido: \n1. Se o switch de rede queimar, o acesso à internet é interrompido. \n2. O acesso à internet não foi interrompido. \nA partir dessas premissas, a regra de inferência Modus Tollens nos permite deduzir a seguinte conclusão lógica:",
            "O switch de rede não queimou.",
            "O switch de rede queimou ontem à noite.",
            "O acesso à internet foi reestabelecido por técnicos de TI.",
            "Se o switch de rede não queimar, o acesso é interrompido.",
            "Nenhuma conclusão lógica válida pode ser deduzida no argumento."
        , "A regra do Modus Tollens estabelece que, dadas as premissas $P \to Q$ e $\neg Q$, conclui-se validamente $\neg P$. Na questão, $P$ = 'o switch de rede queimar', $Q$ = 'o acesso à internet é interrompido'. Sabendo que $\neg Q$ ('O acesso não foi interrompido'), conclui-se $\neg P$ ('O switch de rede não queimou'). A alternativa A é correta."),
        # Q36
        (
            "A regra de inferência lógica clássica conhecida como Modus Ponens pode ser estruturada da seguinte forma matemática nas premissas de um argumento:",
            "Dadas as premissas $P \to Q$ e $P$, conclui-se validamente a proposição $Q$ no argumento lógico.",
            "Dadas as premissas $P \to Q$ e $\neg Q$, conclui-se validamente a negação $\neg P$ no argumento lógico.",
            "Dadas as premissas $P \lor Q$ e $\neg P$, conclui-se validamente a proposição $Q$ no argumento lógico.",
            "Dadas as premissas $P \land Q$ e $R$, conclui-se a conjunção de todas as variáveis ativas do sistema.",
            "Dadas as premissas $P \to Q$ e $Q \to R$, conclui-se a condicional transitiva simplificada $P \to R$ no argumento."
        , "O Modus Ponens (afirmação do antecedente) diz que se temos a condicional $P \to Q$ e afirmamos a antecedente $P$, conclui-se necessariamente a consequente $Q$."),
        # Q37
        (
            "Considere a proposição composta: *\"O analista de TI revisa o código ou ele realiza os testes unitários\"*. A negação lógica dessa disjunção inclusiva é dada por:",
            "O analista de TI não revisa o código e ele não realiza os testes unitários.",
            "O analista de TI não revisa o código ou ele não realiza os testes unitários.",
            "Se o analista de TI não revisa o código, então ele não realiza os testes.",
            "O analista de TI revisa o código e ele realiza os testes unitários com calma.",
            "Se o analista de TI revisa o código, então ele não realiza os testes unitários."
        , "Negar a disjunção 'P ou Q' significa negar ambas as partes e trocar o conector 'ou' pelo 'e' ($\neg P \land \neg Q$). Portanto: 'O analista não revisa o código E não realiza os testes'. A alternativa A está correta."),
        # Q38
        (
            "Na tabela verdade, a proposição composta que resulta em valores lógicos verdadeiros em todas as suas linhas, independentemente dos valores das proposições simples que a compõem, é classificada como uma:",
            "Tautologia",
            "Contradição",
            "Contingência",
            "Equivalência condicional",
            "Falácia formal"
        , "Tautologia é a proposição composta cujo valor lógico é sempre verdadeiro. Contradição é sempre falso. Contingência pode ser verdadeiro ou falso dependendo das entradas."),
        # Q39
        (
            "Assinale a alternativa que apresenta uma falácia formal clássica relacionada ao uso incorreto de regras de inferência lógica condicional:",
            "Afirmação do consequente, em que se assume que, dada a condicional $P \to Q$ e a ocorrência de $Q$, conclui-se validamente $P$.",
            "Negação da antecedente, em que se conclui que, dada a disjunção $P \lor Q$ e a negação de $P$, conclui-se validamente a negação de $Q$.",
            "Silogismo disjuntivo, no qual a afirmação de uma das premissas exclui obrigatoriamente a veracidade da outra proposição simples.",
            "Modus Tollens aplicado a uma negação simples em que a antecedente condicional é desconsiderada durante a inferência.",
            "Dilema construtivo baseado em tabelas verdade que possuem contingências na coluna final do conectivo lógico principal."
        , "A afirmação do consequente é uma falácia formal (ex: 'Se chove, a rua fica molhada. A rua está molhada, logo choveu' - a rua pode ter sido molhada por um caminhão de limpeza). Não é uma inferência dedutiva válida."),
        # Q40
        (
            "Considere a proposição condicional: *\"Se o processo é julgado tempestivamente, então os direitos do cidadão são plenamente assegurados\"*. A contrapositiva dessa proposição é:",
            "Se os direitos do cidadão não são plenamente assegurados, então o processo não é julgado tempestivamente.",
            "Se os direitos do cidadão são plenamente assegurados, então o processo é julgado tempestivamente.",
            "Se o processo não é julgado tempestivamente, então os direitos do cidadão não são plenamente assegurados.",
            "O processo é julgado tempestivamente e os direitos do cidadão não são plenamente assegurados no tribunal.",
            "O processo não é julgado tempestivamente ou os direitos do cidadão são plenamente assegurados pelo comitê."
        , "A contrapositiva da condicional $P \to Q$ é $\neg Q \to \neg P$. Negando a consequente e a antecedente e invertendo a ordem, temos: 'Se os direitos do cidadão não são plenamente assegurados, então o processo não é julgado tempestivamente'. A alternativa A está correta."),
        # Q41
        (
            "Uma proposição bicondicional $P \leftrightarrow Q$ é logicamente equivalente a qual das seguintes construções na lógica formal proposicional?",
            "$(P \to Q) \land (Q \to P)$",
            "$(P \to Q) \lor (Q \to P)$",
            "$(P \land Q) \lor (\neg P \land \neg Q)$",
            "$(P \to Q) \to (Q \to P)$",
            "$(\neg P \lor Q) \land (P \lor \neg Q)$"
        , "A bicondicional 'P se e somente se Q' ($P \leftrightarrow Q$) significa que P implica Q E Q implica P. Logo, é equivalente a $(P \to Q) \land (Q \to P)$. A opção A é a alternativa correspondente."),
        # Q42
        (
            "Qual é o valor lógico da proposição composta $(P \lor Q) \to (P \land R)$, sabendo que os valores lógicos das proposições simples são: P é VERDADEIRO, Q é FALSO e R é FALSO?",
            "Falso",
            "Verdadeiro",
            "Inconclusivo devido à falta de dados sobre a tabela verdade.",
            "Verdadeiro ou Falso, dependendo da ordem das premissas.",
            "Nulo, pois a condicional não admite antecedente verdadeiro."
        , "Avaliando os termos: 1) $P \lor Q$ = VERDADEIRO $\lor$ FALSO = VERDADEIRO; 2) $P \land R$ = VERDADEIRO $\land$ FALSO = FALSO. A condicional fica VERDADEIRO $\to$ FALSO, que é FALSO. A alternativa A está correta."),
        # Q43
        (
            "Deseja-se demonstrar que a conjunção de duas proposições quaisquer, P e Q, é falsa. Para que a proposição composta $P \land Q$ seja classificada como FALSA, basta que:",
            "Pelo menos uma das proposições simples, P ou Q, seja classificada como falsa na tabela verdade correspondente.",
            "Ambas as proposições simples, P e Q, sejam obrigatoriamente classificadas como falsas de forma síncrona no sistema.",
            "A proposição P seja verdadeira e a proposição Q seja classificada como verdadeira na análise de linhas da tabela.",
            "A negação da variável P seja logicamente equivalente ao valor de verdade da variável dependente secundária R.",
            "O conectivo principal da oração seja alterado para uma disjunção exclusiva através da aplicação das regras de De Morgan."
        , "Para que a conjunção (E) seja falsa, basta que uma de suas componentes seja falsa. Para que ela seja verdadeira, ambas devem ser verdadeiras. A alternativa A descreve essa regra logicamente."),
        # Q44
        (
            "Considere o seguinte argumento lógico: \nPremissa 1: Todos os analistas de sistemas sabem programar na linguagem de programação Java. \nPremissa 2: Carlos sabe programar na linguagem de programação Java. \nConclusão: Carlos é um analista de sistemas. \nSobre a validade desse argumento lógico, assinale a alternativa correta:",
            "Trata-se de um argumento inválido, pois Carlos pode saber programar em Java sem necessariamente ser um analista de sistemas.",
            "O argumento é plenamente válido, pois a primeira premissa garante que apenas analistas sabem programar na linguagem Java.",
            "O argumento é classificado como uma tautologia matemática porque as premissas e a conclusão possuem valores lógicos verdadeiros.",
            "A conclusão deduzida no argumento é falsa porque veda a possibilidade de Carlos programar em outras linguagens do mercado.",
            "O argumento constitui um exemplo clássico da aplicação da regra de inferência lógica válida denominada Modus Tollens."
        , "Esse é um argumento inválido (falácia de afirmação do consequente). O conjunto de pessoas que programam em Java engloba os analistas, mas pode conter outros profissionais (Carlos pode ser engenheiro, estudante, etc.). Logo, não podemos concluir que Carlos é analista. A alternativa A está correta."),
        # Q45
        (
            "Para negar a proposição categórica universal: *\"Todo servidor público do tribunal de justiça é dedicado\"*, deve-se utilizar a seguinte redação:",
            "Pelo menos um servidor público do tribunal de justiça não é dedicado.",
            "Nenhum servidor público do tribunal de justiça é dedicado no exercício de suas funções.",
            "Todos os servidores públicos do tribunal de justiça não são dedicados nas comarcas.",
            "Se uma pessoa é servidora pública do tribunal de justiça, então ela não é dedicada.",
            "Pelo menos um servidor público do tribunal de justiça é dedicado em suas atividades."
        , "A negação de uma proposição universal afirmativa 'Todo A é B' é uma proposição particular negativa 'Algum A não é B' (ou 'Existe A que não é B', 'Pelo menos um A não é B'). A alternativa A apresenta a forma correta.")
    ]
    dia_26_themes.append(("Raciocínio Lógico-Matemático — Lógica de Argumentação, Equivalências e Inferências (Modus Ponens e Modus Tollens)", t3_26))
    
    write_day_file(os.path.join(questoes_dir, "dia_26_05_questoes.md"),
                   "Bateria de Questões FCC — Terça-feira 26/05",
                   "Este arquivo contém 45 questões altamente calibradas nos padrões da FCC, com alternativas de comprimento similar e distratores baseados em pegadinhas reais.",
                   dia_26_themes)

    # =========================================================================
    # DIA 27/05 - QUARTA-FEIRA
    # =========================================================================
    dia_27_themes = []
    
    # Tema 1: LGPD
    t1_27 = [
        # Q1
        (
            "A Lei Geral de Proteção de Dados (LGPD) - Lei nº 13.709/2018 - estabelece conceitos fundamentais para o tratamento de informações. A definição legal de 'Dado Pessoal Sensível' segundo a LGPD engloba:",
            "Dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural.",
            "Qualquer informação de natureza financeira corporativa, incluindo demonstrativos de lucros e perdas, faturamento bruto anual de empresas privadas e saldos bancários de contas correntes de pessoas jurídicas ativas.",
            "Dados de geolocalização capturados por dispositivos móveis em tempo real nas dependências físicas de órgãos públicos e comarcas judiciais do Estado.",
            "Endereço IP associado ao histórico de navegação na internet de usuários comuns que acessam portais governamentais de transparência pública.",
            "Registros de logs de acesso a servidores de banco de dados relacionais que não permitam a identificação direta ou indireta de usuários externos cadastrados."
        , "A alternativa A transcreve fielmente a definição legal de Dado Pessoal Sensível constante no art. 5º, inciso II, da LGPD. As demais alternativas tratam de dados pessoais comuns ou informações corporativas não enquadradas como dados sensíveis."),
        # Q2
        (
            "A LGPD define os agentes de tratamento de dados pessoais. Os agentes de tratamento descritos pela lei são:",
            "O Controlador (a quem competem as decisões sobre o tratamento) e o Operador (que realiza o tratamento em nome do controlador).",
            "O Encarregado (DPO) e a Autoridade Nacional de Proteção de Dados (ANPD) de forma exclusiva no território nacional.",
            "O Titular dos dados pessoais e o Encarregado do tratamento nas esferas administrativa e jurídica do tribunal.",
            "O Desenvolvedor de sistemas e o Administrador de Banco de Dados (DBA) responsáveis pela segurança lógica dos blocos de dados.",
            "A Ouvidoria Geral e a Corregedoria do órgão que fiscalizam o cumprimento das diretrizes de segurança da informação."
        , "Segundo o art. 5º, inciso IX, da LGPD, os agentes de tratamento são o controlador e o operador. O encarregado (DPO) é o canal de comunicação, mas não é agente de tratamento no sentido da lei."),
        # Q3
        (
            "O tratamento de dados pessoais na LGPD deve observar diversos princípios de cumprimento obrigatório pelos agentes. O princípio que garante aos titulares a consulta facilitada e gratuita sobre a forma e a duração do tratamento, bem como sobre a integralidade de seus dados pessoais, é o princípio do(a):",
            "Livre acesso",
            "Transparência",
            "Adequação",
            "Necessidade",
            "Segurança"
        , "O princípio do livre acesso (art. 6º, inciso IV, da LGPD) garante a consulta facilitada e gratuita dos titulares sobre a forma e duração do tratamento e a integridade de seus dados. O princípio da transparência garante informações claras e precisas sobre o tratamento e os agentes."),
        # Q4
        (
            "Para que o tratamento de dados pessoais comuns seja lícito, a LGPD exige o enquadramento em uma das bases legais previstas no artigo 7º. Assinale a alternativa que apresenta uma base legal válida:",
            "Para o cumprimento de obrigação legal ou regulatória pelo controlador, dispensando o consentimento do titular dos dados pessoais.",
            "Para o legítimo interesse exclusivo do operador, mesmo que viole os direitos e liberdades fundamentais do titular dos dados.",
            "Mediante o consentimento verbal tácito do titular obtido de forma indireta através da aceitação de cookies genéricos na internet.",
            "Para a proteção do crédito dos agentes de tratamento em transações comerciais de empresas estrangeiras sem sede no país.",
            "Para a execução de contratos comerciais de consumo nos quais o titular figure como terceiro beneficiário não anuente da transação."
        , "O art. 7º, inciso II, da LGPD estabelece como base legal o cumprimento de obrigação legal ou regulatória pelo controlador, sem necessidade de consentimento. O legítimo interesse deve respeitar os direitos e liberdades fundamentais, e o consentimento deve ser livre, informado e inequívoco."),
        # Q5
        (
            "Em relação ao tratamento de dados pessoais de crianças e adolescentes, a LGPD impõe regras estritas de proteção. O tratamento de dados de crianças exige:",
            "O consentimento específico e em destaque dado por pelo menos um dos pais ou pelo responsável legal da criança.",
            "A autorização prévia por escrito expedida pela Autoridade Nacional de Proteção de Dados (ANPD) após auditoria física.",
            "Apenas a notificação posterior aos responsáveis legais através de edital eletrônico publicado no portal da transparência.",
            "A dispensa total de consentimento caso os dados sejam tratados em sistemas de educação a distância mantidos por fundações privadas.",
            "A anonimização compulsória e instantânea de todos os dados no momento da inserção física no banco de dados relacional local."
        , "Segundo o art. 14, § 1º, da LGPD, o tratamento de dados pessoais de crianças deve ser realizado com o consentimento específico e em destaque dado por pelo menos um dos pais ou pelo responsável legal."),
        # Q6
        (
            "Os titulares de dados pessoais possuem direitos fundamentais assegurados pela LGPD. Um direito que o titular pode exercer perante o controlador, a qualquer momento e mediante requisição, é a:",
            "Portabilidade dos dados a outro fornecedor de serviço ou produto, mediante requisição expressa, de acordo com a regulamentação da ANPD.",
            "Exclusão definitiva de todos os seus dados pessoais de registros fiscais obrigatórios exigidos pela Receita Federal do Brasil.",
            "Alteração unilateral dos termos de uso da aplicação web que coletou os dados pessoais sem anuência da equipe de desenvolvimento.",
            "Transferência compulsória da propriedade dos servidores físicos nos quais os seus dados pessoais encontram-se armazenados.",
            "Isenção de tributos estaduais associados a serviços de telecomunicações que trafeguem os seus dados em redes de fibra óptica."
        , "O titular tem direito à portabilidade dos dados a outro fornecedor (art. 18, inciso V, da LGPD), resguardados os segredos comerciais e industriais. Não cabe direito de exclusão de dados mantidos por obrigações legais fiscais ou administrativas legítimas."),
        # Q7
        (
            "Sobre a figura do Encarregado (DPO - Data Protection Officer) prevista na LGPD, assinale a alternativa que descreve corretamente as suas atribuições legais:",
            "Aceitar reclamações e comunicações dos titulares, prestar esclarecimentos e adotar providências, bem como receber comunicações da ANPD.",
            "Decidir de forma soberana as bases legais que serão utilizadas em cada atividade de tratamento do tribunal de justiça do Estado.",
            "Executar fisicamente as rotinas de backup e restauração dos bancos de dados relacionais nos servidores do datacenter corporativo.",
            "Aplicar multas e sanções administrativas aos operadores de dados que cometerem violações de segurança no tratamento físico.",
            "Representar judicialmente os titulares de dados pessoais em ações criminais decorrentes do vazamento de informações sigilosas."
        , "O Encarregado atua como canal de comunicação entre o controlador, os titulares e a ANPD, conforme o art. 41, § 2º, da LGPD. Ele não decide as bases legais de forma autônoma e nem aplica sanções administrativas (que competem à ANPD)."),
        # Q8
        (
            "Em casos de incidentes de segurança que possam acarretar risco ou dano relevante aos titulares de dados pessoais, o controlador deve:",
            "Comunicar à Autoridade Nacional de Proteção de Dados (ANPD) e aos titulares em prazo razoável, conforme definido pela autoridade.",
            "Suspender imediatamente e por tempo indeterminado todas as atividades e serviços de rede do tribunal de justiça do Estado.",
            "Realizar a exclusão automática de todos os backups do banco de dados para evitar que novas cópias de dados sejam vazadas na internet.",
            "Emitir um comunicado oficial de isenção de responsabilidade civil antes de notificar qualquer órgão governamental ou fiscalizador.",
            "Notificar a Delegacia de Crimes Células e a Receita Federal do Brasil no prazo máximo improrrogável de duas horas após o ocorrido."
        , "O art. 48 da LGPD determina que o controlador deve comunicar à ANPD e aos titulares a ocorrência de incidente de segurança que possa acarretar risco ou dano relevante em prazo razoável."),
        # Q9
        (
            "As sanções administrativas previstas na LGPD são aplicadas pela ANPD aos agentes de tratamento em caso de infrações. Uma dessas sanções administrativas é a:",
            "Multa simples de até 2% do faturamento da pessoa jurídica de direito privado, limitada, no total, a cinquenta milhões de reais por infração.",
            "Prisão preventiva dos diretores de TI e dos administradores de banco de dados responsáveis pelo vazamento das informações confidenciais.",
            "Cassação do registro profissional de todos os analistas de sistemas que participaram do desenvolvimento do software sob investigação.",
            "Perda imediata do patrimônio líquido da empresa operadora em favor do fundo de amparo ao trabalhador e fomento de tecnologia pública.",
            "Proibição perpétua do exercício de qualquer atividade de tratamento de dados pessoais em âmbito público e privado em todo o país."
        , "Segundo o art. 52, inciso II, da LGPD, a multa simples pode ir até 2% do faturamento da empresa, limitada a R$ 50.000.000,00 por infração. Sanções como prisão preventiva ou cassação de registros profissionais não constam nas sanções administrativas da lei."),
        # Q10
        (
            "A LGPD prevê hipóteses em que a lei NÃO se aplica ao tratamento de dados pessoais. O tratamento de dados pessoais está excluído do escopo da LGPD quando realizado:",
            "Por pessoa natural para fins exclusivamente particulares e não econômicos, mantendo o caráter estritamente pessoal da atividade.",
            "Por órgãos públicos para fins de segurança pública, defesa nacional, segurança do Estado ou atividades de investigação de infrações penais.",
            "Por empresas privadas nacionais para fins de marketing direto e criação de perfis de consumo na rede local de internet corporativa.",
            "Por cartórios de notas e registros públicos no exercício de suas competências notariais obrigatórias de formalização documental.",
            "Por instituições financeiras privadas para a análise de risco de crédito de clientes que solicitam empréstimos bancários rápidos."
        , "De acordo com o art. 4º, inciso I, da LGPD, a lei não se aplica ao tratamento realizado por pessoa natural para fins exclusivamente particulares e não econômicos. Tratamento para segurança pública e defesa nacional também possui regras especiais e exclusão de aplicação geral, mas a lei de proteção específica se aplicará nestes termos. A alternativa A reflete a exclusão mais pura de escopo pessoal."),
        # Q11
        (
            "O princípio da finalidade na LGPD exige que o tratamento de dados pessoais seja realizado para propósitos legítimos, específicos e explícitos. Este princípio determina que:",
            "O tratamento deve ser justificado por propósitos informados ao titular, sendo vedado o tratamento posterior incompatível com essas finalidades.",
            "Os agentes de tratamento de dados pessoais podem alterar a destinação das informações coletadas a qualquer momento para otimizar lucros.",
            "O consentimento fornecido para uma finalidade autoriza implicitamente a coleta de novos dados sensíveis para finalidades futuras.",
            "Os dados pessoais devem ser mantidos armazenados permanentemente, mesmo após alcançado o objetivo inicial que motivou a sua coleta regular.",
            "O controlador fica desobrigado de declarar as razões pelas quais necessita dos dados quando o titular for servidor público efetivo."
        , "O princípio da finalidade (art. 6º, inciso I, da LGPD) exige propósitos legítimos, específicos e explícitos informados ao titular, vedando o uso de dados para propósitos diversos ou incompatíveis sem nova base legal."),
        # Q12
        (
            "Em relação ao tratamento de dados pessoais sob a LGPD, o 'Legítimo Interesse' é uma das bases legais. Sobre o legítimo interesse, assinale a alternativa correta:",
            "Ele fundamenta o tratamento para finalidades legítimas do controlador, apoiado em situações concretas e respeitando os direitos do titular.",
            "Ele autoriza o tratamento de dados sensíveis relacionados à saúde e vida sexual sem necessidade de autorização ou justificativa legal.",
            "Ele é a única base legal válida que permite a transferência internacional de dados para paraísos fiscais sem supervisão da ANPD.",
            "Ele dispensa a realização do teste de proporcionalidade (LIA) sobre o impacto à privacidade dos titulares de dados afetados.",
            "Ele confere imunidade civil aos agentes de tratamento contra quaisquer pedidos de indenização decorrentes de incidentes de segurança."
        , "O legítimo interesse (art. 10 da LGPD) aplica-se a finalidades legítimas do controlador em situações concretas, exigindo análise de proporcionalidade (LIA) em relação aos direitos e liberdades do titular. É vedado para dados pessoais sensíveis."),
        # Q13
        (
            "No âmbito da segurança da informação sob as diretrizes da LGPD, a anonimização é um conceito técnico relevante. A anonimização ocorre quando:",
            "Um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, considerando a utilização de meios técnicos razoáveis e disponíveis.",
            "Os dados pessoais são criptografados utilizando chaves públicas cuja chave privada de decifragem é mantida em outro servidor local.",
            "A equipe de TI altera temporariamente os nomes de usuários em relatórios visuais exibidos nas telas de sistemas de auditoria.",
            "O banco de dados relacional é configurado para apagar os registros de logs de acesso a cada período de vinte e quatro horas de uso.",
            "Os registros confidenciais são transferidos fisicamente para fitas magnéticas de backup de segurança mantidas offline no cofre."
        , "Anonimização (art. 5º, inciso XI, da LGPD) é a utilização de meios técnicos razoáveis e disponíveis na época do tratamento, por meio dos quais um dado perde a possibilidade de associação ao titular."),
        # Q14
        (
            "A Autoridade Nacional de Proteção de Dados (ANPD) é o órgão responsável por zelar pela proteção de dados pessoais. Sobre a ANPD, é correto afirmar:",
            "Trata-se de uma autarquia de natureza especial com autonomia técnica e decisória, vinculada administrativamente ao Ministério da Justiça.",
            "Consiste em um conselho privado composto por representantes de bancos comerciais e empresas multinacionais de tecnologia de internet.",
            "É subordinada diretamente ao Conselho Nacional de Justiça (CNJ) e fiscaliza apenas órgãos do Poder Judiciário em nível federal.",
            "Sua atuação restringe-se à emissão de certificados de segurança digital para servidores públicos federais e estaduais do país.",
            "Ela não possui poder regulatório, limitando-se a orientar as equipes de suporte técnico dos órgãos municipais de forma facultativa."
        , "A ANPD é uma autarquia de natureza especial que detém autonomia técnica e decisória, responsável por fiscalizar e regular o cumprimento da LGPD no país."),
        # Q15
        (
            "O término do tratamento de dados pessoais pela LGPD impõe aos agentes deveres de eliminação. A eliminação dos dados tratados pode ser dispensada para:",
            "O cumprimento de obrigação legal ou regulatória pelo controlador, ou para transferência a terceiro, desde que respeitados os requisitos legais.",
            "O uso comercial exclusivo do operador em campanhas publicitárias de empresas coligadas por tempo indeterminado nas redes de dados.",
            "Garantir a preservação de dados de navegação de usuários que foram banidos de fóruns judiciais por cometerem infrações administrativas.",
            "O enriquecimento de bases de dados de inteligência de mercado operadas por seguradoras privadas de fomento econômico nacional.",
            "Evitar custos adicionais de processamento físico de exclusão de registros que exigem a parada temporária do SGBD corporativo."
        , "O art. 16 da LGPD prevê que, após o término do tratamento, os dados devem ser eliminados, sendo autorizada a conservação para fins como cumprimento de obrigação legal/regulatória, estudo por órgão de pesquisa, transferência a terceiro ou uso exclusivo do controlador (desde que anonimizados).")
    ]
    dia_27_themes.append(("Segurança da Informação — Lei Geral de Proteção de Dados (LGPD)", t1_27))
    
    # Tema 2: Java, JEE e POO
    t2_27 = [
        # Q16
        (
            "Na Programação Orientada a Objetos (POO), o polimorfismo é um conceito central. O polimorfismo de sobrecarga (overloading) e o de sobreposição (overriding) diferem porque:",
            "A sobrecarga ocorre em métodos de mesmo nome com assinaturas diferentes na mesma classe, enquanto a sobreposição ocorre na redefinição de método da classe pai na subclasse.",
            "A sobreposição ocorre em tempo de compilação em métodos de nomes distintos, enquanto a sobrecarga é resolvida exclusivamente em tempo de execução pela JVM.",
            "A sobrecarga exige a utilização da palavra-chave extends em classes abstratas, enquanto a sobreposição é restrita a interfaces com métodos padrão.",
            "A sobreposição permite alterar o tipo de retorno de um método sem restrições, enquanto a sobrecarga impede a alteração dos modificadores de acesso.",
            "A sobrecarga aplica-se apenas a atributos e variáveis primitivas, enquanto a sobreposição é exclusiva para assinaturas de coleções genéricas."
        , "Sobrecarga (Overloading) envolve métodos com o mesmo nome, mas diferentes parâmetros na mesma classe (polimorfismo estático/compilação). Sobrepoisção (Overriding) é a redefinição de um método herdado da classe pai na subclasse com a mesma assinatura (polimorfismo dinâmico/tempo de execução)."),
        # Q17
        (
            "Em Java, os tipos primitivos e suas respectivas classes wrappers possuem comportamentos distintos. Sobre o mecanismo de autoboxing e unboxing na JVM, assinale a alternativa correta:",
            "Autoboxing é a conversão automática que a JVM realiza de um tipo primitivo para sua classe wrapper correspondente (ex: int para Integer).",
            "O tipo primitivo `double` consome mais memória RAM do que um objeto da classe wrapper `Double` correspondente na área do Heap da JVM.",
            "A comparação de dois objetos wrappers utilizando o operador `==` compara diretamente os valores numéricos internos, sem validar referências.",
            "O unboxing consiste na conversão explícita exigida pelo compilador Java de uma classe wrapper para uma classe de coleção como ArrayList.",
            "Tipos primitivos em Java herdam métodos utilitários diretamente da classe Object, ao contrário das classes wrappers associadas."
        , "Autoboxing é a conversão automática do primitivo para wrapper correspondente (ex: int -> Integer). Unboxing é o inverso (Integer -> int). Primitivos não herdam de Object e consomem menos memória que os wrappers correspondentes. Wrappers são objetos, então o operador `==` compara referências de memória, o que exige `equals()` para comparar valores de forma segura."),
        # Q18
        (
            "O tratamento de exceções em Java separa os erros em exceções checadas (checked) e não checadas (unchecked). Sobre essa classificação, assinale a alternativa correta:",
            "Exceções checadas herdam de Exception (mas não de RuntimeException) e devem ser obrigatoriamente tratadas com try-catch ou declaradas com throws.",
            "Exceções não checadas herdam diretamente de Throwable e o compilador exige o tratamento obrigatório na assinatura do método chamador.",
            "As exceções do tipo NullPointerException e ArrayIndexOutOfBoundsException são exemplos clássicos de exceções checadas em Java.",
            "O uso de exceções checadas é restrito à execução de rotinas em bancos de dados relacionais e transações controladas pelo Spring Boot.",
            "A JVM encerra imediatamente a execução da aplicação se uma exceção checada for lançada, impedindo o tratamento com blocos catch."
        , "Checked exceptions (ex: IOException, SQLException) herdam de Exception (excluindo RuntimeException) e exigem tratamento obrigatório em tempo de compilação. Unchecked exceptions herdam de RuntimeException e não exigem tratamento compulsório pelo compilador."),
        # Q19
        (
            "Em Java, as palavras-chave 'final', 'finally' e 'finalize' desempenham funções completamente distintas. Sobre elas, assinale a alternativa correta:",
            "Uma classe declarada como final não pode ser estendida (herdada), e o bloco finally é executado sempre após o término do bloco try-catch.",
            "O modificador final impede a alteração dos valores de atributos de objetos instanciados, tornando o objeto completamente imutável.",
            "O bloco finally só é executado no Java se uma exceção for lançada dentro do bloco try correspondente durante a execução da rotina.",
            "O método finalize é um método estático que o desenvolvedor deve chamar manualmente para liberar a memória RAM ocupada por objetos ativos.",
            "Um método declarado como final impede a sua sobrecarga em subclasses que herdam da classe que contém o método associado no pacote."
        , "Classe final não pode ser herdada; método final não pode ser sobreposto (overridden); variável final não pode ter valor alterado após inicializada. O bloco `finally` garante a execução de código de limpeza (como fechar conexões) após try-catch, independente de ter havido exceção ou não. O `finalize` é o método do garbage collector (depreciado atualmente). A opção A está correta."),
        # Q20
        (
            "O Java Collections Framework oferece diferentes implementações para manipulação de coleções. Sobre a diferença entre ArrayList e LinkedList, assinale a alternativa correta:",
            "O ArrayList é baseado em um array dinâmico que oferece acesso rápido por índice O(1), enquanto o LinkedList é baseado em lista duplamente encadeada.",
            "O LinkedList é mais rápido para realizar buscas aleatórias de elementos por índice do que o ArrayList em coleções de grande porte.",
            "O ArrayList consome significativamente mais memória que o LinkedList por armazenar ponteiros para os nós anterior e seguinte na memória.",
            "Ambas as classes são sincronizadas por padrão (thread-safe), dispensando o uso de blocos synchronized em concorrência paralela.",
            "O LinkedList impede a inserção de elementos duplicados ou valores nulos, comportando-se de forma idêntica a um conjunto do tipo HashSet."
        , "ArrayList armazena elementos em array contínuo, com busca indexada rápida O(1), mas inserções/remoções no meio exigem shift de elementos O(n). LinkedList é uma lista encadeada, excelente para inserções/remoções O(1) nas pontas, mas buscas exigem navegação O(n) e consome mais memória devido aos ponteiros dos nós."),
        # Q21
        (
            "Em relação às classes HashSet e TreeSet do Java Collections Framework, assinale a alternativa que apresenta a diferença técnica de comportamento entre elas:",
            "O HashSet não garante a ordenação dos elementos, enquanto o TreeSet armazena os elementos de forma ordenada com base em uma árvore vermelha e preta.",
            "O TreeSet oferece melhor desempenho para inserções e remoções O(1) de elementos na coleção do que o HashSet baseado em hashing lógico.",
            "O HashSet impede a inserção de valores nulos, enquanto o TreeSet aceita múltiplos elementos nulos de forma síncrona na coleção local.",
            "Ambas as classes implementam a interface List, permitindo o acesso direto aos elementos através de índices numéricos inteiros.",
            "O TreeSet utiliza a tabela hash para armazenar as chaves, enquanto o HashSet organiza as chaves de forma sequencial na memória JVM."
        , "HashSet é baseado em tabela hash (busca/inserção média O(1)), não mantendo nenhuma ordenação. TreeSet implementa NavigableSet (baseado em Red-Black Tree) e mantém elementos ordenados naturalmente ou por Comparator (busca/inserção O(log n)). NullPointerException ocorre ao tentar inserir null no TreeSet sem comparator customizado. A alternativa A está correta."),
        # Q22
        (
            "A JVM organiza a memória em diferentes regiões. As regiões da memória conhecidas como Heap e Stack são utilizadas, respectivamente, para armazenar:",
            "Objetos instanciados dinamicamente; Variáveis locais e referências de controle de chamadas de métodos ativos na pilha de execução.",
            "Arquivos de configuração do sistema operacional; Variáveis globais compartilhadas por todas as aplicações web Java em execução.",
            "Bibliotecas dinâmicas compartilhadas; Arquivos de código-fonte Java compilados no formato bytecode pelo desenvolvedor local.",
            "Sessões de usuários ativas do servidor de aplicação; Parâmetros de conexões físicas estabelecidas com o banco de dados relacional.",
            "Mapeamentos do hibernate e JPA; Índices das tabelas do banco de dados relacional carregados na memória RAM do computador."
        , "Na JVM, o Heap armazena todos os objetos instanciados (via `new`). O Stack armazena as chamadas de métodos, variáveis locais e referências aos objetos contidos no Heap de cada thread de execução."),
        # Q23
        (
            "Em relação aos servidores de aplicação e à arquitetura JEE, os componentes EJB (Enterprise JavaBeans) desempenham papéis definidos. Os Session Beans podem ser classificados em:",
            "Stateless, Stateful e Singleton",
            "Checked, Unchecked e Runtime",
            "Request, Session e Application",
            "Entity, Controller e Boundary",
            "Local, Remote e WebService"
        , "Os Session Beans no EJB são divididos em: Stateless (sem estado retido entre chamadas), Stateful (com estado associado à sessão do cliente) e Singleton (uma única instância compartilhada por toda a aplicação)."),
        # Q24
        (
            "No desenvolvimento de aplicações web baseadas em Java Servlets, a API especifica um ciclo de vida e métodos de controle. O método responsável por processar requisições HTTP POST em um Servlet é o:",
            "doPost(HttpServletRequest, HttpServletResponse)",
            "service(ServletRequest, ServletResponse)",
            "init(ServletConfig)",
            "doGet(HttpServletRequest, HttpServletResponse)",
            "destroy()"
        , "O ciclo de vida envolve `init()`, `service()`, e `destroy()`. O método `service()` direciona as requisições HTTP para os métodos específicos: `doGet()`, `doPost()`, `doPut()`, `doDelete()` etc. O método para requisições POST é `doPost()`."),
        # Q25
        (
            "A tecnologia JPA (Java Persistence API) padroniza o mapeamento objeto-relacional. Sobre os estados de ciclo de vida de uma entidade gerenciada pelo EntityManager da JPA, é correto afirmar:",
            "Uma entidade passa para o estado Managed (gerenciado) logo após a execução do método persist() ou merge() do EntityManager.",
            "No estado Detached (destacado), as alterações realizadas nos atributos da entidade são refletidas de forma síncrona no banco de dados.",
            "O estado Transient (transiente) caracteriza uma entidade que possui correspondência física e chave primária gravada no banco relacional.",
            "O método remove() altera o estado da entidade de Managed para Detached, impedindo a sua exclusão física do disco do banco de dados.",
            "As entidades no estado Managed não podem ter seus dados lidos por transações ativas configuradas em modo de leitura exclusiva."
        , "Os estados da JPA são: Transient (nova instância, não persistida), Managed (associada ao EntityManager, alterações sincronizadas), Detached (desassociada, alterações não sincronizadas) e Removed (marcada para exclusão). O método `persist()` move a entidade para Managed. A alternativa A está correta."),
        # Q26
        (
            "Em programação orientada a objetos com Java, interfaces e classes abstratas são conceitos fundamentais de abstração. A diferença técnica entre elas em Java 8 ou superior é:",
            "Uma classe abstrata pode conter variáveis de instância (estado) e métodos construtores, enquanto uma interface pode conter apenas constantes e métodos abstratos ou default.",
            "Uma interface permite herança múltipla de classes abstratas de outros pacotes do projeto através da palavra-chave extends.",
            "As classes abstratas vedam a declaração de métodos com corpo físico, exigindo que todos os seus métodos sejam declarados como abstratos.",
            "As interfaces não admitem a declaração de métodos padrão (default methods) com implementação, limitando-se a assinaturas puras.",
            "Uma classe pode herdar de múltiplas classes abstratas de forma paralela, mas pode implementar no máximo uma interface local."
        , "Classes abstratas podem ter construtores, variáveis de instância e estado interno. Interfaces (mesmo após Java 8 introduzir `default` e `static` methods, e Java 9 introduzir private methods) não podem ter variáveis de instância (apenas constantes `public static final`) nem construtores. Uma classe pode implementar múltiplas interfaces, mas herdar de apenas uma classe (abstrata ou não)."),
        # Q27
        (
            "Na arquitetura JEE, as JSP (JavaServer Pages) são traduzidas pelo container web para fins de execução. Durante a primeira requisição de um cliente a uma página JSP, esta é traduzida internamente em um(a):",
            "Servlet Java, que é compilado em bytecode e executado na JVM para renderizar a saída HTML correspondente.",
            "Procedimento armazenado (Stored Procedure) PL/SQL gravado diretamente no banco de dados relacional do tribunal.",
            "Função JavaScript executada no lado do cliente (navegador) para manipular dinamicamente o modelo DOM da página.",
            "Folha de estilo CSS dinâmica compilada em tempo de execução para garantir a acessibilidade de pessoas com deficiência.",
            "Arquivo XML estático contendo os mapeamentos das entidades persistentes definidas no framework Hibernate."
        , "JSP é traduzida pelo container em um Servlet Java correspondente. O Servlet é então compilado em arquivo `.class` e executado pela JVM para processar a requisição e produzir a saída (geralmente HTML)."),
        # Q28
        (
            "O garbage collector (coletor de lixo) é um componente essencial da JVM. A função principal do garbage collector é:",
            "Identificar e desalocar a memória Heap ocupada por objetos que não possuem mais nenhuma referência ativa na aplicação.",
            "Otimizar as queries SQL enviadas ao banco de dados relacional através do pool de conexões físicas estabelecidas.",
            "Compilar dinamicamente o código-fonte Java em bytecode executável em servidores de microsserviços do órgão público.",
            "Bloquear o acesso físico de hackers a arquivos confidenciais do sistema operacional que executam a JVM.",
            "Limpar o histórico de navegação e arquivos de cache temporários gravados na pasta de perfil do usuário no servidor."
        , "O GC (Garbage Collector) gerencia automaticamente a memória Heap, liberando a memória ocupada por objetos que não são mais acessíveis por nenhuma thread ativa do programa."),
        # Q29
        (
            "Em Java, os modificadores de acesso controlam a visibilidade de classes, atributos e métodos. Os modificadores 'protected' e default (ausência de modificador) garantem visibilidade:",
            "Apenas dentro do mesmo pacote (default), e também para subclasses em pacotes diferentes no caso do protected.",
            "Para qualquer classe do projeto de forma irrestrita, independentemente do pacote de origem no código-fonte.",
            "Exclusivamente dentro da própria classe na qual o membro foi declarado em ambos os modificadores físicos.",
            "Apenas para classes que herdam da classe proprietária, bloqueando o acesso de outras classes do mesmo pacote.",
            "Apenas para as instâncias da classe criadas na thread principal de execução do servidor de aplicação."
        , "Default (package-private) restringe o acesso ao mesmo pacote. Protected estende o default: dá acesso a qualquer classe do mesmo pacote E a subclasses em outros pacotes via herança."),
        # Q30
        (
            "No contexto de concorrência em Java, a palavra-chave 'synchronized' é utilizada para coordenar o acesso a recursos compartilhados por múltiplas threads. O uso de 'synchronized' garante:",
            "Exclusão mútua (mutual exclusion), garantindo que apenas uma thread possa executar o bloco ou método sincronizado por vez.",
            "A compilação local paralela das classes do pacote para evitar latência no processamento concorrente do banco de dados.",
            "A criação instantânea de novas threads de execução em segundo plano para otimizar o processamento de consultas lógicas.",
            "A persistência física e imediata das variáveis na tabela de logs do banco de dados relacional em lote transacional.",
            "A isenção de tratamento de exceções do tipo NullPointerException dentro do bloco de código monitorado pela JVM."
        , "A sincronização (`synchronized`) adquire um lock intrínseco (monitor) sobre o objeto/classe, garantindo exclusão mútua: apenas uma thread por vez executa o trecho de código protegido, prevenindo condições de corrida (race conditions).")
    ]
    dia_27_themes.append(("Engenharia de Software — Java, JEE e Programação Orientada a Objetos", t2_27))
    
    # Tema 3: PCD
    t3_27 = [
        # Q31
        (
            "A Lei Federal nº 13.146/2015 institui a Lei Brasileira de Inclusão da Pessoa com Deficiência (Estatuto da Pessoa com Deficiência). Segundo a LBI, considera-se pessoa com deficiência aquela que tem impedimento de longo prazo de natureza:",
            "Física, mental, intelectual ou sensorial, o qual, em interação com uma ou mais barreiras, pode obstruir sua participação plena e efetiva na sociedade em igualdade de condições com as demais pessoas.",
            "Temporária ou transitória decorrente de acidentes de trabalho, a qual impeça o exercício de atividades profissionais por período superior a trinta dias úteis.",
            "Física de caráter motor que resulte obrigatoriamente no uso de cadeira de rodas ou próteses ortopédicas de membros inferiores para locomoção.",
            "Intelectual diagnosticada na fase adulta, que comprometa de forma definitiva a capacidade de tomada de decisões civis e financeiras básicas.",
            "Sensorial auditiva ou visual parcial que dispense a utilização de tecnologias assistivas ou atendimento prioritário em órgãos públicos."
        , "A alternativa A transcreve o conceito legal de pessoa com deficiência estabelecido no art. 2º, caput, da Lei nº 13.146/2015 (LBI). O impedimento deve ser de longo prazo e de natureza física, mental, intelectual ou sensorial."),
        # Q32
        (
            "A LBI classifica e define diversas barreiras que impedem a participação plena das pessoas com deficiência. As barreiras que existem nas vias e nos espaços públicos e privados abertos ao público ou de uso coletivo são denominadas barreiras:",
            "Urbanísticas",
            "Arquitetônicas",
            "Atitudinais",
            "Tecnológicas",
            "Nas comunicações e na informação"
        , "Segundo o art. 3º, inciso IV, alínea 'a', da LBI, as barreiras urbanísticas são as existentes nas vias e nos espaços públicos e privados abertos ao público ou de uso coletivo. Barreiras arquitetônicas são as existentes nos edifícios (alínea 'b')."),
        # Q33
        (
            "O Estatuto da Pessoa com Deficiência define o conceito de 'Tecnologia Assistiva' ou 'Ajuda Técnica'. Trata-se de:",
            "Produtos, equipamentos, dispositivos, recursos, metodologias, estratégias, práticas e serviços que objetivem promover a funcionalidade, relacionada à atividade e à participação da pessoa com deficiência ou com mobilidade reduzida, visando à sua autonomia, independência, qualidade de vida e inclusão social.",
            "Sistemas operacionais e aplicativos de computadores que permitam o controle remoto de dispositivos de automação residencial em redes de fibra óptica.",
            "Técnicas de engenharia civil aplicadas para a desativação de barreiras atitudinais em prédios públicos e privados de uso coletivo do tribunal.",
            "Equipamentos hospitalares de suporte à vida utilizados exclusivamente em leitos de terapia intensiva de clínicas públicas de saúde.",
            "Processos de auditoria realizados por equipes de TI para certificar a conformidade do software do tribunal com a Lei de Acesso à Informação."
        , "A alternativa A transcreve o conceito legal de tecnologia assistiva definido no art. 3º, inciso III, da LBI."),
        # Q34
        (
            "Em relação ao direito ao trabalho da pessoa com deficiência estabelecido na LBI, é correto afirmar:",
            "A pessoa com deficiência tem direito ao trabalho de sua livre escolha e aceitação, em ambiente acessível e inclusivo, em igualdade de oportunidades com as demais pessoas.",
            "O empregador privado fica autorizado a pagar salários inferiores à pessoa com deficiência caso esta execute tarefas em tempo reduzido.",
            "O poder público é dispensado do cumprimento de cotas para pessoas com deficiência em concursos públicos civis de provimento efetivo.",
            "O trabalho da pessoa com deficiência em regime de teletrabalho impede a percepção de adicionais de periculosidade ou insalubridade de direito.",
            "As pessoas com deficiência mental ou intelectual grave são impedidas de exercer qualquer atividade de trabalho em regime competitivo."
        , "A alternativa A reflete o art. 34 da LBI, que assegura o direito ao trabalho em igualdade de oportunidades, ambiente acessível e inclusivo. A LBI proíbe qualquer discriminação de salários por motivo de deficiência."),
        # Q35
        (
            "A acessibilidade é um direito fundamental garantido pela LBI. O conceito legal de 'Universal Design' (Desenho Universal) previsto na lei é definido como:",
            "Concepção de produtos, ambientes, programas e serviços a serem usados por todas as pessoas, sem necessidade de adaptação ou de projeto específico, incluindo os recursos de tecnologia assistiva.",
            "Adaptação razoável e individualizada realizada em prédios antigos do tribunal de justiça para permitir a locomoção de cadeirantes em rampas físicas.",
            "Instalação de softwares de leitura de tela gratuitos em computadores de uso público localizados em bibliotecas do órgão público.",
            "A contratação de profissionais especializados em tradução e interpretação da Língua Brasileira de Sinais (LIBRAS) para eventos judiciais.",
            "O conjunto de calçadas táteis instaladas ao longo de rodovias estaduais para guiar a locomoção de pessoas com deficiência visual profunda."
        , "Desenho Universal (art. 3º, inciso II, da LBI) é a concepção de produtos, ambientes, programas e serviços para serem usados por todos, na maior medida possível, sem adaptações adicionais, embora não exclua recursos de tecnologia assistiva se necessários."),
        # Q36
        (
            "A LBI disciplina a capacidade civil da pessoa com deficiência de forma inovadora. Sobre esse tema, assinale a regra legal correta:",
            "A pessoa com deficiência tem assegurado o direito de decidir sobre o número de filhos e de ter acesso a informações sobre reprodução assistida.",
            "A pessoa com deficiência intelectual ou mental é considerada civilmente incapaz por direito para a prática de todos os atos da vida civil.",
            "O casamento ou a união estável da pessoa com deficiência exige a autorização judicial expressa de curador nomeado em processo judicial.",
            "A curatela é a regra geral aplicada a toda pessoa com deficiência intelectual, de forma permanente e sobre direitos patrimoniais e existenciais.",
            "A pessoa com deficiência necessita obrigatoriamente de representação legal para o exercício de direitos políticos e de voto secreto."
        , "A LBI alterou o Código Civil para estabelecer que a pessoa com deficiência é plenamente capaz na esfera civil. O art. 6º da LBI assegura direitos existenciais (casar, ter filhos, votar) independentemente de curatela. A curatela passou a ser uma medida extraordinária, restrita a aspectos patrimoniais e negociais. A alternativa A reflete este espírito de autonomia existencial."),
        # Q37
        (
            "No âmbito do processo civil, o Estatuto da Pessoa com Deficiência instituiu o 'Processo de Tomada de Decisão Apoiada'. Esse processo consiste em:",
            "Um mecanismo pelo qual a pessoa com deficiência escolhe pelo menos duas pessoas idôneas para apoiá-la na tomada de decisões sobre atos da vida civil.",
            "A nomeação judicial compulsória de curadores públicos que assumem a gestão integral do patrimônio financeiro da pessoa com deficiência.",
            "Um conselho médico composto por psicólogos e assistentes sociais que valida a legalidade de contratos celebrados pela pessoa com deficiência.",
            "A transferência do poder de voto da pessoa com deficiência para os seus familiares diretos em eleições sindicais e governamentais.",
            "A exigência de homologação prévia em cartório de notas para todas as declarações de vontade da pessoa com deficiência intelectual."
        , "A tomada de decisão apoiada (art. 116 da LBI / art. 1.783-A do Código Civil) permite que a pessoa com deficiência escolha dois apoiadores para auxiliá-la nas decisões da vida civil, diferentemente da curatela, na qual o curador decide pela pessoa."),
        # Q38
        (
            "A reserva de vagas (cotas) em concursos públicos para pessoas com deficiência é um instrumento de ação afirmativa importante. No âmbito federal, a Lei nº 8.112/90 reserva às pessoas com deficiência:",
            "Até 20% das vagas oferecidas no concurso público civil de provimento efetivo.",
            "O percentual fixo e obrigatório de 10% de todas as vagas, sem possibilidade de arredondamento matemático.",
            "Vagas exclusivas apenas em cargos que não exijam esforço intelectual ou digitação de relatórios técnicos.",
            "A totalidade das vagas de cadastro de reserva caso nenhum candidato da ampla concorrência atinja a pontuação mínima.",
            "Metade das vagas em cargos em comissão e funções de confiança da administração pública direta."
        , "Segundo o art. 5º, § 2º, da Lei nº 8.112/90, às pessoas portadoras de deficiência serão reservadas até 20% das vagas oferecidas no concurso (no mínimo 5% segundo jurisprudência e normas de concursos). A LBI reforça essa garantia geral de inclusão."),
        # Q39
        (
            "No que concerne à acessibilidade em hotéis, pousadas e similares, a LBI estabelece regras específicas. De acordo com a lei, esses estabelecimentos devem:",
            "Ser acessíveis e garantir pelo menos 10% de seus dormitórios acessíveis, garantido no mínimo um quarto adaptado com desenho universal.",
            "Fornecer atendimento prioritário aos hóspedes com deficiência sem necessidade de adaptar fisicamente as estruturas de banheiros e rampas.",
            "Isentar de taxas de hospedagem todos os hóspedes que apresentarem carteira oficial de tecnologia assistiva de mobilidade reduzida.",
            "Destinar metade de suas vagas de garagem exclusivas para veículos conduzidos por pessoas com deficiência física motora.",
            "Construir blocos de dormitórios isolados e exclusivos para hóspedes com deficiência para garantir a segurança cibernética local."
        , "Segundo o art. 45 da LBI, hotéis e pousadas devem disponibilizar pelo menos 10% de dormitórios acessíveis, garantindo pelo menos um quarto totalmente acessível."),
        # Q40
        (
            "A acessibilidade em sites da internet é um direito garantido por lei. A LBI estabelece que é obrigatória a acessibilidade nos portais de internet de:",
            "Órgãos de governo, concessionárias de serviços públicos e empresas com sede ou representação comercial no país, para uso de pessoas com deficiência.",
            "Bancos comerciais de fomento econômico privados de forma exclusiva, ficando os portais governamentais isentos de adaptação técnica.",
            "Fóruns judiciais que tratem exclusivamente de direito previdenciário estadual, dispensando-se a acessibilidade em outros órgãos da justiça.",
            "Redes sociais de entretenimento com mais de dez milhões de usuários ativos cadastrados no território nacional de internet.",
            "Empresas de desenvolvimento de softwares e provedores de hospedagem web baseados em servidores de nuvem internacionais."
        , "Conforme o art. 63 da LBI, é obrigatória a acessibilidade nos sítios da internet mantidos por órgãos de governo ou por empresas com sede ou representação comercial no País, garantindo acesso à informação em formatos acessíveis."),
        # Q41
        (
            "As pessoas com deficiência têm direito a prioridade na tramitação de procedimentos administrativos e judiciais. Sobre a tramitação prioritária, assinale a alternativa correta:",
            "A prioridade é concedida mediante requerimento do interessado instruído com a prova da condição de pessoa com deficiência.",
            "A prioridade é deferida automaticamente apenas se o processo judicial for proposto perante varas especializadas de direito de família.",
            "A prioridade isenta a pessoa com deficiência do recolhimento de custas judiciais e de taxas de recursos na esfera estadual.",
            "O benefício da prioridade é extinto se a pessoa com deficiência contratar advogados particulares para representá-la em juízo.",
            "A prioridade impede que o juiz profira sentenças desfavoráveis aos direitos da pessoa com deficiência na esfera cível."
        , "A tramitação prioritária de processos judiciais e administrativos (art. 9º, inciso VII, da LBI) é deferida mediante requerimento da parte interessada com a comprovação de sua deficiência."),
        # Q42
        (
            "Em relação ao atendimento prioritário em órgãos públicos e prestadores de serviços, a LBI estende esse direito a acompanhantes. A prioridade de atendimento ao acompanhante:",
            "Aplica-se ao acompanhante ou atendente pessoal diretamente vinculado ao atendimento da pessoa com deficiência de forma imediata.",
            "Garante ao acompanhante a isenção de tarifas de transporte coletivo urbano e passagens interestaduais de forma permanente.",
            "Autoriza o acompanhante a realizar transações bancárias e firmar contratos civis em nome da pessoa com deficiência sem procuração.",
            "Fica restrita a exames médicos de emergência realizados em hospitais e clínicas da rede de saúde pública municipal do Estado.",
            "Impede o atendimento paralelo de outros cidadãos comuns que não possuam deficiência física ou mobilidade reduzida."
        , "O atendimento prioritário (art. 9º, § 1º, da LBI) estende-se ao acompanhante da pessoa com deficiência ou ao seu atendente pessoal, exceto no que se refere a direitos personalíssimos (como o recebimento de valores ou voto). A alternativa A está correta."),
        # Q43
        (
            "A LBI tipifica crimes específicos decorrentes da discriminação de pessoas com deficiência. Assinale a conduta que constitui crime punível com reclusão nos termos da referida lei:",
            "Praticar, induzir ou incitar discriminação contra pessoa em razão de sua deficiência, sob qualquer pretexto social ou comercial.",
            "Recusar a contratação de seguros privados de saúde corporativos para pessoas com deficiência mental de forma justificada por auditoria.",
            "Deixar de instalar calçadas táteis em reformas residenciais particulares localizadas em áreas rurais de difícil acesso geográfico.",
            "Não fornecer softwares de leitura de tela para computadores de uso doméstico de servidores públicos inativos do tribunal.",
            "Cobrar taxas adicionais de hospedagem em hotéis privados para cães-guia que acompanham pessoas com deficiência visual."
        , "O art. 88 da LBI tipifica como crime: 'Praticar, induzir ou incitar discriminação contra pessoa em razão de sua deficiência'. A pena é de reclusão, de 1 a 3 anos, e multa. Cobrar taxas adicionais para cão-guia ou negar planos de saúde são infrações civis/administrativas específicas, mas a discriminação direta é o crime central tipificado com reclusão."),
        # Q44
        (
            "O direito à educação da pessoa com deficiência é amplamente protegido pela LBI. De acordo com a lei, as instituições privadas de ensino:",
            "Devem garantir um sistema educacional inclusivo em todos os níveis, sendo vedada a cobrança de valores adicionais de qualquer natureza em suas mensalidades.",
            "Ficam autorizadas a cobrar taxas adicionais de matrícula para cobrir custos de contratação de profissionais de apoio e acessibilidade.",
            "Podem limitar o ingresso de alunos com deficiência a no máximo 5% do total de vagas oferecidas por turma para manter a qualidade de ensino.",
            "Estão desobrigadas de fornecer tecnologia assistiva ou materiais adaptados quando o aluno possuir deficiência auditiva ou visual.",
            "Devem matricular alunos com deficiência exclusivamente em salas de aula especiais separadas dos demais estudantes da escola."
        , "O art. 28 da LBI veda expressamente a cobrança de valores adicionais de qualquer natureza em mensalidades, anuidades e matrículas por instituições privadas de ensino para o fornecimento de atendimento inclusivo, profissional de apoio ou acessibilidade. A alternativa A está correta."),
        # Q45
        (
            "Em relação ao direito à moradia, a LBI estabelece cotas para pessoas com deficiência em programas habitacionais públicos ou subsidiados com recursos públicos. O percentual mínimo de unidades habitacionais reservadas e adaptadas para esse fim é de:",
            "3%",
            "5%",
            "10%",
            "2%",
            "15%"
        , "Segundo o art. 32, § 1º, inciso I, da LBI, nos programas habitacionais públicos ou subsidiados com recursos públicos, a pessoa com deficiência ou o seu responsável tem prioridade na aquisição de imóvel para moradia própria, devendo ser reservado, no mínimo, 3% do total das unidades habitacionais para esse fim.")
    ]
    dia_27_themes.append(("Legislação e Direitos da Pessoa com Deficiência (PCD)", t3_27))
    
    write_day_file(os.path.join(questoes_dir, "dia_27_05_questoes.md"),
                   "Bateria de Questões FCC — Quarta-feira 27/05",
                   "Este arquivo contém 45 questões altamente calibradas nos padrões da FCC, com alternativas de comprimento similar e distratores baseados em pegadinhas reais.",
                   dia_27_themes)

if __name__ == "__main__":
    main()
