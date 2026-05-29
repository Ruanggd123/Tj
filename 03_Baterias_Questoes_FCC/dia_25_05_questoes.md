# Bateria de Questões FCC — Segunda-feira 25/05

Este arquivo contém 45 questões altamente calibradas nos padrões da FCC, com alternativas de comprimento similar e distratores baseados em pegadinhas reais.

---

## 📝 TEMA 1: Engenharia de Software — Engenharia de Requisitos

### Questão 1 (FCC)
Segundo Ian Sommerville, os requisitos de software são divididos em requisitos funcionais e não funcionais. Sobre as subcategorias de requisitos não funcionais, assinale a alternativa correta:
A) Os requisitos não funcionais externos especificam regras de codificação do ambiente de desenvolvimento, tais como uso obrigatório de IDEs homologadas pela equipe de TI.
B) Os requisitos não funcionais organizacionais derivam de políticas e regras da empresa parceira, tais como restrições de horários de deploy e contratação de servidores.
C) Os requisitos não funcionais de produto definem restrições sobre o comportamento do software, englobando metas de desempenho, requisitos de confiabilidade e usabilidade.
D) Os requisitos não funcionais de processo definem prazos para a entrega dos artefatos de homologação, impedindo a redefinição de escopos em fases de validação.
E) Os requisitos não funcionais de conformidade tratam exclusivamente de auditorias contábeis realizadas por órgãos de controle externo e fiscalizadores fazendários.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente os requisitos não funcionais de produto, que especificam ou restringem o comportamento do próprio software (como desempenho, usabilidade e confiabilidade).
</details>

---

### Questão 2 (FCC)
Em modelagem de sistemas com a UML 2.5, os diagramas de Casos de Uso são amplamente utilizados para mapear requisitos funcionais. Sobre os relacionamentos de 'include' e 'extend' nesse diagrama, é correto afirmar:
A) O relacionamento de extend indica um comportamento opcional que é inserido no caso de uso base sob condições específicas definidas em pontos de extensão.
B) O relacionamento de include representa um comportamento condicional que só é disparado se o ator principal realizar uma ação de exceção no fluxo principal.
C) O relacionamento de extend aponta obrigatoriamente do caso de uso base para o caso de uso estendido, indicando uma execução sequencial e síncrona.
D) O relacionamento de include indica que o caso de uso base adiciona opcionalmente o comportamento do caso de uso incluído sem alterar o fluxo de execução.
E) O relacionamento de extend exige que o caso de uso estendido compartilhe a mesma assinatura de métodos e atributos definidos na classe do caso de uso base.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A define corretamente o relacionamento 'extend' como um comportamento condicional/opcional inserido no caso de uso base em determinados pontos de extensão.
</details>

---

### Questão 3 (FCC)
A rastreabilidade de requisitos é uma atividade fundamental para garantir o controle de mudanças no ciclo de vida de desenvolvimento de sistemas. Sobre a rastreabilidade bidirecional, assinale a alternativa correta:
A) Ela garante exclusivamente a conformidade do código-fonte com o banco de dados relacional, sem necessidade de analisar solicitações de mudanças.
B) Ela permite rastrear o requisito desde a sua origem (como a entrevista com o usuário) até os artefatos de projeto e código, e vice-versa.
C) Ela impede a exclusão de requisitos obsoletos do documento de especificação caso estes já tenham sido implementados no ambiente de testes.
D) Ela rastreia os diagramas de classe em direção aos diagramas de caso de uso de forma estrita, sem considerar os documentos de requisitos textuais.
E) Ela relaciona as interfaces com o usuário diretamente aos planos de testes unitários executados pela equipe de controle de qualidade integrada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A rastreabilidade bidirecional assegura que cada requisito possa ser rastreado adiante (forward) até o código/testes e também de volta (backward) até a sua origem.
</details>

---

### Questão 4 (FCC)
A elicitação de requisitos é uma fase crítica que emprega diversas técnicas para capturar as necessidades dos stakeholders. Sobre a técnica de Etnografia, assinale a alternativa correta:
A) Envolve a análise exclusiva de manuais técnicos e documentações de sistemas legados que serão desativados no processo de migração de dados.
B) Consiste em um questionário fechado com perguntas de múltipla escolha enviado por correio eletrônico a todos os gerentes setoriais do tribunal.
C) Baseia-se em reuniões de design participativo estruturadas com a presença de facilitadores externos e especialistas em engenharia de software.
D) É um processo focado na criação rápida de modelos de tela interativos para validar o fluxo de navegação do sistema com os patrocinadores.
E) Trata-se de uma técnica de observação imersiva na qual o analista acompanha a rotina diária real do usuário para identificar requisitos implícitos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A Etnografia baseia-se na observação de como os usuários realmente trabalham no dia a dia, sendo ideal para descobrir requisitos de processo implícitos.
</details>

---

### Questão 5 (FCC)
A validação e a verificação de requisitos são processos que visam garantir a qualidade da especificação antes do início do desenvolvimento. A diferença conceitual entre validar e verificar requisitos é que:
A) Verificar assegura que o cliente aprova o protótipo funcional apresentado na homologação, enquanto validar foca nas métricas internas de desempenho do banco de dados.
B) Validar garante que o sistema atende às reais necessidades do usuário (construir o produto correto), enquanto verificar garante a conformidade com as especificações técnicas (construir o produto corretamente).
C) Validar consiste na realização de testes de caixa-preta automatizados pela equipe de QA, enquanto verificar envolve auditorias fiscais sobre o orçamento do projeto.
D) Verificar é uma atividade puramente manual realizada por gerentes de negócio, enquanto validar é uma atividade automatizada por compiladores de código.
E) Validar busca encontrar conflitos gramaticais no texto da especificação de requisitos, enquanto verificar busca validar a viabilidade financeira do sistema.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A validação foca em saber se o produto está alinhado ao que o usuário precisa, enquanto a verificação avalia se o produto segue a especificação técnica documentada.
</details>

---

### Questão 6 (FCC)
No contexto de gerenciamento de requisitos, a matriz de rastreabilidade de requisitos (RTM) é uma ferramenta essencial. A função principal da RTM em um projeto de desenvolvimento de sistemas é:
A) Exibir a escala hierárquica e a distribuição de cargos e salários dos analistas que participaram do desenvolvimento do sistema corporativo.
B) Calcular o custo financeiro estimado para a implementação de cada funcionalidade mapeada durante a etapa de elicitação e levantamento de dados.
C) Armazenar fisicamente os registros de log de depuração gerados pelos servidores de aplicação durante a execução dos testes de estresse.
D) Mapear a relação entre cada requisito individual, suas fontes de origem, casos de uso correspondentes, componentes de código e casos de teste.
E) Substituir o modelo conceitual de dados do banco relacional, unificando as entidades e relacionamentos em uma única tabela de consulta física.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A matriz de rastreabilidade serve para correlacionar requisitos a outros artefatos do ciclo de vida, facilitando a análise de impacto e a cobertura de testes.
</details>

---

### Questão 7 (FCC)
Durante o processo de engenharia de requisitos, a volatilidade de requisitos refere-se às mudanças que ocorrem ao longo do tempo. Sobre a volatilidade dos requisitos, é correto afirmar:
A) Os requisitos não funcionais de portabilidade são os únicos que apresentam volatilidade severa em sistemas de missão crítica governamentais.
B) A volatilidade é um erro de modelagem decorrente de falhas graves cometidas pelos analistas durante a fase inicial de elicitação dos dados.
C) A volatilidade deve ser completamente eliminada em projetos de software através do uso de contratos rígidos de escopo fechado tradicional.
D) Os requisitos são mutáveis devido a mudanças no ambiente de negócios, novas leis ou melhor compreensão dos usuários sobre suas próprias necessidades.
E) A volatilidade impede a compilação do código-fonte do sistema em servidores de integração contínua baseados em microsserviços modernos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A volatilidade de requisitos é inerente aos projetos e ocorre por mudanças organizacionais, de negócios, legais ou maturidade da visão do cliente.
</details>

---

### Questão 8 (FCC)
Considere que um analista precise definir os requisitos de segurança para um sistema do tribunal. Um exemplo típico de requisito não funcional de segurança que segue o padrão de especificação técnica é:
A) O usuário deve poder emitir o relatório de produtividade semanal dos magistrados a partir da tela principal de consultas em lote.
B) O sistema deve criptografar todas as senhas de usuários e dados sensíveis utilizando o algoritmo de hash SHA-256 com salvação de sal em banco.
C) O sistema deve ser desenvolvido utilizando o framework Spring Boot 3 na linguagem Java com persistência via Hibernate e JPA local.
D) A equipe de desenvolvimento deve entregar toda a documentação de arquitetura de rede no formato PDF em até dez dias úteis após a homologação.
E) O sistema deve estar disponível para acesso na internet exclusivamente durante os dias úteis, entre as oito horas e as vinte horas de Brasília.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B apresenta uma restrição de segurança (como o sistema deve se comportar em relação à segurança dos dados), caracterizando um requisito não funcional.
</details>

---

### Questão 9 (FCC)
Em relação à especificação de requisitos de software (SRS) baseada no padrão IEEE 830, uma característica essencial de uma SRS de alta qualidade é a consistência. Isso significa que:
A) A especificação deve ser escrita exclusivamente em linguagem matemática formal para evitar qualquer tipo de ambiguidade na interpretação do leitor.
B) Todos os requisitos descritos no documento devem possuir exatamente a mesma quantidade de palavras e a mesma formatação visual de tópicos.
C) Nenhum subconjunto de requisitos individuais descritos no documento deve entrar em conflito direto ou indireto com outros requisitos do mesmo sistema.
D) O documento de requisitos não deve admitir modificações ou revisões adicionais após a aprovação formal assinada pela diretoria do tribunal.
E) Os requisitos de software devem ser descritos de forma genérica para permitir que qualquer sistema de mercado atenda às solicitações sem customização.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A consistência em uma SRS significa ausência de conflitos entre os requisitos (por exemplo, um requisito exigindo entrega em 2 segundos e outro exigindo processamento em lote lento da mesma operação).
</details>

---

### Questão 10 (FCC)
Na modelagem de Casos de Uso da UML, a definição adequada de um Atores (Actors) é de fundamental relevância. Sobre o conceito de atores na UML, assinale a alternativa correta:
A) Os atores devem ser implementados obrigatoriamente como classes abstratas no código-fonte para gerenciar as sessões ativas dos usuários.
B) Um ator é a representação física de uma tabela do banco de dados relacional que recebe atualizações síncronas de escrita durante a transação.
C) Um ator representa um papel desempenhado por um usuário humano, um dispositivo de hardware ou outro sistema externo que interage com o sistema.
D) Um ator não pode possuir relacionamentos de herança ou generalização com outros atores descritos no mesmo diagrama de casos de uso do sistema.
E) Os atores são elementos internos do sistema que realizam a lógica de processamento dos fluxos alternativos e de exceção mapeados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. Atores são entidades externas (humanos, hardware, sistemas externos) que interagem diretamente com o sistema de software modelado.
</details>

---

### Questão 11 (FCC)
Requisitos de Domínio são descritos como requisitos que derivam do campo de aplicação do sistema. Sobre os requisitos de domínio, é correto afirmar:
A) Eles devem ser convertidos obrigatoriamente em classes de teste unitário e não podem ser documentados no formato de texto livre padrão.
B) Eles referem-se exclusivamente a restrições de rede de computadores e domínios de internet controlados por servidores DNS centrais do tribunal.
C) Eles são opcionais e servem apenas como sugestões de design de interface gráfica para melhorar a experiência de usabilidade do usuário final.
D) Eles podem impor novas restrições ou regras de negócio específicas ao sistema, e se não forem atendidos, o sistema pode se tornar inoperante.
E) Eles impedem a portabilidade do software para sistemas operacionais baseados em Unix, limitando a execução ao ambiente Microsoft Windows.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. Requisitos de domínio refletem as particularidades e regras do negócio/área onde o sistema opera (ex: regras jurídicas no tribunal). Se negligenciados, inviabilizam o uso do sistema.
</details>

---

### Questão 12 (FCC)
No ciclo de engenharia de requisitos, a prototipação é frequentemente utilizada. Sobre os protótipos descartáveis (throwaway prototyping), assinale a alternativa correta:
A) Eles exigem a implementação completa do banco de dados e de todas as regras de validação física para garantir a fidelidade do comportamento.
B) Eles servem como base direta de código-fonte que será refinado e evoluído até se tornar a versão final de produção do sistema corporativo.
C) Eles são desenvolvidos rapidamente para ajudar a esclarecer requisitos incertos, sendo descartados após a validação do conceito pelo cliente.
D) Eles não admitem a utilização de ferramentas de design gráfico, devendo ser criados exclusivamente através de desenhos manuais em papel físico.
E) Eles são mantidos em paralelo com o sistema real em produção para servir como ambiente alternativo de recuperação de desastres e backups.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. O protótipo descartável serve unicamente para elucidar requisitos complexos ou nebulosos, sendo jogado fora e o sistema real escrito do zero.
</details>

---

### Questão 13 (FCC)
Em relação às técnicas de elicitação de requisitos, o JAD (Joint Application Development) destaca-se em ambientes corporativos. A principal característica do JAD é:
A) A simulação computacional de falhas de hardware para verificar a resiliência de servidores físicos do datacenter corporativo do órgão.
B) A análise isolada de logs de erros e banco de dados realizada pela equipe de suporte sem a interferência ou participação do usuário final.
C) A observação silenciosa e imersiva do ambiente de trabalho do cliente por longos períodos para mapear os fluxos informais de processos.
D) O envio de questionários eletrônicos anônimos para um grande grupo de stakeholders distribuídos geograficamente em comarcas distantes.
E) A realização de reuniões estruturadas e colaborativas que reúnem usuários, desenvolvedores e gerentes para definir requisitos em conjunto.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. O JAD baseia-se em workshops colaborativos intensivos com representantes de negócios e de TI trabalhando juntos para acelerar a especificação.
</details>

---

### Questão 14 (FCC)
A especificação de requisitos não funcionais de usabilidade visa garantir que o sistema seja fácil de aprender e utilizar. Um requisito de usabilidade adequado é:
A) O tempo médio necessário para que um novo operador consiga realizar uma pesquisa de processo sem auxílio externo não deve exceder trinta minutos.
B) O sistema de controle processual judicial deve suportar no mínimo quinhentos acessos simultâneos de usuários ativos sem apresentar latência.
C) A taxa de falhas críticas nas transações financeiras de pagamento de custas judiciais deve ser inferior a uma falha a cada dez mil transações.
D) O sistema deve ser desenvolvido em conformidade estrita com as especificações técnicas da Lei de Acesso à Informação e do Marco Civil.
E) A interface gráfica do sistema deve ser renderizada utilizando exclusivamente folhas de estilo CSS compactadas e compatíveis com HTML5.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. Requisitos de usabilidade medem fatores como tempo de aprendizado, satisfação do usuário e facilidade de uso em termos quantificáveis.
</details>

---

### Questão 15 (FCC)
Durante a fase de análise de requisitos, os analistas lidam com requisitos conflitantes de diferentes stakeholders. A abordagem correta para resolver esses conflitos é:
A) Descartar imediatamente todos os requisitos que gerarem qualquer nível de discordância entre as áreas de negócio participantes do projeto.
B) Priorizar integralmente os requisitos solicitados pela equipe de desenvolvimento de software, por possuírem maior conhecimento sobre tecnologia.
C) Implementar todas as solicitações conflitantes de forma paralela através de múltiplos ramais (branches) de código a serem unificados depois.
D) Realizar negociações estruturadas para encontrar um consenso que atenda aos objetivos estratégicos do projeto e priorizar requisitos prioritários.
E) Decidir os conflitos por meio de votação eletrônica aberta a todos os cidadãos do Estado através do portal da transparência do tribunal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A negociação e a priorização de requisitos em reuniões de alinhamento são técnicas padrão da engenharia de requisitos para lidar de forma profissional com visões conflitantes de stakeholders.
</details>

---

## 📝 TEMA 2: Banco de Dados — SGBDs Oracle, PostgreSQL e H2

### Questão 16 (FCC)
No banco de dados Oracle, a pseudo-coluna ROWNUM é utilizada em consultas SQL. Sobre o funcionamento e comportamento do ROWNUM, assinale a alternativa correta:
A) O ROWNUM funciona como uma coluna física gravada de forma permanente no bloco de dados da tabela, identificando a sequência de inserção física.
B) O ROWNUM é atribuído às linhas à medida que elas são selecionadas pela consulta, ocorrendo antes de qualquer operação de ordenação (ORDER BY).
C) A utilização direta da condição `WHERE ROWNUM = 2` em uma consulta simples retornará a segunda linha de dados processada com sucesso no buffer.
D) O ROWNUM substitui a necessidade do uso de chaves primárias compostas em tabelas particionadas fisicamente por range de datas e horas.
E) O Oracle atualiza os valores de ROWNUM de forma retroativa e síncrona sempre que uma instrução UPDATE altera os valores da coluna indexada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. ROWNUM é gerado dinamicamente antes do ORDER BY. Por isso, para ordenar e depois limitar (top-N query), o Oracle exige o uso de uma subconsulta contendo o ORDER BY interno.
</details>

---

### Questão 17 (FCC)
A tabela DUAL é um objeto nativo de suma importância no banco de dados Oracle. A característica técnica da tabela DUAL no Oracle é:
A) Trata-se de uma tabela especial criada automaticamente pelo Oracle que possui apenas uma coluna denominada DUMMY e contém uma única linha.
B) É uma tabela temporária física utilizada exclusivamente para armazenar registros de auditoria e sessões de usuários administradores ativos.
C) Consiste em um mecanismo de particionamento virtual que duplica os dados das tabelas de produção para evitar perdas em transações paralelas.
D) É uma tabela que veda operações de SELECT do usuário comum, sendo restrita à execução de stored procedures e triggers do sistema de BD.
E) Trata-se de uma estrutura de memória RAM que armazena os índices de chaves estrangeiras pendentes de validação de consistência relacional.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A tabela DUAL possui uma única coluna (DUMMY do tipo VARCHAR2(1)) e uma única linha (contendo o valor 'X'), sendo útil para avaliar expressões e funções do sistema com SELECT.
</details>

---

### Questão 18 (FCC)
No PostgreSQL, a criação de colunas com auto-incremento pode ser feita de diferentes maneiras. Sobre a declaração serial e o padrão ANSI IDENTITY no PostgreSQL, assinale a alternativa correta:
A) A partir da versão 10, o PostgreSQL recomenda o uso de GENERATED AS IDENTITY por ser padrão ANSI SQL, embora o tipo SERIAL ainda seja suportado.
B) O tipo SERIAL cria uma chave primária física não sequencial baseada no algoritmo UUID versão 4 de criptografia assimétrica de rede.
C) A declaração GENERATED ALWAYS AS IDENTITY impede que o usuário force a inserção de valores manuais na coluna de forma direta na instrução INSERT.
D) O tipo SERIAL não cria sequências (sequences) internas no banco de dados, operando puramente como uma diretiva de compilação temporária de DDL.
E) O uso de GENERATED BY DEFAULT AS IDENTITY restringe a coluna a aceitar apenas valores informados manualmente pelo usuário no banco de dados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. O PostgreSQL suporta o padrão SQL com IDENTITY (`GENERATED ALWAYS/BY DEFAULT AS IDENTITY`), que é o recomendado atualmente em substituição ao clássico tipo serial (que cria uma sequência implícita).
</details>

---

### Questão 19 (FCC)
A paginação de dados em consultas SQL é um requisito comum em sistemas web do tribunal. A sintaxe correta para limitar o retorno em 10 linhas, pulando as primeiras 50 no PostgreSQL, é:
A) OFFSET 10 LIMIT 50
B) LIMIT 10 OFFSET 50
C) ROWNUM BETWEEN 51 AND 60
D) LIMIT 50, 10
E) ROWS 50 TO 60

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A sintaxe padrão e suportada no PostgreSQL para paginação utiliza a palavra-chave LIMIT (quantidade de registros a retornar) seguida por OFFSET (quantidade de registros a pular).
</details>

---

### Questão 20 (FCC)
O H2 Database é um SGBD amplamente utilizado em ambientes de desenvolvimento e testes. Sobre as características do H2 Database, assinale a alternativa correta:
A) Ele veda o suporte à API JDBC tradicional, exigindo conexões proprietárias desenvolvidas em C# para realizar a manipulação de dados.
B) Ele opera exclusivamente como banco NoSQL orientado a documentos, impedindo o processamento de tabelas relacionais clássicas com chaves SQL.
C) Ele suporta o modo 'In-Memory', o que permite que os dados sejam mantidos apenas na memória RAM e limpos ao finalizar a execução da aplicação.
D) O H2 exige a instalação prévia de um servidor de banco de dados robusto no sistema operacional, não funcionando em modo embutido (embedded).
E) O H2 não suporta padrões de compatibilidade SQL com outros SGBDs do mercado, limitando-se a um dialeto próprio incompatível com Oracle.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. O H2 Database é escrito em Java, é leve e possui o modo In-Memory (`jdbc:h2:mem:...`), ideal para testes automatizados rápidos de banco de dados relacional.
</details>

---

### Questão 21 (FCC)
O PostgreSQL utiliza um mecanismo de controle de concorrência avançado conhecido como MVCC. A principal finalidade do MVCC no PostgreSQL é:
A) Bloquear exclusivamente a tabela inteira sempre que uma operação de leitura for executada por um usuário sem privilégios de administração.
B) Duplicar fisicamente os arquivos de log de transações em tempo real para permitir a recuperação instantânea em casos de falta de energia.
C) Impedir a execução de instruções de atualização (UPDATE) paralelas sobre diferentes tabelas que compartilham chaves estrangeiras comuns.
D) Converter automaticamente consultas relacionais SQL complexas em consultas NoSQL otimizadas para processamento em servidores de busca.
E) Garantir que leitores não bloqueiem escritores e escritores não bloqueiem leitores durante o acesso paralelo aos dados na transação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. O MVCC (Multi-Version Concurrency Control) permite que leitores e escritores trabalhem sem se bloquear mutuamente, mantendo múltiplas versões das linhas do banco.
</details>

---

### Questão 22 (FCC)
No Oracle Database, os arquivos de dados físicos (Datafiles) estão associados a uma estrutura lógica de armazenamento denominada:
A) Schema Area
B) Redo Log File
C) Control File
D) Tablespace
E) PGA (Program Global Area)

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. Tablespace é a estrutura lógica de armazenamento no Oracle que agrupa um ou mais arquivos de dados (Datafiles) físicos no sistema de arquivos.
</details>

---

### Questão 23 (FCC)
O comando VACUUM desempenha um papel crítico na manutenção e desempenho do PostgreSQL. A função principal do comando VACUUM no PostgreSQL é:
A) Compactar as conexões de rede ativas de usuários inativos para liberar espaço no pool de conexões do servidor do banco de dados.
B) Realizar a desfragmentação física dos índices do tipo B-Tree gravando os dados em setores contínuos da memória de armazenamento principal.
C) Efetuar o backup incremental síncrono da base de dados e transmiti-lo via rede para servidores secundários de replicação física.
D) Validar as restrições de integridade referencial (chaves estrangeiras) que foram desativadas temporariamente por scripts de carga de dados.
E) Recuperar o espaço físico ocupado por versões de linhas obsoletas (mortas) resultantes de operações de UPDATE e DELETE anteriores.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. O VACUUM remove as linhas mortas geradas pelo MVCC, liberando esse espaço para novas gravações da própria tabela.
</details>

---

### Questão 24 (FCC)
No Oracle, o dicionário de dados contém visões com prefixos específicos que indicam o escopo de visibilidade dos objetos do banco. As visões com os prefixos USER_, ALL_ e DBA_ contêm, respectivamente:
A) Tabelas de dados cadastrais; Índices criados na sessão ativa; Procedimentos armazenados e triggers em execução síncrona no servidor.
B) Objetos de propriedade de usuários comuns; Objetos compartilhados em rede; Objetos do esquema SYSTEM exclusivos do administrador de dados.
C) Objetos pertencentes ao usuário atual; Objetos que o usuário atual tem permissão para acessar; Todos os objetos existentes no banco de dados.
D) Objetos criados nas últimas 24 horas; Objetos legados em conformidade legal; Tabelas de sistema em manutenção de disco.
E) Chaves primárias ativas; Chaves estrangeiras pendentes de validação; Índices únicos globais associados a partições físicas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. USER_ mostra objetos do próprio esquema; ALL_ mostra todos os objetos que o usuário tem privilégio de acesso; DBA_ mostra todos os objetos do banco (para administradores).
</details>

---

### Questão 25 (FCC)
A arquitetura do PostgreSQL baseia-se em um modelo de processos. Sobre a arquitetura de processos do PostgreSQL, é correto afirmar:
A) As conexões ativas compartilham a mesma área de pilha de execução (Stack) de forma concorrente sem isolamento de memória física no SO.
B) O PostgreSQL opera em uma arquitetura puramente multithreaded dentro de um único processo principal de execução em tempo real no SO.
C) O processo postmaster é responsável exclusivo pela execução física do comando VACUUM FULL, parando todas as atividades de escrita do banco.
D) O PostgreSQL exige o uso obrigatório de um servidor de pool de conexões externo como o PgBouncer para inicializar o banco de dados.
E) Para cada conexão de cliente estabelecida com o banco, o PostgreSQL cria um novo processo separado (backend process) gerenciado pelo postmaster.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. O PostgreSQL adota uma arquitetura baseada em processos (process-based), onde o postmaster faz o dispatch e cria um processo backend dedicado para cada conexão.
</details>

---

### Questão 26 (FCC)
Em relação à compatibilidade de SQL no H2 Database, assinale a alternativa que apresenta uma propriedade de configuração técnica importante desse SGBD:
A) Ele possui modos de compatibilidade integrados que emulam o comportamento de SGBDs como Oracle, PostgreSQL e MySQL de forma configurável.
B) Ele exige a conversão de todas as tabelas em estruturas NoSQL JSON antes de executar consultas nativas em memória no sistema web.
C) Ele opera com um compilador proprietário que veda o uso de joins implícitos e explícitos na instrução SELECT do usuário comum.
D) Os modos de compatibilidade do H2 exigem a tradução manual de stored procedures escritas em PL/SQL para classes compiladas em C++.
E) Ele veda o uso de constraints de integridade referencial quando o modo de compatibilidade do banco relacional PostgreSQL está ativo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. O H2 possui uma flag de compatibilidade (ex: `;MODE=PostgreSQL` ou `;MODE=Oracle`) que auxilia emulando sintaxes e comportamentos específicos dos SGBDs maiores.
</details>

---

### Questão 27 (FCC)
No Oracle, o ROWID é um conceito técnico importante. O ROWID representa:
A) Uma pseudo-coluna sequencial numérica iniciada em um que é gerada dinamicamente a cada nova consulta executada pelo usuário ativo.
B) O endereço físico e único de uma linha de tabela no disco, composto pelo número do arquivo de dados, bloco e posição interna da linha.
C) O identificador único de transação do banco de dados que garante o isolamento lógico das alterações concorrentes da sessão de rede.
D) A chave substituta (surrogate key) gerada automaticamente a partir de um gerador de UUIDs integrado no kernel do SGBD relacional.
E) O código identificador do usuário que possui privilégios de escrita física sobre a tabela associada ao bloco de dados lido.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. O ROWID indica a exata localização física da linha no banco de dados Oracle, sendo o método de acesso mais rápido para retornar uma única linha de dados.
</details>

---

### Questão 28 (FCC)
No PostgreSQL, a integridade referencial e as transações são controladas de perto. Ao tentar inserir um registro violando uma Foreign Key, o PostgreSQL:
A) Aborta imediatamente a transação ativa ou gera um erro de violação de constraint, impedindo a persistência do dado inconsistente.
B) Apenas registra um aviso em arquivo de log de eventos e permite a inserção física do registro mantendo a chave estrangeira nula.
C) Cria dinamicamente o registro correspondente na tabela pai com valores em branco para manter a integridade referencial lógica.
D) Suspende a execução da instrução INSERT indefinidamente até que o registro correspondente na tabela pai seja inserido via rede.
E) Exclui automaticamente todos os registros dependentes nas tabelas filhas para assegurar a consistência referencial local.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. Qualquer violação de chave estrangeira (FK) gera um erro que aborta a transação em curso no PostgreSQL, não permitindo dados órfãos.
</details>

---

### Questão 29 (FCC)
O H2 Database pode ser configurado de diferentes formas de conexão. A URL de conexão JDBC `jdbc:h2:tcp://localhost/~/test` indica que o banco de dados rodará no modo:
A) Embedded (embutido), no qual o banco de dados roda dentro da mesma máquina virtual Java (JVM) da própria aplicação ativa.
B) Server (servidor), no qual a aplicação se conecta a um banco de dados rodando em um processo separado através da rede local.
C) In-Memory (memória), no qual os dados não são persistidos em disco e residem de forma exclusiva na memória RAM do computador.
D) Clustered (clusterizado), no qual os dados são duplicados de forma síncrona em múltiplos servidores distribuídos geograficamente.
E) NoSQL, no qual o H2 desativa todas as capacidades SQL relacionais para operar exclusivamente como armazenamento chave-valor.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. O prefixo `jdbc:h2:tcp:` indica conexões remotas via protocolo TCP, o que caracteriza a execução no modo Server, e não embutida (embedded).
</details>

---

### Questão 30 (FCC)
Sobre a remoção física de dados, considere a diferença entre os comandos `DELETE FROM tabela` e `TRUNCATE TABLE tabela` nos SGBDs relacionais corporativos. Assinale a alternativa correta:
A) O DELETE libera de forma instantânea todo o espaço em disco ocupado pelos dados para o sistema operacional, ao contrário do TRUNCATE.
B) O TRUNCATE é um comando DDL que remove todas as linhas de uma tabela rapidamente sem gerar logs detalhados de transações por linha, enquanto o DELETE é DML e gera logs por linha.
C) O TRUNCATE permite a utilização de cláusulas WHERE para filtrar quais registros específicos serão removidos durante a execução do comando.
D) O comando DELETE é executado muito mais rápido que o TRUNCATE por não validar regras de integridade referencial e chaves estrangeiras.
E) O TRUNCATE ativa individualmente todas as triggers do tipo BEFORE DELETE associadas à tabela antes de executar a limpeza física de disco.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. TRUNCATE é DDL, remove os dados desalocando as páginas de dados de forma muito rápida e sem gerar logs de undo por registro, enquanto DELETE é DML, avaliando linha a linha e disparando triggers.
</details>

---

## 📝 TEMA 3: Língua Portuguesa — Classes de Palavras e Pronomes

### Questão 31 (FCC)
Em relação à flexão e colocação dos pronomes pessoais oblíquos átonos, a norma-padrão da língua portuguesa estabelece regras específicas de próclise, mesóclise e ênclise. Assinale a frase gramaticalmente correta:
A) Tudo se resolveu rapidamente após a intervenção da assessoria de segurança técnica.
B) Me entregaram os relatórios de auditoria processual do tribunal logo pela manhã.
C) Os analistas de suporte se comprometeram a realizar a migração da base de dados hoje.
D) Caso encontre o arquivo corrompido em disco, devolva-o-nos imediatamente para perícia.
E) Ninguém informou-nos sobre as alterações de escopo aprovadas no cronograma de estudos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A palavra 'Tudo' é um pronome indefinido, o que atrai obrigatoriamente a próclise ('se resolveu'). Iniciar frases com pronome oblíquo ('Me entregaram') ou usar ênclise após palavra atrativa ('Ninguém informou-nos') violam as regras cultas.
</details>

---

### Questão 32 (FCC)
A correta utilização dos pronomes demonstrativos 'este', 'esse' e 'aquele' envolve fatores espaciais, temporais e textuais. Assinale a alternativa que apresenta o emprego correto desses pronomes:
A) O diretor de TI pediu este documento que está com você na sala de reuniões ao lado.
B) Esse projeto que finalizei no ano de 1998 foi muito elogiado pela equipe técnica.
C) Aquele relatório que você está lendo agora contém inconsistências de dados cadastrais.
D) Esta ferramenta que tenho em mãos é excelente para monitorar a rede do tribunal.
E) Espero que este ano de 2010 seja produtivo para as atividades do Poder Judiciário.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. 'Esta' é usado para o que está perto de quem fala (primeira pessoa). 'Esse' é para o que está perto de quem ouve (segunda pessoa) ou passado recente, e 'aquele' para o que está distante de ambos ou passado remoto. O uso de 'Esta' para a ferramenta que a pessoa segura está correto.
</details>

---

### Questão 33 (FCC)
O pronome relativo 'cujo' possui regras de concordância e emprego muito específicas exigidas pela banca FCC. Assinale a frase que respeita integralmente a norma-padrão no uso desse pronome:
A) A comarca de justiça cujo a acessibilidade física é inadequada passará por reformas.
B) O analista de requisitos, cujo o relatório de elicitação foi entregue, pediu demissão.
C) Este é o servidor de banco de dados cujas informações técnicas de acesso foram alteradas.
D) Aquele é o coordenador do comitê de segurança de cujo eu te falei ontem à noite.
E) Esta é a linguagem de programação de cuja os desenvolvedores mais gostam de programar.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. 'Cujo' concorda em gênero e número com o termo subsequente (coisa possuída: 'cujas informações') e rejeita artigo subsequente ('cujo o' está incorreto). Também exige preposição caso a regência verbal a demande (quem fala, fala 'de algo' -> 'de que falei', e não 'de cujo falei'). A alternativa C está correta.
</details>

---

### Questão 34 (FCC)
No que tange à substituição de termos das orações por pronomes oblíquos átonos, assinale a redação correta segundo a regência e colocação pronominal:
A) O diretor de TI enviou os e-mails aos analistas. / O diretor de TI enviou-lhes aos analistas.
B) Os técnicos instalaram os patches de segurança no servidor. / Os técnicos instalaram-nos no servidor.
C) A assessoria analisará os contratos da licitação de rede. / A assessoria analisar-lhes-á com calma.
D) Nós encontramos as falhas graves na base de dados. / Nós encontramo-las na base de dados.
E) O comitê propôs a mudança de escopo na reunião. / O comitê propôs-la com argumentos sólidos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. Na frase 'instalaram os patches', o objeto direto 'os patches' termina em som nasal, o que exige a transformação do pronome 'os' em 'nos' -> 'instalaram-nos'. Em D, 'encontramos' termina em -s, que cai ao se associar a 'as', virando 'encontramo-las' (mas há próclise atrativa por 'Nós', o que tornaria correto 'Nós as encontramos'). A alternativa B é plenamente correta.
</details>

---

### Questão 35 (FCC)
O pronome relativo 'onde' deve ser empregado exclusivamente para indicar relação de lugar físico. Assinale a frase em que o uso do pronome relativo 'onde' está gramaticalmente correto:
A) Eles vivenciaram uma época histórica difícil onde os recursos tecnológicos eram escassos.
B) A engenharia de requisitos é uma área complexa onde ocorrem constantes mudanças de escopo.
C) O tribunal passou por uma reestruturação organizacional onde muitos setores foram unificados.
D) A nova política de segurança cibernética onde o uso de tokens é obrigatório gerou debates.
E) Este é o prédio do fórum judicial onde serão realizadas as audiências de conciliação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. 'Onde' deve referir-se apenas a lugares físicos/geográficos (ex: 'prédio do fórum'). Para ideias abstratas, deve-se usar 'em que', 'no qual', 'na qual' etc.
</details>

---

### Questão 36 (FCC)
Na Língua Portuguesa, as classes de palavras modificam-se em termos semânticos e sintáticos a depender do contexto. Na oração *'O analisar das métricas revelou gargalos de desempenho no banco de dados'*, a palavra *'analisar'* classifica-se como:
A) Advérbio de intensidade, modificando o sentido do termo 'métricas' para indicar a profundidade da análise.
B) Verbo em sua forma nominal de infinitivo, exercendo a função sintática de adjunto adverbial de modo.
C) Adjetivo explicativo, qualificando a ação subsequente executada pela equipe de infraestrutura de TI.
D) Conjunção coordenativa explicativa, conectando as orações subordinadas subjetivas do período composto.
E) Substantivo, devido ao processo de derivação imprópria (substantivação) ocasionado pelo artigo antecedente.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. O infinitivo verbal 'analisar' precedido pelo artigo 'O' passa a funcionar como substantivo (substantivação/derivação imprópria).
</details>

---

### Questão 37 (FCC)
O pronome 'se' pode exercer diversas funções sintáticas e morfológicas na oração. Assinale a alternativa em que o 'se' funciona como pronome apassivador (partícula apassivadora):
A) Se todos os testes unitários passarem na homologação, o deploy será autorizado hoje.
B) Precisa-se de novos analistas de infraestrutura de rede para o suporte técnico.
C) O desenvolvedor queixou-se das constantes interrupções na sala de desenvolvimento.
D) Eles arrependeram-se de não terem migrado as bases de dados para o PostgreSQL.
E) Mapearam-se todos os requisitos não funcionais de desempenho no início do projeto.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. Na voz passiva sintética, o verbo transitivo direto ('mapear') concorda com o sujeito paciente ('todos os requisitos não funcionais...'). O 'se' é pronome apassivador. Em B, 'precisar' exige preposição 'de' (VTI), sendo o 'se' índice de indeterminação do sujeito.
</details>

---

### Questão 38 (FCC)
A contração da preposição com pronomes relativos é determinada pela regência do verbo subordinado. Assinale a frase gramaticalmente correta quanto à regência e uso do pronome relativo:
A) O projeto do novo fórum digital em cujo o engenheiro civil trabalhou nele foi aprovado.
B) Estes são os servidores públicos de cujos o diretor de TI solicitou o desligamento físico.
C) Esta é a linguagem de programação com que os analistas de sistemas mais simpatizam nela.
D) Aquele é o banco de dados relacional de cuja integridade física nós dependemos dela.
E) Este é o sistema de controle de processos a cujo desenvolvimento nós nos referimos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. O verbo 'referir-se' exige a preposição 'a' ('referir-se a algo'). Essa preposição deve anteceder o pronome relativo 'cujo' -> 'a cujo desenvolvimento'. Outras opções possuem erros de redundância ('nela', 'dela', 'nele') ou de acoplamento com artigo ('de cujos o').
</details>

---

### Questão 39 (FCC)
As conjunções coordenativas e subordinativas são classes de palavras que estabelecem nexos lógicos no período composto. Na oração *'Embora o sistema apresente boa usabilidade, a lentidão no processamento gerou reclamações dos usuários'*, a conjunção *'Embora'* estabelece relação de:
A) Consequência, apresentando o resultado direto das constantes falhas de infraestrutura de rede corporativa.
B) Condição, estabelecendo uma restrição obrigatória para que a oração principal ocorra no tempo correto.
C) Causa, explicando o motivo pelo qual as reclamações foram registradas pela assessoria de TI do tribunal.
D) Concessão, indicando uma ideia de oposição ou contraste que não impede a realização da oração principal.
E) Conformidade, demonstrando o acordo entre os testes de usabilidade e o desempenho físico dos servidores.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. 'Embora' é uma conjunção subordinativa concessiva típica, expressando um obstáculo que não é suficiente para impedir o fato da oração principal.
</details>

---

### Questão 40 (FCC)
Considere a colocação pronominal em períodos que contêm locuções verbais ou tempos compostos. Assinale a frase correta de acordo com as normas gramaticais vigentes:
A) Os analistas de sistemas deveriam se ter atentado aos prazos de entrega do projeto de TI.
B) Os analistas de sistemas deveriam-se ter atentado aos prazos de entrega do projeto de TI.
C) Os analistas de sistemas deveriam ter-se atentado aos prazos de entrega do projeto de TI.
D) Os analistas de sistemas deveriam ter atentado-se aos prazos de entrega do projeto de TI.
E) Os analistas de sistemas se deveriam ter atentado aos prazos de entrega do projeto de TI.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. Em locuções verbais com infinitivo ou gerúndio (sem palavra atrativa), o pronome pode ser colocado após o auxiliar (com hífen) ou após o principal. Mas em tempos compostos com particípio ('ter atentado'), o pronome não pode vir após o particípio ('atentado-se' é incorreto). O correto é após o auxiliar ter: 'ter-se atentado' ou antes dele. A opção C é a padrão correta.
</details>

---

### Questão 41 (FCC)
O pronome relativo 'quem' refere-se exclusivamente a pessoas ou entes personificados e exige preposição em determinados contextos. Assinale a frase gramaticalmente correta:
A) O engenheiro civil a quem o tribunal contratou para as reformas apresentou as plantas físicas.
B) Este é o analista de banco de dados quem resolveu a falha crítica de integridade referencial.
C) Aquele é o magistrado de quem o relatório de produtividade foi solicitado pelo comitê de TI.
D) Os técnicos a quem nós nos dirigimos no setor de infraestrutura de redes foram atenciosos.
E) Os usuários quem reclamaram da usabilidade do sistema judicial de prazos foram ouvidos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. O pronome 'quem' exige preposição quando é objeto ('a quem nos dirigimos'). O verbo 'dirigir-se' exige a preposição 'a' ('dirigir-se a alguém'). Portanto, 'a quem nos dirigimos' está correto. Em B e E, falta preposição ou o pronome relativo adequado seria 'que' ou 'o qual'.
</details>

---

### Questão 42 (FCC)
Advérbios são classes de palavras que modificam verbos, adjetivos ou outros advérbios. Na frase *'O banco de dados do tribunal respondeu extremamente rápido às consultas de auditoria'*, a palavra *'extremamente'* classifica-se como advérbio de:
A) Lugar, situando espacialmente as consultas executadas pelos usuários cadastrados no tribunal de justiça.
B) Modo, descrevendo a forma como as tabelas relacionais físicas do banco de dados foram estruturadas.
C) Tempo, indicando o momento exato em que a equipe de infraestrutura de TI realizou as medições.
D) Intensidade, modificando o advérbio 'rápido' para intensificar a velocidade de resposta do sistema.
E) Conformidade, expressando o alinhamento das buscas SQL com as políticas internas do órgão público.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. 'Extremamente' é um advérbio de intensidade que modifica o advérbio de modo 'rápido', acentuando sua força semântica.
</details>

---

### Questão 43 (FCC)
Em relação ao uso de pronomes de tratamento em comunicações oficiais no tribunal, a norma culta exige concordância verbal e pronominal específica. Assinale a alternativa correta:
A) Vossa Excelência deve apresentar seus relatórios de produtividade técnica na próxima reunião de conselho.
B) Vossa Excelência deve apresentar vossos relatórios de produtividade técnica na próxima reunião de conselho.
C) Vossa Senhoria deveis comparecer à assessoria jurídica com vossos assessores de segurança de redes.
D) Sua Excelência (referindo-se à pessoa com quem se fala) determinou a abertura de nova licitação pública.
E) Vossa Magnificência deveis assinar os termos de cooperação técnica com vossas próprias mãos ontem.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. Pronomes de tratamento exigem a concordância com a terceira pessoa (verbal e pronominal: 'deve apresentar seus relatórios'), mesmo se referindo à segunda pessoa. 'Vossa' é usado para falar com a pessoa, e 'Sua' para falar sobre a pessoa. A alternativa A está correta.
</details>

---

### Questão 44 (FCC)
Assinale a frase em que o pronome oblíquo exerce papel sintático de adjunto adnominal (valor possessivo):
A) O analista de suporte entregou-lhe os relatórios de erros gerados pelo banco de dados relacional.
B) A diretoria de TI comunicou-lhe as novas diretrizes de segurança adotadas nas redes locais.
C) O vento forte levou-lhe o chapéu de feltro enquanto caminhava pelo pátio externo do tribunal.
D) Ninguém lhe disse que as consultas SQL com ROWNUM deveriam ser revisadas na homologação.
E) O coordenador do projeto permitiu-lhe acessar o servidor de homologação durante os testes.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. Em 'levou-lhe o chapéu', o pronome 'lhe' equivale a 'seu chapéu' (levou o seu chapéu), exercendo a função sintática de adjunto adnominal (ideia de posse vinculada ao substantivo). Nas outras opções, o 'lhe' funciona como objeto indireto.
</details>

---

### Questão 45 (FCC)
Preposições são palavras invariáveis que ligam dois termos de uma oração. Na frase *"O sistema foi desenvolvido sob rígidas normas de segurança cibernética"*, a preposição *"sob"* indica uma relação semântica de:
A) Lugar físico ou espacial, situando geograficamente o servidor de banco de dados nos blocos do datacenter.
B) Oposição ou contrariedade, demonstrando que o sistema violou as regras de segurança homologadas no órgão.
C) Tempo ou duração, limitando o período em que a equipe de suporte pôde atuar na correção de bugs de rede.
D) Subordinação ou conformidade, expressando que o desenvolvimento seguiu as diretrizes técnicas definidas.
E) Causa ou motivo, explicando a razão pela qual as vulnerabilidades foram exploradas por agentes externos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A preposição 'sob' indica subordinação, dependência ou conformidade em relação a algo (sob normas = em conformidade com as normas).
</details>

---
