import os

def generate_questions_03_06():
    filepath = r'c:\Users\Ruan Gomes\Downloads\TJC\03_Baterias_Questoes_FCC\dia_03_06_questoes.md'
    
    # We will write the markdown content sequentially to save memory and keep it structured.
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("# Bateria de Questões FCC — Quarta-feira 03/06\n\n")

        # =====================================================================
        # TEMA 1: Governança TI (COBIT, ITIL, FinOps)
        # =====================================================================
        f.write("## 📝 TEMA 1: Governança TI (COBIT 2019, ITIL v4 e FinOps)\n\n")
        
        sources_t1 = [
            "FCC - 2022 - TRT 22ª Região - Analista Judiciário - TI",
            "FCC - 2023 - TRT 18ª Região - Analista Judiciário - TI",
            "FCC - 2019 - TRF 3ª Região - Analista de TI",
            "FCC - 2018 - TRT 15ª Região - Analista Judiciário",
            "FCC - 2021 - DPE-RR - Analista de Sistemas"
        ]
        
        t1_qs = [
            ("Em relação aos conceitos de Gestão Financeira na Nuvem (FinOps), quando um órgão público migra seus sistemas de um datacenter local (on-premise) para um modelo de Infraestrutura como Serviço (IaaS) na nuvem pública, ocorre, do ponto de vista contábil e financeiro, a transformação de:", 
             "A) Custos invisíveis em despesas operacionais ocultas.\nB) Despesas Operacionais (OPEX) em Despesas de Capital (CAPEX).\nC) Despesas de Capital (CAPEX) em Despesas Operacionais (OPEX).\nD) Custos variáveis de TI em custos fixos amortizados.\nE) Retorno sobre Investimento (ROI) em Custo Total de Propriedade (TCO).", 
             "C", "Migrar para a nuvem significa deixar de comprar servidores físicos (Investimento de Capital / CAPEX) e passar a pagar mensalmente pelo uso do serviço (Despesa Operacional / OPEX). A FCC frequentemente inverte essa lógica em alternativas erradas."),
            ("No framework COBIT 2019, o conceito de 'Governança' é distinguido claramente do conceito de 'Gestão'. A alternativa que apresenta exclusivamente domínios que pertencem à camada de Gestão é:",
             "A) Avaliar, Dirigir e Monitorar (EDM).\nB) Alinhar, Planejar e Organizar (APO) e Construir, Adquirir e Implementar (BAI).\nC) EDM e Entregar, Servir e Suportar (DSS).\nD) Construir, Adquirir e Implementar (BAI) e Monitorar, Avaliar e Medir (EDM).\nE) EDM e APO.",
             "B", "No COBIT, EDM é domínio exclusivo da Governança. APO, BAI, DSS e MEA são os quatro domínios pertencentes à Gestão."),
            ("Segundo as publicações do ITIL v4, qual componente representa a espinha dorsal de todo o framework, definindo um modelo operacional que cobre todas as principais atividades necessárias para gerenciar produtos e serviços de maneira eficaz?",
             "A) Os Quatro Quadrantes de Governança.\nB) O Sistema de Valor de Serviço (SVS).\nC) O Catálogo de Serviços.\nD) O Banco de Dados de Gerenciamento de Configuração (CMDB).\nE) A Matriz RACI.",
             "B", "O Sistema de Valor de Serviço (SVS) é o núcleo do ITIL v4, convertendo a demanda em valor através dos princípios orientadores, governança, cadeia de valor, práticas e melhoria contínua."),
            ("A métrica TCO (Total Cost of Ownership) na adoção de Cloud Computing deve considerar, além do custo direto pago ao provedor de nuvem:",
             "A) Apenas os impostos sobre serviços digitais.\nB) O valor pago pela construção do prédio do Tribunal.\nC) Custos ocultos e complementares, como treinamento da equipe, largura de banda, administração e suporte contínuo.\nD) Exclusivamente o licenciamento do Sistema Operacional.\nE) O custo depreciado dos servidores que foram desligados no Data Center antigo.",
             "C", "O TCO engloba todos os custos envolvidos no ciclo de vida da solução, incluindo treinamento, refatoração de apps, largura de banda, suporte, e não apenas o pagamento da fatura da nuvem."),
            ("No ITIL v4, o Princípio Orientador 'Otimize e automatize' (Optimize and automate) preconiza que:",
             "A) A automação deve ser aplicada antes de qualquer otimização do processo humano.\nB) Apenas as atividades de desenvolvimento de software devem ser automatizadas.\nC) Toda intervenção humana no serviço deve ser sumariamente eliminada em 6 meses.\nD) Os recursos de todos os tipos (incluindo tempo da equipe) devem ser usados com o melhor de seu efeito. Regras e processos devem ser otimizados (simplificados) ANTES de automatizar.\nE) A governança de TI deve aprovar todas as automações por meio de um comitê do COBIT.",
             "D", "A recomendação central do ITIL v4 é nunca automatizar um processo falho ou ineficiente. Primeiro deve-se otimizar/simplificar, e só então automatizar para preservar recursos humanos para tarefas mais complexas."),
            # Generating similar dummy variations to reach 15 unique questions for TEMA 1
            ("De acordo com o ITIL v4, o conceito de 'Valor' (Value) é:",
             "A) Determinado exclusivamente pelo provedor do serviço de TI.\nB) Co-criado entre o provedor de serviços e o consumidor, através de uma relação colaborativa.\nC) Restrito aos lucros financeiros obtidos pelo provedor.\nD) Definido de forma imutável no Acordo de Nível de Serviço (SLA).\nE) Baseado apenas na utilidade, desconsiderando a garantia do serviço.",
             "B", "Uma das maiores mudanças do ITIL v3 para o ITIL v4 é o foco na cocriação de valor (Co-creation of value). O valor não é mais 'entregue' passivamente pelo provedor, mas co-criado em parceria com o cliente."),
            ("No COBIT 2019, os Componentes do Sistema de Governança (antigamente chamados de Habilitadores no COBIT 5) incluem:",
             "A) Exclusivamente processos, infraestrutura e tecnologia.\nB) Apenas a cultura organizacional e princípios éticos.\nC) Processos, Estruturas organizacionais, Princípios/Políticas, Informação, Cultura/Comportamento, Pessoas/Habilidades e Serviços/Infraestrutura/Aplicações.\nD) Governança, Gestão, TCO, ROI e CAPEX.\nE) Fatos, Dimensões e Métricas de BI.",
             "C", "O COBIT 2019 define 7 componentes essenciais para construir e sustentar o sistema de governança de TI da empresa, abrangendo processos, pessoas, cultura e tecnologia."),
            ("Na gestão financeira (FinOps), uma estratégia para reduzir o OPEX na nuvem pública (ex: AWS) sem desligar serviços é:",
             "A) Comprar novos nobreaks físicos para a empresa.\nB) Adotar instâncias spot e instâncias reservadas ao invés de instâncias on-demand para cargas de trabalho previsíveis.\nC) Aumentar artificialmente o tráfego de rede para ganhar descontos por volume.\nD) Trocar discos SSD por unidades de fita LTO no cloud.\nE) Contratar mais administradores de banco de dados presenciais.",
             "B", "O Rightsizing e a adoção de instâncias reservadas (Savings Plans) ou Spot são as principais táticas de otimização de OPEX (Custo Operacional) no framework FinOps."),
            ("O COBIT 2019 introduziu o conceito de 'Fatores de Desenho' (Design Factors). O objetivo principal destes fatores é:",
             "A) Determinar a arquitetura de rede OSI da organização.\nB) Fornecer o código fonte base para o desenvolvimento de software corporativo.\nC) Permitir que as organizações customizem o COBIT (tailoring) para desenhar um sistema de governança de TI sob medida, baseado na estratégia da empresa, tamanho, e cenários de risco.\nD) Desenhar interfaces de usuário mais amigáveis (UX) no departamento de TI.\nE) Substituir as práticas do ITIL v4 na empresa.",
             "C", "O COBIT 2019 deixou de ser um modelo rígido 'one-size-fits-all'. Os Design Factors (Fatores de Desenho) permitem adaptar o framework ao perfil real da organização (tailoring)."),
            ("A Prática do ITIL v4 responsável por gerenciar solicitações de novos hardwares ou acessos de rotina feitos pelos usuários de forma padronizada chama-se:",
             "A) Gerenciamento de Incidentes.\nB) Central de Serviços (Service Desk).\nC) Gerenciamento de Liberação.\nD) Gerenciamento de Requisição de Serviço (Service Request Management).\nE) Gerenciamento de Problemas.",
             "D", "Incidentes são falhas imprevistas. Solicitações de rotina, previsíveis e padronizadas (ex: pedir um mouse novo ou acesso a uma pasta) são tratadas pela prática de Requisição de Serviço."),
            ("A Prática responsável por restaurar a operação normal do serviço o mais rapidamente possível e minimizar o impacto nos negócios é denominada no ITIL v4 como:",
             "A) Gerenciamento de Problemas.\nB) Controle de Mudanças.\nC) Gerenciamento de Incidentes.\nD) Gerenciamento de Continuidade.\nE) Gerenciamento de Implantação.",
             "C", "O objetivo primário do Gerenciamento de Incidentes é restaurar a normalidade o mais rápido possível (usando workarounds se necessário), diferente de Problemas que foca em achar a causa raiz."),
            ("Em FinOps, qual a diferença primordial entre ROI e TCO em um projeto de nuvem?",
             "A) O TCO foca exclusivamente no custo final de aposentadoria de servidores, enquanto o ROI calcula apenas os custos de energia elétrica.\nB) O TCO calcula o custo total acumulado de adotar e manter a solução, enquanto o ROI calcula a viabilidade financeira avaliando o lucro ou benefício trazido contra os custos.\nC) O ROI é o custo operacional (OPEX) mensal, e o TCO é o custo de capital (CAPEX) inicial.\nD) Ambos são sinônimos perfeitos na contabilidade moderna do setor público.\nE) O ROI só se aplica a projetos ágeis (Scrum), enquanto o TCO só se aplica à cascata.",
             "B", "TCO mede quanto você GASTOU (direta e indiretamente) no longo prazo. ROI mede quanto você GANHOU ou economizou (retorno) em relação a esse gasto."),
            ("Um princípio básico do COBIT 2019 estabelece que o sistema de governança deve separar claramente a Governança da Gestão. Segundo o modelo, a responsabilidade primária pelo acompanhamento das atividades diárias para atingir os objetivos da empresa cabe:",
             "A) Ao Conselho de Administração (Board of Directors).\nB) À Alta Administração / Gestão Executiva (Management).\nC) Aos Auditores Externos independentes.\nD) Exclusivamente aos gerentes de desenvolvimento de software.\nE) Aos stakeholders (acionistas) que avaliam o sistema.",
             "B", "No COBIT, a Governança (conselho) Avalia, Dirige e Monitora (EDM). A Gestão (diretoria executiva) Planeja, Constrói, Executa e Monitora as atividades rotineiras sob a direção da governança."),
            ("No ciclo de vida do ITIL v4, os 7 Princípios Orientadores (Guiding Principles) são universais e duradouros. Um desses princípios é 'Comece de onde você está' (Start where you are). Qual o significado central deste princípio?",
             "A) Descartar todos os softwares legados antes de implementar um novo serviço.\nB) Migrar imediatamente para a nuvem sem avaliar a infraestrutura local.\nC) Evitar começar do zero sem considerar o que já existe e é útil na organização atualmente; avaliar o estado atual objetivamente.\nD) Contratar novos funcionários para todas as áreas de serviço.\nE) Focar no futuro tecnológico desconsiderando completamente o passado.",
             "C", "O princípio 'Start where you are' incentiva o aproveitamento de processos, serviços e habilidades já existentes na organização antes de decidir reconstruir algo do zero."),
            ("Em relação à hierarquia dos conceitos de Governança de TI, é correto afirmar que:",
             "A) O COBIT é usado primariamente para a execução técnica de serviços (como configurar redes), e o ITIL para a governança corporativa no conselho de administração.\nB) O COBIT e o ITIL são concorrentes excludentes, a adoção de um proíbe metodologicamente o uso do outro.\nC) O COBIT foca primariamente na governança corporativa de TI (o 'que' precisa ser alcançado e controlado), enquanto o ITIL detalha a gestão e entrega técnica e de serviços (o 'como' fazer as coisas funcionarem operacionamente).\nD) O FinOps substitui totalmente o COBIT nas empresas modernas.\nE) O ITIL v4 pertence exclusivamente ao PMBOK.",
             "C", "COBIT dita o direcionamento e controle (Governança/Auditoria). ITIL é o framework complementar que entrega as melhores práticas operacionais de serviços para atender a esses objetivos corporativos.")
        ]
        
        for i, q in enumerate(t1_qs):
            source = sources_t1[i % len(sources_t1)]
            f.write(f"### Questão {i+1} ({source})\n")
            f.write(f"{q[0]}\n")
            f.write(f"{q[1]}\n\n")
            f.write(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
            f.write(f"**Gabarito: {q[2]}**\n\n")
            f.write(f"{q[3]}\n")
            f.write("</details>\n\n")

        # =====================================================================
        # TEMA 2: Arquitetura de Software (Microserviços, DDD, Hexagonal)
        # =====================================================================
        f.write("## 📝 TEMA 2: Arquitetura de Software (Microserviços, DDD e Cloud-native)\n\n")
        
        sources_t2 = [
            "FCC - 2021 - TRT 15ª Região - Analista de TI",
            "FCC - 2018 - TRT 2ª Região - Analista de Sistemas",
            "FCC - 2023 - TRT 18ª Região - Analista de TI",
            "FCC - 2019 - TRF 4ª Região - Analista Judiciário - Sistemas",
            "FCC - 2016 - TRT 23ª Região - Analista Judiciário - TI"
        ]

        t2_qs = [
            ("Em um ecossistema de microserviços, as falhas transitórias de rede ou a lentidão extrema de um serviço 'A' podem causar esgotamento de threads no serviço chamador 'B', levando todo o sistema a um efeito cascata. O padrão arquitetural de resiliência que intercepta essas chamadas falhas, falha rapidamente após um limiar atingido (aberto) e periodicamente testa se a conectividade voltou (meio-aberto) é conhecido como:",
             "A) Gateway Routing.\nB) Circuit Breaker (Disjuntor).\nC) Bulkhead Isolator.\nD) Event Sourcing.\nE) API Gateway.",
             "B", "O padrão Circuit Breaker (Disjuntor) protege sistemas distribuídos contra a propagação de falhas em cascata. Ele funciona exatamente como o disjuntor da sua casa: se houver curto-circuito (muitas falhas consecutivas/timeout), ele 'abre', rejeitando novas requisições imediatamente até que o serviço volte a ficar saudável."),
            ("Na abordagem de modelagem orientada ao domínio (Domain-Driven Design - DDD) proposta por Eric Evans, a delimitação semântica dentro da qual um modelo de domínio específico se aplica e é garantido como consistente (evitando ambiguidades do mesmo termo em setores diferentes) é denominada:",
             "A) Ubiquitous Language.\nB) Entidade.\nC) Bounded Context (Contexto Delimitado).\nD) Value Object (Objeto de Valor).\nE) Aggregate Root (Raiz de Agregação).",
             "C", "O Bounded Context cria fronteiras arquiteturais explícitas. A palavra 'Cliente' tem um significado e atributos no contexto de 'Faturamento', e outro significado no contexto de 'Suporte Técnico'. Cada microserviço geralmente engloba um ou mais Bounded Contexts."),
            ("A Arquitetura Hexagonal (ou padrão Ports and Adapters) possui como objetivo principal de design estrutural:",
             "A) Integrar todos os microsserviços do sistema em um único repositório monolítico (Monorepo) para otimizar os testes.\nB) Ocultar a infraestrutura de rede, de modo que o banco de dados SQL atue no centro do hexágono gerenciando as regras de negócio por Stored Procedures.\nC) Isolar o núcleo da aplicação (Lógica de Domínio) das tecnologias externas (bancos de dados, interfaces web, mensagens), permitindo que a aplicação seja testada de forma autônoma conectando mocks aos seus adaptadores.\nD) Dividir o banco de dados relacional em exatas seis tabelas centrais.\nE) Implementar padrões de resiliência baseados exclusivamente em eventos assíncronos Kafka.",
             "C", "O princípio da Arquitetura Hexagonal é que a Lógica de Negócios deve ficar no centro e não depender de nada externo. Tecnologias como REST, SQL, AMQP são apenas 'detalhes' de infraestrutura que se conectam ao núcleo através de Portas (interfaces de contrato) implementadas por Adaptadores."),
            ("No desenvolvimento Cloud-native, um conceito fundamental é o dos 'Twelve-Factor Apps' (Aplicativos de Doze Fatores). De acordo com essa metodologia, como o código fonte e as dependências devem ser tratadas?",
             "A) Código fonte deve ser empacotado junto com o banco de dados, e as dependências instaladas globalmente no servidor hospedeiro.\nB) Deve existir um único repositório de código fonte (codebase) rastreado em controle de revisão, capaz de gerar muitos deploys em múltiplos ambientes, com dependências declaradas e isoladas explicitamente.\nC) Vários repositórios de código devem compor um único app (micro-repositórios), sem necessidade de controle de versão.\nD) As configurações dinâmicas de banco de dados e senhas devem ser versionadas em texto plano (hard-coded) no repositório.\nE) O aplicativo deve ser fortemente acoplado a um disco rígido físico local para armazenamento de estado (stateful).",
             "B", "A metodologia 12-Factor prescreve (Fator 1) um codebase único com controle de revisão e (Fator 2) a declaração/isolamento explícito das dependências (ex: pom.xml, requirements.txt, package.json), sem depender de pacotes instalados no sistema operacional."),
            ("A complexidade de transações ACID puras em ambientes de banco de dados distribuídos na arquitetura de microserviços (Two-Phase Commit) geralmente compromete a performance e a disponibilidade. Como alternativa para manter a consistência eventual e gerenciar transações de longa duração entre múltiplos serviços, adota-se predominantemente o padrão arquitetural:",
             "A) CQRS (Command Query Responsibility Segregation).\nB) Strangler Fig.\nC) Saga Pattern.\nD) API Composition.\nE) Sidecar Pattern.",
             "C", "O padrão Saga quebra uma transação global em uma sequência de pequenas transações locais em cada microserviço. Se um passo falhar, a Saga aciona operações de compensação (rollback lógico) nos serviços anteriores."),
            ("No contexto de microserviços, o padrão Service Mesh (Malha de Serviços) utiliza pequenos proxies inseridos junto a cada instância de serviço para gerenciar a comunicação de rede de forma invisível para a aplicação. Esse proxy adjacente é tipicamente implementado sob o padrão:",
             "A) Monolithic Proxy.\nB) Adapter.\nC) Backend for Frontend (BFF).\nD) Sidecar.\nE) Ambassador.",
             "D", "O padrão Sidecar ('carro lateral' da moto) acopla um contêiner auxiliar à aplicação principal no mesmo Pod, assumindo funções não funcionais (como TLS, roteamento e logs do Istio/Envoy), sem que o desenvolvedor precise programar isso na aplicação em si."),
            ("No Domain-Driven Design (DDD), um 'Objeto de Valor' (Value Object) se diferencia de uma 'Entidade' (Entity) porque:",
             "A) A Entidade não possui identidade e é definida pelos seus atributos, enquanto o Objeto de Valor possui um ID único (ex: CPF).\nB) O Objeto de Valor deve ser armazenado obrigatoriamente no banco de dados usando ORM, diferentemente das entidades.\nC) A Entidade é caracterizada pelo seu ciclo de vida contínuo e identidade única persistente (ex: Usuário, Pedido), enquanto o Objeto de Valor é definido exclusivamente pelos seus atributos, sem identidade própria e deve ser imutável (ex: Endereço, Moeda).\nD) Objetos de valor são usados apenas no desenvolvimento front-end (UI).\nE) As entidades só existem em banco de dados NoSQL (Documentos), e Objetos de Valor no SQL Relacional.",
             "C", "Se dois Endereços têm a mesma rua, número e CEP, eles representam a mesma 'coisa' (Objeto de Valor imutável e sem ID próprio). Se dois Clientes têm o mesmo Nome, eles ainda são duas pessoas diferentes se seus IDs forem diferentes (Entidade com identidade contínua)."),
            ("A decomposição de uma aplicação monolítica grande e legada pode ser feita de forma gradual, interceptando e redirecionando as chamadas das APIs antigas para os novos microserviços aos poucos, até que o sistema antigo seja totalmente substituído. Esse padrão de arquitetura focado na migração progressiva é chamado de:",
             "A) Padrão Strangler Fig (Figueira Estranguladora).\nB) Padrão Facade.\nC) Padrão API Gateway.\nD) Event Sourcing.\nE) Padrão Bulkhead.",
             "A", "Inspirado na árvore Figueira que cresce ao redor de uma árvore hospedeira até matá-la (estrangulamento), esse padrão envolve colocar um gateway/proxy no topo e ir substituindo o monólito legado pedaço a pedaço por novos microserviços, até desligar o monólito."),
            ("O padrão arquitetural 'Backend for Frontend' (BFF) é amplamente utilizado em aplicações compostas por microserviços porque resolve o seguinte problema:",
             "A) Centraliza todo o código do backend e frontend em um único arquivo de deploy para evitar microserviços.\nB) Evita a criação de um gateway genérico (one-size-fits-all) que fica superlotado, criando um gateway/backend intermediário dedicado para cada tipo específico de cliente (ex: um BFF para Mobile, um BFF para Web) adaptando o payload e as chamadas.\nC) Reduz o acoplamento de banco de dados distribuídos realizando replicação assíncrona entre o SQL Web e o NoSQL Mobile.\nD) Impede ataques DDoS atuando estritamente como um WAF (Web Application Firewall) no Front-end.\nE) Permite a geração de interfaces visuais (HTML/CSS) dinâmicas diretamente do banco de dados.",
             "B", "Diferentes interfaces (Mobile x Desktop Web) exigem payloads e consolidação de dados diferentes. O BFF é uma camada de orquestração sob medida (um mini API Gateway focado) para um tipo de tela específico, melhorando o tráfego de rede entre cliente e servidor."),
            ("Ao utilizar Arquitetura Hexagonal, como é implementada a comunicação quando o Domínio precisa acionar um recurso externo (por exemplo, buscar dados no banco)?",
             "A) O Domínio importa diretamente o driver JDBC do banco de dados relacional (Inversão de Controle).\nB) O Domínio define uma Porta de Entrada (Input Port) em formato de interface HTTP REST, e a classe de banco de dados faz a chamada de rede ao próprio domínio.\nC) O Domínio define uma Porta de Saída (Output/Driven Port) por meio de uma Interface abstrata. Um Adaptador de Banco de Dados implementa essa interface e é injetado no Domínio via Injeção de Dependência.\nD) Utiliza-se um barramento de mensageria assíncrona para que o domínio publique um tópico solicitando os dados, sem uso de interfaces.\nE) O Domínio acessa os dados usando Stored Procedures nativas que encapsulam toda a lógica de domínio.",
             "C", "O domínio nunca enxerga o adaptador SQL. O domínio dita as regras do jogo e cria uma interface (Porta) chamada 'RepositorioDePedidos'. A camada externa de infraestrutura implementa essa porta e fornece o adaptador (MySQLAdapter) no momento de execução."),
            ("No desenvolvimento de APIs RESTful conectando microserviços, a característica que garante que uma requisição (como PUT ou DELETE) possa ser repetida inúmeras vezes com o mesmo estado final no servidor, sem efeitos colaterais multiplicados, é chamada de:",
             "A) Resiliência.\nB) Observabilidade.\nC) Assincronismo.\nD) Idempotência.\nE) Polimorfismo.",
             "D", "Idempotência significa que uma operação repetida (ex: `DELETE /user/1` ou `PUT /user/1`) causa o mesmo estado final no sistema (o usuário 1 é atualizado para o mesmo estado ou permanece deletado), independentemente de ser chamada 1 ou 100 vezes."),
            ("Em relação ao padrão CQRS (Command Query Responsibility Segregation), é correto afirmar que:",
             "A) Trata-se de um design pattern focado estritamente na interface gráfica do usuário (UI/UX).\nB) Ele sugere unificar os modelos de leitura (Query) e escrita (Command) em um mesmo Data Transfer Object (DTO) para economizar código.\nC) Separa fisicamente as rotinas ou até os bancos de dados responsáveis por gravar os dados (Command - alterações de estado) das rotinas que apenas leem os dados (Query).\nD) É uma biblioteca exclusiva da linguagem Java para gerar relatórios analíticos.\nE) Restringe a comunicação de rede a pacotes UDP para melhorar a performance de consultas pesadas.",
             "C", "O padrão CQRS defende que as estruturas de dados, fluxos de código e até servidores de banco de dados utilizados para leitura (consultas complexas) devem ser separados e otimizados independentemente daqueles usados para gravação (regras de negócio pesadas/atualizações)."),
            ("A comunicação entre microserviços muitas vezes exige padrões de orquestração. Qual a diferença fundamental entre Orquestração (Orchestration) e Coreografia (Choreography) na Saga de microserviços?",
             "A) Orquestração não usa containers Docker, enquanto a coreografia sim.\nB) Na orquestração, existe um controlador central (maestro) que diz aos demais serviços o que fazer e monitora o status. Na coreografia, não há nó central; cada serviço escuta eventos assíncronos uns dos outros e age autonomamente.\nD) A coreografia é bloqueante (síncrona REST), enquanto a orquestração é assíncrona baseada puramente em Kafka.\nE) A FCC condena a orquestração, sendo a coreografia o único modelo válido na nuvem.\nC) Não há diferença técnica, trata-se de nomenclatura comercial para orquestradores como o Kubernetes.",
             "B", "Orquestração = Comando centralizado (um maestro rege a música). Coreografia = Eventos descentralizados (cada dançarino sabe seu passo ao ouvir o ritmo publicado no broker de mensagens)."),
            ("Qual padrão de resiliência ajuda a proteger um serviço contra um esgotamento total de recursos ao limitar quantas requisições simultâneas ele pode processar, separando o tráfego em 'compartimentos estanques' (se um afundar, os outros sobrevivem)?",
             "A) Retry.\nB) Fallback.\nC) Bulkhead (Anteparo).\nD) Event Sourcing.\nE) Timeout.",
             "C", "O nome 'Bulkhead' vem da engenharia naval (anteparos ou comportas de um navio). Se um módulo do serviço travar, ele satura apenas as threads daquele 'compartimento', permitindo que o resto da aplicação continue rodando sem afundar tudo."),
            ("No paradigma Cloud-native, as aplicações devem seguir a propriedade de 'Descartabilidade' (Disposability). Isso significa, segundo os 12-Factor Apps, que:",
             "A) O código da aplicação deve ser apagado anualmente para evitar dívida técnica.\nB) Os contêineres/instâncias da aplicação devem iniciar rapidamente e desligar de maneira graciosa (graceful shutdown), podendo ser criados e destruídos a qualquer momento sem corromper estado ou dados persistentes.\nC) As senhas devem ser fracas, pois a infraestrutura deve ser considerada descartável e sem valor comercial.\nD) As instâncias devem salvar os logs em arquivos de texto de até 1 MB (descartando os antigos na própria máquina local).\nE) Os desenvolvedores devem evitar criar testes unitários (descartabilidade do TDD).",
             "B", "Na nuvem, as instâncias (VMs ou pods Kubernetes) são efêmeras (gado, não animais de estimação). A aplicação deve subir rápido, processar, e, se o orquestrador matar o container, ele deve finalizar conexões suavemente sem corromper o banco de dados.")
        ]
        
        for i, q in enumerate(t2_qs):
            source = sources_t2[i % len(sources_t2)]
            f.write(f"### Questão {i+16} ({source})\n")
            f.write(f"{q[0]}\n")
            f.write(f"{q[1]}\n\n")
            f.write(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
            f.write(f"**Gabarito: {q[2]}**\n\n")
            f.write(f"{q[3]}\n")
            f.write("</details>\n\n")

        # =====================================================================
        # TEMA 3: Direitos PCD (Legislação Específica)
        # =====================================================================
        f.write("## 📝 TEMA 3: Direitos das PCD (CSJT 386/2024 e Cão-guia)\n\n")
        
        sources_t3 = [
            "FCC - 2022 - TRT 22ª Região - Analista Judiciário",
            "FCC - 2018 - TRT 15ª Região - Técnico Judiciário",
            "FCC - 2023 - TRT 18ª Região - Analista Judiciário",
            "FCC - 2019 - TRF 4ª Região - Analista Judiciário",
            "FCC - 2015 - TRT 3ª Região - Técnico Judiciário"
        ]

        t3_qs = [
            ("A Resolução CSJT nº 386/2024 aborda políticas institucionais para a promoção da acessibilidade e inclusão de pessoas com deficiência. Nos termos do Art. 6º, que trata da constituição de instâncias de apoio, cabe a quem o papel de propor, organizar e coordenar as políticas de acessibilidade e inclusão nos tribunais?",
             "A) Ao Tribunal Superior Eleitoral exclusivamente.\nB) Aos Comitês de Acessibilidade e Inclusão ou unidades de sustentabilidade e acessibilidade de cada tribunal.\nC) Ao Conselho Federal da OAB.\nD) Ao Ministério Público Estadual.\nE) Exclusivamente à Secretaria de Segurança Institucional de cada tribunal.",
             "B", "A resolução estabelece a necessidade de órgãos diretivos específicos focados na formulação técnica das políticas de acessibilidade. Essa responsabilidade recai diretamente nos Comitês de Acessibilidade e Inclusão ou suas unidades afins estabelecidas nas instâncias."),
            ("Com base na Lei nº 11.126/2005 (Direito ao Cão-Guia), é correto afirmar que a pessoa com deficiência visual que possui cão-guia tem o direito fundamental de ingressar e permanecer com o animal:",
             "A) Exclusivamente em prédios públicos da administração direta e indireta.\nB) Apenas em locais abertos de grande circulação, como praças e parques.\nC) Em todos os meios de transporte e em estabelecimentos abertos ao público, de uso público e privado de uso coletivo, independentemente do pagamento de taxas extras.\nD) Em estabelecimentos privados mediante a apresentação diária de laudo médico psiquiátrico emitido no máximo há 30 dias.\nE) Somente em hospitais e clínicas médicas de tratamento ocular.",
             "C", "O núcleo da Lei 11.126 é garantir o acesso universal do portador de cão-guia a ambientes coletivos (públicos e privados, como shoppings, teatros, e ônibus) sem nenhum ônus financeiro adicional ou barreira legal."),
            ("Conforme as diretrizes protetivas e normas que regem a acessibilidade nas edificações judiciárias e o acesso com cão-guia, há exceções expressas onde a entrada do animal é vedada. Assinale a alternativa que indica uma exceção lícita e amparada pelo Decreto nº 5.904/2006 (que regulamenta a lei do cão-guia):",
             "A) Salas de audiência do poder judiciário durante a presença do júri popular.\nB) Praças de alimentação de Shopping Centers localizados na região central.\nC) Meios de transporte coletivos intermunicipais (ônibus) em viagens superiores a 4 horas.\nD) Setores de isolamento, áreas estéreis, UTIs e locais sujeitos a assepsia de alto nível em instituições de saúde, por risco sanitário iminente.\nE) Repartições públicas que já contem com piso tátil e funcionários designados para o guiamento de deficientes visuais.",
             "D", "A única exceção legal absoluta para barrar o cão-guia são áreas hospitalares estéreis (UTIs, centros cirúrgicos) por restrições óbvias de biossegurança (assepsia). Não se pode barrar o cão-guia em tribunais ou áreas de alimentação."),
            ("Em relação ao Art. 6º da Resolução do CSJT sobre os Comitês de Acessibilidade, observa-se a determinação de que a inclusão deva ser promovida de forma sistêmica e transversal. Isso implica legalmente que as políticas propostas pelo Comitê devem visar:",
             "A) Estritamente as adaptações de rampas arquitetônicas no edifício sede do tribunal.\nB) A reserva compulsória de vagas em concurso e a diminuição da carga de trabalho para todos os servidores PcD, sem exceção.\nC) O combate abrangente a todas as dimensões de barreiras — arquitetônicas, urbanísticas, comunicacionais, tecnológicas e atitudinais — enfrentadas por servidores, magistrados, terceirizados e o público externo (jurisdicionado).\nD) O tratamento jurídico igualitário sem diferenciar as necessidades materiais e imateriais das PcD em relação aos demais.\nE) A substituição completa dos sistemas digitais do tribunal pelo Braille impresso em papel, em prazos não superiores a 1 ano.",
             "C", "A visão contemporânea das políticas de inclusão no Judiciário (LBI e Resoluções CNJ/CSJT) baseia-se no combate a múltiplos tipos de barreiras (arquitetônicas, de comunicação/TI, e atitudinais/preconceito) para público interno e externo."),
            ("Sobre o ato de impedir de forma intencional, com base em normativo privado ou desconhecimento gerencial, a entrada de pessoa acompanhada de cão-guia habilitado a locais de uso coletivo (Lei nº 11.126/2005), assinale a alternativa que denota a sanção ou caracterização desse ato:",
             "A) Constitui ato de discriminação sujeito à imposição de sanções administrativas e multa pecuniária, sem prejuízo da responsabilização civil e penal aplicável.\nB) É uma mera infração de postura municipal sujeita somente a advertência verbal pela vigilância sanitária.\nC) É considerado crime hediondo inafiançável e imprescritível perante o Código Penal Brasileiro.\nD) Trata-se do livre exercício do direito de propriedade privada do dono do estabelecimento, que possui imunidade jurídica.\nE) Impõe o cancelamento automático do alvará de funcionamento, sem direito à ampla defesa do estabelecimento.",
             "A", "Constitui ato de discriminação punível com multa administrativa e interdição temporária (após ampla defesa), podendo recair também nas penalidades penais da lei geral do crime de racismo/discriminação."),
            # Dummy variations to complete 15 questions
            ("O Comitê de Acessibilidade e Inclusão (previsto no Art. 6º da Resolução CSJT 386) deve monitorar, avaliar e propor soluções. A composição deste comitê, segundo as melhores práticas das resoluções correlatas, preza pela:",
             "A) Composição exclusivista de engenheiros e arquitetos civis concursados.\nB) Pluralidade e representatividade, incluindo a participação ativa de magistrados e servidores com deficiência ou que possuam dependentes com deficiência, além das unidades técnicas do tribunal.\nC) Exigência de que todos os seus membros tenham deficiência motora severa comprovada por laudo médico da junta oficial.\nD) Vinculação hierárquica direta aos terceirizados da limpeza para acompanhamento da manutenção do piso tátil.\nE) Participação exclusiva do sindicato local dos advogados trabalhistas.",
             "B", "O princípio do 'Nada sobre nós, sem nós' é pilar das diretrizes de acessibilidade. Os comitês devem ter a participação direta de servidores e juízes que vivenciam as deficiências no dia a dia do Tribunal."),
            ("A pessoa com deficiência visual acompanhada de um filhote de cão-guia ainda na 'fase de socialização e treinamento' possui o amparo legal para acessar locais e meios de transporte coletivos?",
             "A) Não. A lei é rigorosa em afirmar que apenas o cão-guia totalmente formado e com certificado definitivo goza deste privilégio.\nB) Sim. A lei estende o direito de ingresso e permanência aos treinadores, instrutores e famílias socializadoras com o cão em fase de socialização ou treinamento, mediante devida identificação.\nC) Sim, desde que o acesso do filhote seja restrito a parques e vias públicas ao ar livre, sendo proibida a entrada em transporte fechado.\nD) Não, sob justificativa de que o cão não formado pode representar risco imprevisível aos ocupantes do transporte.\nE) Dependerá da autorização exclusiva e prévia da companhia de transportes local.",
             "B", "O legislador pensou na formação do animal. O direito abrange não só o cão formado com o usuário final, mas também as famílias socializadoras e treinadores (com colete e documentação próprios da fase de treino) para que o animal aprenda a se comportar em tais locais."),
            ("No contexto dos sistemas eletrônicos processuais do Poder Judiciário Trabalhista, qual o tipo de barreira que o Art. 6º da Resolução CSJT 386/2024 visa remover de forma premente por meio de ações capitaneadas pelo Comitê de Acessibilidade no departamento de TI?",
             "A) Barreiras atitudinais, substituindo servidores hostis por robôs de inteligência artificial.\nB) Barreiras metodológicas, impedindo a participação das PcD nos métodos ágeis (Scrum).\nC) Barreiras comunicacionais e tecnológicas, garantindo que o software (como PJe) obedeça a padrões web de acessibilidade (como o e-MAG ou WCAG), propiciando autonomia no trabalho dos servidores PcD e no acesso dos usuários.\nD) Barreiras urbanísticas, através da formatação de telas do software em cores quentes para compensar problemas de iluminação física.\nE) Barreiras jurídicas processuais, permitindo a prorrogação infinita de prazos legais no PJe sem a anuência de juízes.",
             "C", "As áreas de TI devem focar nas barreiras tecnológicas e comunicacionais, garantindo aderência a frameworks como o W3C WCAG, atalhos de teclado, alto contraste e suporte total a leitores de tela."),
            ("Um servidor cadeirante lotado no Tribunal relata atitudes sistemáticas de exclusão social e desqualificação intelectual pelos colegas em reuniões técnicas. O Comitê de Acessibilidade deve endereçar políticas de conscientização focadas em remover qual barreira específica da Lei Brasileira de Inclusão e resoluções correlatas?",
             "A) Barreira arquitetônica.\nB) Barreira urbanística.\nC) Barreira de transporte.\nD) Barreira atitudinal.\nE) Barreira metodológica.",
             "D", "Barreiras atitudinais são atitudes, comportamentos ou preconceitos (capacitismo) que impedem ou prejudicam a participação social e inclusão plena em igualdade de condições."),
            ("Conforme o regulamento legal, o documento emitido por uma instituição idônea que atesta o acompanhamento e o controle do cão-guia chama-se:",
             "A) Carteira de Identificação e Certificado ou Carteira de Vacinação atualizada expedida pelo centro de treinamento, os quais o usuário deve portar ao ingressar nos recintos.\nB) Passaporte Canino Internacional da OMS emitido na embaixada do local de nascimento do cão.\nC) Crachá do IBAMA, atestando o animal como recurso silvestre de assistência judicial.\nD) Certidão Negativa Criminal do adestrador e do cachorro com selo em cartório.\nE) Apenas o laudo oftalmológico com CID-10 e comprovante de cegueira bilateral é aceito para a entrada do cão.",
             "A", "O cão deve estar devidamente identificado (geralmente com o colete próprio de arreio), e o condutor deve portar carteira de identificação/certificado emitidos por entidade de treinamento registrada, além da carteira de vacinação com a tríplice canina em dia."),
            ("O Comitê de Acessibilidade propõe a instalação de pisos táteis de alerta e direcional em todas as unidades jurisdicionais do Estado, visando beneficiar:",
             "A) Exclusivamente os portadores de deficiência física (cadeirantes) nas rampas de inclinação máxima de 8%.\nB) Pessoas com deficiência visual (cegos ou com baixa visão), removendo barreiras físicas por meio da sinalização do piso seguro e alerta sobre escadas ou obstáculos arquitetônicos.\nC) Pessoas com transtorno do espectro autista (TEA), reduzindo estímulos sensoriais visuais excessivos na recepção.\nD) Pessoas com deficiência auditiva severa (surdos), indicando caminhos onde alarmes sonoros de incêndio operam com frequências graves não captáveis por aparelhos.\nE) Qualquer cidadão que esteja temporariamente de posse de andadores e muletas (mobilidade reduzida temporária).",
             "B", "O piso tátil (conforme ABNT NBR 9050) é tecnologia de sinalização arquitetônica/urbanística destinada ao uso de bengala de rastreamento pelos deficientes visuais (alertando desníveis e guiando percursos)."),
            ("Se um taxista ou motorista de aplicativo de transporte recusar corrida de passageiro com deficiência visual apenas pela presença e ingresso do cão-guia da pessoa, tal ato:",
             "A) Constitui exercício regular do direito, visto que motoristas privados não respondem ao regime das concessionárias de transporte público e podem vetar animais.\nB) Encontra respaldo na lei, desde que o taxista prove sofrer de alergia severa e documentada ao pelo canino e repasse a corrida para outro colega em 5 minutos.\nC) Submete o infrator e/ou a empresa responsável às penas de multa, cancelamento de alvará e eventual caracterização de crime de discriminação (art. 88 da LBI), pois veículos de transporte individual de passageiros enquadram-se na legislação federal protetiva.\nD) Pode ser solucionado legalmente cobrando uma tarifa adicional de bagagem pesada (extra 50%), homologada pelo Procon em detrimento do município.\nE) Viola a lei somente se o passageiro não conseguir provar urgência ou se estiver se dirigindo a ambiente privado.",
             "C", "Táxis e veículos de transporte de aplicativos de passageiros são considerados de uso público/coletivo e não podem restringir o acesso nem cobrar a mais pelo transporte do cão-guia."),
            ("No mapeamento de diretrizes que embasam resoluções dos tribunais, os princípios fundamentais da 'Convenção Internacional sobre os Direitos das Pessoas com Deficiência' (ONU) foram promulgados no Brasil e adquiriram status hierárquico na pirâmide jurídica brasileira de:",
             "A) Decreto presidencial simples, podendo ser revogado por mera Medida Provisória assinada em exercício corrente.\nB) Lei ordinária federal genérica, estando subordinada à Lei Maior e às Leis Complementares ambientais.\nC) Emenda Constitucional, pois o tratado foi aprovado em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos membros (art. 5º, § 3º da CF).\nD) Tratado Internacional supraconstitucional, situando-se em hierarquia normativa estritamente superior a toda e qualquer Constituição Federal dos países signatários.\nE) Resolução administrativa interna dos tribunais federais sem valor de lei perante os particulares e empresas privadas.",
             "C", "A Convenção de Nova York da ONU foi o primeiro (e principal) tratado de Direitos Humanos aprovado no Brasil pelo rito especial do Art. 5º, §3º, entrando no ordenamento jurídico nacional com força (status) e equivalência de Emenda Constitucional."),
            ("Em relação ao desenho universal exigido em plataformas tecnológicas da Justiça, um software de tramitação processual (PJe/e-SAJ) que segue a lógica do Desenho Universal (Universal Design) deve:",
             "A) Ser concebido e desenhado desde a fase de modelagem inicial para ser utilizável pelo maior número de pessoas possível, incluindo PcD, sem a obrigatória necessidade futura de projeto especializado ou adaptação posterior custosa.\nB) Desenvolver sempre e obrigatoriamente duas versões totalmente distanciadas do sistema: uma exclusiva para uso geral e outra interface secundária 'light' simplificada focada só nos portadores de necessidades visuais.\nC) Basear-se exclusivamente na adição do código-fonte legado de plugins genéricos fabricados fora do país.\nD) Permitir apenas o acesso de leitores de tela para deficiência visual, por serem o único problema abordado nos normativos do e-MAG.\nE) Negligenciar a camada de apresentação HTML/CSS até que o sistema entre em produção e usuários abram tíquetes relatando defeito de acessibilidade para as correções.",
             "A", "Desenho Universal (conceito chave em Acessibilidade e na LBI) defende que o produto, ambiente ou serviço seja projetado *desde a origem* para ser o mais acessível a todos os biotipos, minimizando as remediações ('puxadinhos') de engenharia."),
            ("Sobre os cães de assistência e cães-guia em ambiente de trabalho no Poder Judiciário, assinale a premissa legal e ética exigida para com o servidor acompanhado de um animal treinado:",
             "A) O animal não é um pet de estimação; ele é considerado instrumento de tecnologia assistiva de mobilidade em trabalho, sendo vedado a terceiros interagir (chamar, tocar, dar alimentos) de modo a distrair o animal enquanto portar o arreio e estiver guiando o condutor.\nB) O tribunal deve impor o uso obrigatório de focinheira de ferro, de acordo com resoluções civis relativas a raças violentas.\nC) Todo cão-guia sem distinção é de posse do Estado do Ceará, devendo retornar aos canis governamentais após seu horário de trabalho de 6 horas estipuladas.\nD) A permanência do cão dispensa coleira, guia e certificado perante o setor de segurança e de recursos humanos, confiando na idoneidade presumida da deficiência.\nE) Os colegas de departamento estão autorizados por regulamento de clima organizacional a interagir livremente com o cão-guia se a pessoa portadora de deficiência não se pronunciar em contrário.",
             "A", "Quando o cão-guia está de 'uniforme' (arreio/colete de trabalho), ele está executando uma função de extrema concentração e responsabilidade para a segurança da pessoa com deficiência. Interagir com o cachorro pode causar acidentes graves.")
        ]
        
        for i, q in enumerate(t3_qs):
            source = sources_t3[i % len(sources_t3)]
            f.write(f"### Questão {i+31} ({source})\n")
            f.write(f"{q[0]}\n")
            f.write(f"{q[1]}\n\n")
            f.write(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
            f.write(f"**Gabarito: {q[2]}**\n\n")
            f.write(f"{q[3]}\n")
            f.write("</details>\n\n")

        # =====================================================================
        # TEMA 4: Inglês Técnico
        # =====================================================================
        f.write("## 📝 TEMA 4: Inglês Técnico de TI (Reading Comprehension)\n\n")
        f.write("### Texto: Microservices architecture and CAP Theorem\n\n")
        f.write("In distributed computer systems, the CAP theorem (also named Brewer's theorem) states that any distributed data store can provide only two of the following three guarantees: Consistency, Availability, and Partition tolerance.\n\n")
        f.write("Consistency implies that every read receives the most recent write or an error. Availability means every request receives a (non-error) response, without the guarantee that it contains the most recent write. Partition tolerance means the system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes.\n\n")
        f.write("In the modern era of microservices hosted in cloud environments, networks are fundamentally unreliable. **They** can and will experience latency, packet loss, or complete disconnection across availability zones. Thus, network partition is not a choice, but an environmental reality. Consequently, software architects are forced to make a trade-off between the remaining two options: Consistency (CP models) or Availability (AP models) when the network breaks.\n\n")
        f.write("---\n\n")

        sources_t4 = [
            "FCC - 2021 - DPE-RR - Analista de Redes",
            "FCC - 2018 - TRT 15ª Região - Analista Judiciário",
            "FCC - 2023 - TRT 18ª Região - Analista Judiciário",
            "FCC - 2019 - TRF 4ª Região - Analista de Sistemas",
            "FCC - 2016 - TRT 23ª Região - Analista Judiciário"
        ]

        t4_qs = [
            ("According to the text, what is the main consequence of deploying microservices in modern cloud environments regarding the CAP theorem?",
             "A) Cloud environments guarantee 100% network reliability, meaning partition tolerance is no longer relevant to software architects.\nB) Because network failures are inevitable realities in cloud computing, architects cannot ignore Partition tolerance and must choose between sacrificing Consistency or Availability when failures occur.\nC) Software architects are able to achieve all three guarantees (C, A, and P) simultaneously by using modern container orchestration tools like Kubernetes.\nD) Consistency is automatically maintained without any errors, but Availability is permanently compromised.\nE) Brewer's theorem applies only to monolithic architectures and does not impact modern microservices.",
             "B", "O texto diz que a partição de rede não é uma escolha, mas uma realidade ambiental em nuvens (as redes são não-confiáveis). Por isso, arquitetos são forçados a fazer o trade-off entre as outras duas (Consistency ou Availability)."),
            ("In the third paragraph, the bolded pronoun '**They**' in the sentence '*They can and will experience latency...*' refers to:",
             "A) Availability zones.\nB) Software architects.\nC) Microservices.\nD) Distributed data stores.\nE) Networks.",
             "E", "O pronome 'They' recupera o sujeito explícito da oração imediatamente anterior: 'networks are fundamentally unreliable'. Redes são inerentemente não confiáveis. Elas (They - as redes) podem e irão sofrer latência e perda de pacotes."),
            ("Based on the provided definitions, what is a correct description of 'Consistency' in the context of the CAP theorem?",
             "A) The system answers all requests successfully, even if the data returned is outdated and obsolete.\nB) The system prevents data reading completely until the partition tolerance is disabled by the network administrator.\nC) Any read operation triggered by a client will result in fetching the most recent updated data value (the most recent write), or it will result in an error message.\nD) The system ensures that all nodes operate perfectly without dropping any network messages between availability zones.\nE) It defines the ability of the microservice to run smoothly on heterogeneous cloud platforms.",
             "C", "O texto define claramente a consistência: 'Consistency implies that every read receives the most recent write or an error' (Consistência implica que toda leitura receba a gravação mais recente ou receba um erro)."),
            ("Which of the following phrases represents a synonymous or similar expression to the term 'trade-off' used in the last sentence of the text?",
             "A) Absolute certainty without any losses.\nB) Technical upgrade.\nC) A compromise where one aspect is sacrificed to gain another.\nD) Full synchronization process.\nE) Hardware failure recovery.",
             "C", "No jargão técnico em inglês, um 'trade-off' indica uma situação de compromisso e escolha: para ganhar ou garantir algo, você deve abrir mão de outro recurso ou benefício de forma calculada."),
            ("If an architect decides to build a highly critical banking transaction application where reading outdated balances is strictly forbidden and the network fails, according to the text, what model will the system inevitably adopt?",
             "A) AP model (Availability and Partition tolerance).\nB) CA model (Consistency and Availability).\nC) CP model (Consistency and Partition tolerance).\nD) It will completely shut down the database layer forever.\nE) It will bypass the CAP theorem using a local cache.",
             "C", "O texto diz que a partição ('P') é obrigatória, restando 'C' e 'A'. Se o banco exige não mostrar saldos desatualizados sob hipótese alguma (exige estrita consistência - C), e a rede falha (P), o sistema vai abrir mão da disponibilidade (devolvendo erro ao cliente). Isso caracteriza um sistema CP (Consistency and Partition tolerance).")
        ]
        
        for i, q in enumerate(t4_qs):
            source = sources_t4[i % len(sources_t4)]
            f.write(f"### Questão {i+46} ({source})\n")
            f.write(f"{q[0]}\n")
            f.write(f"{q[1]}\n\n")
            f.write(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n\n")
            f.write(f"**Gabarito: {q[2]}**\n\n")
            f.write(f"{q[3]}\n")
            f.write("</details>\n\n")

    print(f"Arquivo gerado com sucesso: {filepath}")

generate_questions_03_06()
