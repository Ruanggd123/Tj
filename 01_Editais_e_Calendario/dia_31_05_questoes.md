# Bateria de Questões FCC — Domingo 31/05 (Bateria Extra Diamante)

## 📝 TEMA 2: Integração Contínua e DevOps

### Questão 1 (FCC - 2023 - TRT 11ª Região (AM e RR) - Analista Judiciário - Tecnologia da Informação)
A cultura DevOps baseia-se em princípios fundamentais que visam aproximar o desenvolvimento (Dev) da operação (Ops). Um acrônimo frequentemente utilizado para resumir os pilares essenciais do DevOps é o CALMS. Neste contexto, a letra "A" do acrônimo refere-se a:
A) Agility, promovendo a adoção de metodologias ágeis como Scrum e Kanban.
B) Automation, buscando a automação contínua de processos de build, teste e deploy.
C) Architecture, focando no desenho de arquiteturas orientadas a microsserviços.
D) Analytics, enfatizando a análise de dados para tomada de decisões operacionais.
E) Availability, garantindo a alta disponibilidade dos serviços em produção.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

O acrônimo CALMS foi cunhado por Jez Humble e é a base conceitual do DevOps:
- **C (Culture)**: Mudança cultural, colaboração entre equipes.
- **A (Automation)**: Automação de tarefas repetitivas (CI/CD, testes, IaC). A alternativa B está correta.
- **L (Lean)**: Princípios Lean, eliminação de desperdícios, foco no fluxo de valor.
- **M (Measurement)**: Medição de tudo, coleta de métricas e KPIs.
- **S (Sharing)**: Compartilhamento de conhecimento, ferramentas e responsabilidades.

Portanto, as outras alternativas estão incorretas:
A) Incorreta. Agilidade é um conceito relacionado, mas o "A" do CALMS é de Automação.
C) Incorreta. Arquitetura (como microsserviços) facilita o DevOps, mas não compõe o acrônimo.
D) Incorreta. Analytics não é o termo correto (o foco em métricas é dado pelo "M" de Measurement).
E) Incorreta. Availability é uma meta operacional (tratada também por SRE), não sendo o pilar "A" do CALMS.
</details>

---
### Questão 2 (FCC - 2022 - TRT 22ª Região (PI) - Analista Judiciário - Tecnologia da Informação)
Na adoção de práticas ágeis e DevOps, os conceitos de Integração Contínua (CI), Entrega Contínua (CD) e Implantação Contínua (CD) desempenham papéis cruciais, mas distintos. A principal diferença entre Entrega Contínua (Continuous Delivery) e Implantação Contínua (Continuous Deployment) é que:
A) a Entrega Contínua requer que o código seja compilado automaticamente, enquanto a Implantação Contínua dispensa a compilação.
B) na Entrega Contínua, a liberação para o ambiente de produção exige uma aprovação manual, enquanto na Implantação Contínua a passagem para produção é automatizada, sem intervenção humana.
C) a Implantação Contínua é utilizada exclusivamente em ambientes de homologação, ao passo que a Entrega Contínua afeta apenas o ambiente de produção.
D) a Entrega Contínua foca apenas na automação de testes unitários, enquanto a Implantação Contínua foca na automação de testes de integração e de carga.
E) não existe diferença prática; os termos são sinônimos e cunhados por autores diferentes na literatura de DevOps.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **Integração Contínua (CI)**: Consiste em integrar o código de vários desenvolvedores em um repositório centralizado frequentemente, acompanhado de build e testes automatizados.
- **Entrega Contínua (Continuous Delivery)**: Extensão do CI, onde o software é construído de forma que possa ser liberado para produção a qualquer momento. No entanto, a decisão de fazer o deploy (a implantação real em produção) é **manual**.
- **Implantação Contínua (Continuous Deployment)**: Vai um passo além da Entrega Contínua. Toda alteração que passa nos testes automatizados é implantada **automaticamente** em produção, sem intervenção manual.

Analisando as alternativas:
A) Incorreta. Ambas exigem build/compilação automatizada (oriunda da CI).
B) Correta. A diferença fundamental está na necessidade (ou não) de aprovação manual para o deploy em produção.
C) Incorreta. Ambas visam a produção, mas de formas diferentes (manual vs. automática).
D) Incorreta. Ambas dependem de todos os níveis de testes para garantir a qualidade do software antes da produção.
E) Incorreta. Existem diferenças cruciais na automação da etapa final (deploy).
</details>

---
### Questão 3 (FCC - 2023 - TRT 12ª Região (SC) - Analista Judiciário - Tecnologia da Informação)
Uma das práticas fundamentais no DevOps é a utilização de pipelines de CI/CD para automatizar o ciclo de vida do desenvolvimento. Ao utilizar o Jenkins, a criação de pipelines como código (Pipeline as Code) geralmente é feita por meio de um arquivo que define os estágios de execução. Este arquivo é denominado por padrão como:
A) docker-compose.yml
B) Jenkinsfile
C) build.xml
D) pom.xml
E) playbook.yml

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

O conceito de Pipeline as Code permite que o processo de build, teste e deploy seja versionado junto com o código da aplicação.
No Jenkins, esse arquivo é chamado de **Jenkinsfile**.

Analisando as alternativas:
A) Incorreta. `docker-compose.yml` é utilizado pelo Docker Compose para definir e executar aplicativos Docker multicontêineres.
B) Correta. O `Jenkinsfile` é o arquivo de configuração de pipelines no Jenkins (escrito em sintaxe Declarativa ou Scripted).
C) Incorreta. `build.xml` é o arquivo de configuração padrão do Apache Ant.
D) Incorreta. `pom.xml` (Project Object Model) é o arquivo de configuração e dependências do Apache Maven.
E) Incorreta. `playbook.yml` é um arquivo de configuração do Ansible (ferramenta de gerência de configuração/IaC).
</details>

---
### Questão 4 (FCC - 2024 - TRF 3ª Região - Analista Judiciário - Tecnologia da Informação)
No contexto de implantação de microsserviços sem indisponibilidade (Zero Downtime Deployment), duas estratégias muito utilizadas são o *Blue-Green Deployment* e o *Canary Release*. Sobre o *Blue-Green Deployment*, é correto afirmar que:
A) direciona gradualmente e em pequenas porcentagens o tráfego de usuários para a nova versão, monitorando os erros antes de liberar para o restante.
B) mantém dois ambientes de produção idênticos, alternando o roteamento do tráfego do ambiente atual (ativo) para o novo ambiente, reduzindo riscos de downtime.
C) realiza a atualização da infraestrutura substituindo os nós do cluster um a um (Rolling Update), mantendo a mesma base de dados ativa para ambas as versões.
D) desativa completamente o ambiente de produção para realizar a atualização, e após testes, restabelece o tráfego; embora gere downtime, garante a integridade.
E) é uma técnica exclusiva do Kubernetes que utiliza o conceito de HPA (Horizontal Pod Autoscaler) para balanceamento de carga entre pods.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **Blue-Green Deployment**: Consiste em manter dois ambientes de produção distintos e idênticos (Blue e Green). Apenas um deles está ativo (recebendo tráfego real) por vez. A nova versão é implantada no ambiente inativo. Após testes, o roteador/load balancer é alterado para apontar para o novo ambiente, o que torna o rollback extremamente simples e instantâneo.
- **Canary Release**: Libera a nova versão para uma pequena parcela de usuários (ex: 5%), monitorando erros. Se tudo correr bem, o tráfego é ampliado gradativamente (a alternativa A descreve isso).

Analisando as alternativas:
A) Incorreta. Esta é a definição exata de *Canary Release*.
B) Correta. Descreve perfeitamente o *Blue-Green Deployment*.
C) Incorreta. Refere-se à técnica de *Rolling Update* (ou *Rolling Deployment*).
D) Incorreta. Isso caracteriza um *Recreate Deployment* ou *Big Bang*, que gera indisponibilidade (downtime).
E) Incorreta. Blue-Green é um padrão arquitetural que independe da ferramenta e não está intrinsecamente ligado ao HPA.
</details>

---
### Questão 5 (FCC - 2018 - TRT 15ª Região (SP) - Analista Judiciário - Tecnologia da Informação)
O Docker tornou-se uma ferramenta de infraestrutura padrão em ambientes de CI/CD. Na arquitetura do Docker, a estrutura responsável por armazenar em formato somente leitura (read-only) os templates que contêm instruções para criar um contêiner é chamada de:
A) Docker Daemon (dockerd).
B) Docker Compose.
C) Docker Image (Imagem).
D) Docker Registry.
E) Docker Swarm.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Para entender o Docker, é preciso conhecer seus principais componentes:
A) Incorreta. O Docker Daemon é o serviço que roda no host responsável por gerenciar os objetos do Docker, como imagens, contêineres e redes.
B) Incorreta. Docker Compose é uma ferramenta para definir e executar aplicações multi-contêineres, orquestrando-os localmente.
C) Correta. Uma **Imagem Docker** é um template read-only contendo um conjunto de instruções para a criação de um contêiner (a aplicação em execução).
D) Incorreta. Docker Registry é um repositório centralizado onde as imagens são armazenadas e distribuídas (ex: Docker Hub).
E) Incorreta. Docker Swarm é a ferramenta nativa de orquestração de contêineres em cluster do Docker.
</details>

---
### Questão 6 (FCC - 2022 - TRT 5ª Região (BA) - Analista Judiciário - Tecnologia da Informação)
O uso de Infraestrutura como Código (IaC - Infrastructure as Code) é um dos pilares do DevOps para automação do provisionamento. Duas abordagens comuns no IaC são a declarativa e a imperativa. Uma das ferramentas de IaC baseadas no modelo declarativo, mantida pela HashiCorp, muito utilizada para provisionar recursos em diferentes provedores de nuvem, é o:
A) Terraform.
B) Chef.
C) Jenkins.
D) Git.
E) Ansible.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

No paradigma declarativo, o usuário define o "estado desejado" da infraestrutura, e a ferramenta se encarrega de realizar os passos necessários para alcançar esse estado. No imperativo, o usuário define os comandos específicos ("como fazer") para chegar ao estado.

A) Correta. O **Terraform** (da HashiCorp) é a ferramenta de provisionamento de IaC mais popular, usando HCL (HashiCorp Configuration Language) em um modelo declarativo.
B) Incorreta. O Chef é voltado primariamente para gerência de configuração (assim como Puppet), tendendo frequentemente ao uso de receitas imperativas (baseadas em Ruby).
C) Incorreta. Jenkins é focado em CI/CD e não é uma ferramenta nativa de provisionamento IaC.
D) Incorreta. Git é um sistema de controle de versão (VCS), servindo de base para o IaC (e GitOps), mas não provisiona infraestrutura por si só.
E) Incorreta. O Ansible é excelente para gerência de configuração. Embora seja YAML e tenha características declarativas, é mais procedural/imperativo do que o Terraform quando o assunto é o provisionamento do ciclo de vida da infraestrutura de nuvem, e não é mantido pela HashiCorp (é da Red Hat/IBM).
</details>

---
### Questão 7 (FCC - 2021 - TCE-SC - Auditor Fiscal de Controle Externo - Informática)
A inserção de práticas de segurança diretamente nos pipelines de integração e entrega contínua, visando tratar falhas de segurança nas etapas iniciais de desenvolvimento, remete ao termo DevSecOps. Uma das práticas mais comuns adotadas no CI/CD para analisar estaticamente o código-fonte em busca de vulnerabilidades antes mesmo da compilação é denominada:
A) DAST (Dynamic Application Security Testing).
B) SAST (Static Application Security Testing).
C) RASP (Runtime Application Self-Protection).
D) IAST (Interactive Application Security Testing).
E) Pentest (Testes de Intrusão manuais).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

DevSecOps promove a abordagem *Shift-Left*, antecipando testes de segurança:
A) Incorreta. DAST é análise **dinâmica**. Ocorre com a aplicação em execução para identificar falhas de injeção, XSS, etc.
B) Correta. SAST é análise **estática**. Inspeciona o código-fonte, o bytecode ou os binários sem executar a aplicação (ex: SonarQube, Checkmarx). Pode e deve ser rodado logo no início do pipeline.
C) Incorreta. RASP é uma tecnologia que fica dentro da aplicação em tempo de execução (runtime), capaz de detectar e bloquear ataques enquanto acontecem.
D) Incorreta. IAST é uma abordagem híbrida, combinando técnicas de análise estática e dinâmica na aplicação rodando.
E) Incorreta. Pentest manual geralmente é feito em fases mais tardias, embora essencial, não é focado na automação inicial do código.
</details>

---
### Questão 8 (FCC - 2023 - TST - Analista Judiciário - Tecnologia da Informação)
No ecossistema de orquestração de contêineres e DevOps, o Kubernetes (K8s) desempenha um papel central. Na arquitetura do Kubernetes, o componente do *Control Plane* responsável por expor a API do Kubernetes, atuando como o ponto de entrada principal para os comandos executados via `kubectl`, é o:
A) kube-scheduler.
B) etcd.
C) kube-apiserver.
D) kube-controller-manager.
E) kubelet.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A arquitetura do Kubernetes se divide em Master (Control Plane) e Worker Nodes:
A) Incorreta. O `kube-scheduler` é o responsável por decidir em qual nó um novo Pod (contêiner) vai ser executado, baseando-se em recursos disponíveis e regras de afinidade.
B) Incorreta. O `etcd` é um armazenamento de chave-valor distribuído e altamente disponível usado como o banco de dados de suporte do Kubernetes para todos os dados do cluster.
C) Correta. O `kube-apiserver` é o *front-end* do Control Plane. Toda a comunicação dentro e fora do cluster K8s passa por ele (incluindo as ações do `kubectl`).
D) Incorreta. O `kube-controller-manager` gerencia os controladores que regulam o estado do cluster, como o Node Controller e o ReplicaSet Controller.
E) Incorreta. O `kubelet` não faz parte do Control Plane. É o agente que roda em cada *Worker Node*, garantindo que os contêineres estejam em execução e saudáveis nos Pods.
</details>

---
### Questão 9 (FCC - 2024 - TRF 3ª Região - Analista Judiciário - Tecnologia da Informação)
O GitOps é um modelo operacional em evolução no contexto DevOps que utiliza o Git como a fonte única da verdade (Single Source of Truth) para infraestrutura e aplicações declarativas. Uma das características fundamentais do modelo GitOps é o uso de agentes *pull-based* (operadores). Diferente de abordagens tradicionais de CI/CD baseadas em *push*, em um modelo *pull* no GitOps:
A) o repositório Git envia ativamente comandos via SSH para os servidores de produção assim que um novo commit é recebido.
B) um operador rodando dentro do próprio cluster de destino (como o ArgoCD ou Flux) monitora o repositório Git e aplica as mudanças para sincronizar o estado atual com o estado desejado.
C) as imagens Docker geradas no CI enviam uma notificação para o cluster, forçando-o a baixar as novas versões.
D) o Jenkins invoca scripts Terraform a partir de gatilhos acionados manualmente por um administrador de redes.
E) a sincronização com a infraestrutura é feita exclusivamente pela execução manual do comando `git pull` nos nós de produção.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

GitOps baseia-se em infraestrutura declarativa onde as configurações residem no Git.
A) Incorreta. Essa é uma descrição de um modelo *Push* (como frequentemente feito pelo Jenkins ou GitLab CI tradicional).
B) Correta. No GitOps puro (*Pull-based*), existem ferramentas (como ArgoCD ou FluxCD) instaladas *dentro* do cluster de destino. Elas "puxam" as informações monitorando o repositório Git. Se houver divergência entre o estado do cluster e o que está no Git, elas convergem o cluster para o estado do Git automaticamente (ou sob demanda).
C) Incorreta. Imagens não controlam o deploy ativamente, elas são apenas artefatos armazenados em um Registry.
D) Incorreta. Descreve uma ação tradicional orientada a CI/CD, não a filosofia autônoma pull-based do GitOps.
E) Incorreta. GitOps preza pela automação extrema; `git pull` manual contradiz seus princípios fundamentais.
</details>

---
### Questão 10 (FCC - 2018 - TRT 2ª Região (SP) - Analista Judiciário - Tecnologia da Informação)
Nas pipelines de integração contínua (CI), a análise da qualidade do código-fonte é um passo recomendado. Uma ferramenta amplamente utilizada para medir a qualidade do código (avaliando cobertura de testes, complexidade ciclomática, código duplicado, vulnerabilidades e "code smells") e que se integra nativamente à maioria dos servidores de CI é o:
A) Ansible.
B) Kubernetes.
C) SonarQube.
D) Maven.
E) Docker.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. Ansible é para gerência de configuração e IaC.
B) Incorreta. Kubernetes orquestra contêineres em produção.
C) Correta. O **SonarQube** (ou SonarCloud) é a ferramenta líder em inspeção contínua da qualidade e segurança do código, reportando "Code Smells" (códigos que cheiram mal, ou seja, são difíceis de manter), bugs, vulnerabilidades de segurança e cobertura de código (porcentagem do código coberto por testes unitários).
D) Incorreta. Maven é uma ferramenta de build e gestão de dependências em Java, e embora execute testes e gere relatórios, a inspeção de qualidade centralizada é papel do SonarQube.
E) Incorreta. Docker isola a aplicação em contêineres.
</details>

---
### Questão 11 (FCC - 2023 - TRT 11ª Região (AM e RR) - Analista Judiciário - Tecnologia da Informação)
O conceito de "Shift-Left" no ciclo de vida de desenvolvimento de software e DevOps significa:
A) deslocar os servidores de produção física para a nuvem pública, priorizando a lateral esquerda de diagramas de topologia de rede.
B) atrasar a execução dos testes até que todo o código esteja implementado, garantindo a avaliação do produto de forma integral no lado direito do cronograma.
C) antecipar e incorporar as práticas de testes, segurança e qualidade para as fases mais iniciais (à esquerda) do ciclo de desenvolvimento, em vez de deixá-las para o final.
D) promover desenvolvedores seniores a posições gerenciais (deslocamento para o lado esquerdo do organograma da empresa).
E) migrar as bases de dados relacionais (SQL) para não relacionais (NoSQL).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Imagine o fluxo de ciclo de vida de desenvolvimento de software (SDLC) da esquerda para a direita (Requisitos -> Design -> Código -> Testes -> Deploy -> Manutenção).
A) Incorreta. Não tem relação com diagramas de rede ou migração para nuvem.
B) Incorreta. Isso descreve o oposto do "Shift-Left"; seria postergar (Shift-Right) e é característico de processos em cascata.
C) Correta. **Shift-Left** significa "deslocar para a esquerda", ou seja, realizar tarefas vitais (como integração, testes e verificações de segurança) o mais cedo possível no ciclo. Encontrar um erro na fase de codificação é muito mais barato e rápido de corrigir do que em produção.
D) Incorreta. Falsa e irrelevante conceitualmente.
E) Incorreta. Não tem nenhuma relação com escolha de banco de dados.
</details>

---
### Questão 12 (FCC - 2019 - TRF 4ª Região - Analista Judiciário - Tecnologia da Informação)
O conceito de arquitetura de microsserviços harmoniza-se de forma profunda com a cultura DevOps. Entre os motivos para a adoção de microsserviços visando maximizar os benefícios do DevOps, destaca-se:
A) a centralização de todos os serviços em um único banco de dados monolítico, o que facilita o versionamento dos esquemas através de CI/CD.
B) a dependência forte entre os módulos (alto acoplamento), obrigando os times de infraestrutura e desenvolvimento a trabalharem nas mesmas linguagens de programação.
C) a autonomia na implantação (deploy), permitindo que pequenas equipes desenvolvam, testem e liberem serviços independentemente dos demais componentes do sistema.
D) a eliminação da necessidade de orquestração de contêineres e testes automatizados, já que cada serviço é pequeno o suficiente para não conter erros críticos.
E) a redução da complexidade na monitoração, tendo em vista que microsserviços interagem de forma síncrona sem gerar latência na rede.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Os microsserviços quebram a aplicação em pequenos serviços independentes.
A) Incorreta. Uma premissa dos microsserviços é a descentralização de dados, onde frequentemente cada serviço possui seu próprio banco de dados isolado (Database per Service) para evitar acoplamento.
B) Incorreta. Os microsserviços buscam o **baixo acoplamento**, e permitem autonomia tecnológica (Polyglot Persistence/Programming).
C) Correta. A autonomia de deploy é o grande benefício para o DevOps. Um time pode liberar a versão do serviço A sem precisar compilar, testar ou sincronizar o deploy com os serviços B, C e D.
D) Incorreta. Pelo contrário; microsserviços exigem **mais** automação de deploy, orquestração rigorosa (como K8s) e testes minuciosos, devido à complexidade da infraestrutura distribuída.
E) Incorreta. A complexidade de monitoramento **aumenta** exponencialmente nos microsserviços, exigindo práticas avançadas de Observabilidade, tracing distribuído e logs centralizados.
</details>

---
### Questão 13 (FCC - 2022 - TRT 14ª Região (RO e AC) - Analista Judiciário - Tecnologia da Informação)
No contexto de versionamento e DevOps, o Git desempenha papel crítico. Uma estratégia de ramificação (*branching strategy*) bastante popular para projetos versionados no Git é o GitFlow. No modelo original do GitFlow, as duas *branches* principais de longo tempo de vida que existem durante toda a vida do projeto são:
A) `master` (ou `main`) e `develop`.
B) `feature` e `release`.
C) `hotfix` e `bugfix`.
D) `trunk` e `tag`.
E) `production` e `homologation`.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

O GitFlow (criado por Vincent Driessen) organiza o repositório da seguinte maneira:
A) Correta. O modelo possui duas branches perenes (de vida longa):
- `master` (ou `main`): Contém o código oficial de produção; sempre está em estado implantável.
- `develop`: Contém os últimos códigos entregues para as próximas releases; é a branch de integração.
B) Incorreta. As branches `feature` (novas funcionalidades) e `release` (preparação para produção) são temporárias (efêmeras); são apagadas após o merge.
C) Incorreta. `hotfix` é uma branch temporária, derivada da `master` para correções rápidas em produção, e feito o merge, ela é deletada.
D) Incorreta. *Trunk* é o termo base para o Trunk-Based Development, outra estratégia (diferente do GitFlow), que foca na branch master/main apenas.
E) Incorreta. Estas não são nomenclaturas padrão do modelo GitFlow.
</details>

---
### Questão 14 (FCC - 2023 - TRT 12ª Região (SC) - Analista Judiciário - Tecnologia da Informação)
Dentro da cultura DevOps e de Engenharia de Confiabilidade de Sites (SRE - Site Reliability Engineering), o estabelecimento de métricas quantificáveis de sucesso e disponibilidade dos serviços é essencial. Considere a afirmativa: "O percentual ou número absoluto de requisições falhas aceitáveis que o sistema pode tolerar durante um período sem que haja quebra do compromisso estabelecido com o negócio ou o cliente final". O termo que melhor define este conceito no SRE é o:
A) SLA (Service Level Agreement).
B) SLI (Service Level Indicator).
C) SLO (Service Level Objective).
D) Error Budget (Orçamento de Erro).
E) MTTR (Mean Time To Recovery).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A Google introduziu o SRE com conceitos chaves:
- **SLA**: Acordo contratual de negócio; caso não cumprido, gera multas.
- **SLO**: Objetivo interno da equipe (ex: 99.9% das requisições com sucesso em 30 dias).
- **SLI**: Indicador real medido (ex: qual foi o percentual atingido hoje, digamos 99.95%).
A) Incorreta. SLA é o contrato.
B) Incorreta. SLI é a métrica pontual real.
C) Incorreta. SLO é o alvo.
D) Correta. O **Error Budget** é a margem de erro. Se o SLO é 99.9%, o Error Budget é 0.1%. É a quantidade de falhas "tolerada" que a equipe tem para gastar com novas implementações e experimentações. Se o orçamento esgota, os deploys de novas *features* são congelados e o foco passa a ser 100% estabilidade.
E) Incorreta. MTTR é o Tempo Médio de Recuperação, métrica de quanto tempo demora para o sistema voltar ao ar após cair.
</details>

---
### Questão 15 (FCC - 2021 - TCE-SC - Auditor Fiscal de Controle Externo - Informática)
Uma das práticas modernas de colaboração suportadas pelo DevOps é o chamado "ChatOps". O principal objetivo do ChatOps é:
A) criar fóruns assíncronos para que a equipe de suporte tire dúvidas de usuários finais.
B) permitir a execução de ferramentas, implantações e fluxos de trabalho operacionais diretamente a partir de comandos em interfaces de chat da equipe de desenvolvimento e operação, colaborando de forma transparente.
C) utilizar inteligência artificial para ler códigos fonte e responder a dúvidas de desenvolvedores juniores em uma interface de bate-papo.
D) substituir as metodologias ágeis (como as reuniões diárias do Scrum) por aplicativos de mensagens corporativas visando reduzir o tempo perdido.
E) garantir que toda a comunicação da equipe de projeto seja criptografada e não possa ser rastreada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

O conceito de **ChatOps**:
A) Incorreta. Não é focado no atendimento ao usuário final, mas nas operações da própria equipe de engenharia.
B) Correta. ChatOps é o uso de plataformas de comunicação colaborativa (como Slack, Microsoft Teams ou Discord) integradas a bots (Chatbots) e ferramentas de CI/CD. Por exemplo, um desenvolvedor digita `/deploy production v2.1` no chat, e todos da sala acompanham o comando sendo processado e o log de resultado postado pelo Bot. Traz extrema visibilidade e unifica comunicação e execução.
C) Incorreta. Isso seria uso de Assistentes IA de código, não é o foco histórico e primário do ChatOps (que engloba executar *operações*).
D) Incorreta. O ChatOps não visa substituir metodologias ágeis, e sim adicionar automação e transparência operacional.
E) Incorreta. É um detalhe técnico de segurança, não a finalidade e definição da cultura de ChatOps.
</details>

---


## 📝 TEMA 3: Direito Constitucional

### Questão 1 (FCC - 2022 - TRT 4 - Analista Judiciário)
Sobre os direitos e garantias fundamentais previstos na Constituição Federal:
A) A lei penal não retroagirá, salvo para beneficiar o réu.
B) É permitida a pena de morte em qualquer hipótese de comoção interna grave.
C) É livre a manifestação do pensamento, sendo permitido o anonimato nas denúncias.
D) A prática do racismo constitui crime inafiançável, sujeito a pena de detenção.
E) As associações poderão ser compulsoriamente dissolvidas por ato do Poder Executivo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) **Correta.** Nos termos do art. 5º, XL da CF/88, "a lei penal não retroagirá, salvo para beneficiar o réu". É o princípio da irretroatividade da lei penal gravosa.
B) **Incorreta.** A pena de morte é vedada no Brasil, existindo uma única exceção: em caso de guerra declarada, conforme art. 5º, XLVII, "a".
C) **Incorreta.** O art. 5º, IV consagra que é livre a manifestação do pensamento, sendo expressamente VEDADO o anonimato.
D) **Incorreta.** O crime de racismo é inafiançável e imprescritível, sujeito à pena de RECLUSÃO (e não detenção), nos termos do art. 5º, XLII da CF/88.
E) **Incorreta.** As associações só poderão ser compulsoriamente dissolvidas ou ter suas atividades suspensas por decisão judicial, exigindo-se, no primeiro caso, o trânsito em julgado (art. 5º, XIX).
</details>

---

### Questão 2 (FCC - 2023 - TRT 18 - Analista Judiciário)
Em relação aos direitos sociais expressos na Constituição Federal de 1988:
A) São direitos sociais a educação, a saúde, a alimentação, o trabalho, a moradia, o transporte, o lazer, a segurança, a previdência social, a proteção à maternidade e à infância, a assistência aos desamparados.
B) É garantido o salário mínimo nacional, mas sua fixação e reajustes são definidos por convenção coletiva, sem força de lei.
C) O repouso semanal remunerado deve ocorrer preferencialmente aos sábados e domingos.
D) A licença à gestante é fixada constitucionalmente em cento e oitenta dias, sem prejuízo do emprego e do salário.
E) O aviso prévio é garantido a todos os trabalhadores, sendo sempre fixo e de trinta dias independentemente do tempo de serviço.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) **Correta.** Corresponde à exata literalidade do art. 6º, *caput*, da Constituição Federal, que elenca os direitos sociais fundamentais, incluindo as atualizações introduzidas por Emendas Constitucionais (como o direito ao transporte).
B) **Incorreta.** O salário mínimo deve ser fixado em LEI, nacionalmente unificado, conforme o art. 7º, IV da CF/88.
C) **Incorreta.** A Constituição determina que o repouso semanal remunerado será concedido "preferencialmente aos domingos" (art. 7º, XV), e não sábados e domingos.
D) **Incorreta.** A CF estabelece, em seu art. 7º, XVIII, a licença à gestante pelo prazo de cento e vinte (120) dias.
E) **Incorreta.** O aviso prévio é proporcional ao tempo de serviço, sendo no mínimo de trinta dias, nos termos da lei (art. 7º, XXI).
</details>

---

### Questão 3 (FCC - 2018 - TRT 15 - Analista Judiciário)
Sobre a organização do Estado, a Constituição prevê que os Estados-membros:
A) Podem se subdividir em Municípios, mas não podem se incorporar entre si.
B) Possuem autonomia política, administrativa e financeira, nos termos da Constituição.
C) Podem editar normas gerais e privativas sobre direito civil e penal caso haja urgência.
D) Têm a mesma competência tributária para criar contribuições sociais que a União.
E) Podem criar, mediante lei complementar própria da Assembleia Legislativa, novos Estados em seus territórios.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) **Incorreta.** Os Estados podem incorporar-se entre si, subdividir-se ou desmembrar-se para se anexarem a outros (art. 18, § 3º).
B) **Correta.** Os Estados organizam-se por suas próprias Constituições, respeitados os princípios da CF, possuindo plena autonomia (capacidade de auto-organização, autogoverno e autoadministração).
C) **Incorreta.** Legislar sobre direito civil e penal é competência privativa da União (art. 22, I), não havendo previsão para edição pelos Estados sob justificativa de urgência genérica.
D) **Incorreta.** A União tem competência para a maior parte das contribuições sociais; os Estados podem cobrar contribuição apenas de seus servidores para regime próprio de previdência (art. 149, § 1º).
E) **Incorreta.** A criação de novos Estados é feita por lei complementar federal, editada pelo Congresso Nacional, e não por lei estadual (art. 18, § 3º).
</details>

---

### Questão 4 (FCC - 2021 - TRT 11 - Técnico Judiciário)
O Poder Legislativo da União, conforme a Constituição Federal, é exercido pelo Congresso Nacional, que se compõe de:
A) Câmara dos Deputados e Supremo Tribunal Federal.
B) Câmara dos Deputados e Senado Federal.
C) Senado Federal e Conselho Nacional de Justiça.
D) Câmara dos Deputados e Tribunal de Contas da União.
E) Senado Federal e Câmara de Vereadores do Distrito Federal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) **Incorreta.** O Supremo Tribunal Federal é o órgão de cúpula do Poder Judiciário.
B) **Correta.** Conforme o art. 44 da CF/88: "O Poder Legislativo é exercido pelo Congresso Nacional, que se compõe da Câmara dos Deputados e do Senado Federal". É a consagração do sistema bicameral no plano federal.
C) **Incorreta.** O Conselho Nacional de Justiça (CNJ) é órgão integrante do Poder Judiciário.
D) **Incorreta.** O TCU, embora auxilie o Congresso Nacional no controle externo, não compõe o Poder Legislativo como uma de suas Casas.
E) **Incorreta.** O DF possui Câmara Legislativa, composta por Deputados Distritais, não fazendo parte do Congresso Nacional.
</details>

---

### Questão 5 (FCC - 2019 - TRF 3 - Analista Judiciário)
A respeito do Poder Executivo, é correto afirmar que o Presidente da República:
A) Não pode ser responsabilizado por atos estranhos ao exercício de suas funções na vigência de seu mandato.
B) Pode ser submetido à prisão cautelar a qualquer tempo, mesmo nas infrações comuns sem condenação.
C) Responde originariamente e sempre no Supremo Tribunal Federal quando cometer crimes de responsabilidade.
D) Pode ausentar-se do País por mais de 30 dias sem licença do Congresso Nacional.
E) Pode ser processado criminalmente no STF sem necessidade de qualquer autorização legislativa.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) **Correta.** De acordo com o art. 86, § 4º da CF/88, "O Presidente da República, na vigência de seu mandato, não pode ser responsabilizado por atos estranhos ao exercício de suas funções" (imunidade material temporária).
B) **Incorreta.** O Presidente não está sujeito a prisão nas infrações comuns, enquanto não sobrevier sentença condenatória (art. 86, § 3º).
C) **Incorreta.** Nos crimes de responsabilidade, o Presidente da República é julgado pelo Senado Federal, e não pelo STF (art. 86, caput).
D) **Incorreta.** Ele e o Vice não podem ausentar-se do País por período superior a 15 dias sem licença do Congresso, sob pena de perda do cargo (art. 83).
E) **Incorreta.** Tanto para infrações penais comuns (no STF) quanto para crimes de responsabilidade (no Senado), exige-se prévia autorização por dois terços da Câmara dos Deputados (art. 86, caput).
</details>

---

### Questão 6 (FCC - 2017 - TRE SP - Técnico Judiciário)
O Poder Judiciário tem como um de seus órgãos o Supremo Tribunal Federal (STF). Sobre o STF, a Constituição Federal dispõe que ele se compõe de:
A) Onze Ministros, escolhidos dentre cidadãos com mais de trinta e cinco e menos de setenta anos de idade, de notável saber jurídico e reputação ilibada.
B) Trinta e três Ministros, nomeados pelo Presidente da República e aprovados pela Câmara dos Deputados.
C) Vinte e sete Ministros, um representando cada unidade da federação, indicados pelos Governadores.
D) Quinze Ministros, escolhidos dentre membros do Ministério Público e advogados de notório saber jurídico.
E) Onze Ministros, aprovados exclusivamente pelo Conselho Nacional de Justiça.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) **Correta.** Segundo o art. 101 da CF/88 (com a redação dada pela EC nº 122/2022, que alterou a idade máxima), o STF compõe-se de 11 Ministros, escolhidos dentre cidadãos com mais de 35 e menos de 70 anos de idade, de notável saber jurídico e reputação ilibada.
B) **Incorreta.** Trinta e três (33) é a composição mínima do Superior Tribunal de Justiça (STJ).
C) **Incorreta.** Os Ministros não são representantes dos Estados, e são escolhidos pelo Presidente da República (após aprovação do Senado), não por Governadores.
D) **Incorreta.** Quinze (15) é a composição do Superior Tribunal Militar (STM).
E) **Incorreta.** Os Ministros do STF são indicados pelo Presidente e aprovados pelo Senado Federal (por maioria absoluta), não havendo participação do CNJ na aprovação.
</details>

---

### Questão 7 (FCC - 2016 - TRT 20 - Técnico Judiciário)
No tocante ao processo legislativo federal, a iniciativa das leis complementares e ordinárias cabe:
A) Exclusivamente ao Presidente da República e aos membros da Mesa do Senado Federal.
B) A qualquer cidadão, bastando apresentar o texto da lei no protocolo da Câmara sem qualquer número mínimo de assinaturas.
C) A qualquer membro ou comissão da Câmara dos Deputados, do Senado Federal ou do Congresso Nacional, ao Presidente da República, ao Supremo Tribunal Federal, aos Tribunais Superiores, ao Procurador-Geral da República e aos cidadãos.
D) Ao Conselho Nacional de Justiça e aos Ministros de Estado privativamente.
E) Ao Tribunal de Contas da União, especialmente em matéria tributária e orçamentária.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) **Incorreta.** A iniciativa legislativa não é exclusiva destes; o rol é amplo e inclui diversos órgãos e os cidadãos.
B) **Incorreta.** A iniciativa popular de lei federal exige requisitos rigorosos: subscrição de, no mínimo, um por cento do eleitorado nacional, distribuído pelo menos por cinco Estados, com não menos de três décimos por cento dos eleitores de cada um deles (art. 61, § 2º).
C) **Correta.** É o que prescreve textualmente o *caput* do art. 61 da Constituição Federal.
D) **Incorreta.** O CNJ e os Ministros de Estado não figuram no rol de legitimados para iniciativa geral de leis federais no art. 61.
E) **Incorreta.** O TCU não possui iniciativa legislativa própria, muito menos para matéria tributária e orçamentária (cuja iniciativa principal é do Executivo).
</details>

---

### Questão 8 (FCC - 2019 - TRF 4 - Técnico Judiciário)
Entre os direitos e garantias fundamentais previstos na CF/88, o mandado de injunção será concedido:
A) Sempre que a falta de norma regulamentadora torne inviável o exercício dos direitos e liberdades constitucionais e das prerrogativas inerentes à nacionalidade, à soberania e à cidadania.
B) Sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder.
C) Para proteger direito líquido e certo, não amparado por habeas corpus ou habeas data.
D) Para anular ato lesivo ao patrimônio público ou de entidade de que o Estado participe, à moralidade administrativa, ao meio ambiente e ao patrimônio histórico e cultural.
E) Para assegurar o conhecimento de informações relativas à pessoa do impetrante, constantes de registros ou bancos de dados de entidades governamentais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) **Correta.** O art. 5º, LXXI da CF/88 traz a exata definição do cabimento do Mandado de Injunção, utilizado para combater omissões legislativas que inviabilizem o exercício de direitos constitucionais.
B) **Incorreta.** Trata-se do cabimento do Habeas Corpus (art. 5º, LXVIII).
C) **Incorreta.** Trata-se do cabimento do Mandado de Segurança (art. 5º, LXIX).
D) **Incorreta.** Trata-se do cabimento da Ação Popular (art. 5º, LXXIII).
E) **Incorreta.** Trata-se do cabimento do Habeas Data (art. 5º, LXXII, "a").
</details>

---

### Questão 9 (FCC - 2018 - TRT 6 - Analista Judiciário)
A respeito do controle de constitucionalidade no Direito brasileiro, o controle exercido por via de exceção ou defesa, também conhecido como controle difuso, pode ser realizado:
A) Apenas pelo Supremo Tribunal Federal, em decisões proferidas em controle abstrato.
B) Exclusivamente por Tribunais de segunda instância, sendo vedado aos juízes singulares.
C) Por qualquer juiz ou tribunal, incidenter tantum, no julgamento do caso concreto.
D) Apenas no julgamento da Ação Direta de Inconstitucionalidade.
E) Somente quando provocado pelo Procurador-Geral da República.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) **Incorreta.** O Supremo Tribunal Federal exerce primordialmente o controle concentrado, mas o controle difuso é aberto a qualquer órgão jurisdicional.
B) **Incorreta.** Os juízes singulares (1ª instância) também detêm a competência para exercer o controle de constitucionalidade de forma difusa (incidental).
C) **Correta.** No sistema brasileiro, o controle difuso (ou incidental) caracteriza-se por poder ser exercido por qualquer juiz ou tribunal ao analisar um caso concreto submetido à sua jurisdição. A declaração de inconstitucionalidade é mero pressuposto para resolver a lide principal.
D) **Incorreta.** A Ação Direta de Inconstitucionalidade (ADI) é instrumento típico de controle CONCENTRADO (abstrato) de constitucionalidade.
E) **Incorreta.** O Procurador-Geral da República é um dos legitimados do art. 103 para propor ações do controle concentrado, mas o controle difuso pode ser provocado por qualquer parte em qualquer processo.
</details>

---

### Questão 10 (FCC - 2022 - TRT 22 - Técnico Judiciário)
Segundo a literalidade da Constituição Federal a respeito dos direitos fundamentais, é correto afirmar sobre a locomoção no território nacional:
A) É garantida a livre locomoção em qualquer tempo, inclusive nos estados de sítio e defesa sem possibilidade de restrições.
B) É livre a locomoção no território nacional em tempo de paz, podendo qualquer pessoa, nos termos da lei, nele entrar, permanecer ou dele sair com seus bens.
C) É garantida somente para brasileiros natos, sendo restrita e rigorosamente controlada a circulação de estrangeiros independentemente de estarem regulares.
D) É permitida apenas para os agentes públicos em regular exercício de função oficial, cabendo autorização específica para civis cruzarem fronteiras estaduais.
E) Ocorre sem sujeição a qualquer tipo de lei restritiva de trânsito, inclusive dispensando passaportes ou vistos de estrangeiros.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) **Incorreta.** Durante os estados de exceção constitucionais (estado de sítio e defesa), a liberdade de locomoção pode sofrer medidas coercitivas temporárias.
B) **Correta.** A redação copia o art. 5º, XV, da CF/88, consagrando a liberdade de locomoção (direito de ir, vir e permanecer), destacando ser "em tempo de paz" e condicionada "nos termos da lei".
C) **Incorreta.** A liberdade se estende a qualquer pessoa (brasileiros natos, naturalizados e estrangeiros residentes ou em trânsito no país).
D) **Incorreta.** O direito pertence a todas as pessoas, não sendo prerrogativa exclusiva de agentes públicos.
E) **Incorreta.** O texto constitucional diz expressamente "nos termos da lei", permitindo a exigência de vistos, passaportes, habilitação de trânsito, etc.
</details>

---

### Questão 11 (FCC - 2017 - TST - Analista Judiciário)
A Constituição da República prevê um Capítulo específico destinado às denominadas "Funções Essenciais à Justiça". Assinale a alternativa que indica Instituições abrigadas nesse Capítulo:
A) A Magistratura, o Ministério Público e o Tribunal de Contas da União.
B) O Ministério Público, a Advocacia Pública, a Advocacia e a Defensoria Pública.
C) A Polícia Federal, as Polícias Civis e a Magistratura.
D) A Defensoria Pública, o Supremo Tribunal Federal e os Tribunais Regionais Eleitorais.
E) A Advocacia-Geral da União, as Forças Armadas e o Ministério da Justiça.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) **Incorreta.** A Magistratura pertence ao Poder Judiciário; o TCU está vinculado à organização do Legislativo (função de controle externo).
B) **Correta.** O Título IV, Capítulo IV, da CF/88 elenca as Funções Essenciais à Justiça: Seção I (Ministério Público), Seção II (Advocacia Pública), Seção III (Advocacia) e Seção IV (Defensoria Pública).
C) **Incorreta.** Polícias pertencem à Segurança Pública (Capítulo III do Título V) e Magistratura ao Poder Judiciário.
D) **Incorreta.** STF e TREs são órgãos do Poder Judiciário (Capítulo III do Título IV).
E) **Incorreta.** As Forças Armadas estão localizadas no Capítulo da Defesa do Estado e das Instituições Democráticas.
</details>

---

### Questão 12 (FCC - 2015 - TRT 3 - Analista Judiciário)
De acordo com as regras constitucionais referentes à nacionalidade brasileira, é correto afirmar que é brasileiro nato:
A) O nascido na República Federativa do Brasil, ainda que de pais estrangeiros, desde que estes não estejam a serviço de seu país.
B) O estrangeiro de qualquer nacionalidade que venha a residir no Brasil por mais de quinze anos ininterruptos e sem condenação penal, requerendo a nacionalidade.
C) O nascido no exterior, de pai ou mãe brasileira, desde que o Brasil os registre compulsoriamente assim que completarem dezoito anos.
D) O estrangeiro de país originário de língua portuguesa que fixe residência por um ano ininterrupto no Brasil e possua idoneidade moral.
E) O nascido na República Federativa do Brasil, de pais estrangeiros, mesmo no caso em que ambos estejam no país a serviço da nação de origem.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) **Correta.** Reflete a adoção da regra do *jus soli* (critério territorial) constante do art. 12, I, "a": são brasileiros natos os nascidos na República Federativa do Brasil, ainda que de pais estrangeiros, desde que estes não estejam a serviço de seu país.
B) **Incorreta.** Esta hipótese caracteriza a nacionalidade brasileira NATURALIZADA extraordinária (quinzenária), não nata (art. 12, II, "b").
C) **Incorreta.** O registro não é compulsório pelo Estado aos 18 anos. A CF prevê hipóteses de registro em repartição consular ou de opção após a maioridade caso venham residir no Brasil (art. 12, I, "c").
D) **Incorreta.** Trata-se de nacionalidade brasileira NATURALIZADA ordinária (art. 12, II, "a").
E) **Incorreta.** Pela ressalva do *jus soli*, se os pais (estrangeiros) estiverem a serviço de seu país de origem, o filho nascido no Brasil NÃO será brasileiro nato.
</details>

---

### Questão 13 (FCC - 2014 - TRT 19 - Técnico Judiciário)
Sobre a intervenção federal, a Constituição determina que a União NÃO intervirá nos Estados nem no Distrito Federal, EXCETO em determinadas hipóteses, entre as quais encontra-se o fim de:
A) Manter a integridade nacional.
B) Assegurar o pagamento prioritário de dívidas trabalhistas de empresas públicas.
C) Garantir o livre exercício dos Conselhos Tutelares municipais.
D) Promover o processo de reeleição de governadores, quando houver grave perturbação eleitoral.
E) Garantir a plena e irrestrita autonomia financeira das capitais dos Estados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) **Correta.** Art. 34 da CF: "A União não intervirá nos Estados nem no Distrito Federal, exceto para: I - manter a integridade nacional". É hipótese expressa no texto magno para afastar, excepcionalmente, a autonomia estadual/distrital.
B) **Incorreta.** O pagamento de dívida trabalhista de empresas públicas não enseja decretação de intervenção federal na unidade da federação.
C) **Incorreta.** O art. 34, IV, fala em garantir o livre exercício de qualquer dos Poderes nas unidades da Federação, o que não engloba genericamente conselhos tutelares municipais como "poder de Estado".
D) **Incorreta.** Não há qualquer previsão sobre promoção de reeleições para intervenção federal.
E) **Incorreta.** A garantia de autonomia de capitais não consta no rol taxativo do art. 34 da CF/88.
</details>

---

### Questão 14 (FCC - 2013 - TRT 12 - Analista Judiciário)
Acerca da organização político-administrativa da República Federativa do Brasil, é correto afirmar que Brasília, de acordo com o texto da Constituição Federal, é:
A) A Capital Federal.
B) Um Município autônomo integrante do Distrito Federal, com Prefeito eleito.
C) Um Território Federal em fase de transição para se tornar Estado.
D) Um Estado membro da federação brasileira, sem direito de dividir-se em Municípios.
E) Uma Região Administrativa independente e desvinculada tanto da União quanto do Distrito Federal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) **Correta.** Em regra clara e direta, dispõe o art. 18, § 1º, da CF/88: "Brasília é a Capital Federal."
B) **Incorreta.** O Distrito Federal não pode ser dividido em Municípios (art. 32). Brasília não tem status de Município nem possui Prefeito, mas sim de Capital e integra o DF, governado por Governador.
C) **Incorreta.** Territórios Federais (que atualmente não existem) têm regramento próprio e integram a União; o Distrito Federal é ente federativo autônomo, e Brasília sua capital.
D) **Incorreta.** Brasília não é Estado-membro. O ente se chama Distrito Federal, cuja capital é Brasília.
E) **Incorreta.** Brasília integra a organização do Distrito Federal, não sendo "desvinculada" do arranjo federativo.
</details>

---

### Questão 15 (FCC - 2021 - TRT 24 - Analista Judiciário)
Constitui, de forma expressa, um OBJETIVO fundamental da República Federativa do Brasil na Constituição Federal de 1988:
A) Construir uma sociedade livre, justa e solidária.
B) A dignidade da pessoa humana.
C) Os valores sociais do trabalho e da livre iniciativa.
D) A concessão célere e irrestrita de asilo político.
E) O pluralismo político partidário.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) **Correta.** De acordo com o art. 3º, I, da CF/88, é um dos OBJETIVOS fundamentais: "construir uma sociedade livre, justa e solidária". (Dica: os objetivos fundamentais costumam iniciar com verbos no infinitivo: construir, garantir, erradicar e promover).
B) **Incorreta.** A dignidade da pessoa humana é um FUNDAMENTO da República (art. 1º, III).
C) **Incorreta.** Os valores sociais do trabalho e da livre iniciativa são FUNDAMENTOS (art. 1º, IV).
D) **Incorreta.** A concessão de asilo político é um PRINCÍPIO que rege a República nas suas relações internacionais (art. 4º, X).
E) **Incorreta.** O pluralismo político é um FUNDAMENTO (art. 1º, V).
</details>

---


## 📝 TEMA 2: Testes de Software

### Questão 1 (FCC - 2019 - TRF 4ª Região - Analista Judiciário - Sistemas da Informação)
A equipe de desenvolvimento de um tribunal precisa testar uma aplicação com foco exclusivo nas funções e comportamentos externos do sistema, verificando as entradas e saídas sem a necessidade de observar ou conhecer a estrutura interna do código-fonte. Essa técnica é denominada teste de:
A) Caixa preta.
B) Caixa branca.
C) Teste estrutural.
D) Teste de caminho básico.
E) Teste de mutação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) A alternativa está correta. O teste de caixa preta (ou teste funcional) concentra-se em avaliar as funções, requisitos e regras de negócio do sistema. O testador fornece dados de entrada e analisa as saídas correspondentes sem precisar ter acesso ou conhecimento do código-fonte (lógica interna).
B) A alternativa está incorreta. O teste de caixa branca, ao contrário, exige profundo conhecimento da lógica interna, fluxo de dados e da estrutura do código-fonte.
C) A alternativa está incorreta. Teste estrutural é essencialmente um sinônimo e uma categorização de testes de caixa branca, pois avalia estritamente a estrutura interna do programa.
D) A alternativa está incorreta. O teste de caminho básico é uma técnica específica de caixa branca, criada por McCabe, que utiliza o fluxo lógico para desenhar os casos de teste essenciais.
E) A alternativa está incorreta. O teste de mutação insere falhas intencionais (mutantes) no código para validar não a aplicação em si, mas a eficácia da suíte de testes que foi construída para detectá-las.
</details>

---

### Questão 2 (FCC - 2022 - TRT 22ª Região (PI) - Analista Judiciário - Tecnologia da Informação)
No que diz respeito à engenharia de software, o uso das técnicas de particionamento de classes de equivalência e análise de valor limite são classificadas tipicamente como técnicas de projeto de:
A) Caixa preta.
B) Caixa branca.
C) Caixa cinza.
D) Teste de mesa.
E) Teste de integração.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) A alternativa está correta. Particionamento de equivalência e análise de valor limite focam em segmentar e testar os domínios dos dados de entrada e de saída baseando-se no comportamento especificado, sendo as principais técnicas do escopo do teste funcional, isto é, de caixa preta.
B) A alternativa está incorreta. A caixa branca se preocupa com a cobertura do fluxo de controle, como cobertura de comandos, de ramificações e decisões internas.
C) A alternativa está incorreta. A caixa cinza combina validações de comportamento (preta) com acessos pontuais ao banco ou arquitetura (branca), mas essas duas técnicas específicas derivam exclusivamente da base de conhecimentos da caixa preta.
D) A alternativa está incorreta. O teste de mesa é uma técnica estática e manual onde o algoritmo é testado no papel, acompanhando variáveis.
E) A alternativa está incorreta. O teste de integração cuida de validar os componentes ou módulos interagindo entre si, sem ser o guarda-chuva que define o valor limite.
</details>

---

### Questão 3 (FCC - 2018 - TRT 15ª Região (SP) - Analista Judiciário - Tecnologia da Informação)
No contexto de Testes de Software, a etapa focada em verificar e garantir que diferentes componentes, pacotes ou sistemas independentes funcionem corretamente quando combinados ou acoplados para trabalharem juntos, é conhecida como Teste de:
A) Unidade.
B) Integração.
C) Carga.
D) Aceitação.
E) Regressão.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) A alternativa está incorreta. O teste de unidade isola e avalia o comportamento de um micro-componente ou função (método, classe) de forma independente do resto do sistema.
B) A alternativa está correta. A essência do teste de integração é justamente pegar unidades já testadas isoladamente e verificar a interação, comunicação e a passagem de dados (acoplamento) entre elas quando agrupadas.
C) A alternativa está incorreta. Testes de carga avaliam requisitos não funcionais de desempenho, colocando tráfego e volume no sistema.
D) A alternativa está incorreta. A aceitação avalia o sistema pronto, do ponto de vista do usuário final em um ambiente de homologação.
E) A alternativa está incorreta. A regressão atua para assegurar que partes antes funcionais não quebrem ao receber novas atualizações.
</details>

---

### Questão 4 (FCC - 2018 - TRT 6ª Região (PE) - Analista Judiciário - Tecnologia da Informação)
Durante a fase de manutenção de um sistema, a equipe corrige um defeito crítico apontado pelo cliente. Após a aplicação da correção, o engenheiro de qualidade executa um conjunto de casos de teste que já haviam passado em builds anteriores, visando assegurar que a nova alteração não gerou falhas em componentes que funcionavam perfeitamente. Esta prática descreve o Teste de:
A) Estresse.
B) Regressão.
C) Aceitação final.
D) Cobertura de Caminhos.
E) Usabilidade.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) A alternativa está incorreta. O teste de estresse força a aplicação a ir além do seu limite operacional normal para ver quando e como ocorre a falha do sistema.
B) A alternativa está correta. O Teste de Regressão é caracterizado justamente pela reexecução parcial ou total de uma suíte de testes antigos em versões novas. O foco é detectar "regressões", ou seja, defeitos ou efeitos colaterais inseridos acidentalmente em código previamente correto após alguma refatoração ou acréscimo de funcionalidade.
C) A alternativa está incorreta. O teste de aceitação valida o produto em relação à necessidade real de negócio sob os olhos do cliente/usuário.
D) A alternativa está incorreta. Teste de caminhos tem relação com o cálculo de rotas no diagrama de fluxo estrutural, sendo técnica de caixa branca.
E) A alternativa está incorreta. A usabilidade verifica a ergonomia e facilidade de navegação por parte de humanos nas interfaces gráficas.
</details>

---

### Questão 5 (FCC - 2017 - TST - Analista Judiciário - Suporte em Tecnologia da Informação)
Assinale a afirmativa correta no que se refere aos conceitos e aplicação prática de testes de caixa branca e caixa preta.
A) O teste de caixa branca pode ser aplicado sem nenhuma visualização do código-fonte, baseando-se apenas nos casos de uso.
B) O teste de caixa preta também é conhecido como teste comportamental e foca especificamente nas entradas fornecidas e nas saídas obtidas.
C) A análise de valores limites é uma técnica estrutural tipicamente executada nas fases puras do teste de caixa branca.
D) O teste de condição (validação de variáveis booleanas e ifs aninhados) é um excelente exemplo da abrangência do teste de caixa preta.
E) No teste de caixa preta, exige-se que o testador possua elevado conhecimento técnico da linguagem de programação e arquitetura de dados utilizada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) A alternativa está incorreta. Exige-se categoricamente a análise de fluxos estruturais baseados no código-fonte em um teste de caixa branca.
B) A alternativa está correta. A caixa preta avalia o comportamento (daí ser chamado de teste comportamental) ignorando detalhes de implementação. Avaliam-se apenas as entradas e se a saída atende à especificação funcional.
C) A alternativa está incorreta. Análise de valores limite é uma das principais técnicas do teste de caixa preta (funcional).
D) A alternativa está incorreta. Validar condições e fluxos booleanos requer entender a lógica (caminhos no código), sendo tarefa direta do teste de caixa branca.
E) A alternativa está incorreta. É na caixa preta que o testador age sem depender do conhecimento da linguagem, focando nos requisitos do domínio do negócio. Na caixa branca esse conhecimento avançado em código é, de fato, obrigatório.
</details>

---

### Questão 6 (FCC - 2014 - TRF 4ª Região - Analista Judiciário - Informática)
TDD (Test-Driven Development) é uma prática de engenharia de software proveniente dos métodos ágeis (Extreme Programming) e possui como característica fundamental:
A) a realização do teste de aceitação logo antes do levantamento final de requisitos, utilizando prototipagem.
B) a codificação dos testes unitários imediatamente após o código de negócio principal do sistema estar concluído.
C) a escrita de um teste automatizado, que inicializa falhando, precedendo a codificação mínima necessária na funcionalidade para fazê-lo passar e refatorar.
D) o projeto dos testes em conjunto com a arquitetura e normalização do banco de dados relacional (modelo entidade-relacionamento).
E) o papel central exercido pelos analistas de testes manuais, que não dependem do código para realizar suas validações funcionais sistêmicas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) A alternativa está incorreta. TDD diz respeito ao desenvolvimento guiado por testes (focado num nível de unidade/dev), e não se liga a protótipos em levantamentos de requisitos.
B) A alternativa está incorreta. A lógica de fazer o teste APÓS o código fere completamente a filosofia "Test-Driven" (Dirigido por Testes), devendo ser feito o inverso.
C) A alternativa está correta. O núcleo do TDD é o ciclo Red-Green-Refactor. Primeiro escreve-se um teste para a funcionalidade que ainda não existe, ele falhará (Vermelho). Então escreve-se o código de produção mínimo até o teste passar (Verde) e depois melhora-se o código (Refatoração).
D) A alternativa está incorreta. O projeto de banco de dados não tem nenhuma correlação com a escrita sequencial de testes unitários que direcionam o design do código de aplicação.
E) A alternativa está incorreta. TDD é uma técnica intensiva em desenvolvimento de código (orientada aos programadores) voltada aos testes unitários automatizados.
</details>

---

### Questão 7 (FCC - 2015 - TRE-AP - Analista Judiciário - Tecnologia da Informação)
Para assegurar que o portal de serviços do órgão não apresentará quedas na véspera das eleições, a equipe de qualidade decidiu submeter o sistema a um volume extremo de acessos, forçando o sistema para além dos limites operacionais convencionais a fim de investigar pontos de ruptura. Essa técnica é conhecida como teste de:
A) Estresse.
B) Usabilidade.
C) Regressão.
D) Integração.
E) Funcionalidade.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) A alternativa está correta. O teste de estresse (ou sobrecarga extrema) tem como único propósito levar os recursos do sistema ou infraestrutura a um limite além da sua capacidade normal prevista, validando como o sistema reage, falha e eventualmente como ele se recupera.
B) A alternativa está incorreta. Testes de usabilidade referem-se à avaliação das interfaces para facilidade de uso do indivíduo.
C) A alternativa está incorreta. Regressão trata-se de buscar defeitos secundários causados após alguma mudança no sistema.
D) A alternativa está incorreta. O teste de integração verifica apenas os elos e o acoplamento entre os módulos.
E) A alternativa está incorreta. O teste de funcionalidade certifica se os requisitos e os processos de negócio são atendidos sem foco específico em vazões exorbitantes de carga.
</details>

---

### Questão 8 (FCC - 2018 - TRT 2ª Região (SP) - Analista Judiciário - Tecnologia da Informação)
No nível de projeto de testes estruturais (caixa branca), uma métrica importante e um tipo de teste visam quantificar se os comandos individuais do código-fonte e todas as suas decisões ou condicionais foram executados pelo menos uma vez durante a bateria automatizada. Trata-se da técnica de:
A) Teste de mutação.
B) Teste de cobertura de comandos e decisões.
C) Teste baseado em especificação de requisitos.
D) Particionamento de classe de equivalência.
E) Teste de transição de estados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) A alternativa está incorreta. Mutação não avalia execução primária de decisões lógicas, ela introduz pequenos defeitos deliberados para observar se a própria suíte de testes existente detecta essa anomalia ou se o mutante "sobrevive".
B) A alternativa está correta. Cobertura de comandos (ou instruções) mede a proporção de linhas de código que foram ativadas, e a cobertura de decisões (branch coverage) mede se caminhos lógicos (if/else verdadeiros e falsos) foram testados. Pertencem inteiramente à caixa branca.
C) A alternativa está incorreta. Testes com foco exclusivo na especificação descrevem a técnica de caixa preta comportamental.
D) A alternativa está incorreta. Essa técnica visa gerar partições para minimizar testes em domínios longos e representa ferramentas de caixa preta.
E) A alternativa está incorreta. Transição de estados avalia as mudanças lógicas na perspectiva do negócio e comportamentos visíveis do sistema, sendo tipicamente categorizada em caixa preta.
</details>

---

### Questão 9 (FCC - 2019 - TRF 3ª Região - Analista Judiciário - Informática)
Na Engenharia de Software Contemporânea e Métodos Ágeis, o BDD (Behavior-Driven Development) busca alinhar o desenvolvimento de software aos interesses de negócio, e pode ser caracterizado por:
A) promover o desenvolvimento guiado exclusivamente pelos relatórios sintéticos de cobertura de código contínuo (Code Coverage).
B) definir o comportamento do sistema por meio de uma linguagem ubíqua e colaborativa, tipicamente estruturando cenários em linguagem natural através do padrão Dado-Quando-Então (Given-When-Then).
C) terceirizar, perante contratos, toda a construção de testes unitários estruturais à equipe isolada de representantes comerciais (PO).
D) incentivar que casos de teste automatizados sejam abandonados em favor da testagem unicamente manual nas etapas finais de produção.
E) estruturar a arquitetura técnica do código baseando-se primariamente nas restrições de desempenho da linguagem e esquemas de dados de baixo nível.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) A alternativa está incorreta. O BDD não é centrado em relatórios matemáticos de código. Seu foco recai sobre o comportamento documentado que atenda aos requisitos de negócios, garantindo que o que se constrói importa para o usuário.
B) A alternativa está correta. O Behavior-Driven Development encoraja a colaboração e especifica cenários através de uma linguagem comum a todos os times (ubíqua) estruturada pelo padrão "Dado que (contexto)... Quando (ação)... Então (resultado)", permitindo automatizar facilmente as regras do negócio usando ferramentas como Cucumber.
C) A alternativa está incorreta. BDD integra todos do time de modo multidisciplinar ("Três Amigos"), unindo programadores, testadores e o PO. Ele não é uma técnica de terceirização isolada.
D) A alternativa está incorreta. Pelo contrário, o objetivo máximo da sintaxe BDD (Gherkin/Cucumber) é justamente servir de roteiro direto para execução de testes que se tornam facilmente automatizáveis.
E) A alternativa está incorreta. O BDD se concentra nos cenários de negócio, no que o sistema fará do ponto de vista do usuário final, ignorando abordagens baseadas em minúcias arquiteturais de dados de baixo nível.
</details>

---

### Questão 10 (FCC - 2017 - TRT 11ª Região (AM/RR) - Analista Judiciário - TI)
No fim do fluxo tradicional de desenvolvimento e aprovação, um tipo específico de validação tenta atestar a aderência do software aos contratos de requisitos de alto nível. É focado nas necessidades corporativas e executado, muitas vezes, de modo não estruturado ou usando simulações por representantes do cliente. Assinale a alternativa que dá o nome exato desta etapa:
A) Teste Unitário.
B) Teste de Caixa Branca.
C) Teste de Aceitação.
D) Teste de Estresse de Rede.
E) Teste de Fluxo de Dados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) A alternativa está incorreta. O teste unitário ocorre muito cedo, criado por dev, testando se a microcamada técnica do código faz o que deve, distante da aprovação dos requisitos pelo cliente.
B) A alternativa está incorreta. O teste estrutural caixa branca se atém às instruções lógicas da linguagem, inacessíveis à visão do usuário/cliente comum.
C) A alternativa está correta. O Teste de Aceitação é a última barreira formal de validação funcional antes do deploy para produção, e serve para que o cliente ou usuário chave possa confirmar se o software de fato satisfaz às regras negociais para o qual foi idealizado (famosos UAT, Alpha/Beta Testing).
D) A alternativa está incorreta. Um foco de carga de rede enquadra testes de desempenho/comunicação e nada diz sobre se os fluxos funcionais foram aceitos pelo usuário.
E) A alternativa está incorreta. Teste baseado no ciclo de vida de declaração, uso e destruição de variáveis é de caixa branca.
</details>

---

### Questão 11 (FCC - 2015 - TRT 3ª Região (MG) - Analista Judiciário - TI)
Ao projetar casos de teste empregando de maneira técnica e pragmática a Análise de Valor Limite, o engenheiro de testes focará seus esforços em:
A) traçar caminhos completamente independentes dentro dos grafos de controle do diagrama lógico.
B) selecionar minuciosamente valores numéricos, lógicos ou literais que estejam posicionados exatamente nas fronteiras ou bordas extremas das classes de equivalência.
C) explorar vulnerabilidades abertas em brechas de injeção de SQL e desvio de chamadas de buffer (buffer overflow).
D) avaliar as métricas de tempo de resposta dos servidores e latência durante um teste intermitente e prolongado.
E) executar inspeção e revisão do código-fonte manualmente (code review) ao lado dos pares buscando erros lógicos não óbvios.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) A alternativa está incorreta. Grafos de controle e determinação matemática de caminhos referem-se estritamente ao teste de caminho básico (Complexidade Ciclomática / Caixa branca).
B) A alternativa está correta. A literatura e a prática provam que erros acontecem muito mais comumente nas transições de uma classe de equivalência para outra. Portanto, usar testes nas "fronteiras" (por exemplo, se é válido de 1 a 10, testar 0, 1, 10, 11) caracteriza a Análise de Valor Limite, sendo técnica altamente eficiente de caixa preta.
C) A alternativa está incorreta. Esse universo descreve testes de intrusão, segurança e cibersegurança (Security Testing e Pentest).
D) A alternativa está incorreta. Esse escopo recai nos requisitos de testes não funcionais de performance ou carga, onde se medem tempos, latência e gargalos na infra.
E) A alternativa está incorreta. Inspeções, revisões de pares e walkthroughs configuram testes estáticos, muito longe do projeto dinâmico de valores das fronteiras.
</details>

---

### Questão 12 (FCC - 2012 - TST - Analista Judiciário - TI)
A métrica conhecida como "Complexidade Ciclomática", elaborada inicialmente por Thomas McCabe, é frequentemente utilizada nos projetos de testes de software modernos e serve como um forte indicador para:
A) estabelecer o limite quantitativo máximo de acessos simultâneos ao banco de dados e à camada de persistência.
B) calcular matematicamente a quantidade mínima de caminhos básicos independentes, guiando assim o número essencial de casos de teste para cobrir a base lógica estrutural.
C) definir de antemão a variação dimensional das telas para os testes de resolutividade (cross-browser).
D) estimar a aceitação subjetiva da interface por um conjunto restrito de usuários leigos.
E) aferir o grau exato de risco e criptografia exigida nas transações financeiras externas do sistema.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) A alternativa está incorreta. Esse limite é dimensionado em arquitetura, e testado com testes de estresse, sem relação com cálculo ciclomático.
B) A alternativa está correta. A Complexidade Ciclomática é calculada num grafo de nós e arestas (V = A - N + 2). Esse número V indica a quantidade de caminhos independentes do software, permitindo que a equipe planeje o número exato de testes de caixa branca que atinjam toda a cobertura do código.
C) A alternativa está incorreta. A usabilidade cross-browser valida layout e compatibilidade nas visões (front-end), dispensando matrizes ciclomáticas estruturais do código-fonte.
D) A alternativa está incorreta. Aceitação trata do atendimento da satisfação das regras de negócio pelo cliente.
E) A alternativa está incorreta. O foco em riscos criptográficos pertencerá sempre aos testes de segurança do software e compliance.
</details>

---

### Questão 13 (FCC - 2016 - TRT 20ª Região (SE) - Analista Judiciário - TI)
Em um fluxo contínuo de testes de software modernos (especialmente envolvendo DevOps e TDD), a construção de um 'Stub' ou um 'Mock' (dublês de testes) é recomendada tipicamente em baterias de:
A) Usabilidade e GUI, para automatizar cliques sequenciais imitando com perfeição as ações musculares do usuário final.
B) Unidade ou Integração de pequeno escopo, visando simular artificialmente o comportamento de componentes, serviços de terceiros ou métodos que são pesados, lentos, ou ainda não desenvolvidos, para isolar a peça sob teste.
C) Estresse global, para forçar intencionalmente falhas de memória RAM simulando vazamentos (leaks).
D) Aceitação de clientes, garantindo simulações de fidelidade visual da interface frente à concorrência.
E) Segurança e proteção de dados, exercendo a figura isolada de um invasor simulado em testes de intrusão.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) A alternativa está incorreta. Ferramentas de automação de UI como Selenium simulam passos em tela, mas Stubs e Mocks são artifícios implementados programaticamente no código.
B) A alternativa está correta. Dublês de teste, como Stubs e Mocks, são muito úteis na camada Unitária e Integração menor. O princípio básico neles é falsificar (mockar) comportamentos de APIs externas, bancos de dados ou qualquer módulo complexo (que o seu alvo de teste consome), a fim de isolar estritamente seu ambiente.
C) A alternativa está incorreta. Vazamentos de memória não dependem de mocks, e sim de rastreamentos de heap no ambiente de performance.
D) A alternativa está incorreta. Em validações de aceitação do usuário evita-se os mocks para testar o sistema real de forma idêntica à que ele operará no mercado.
E) A alternativa está incorreta. Simulações invasivas pertencem ao domínio dos Ethical Hackers/Testes de Vulnerabilidade, e não usam a teoria de mocks funcionais do TDD.
</details>

---

### Questão 14 (FCC - 2014 - TRT 19ª Região (AL) - Analista Judiciário - TI)
Segundo as boas práticas de Engenharia e Garantia de Qualidade de Software, existe uma forte distinção conceitual sobre as atividades primordiais de "Verificação" e "Validação" (V&V). Assinale a alternativa que as diferencia adequadamente:
A) A Verificação busca atestar se "o software está sendo construído corretamente" de acordo com padrões e designs internos; enquanto a Validação questiona se "o produto certo está sendo construído" e se ele atende plenamente o usuário.
B) A Verificação ocorre unicamente após a entrega do produto final e a Validação acontece exclusivamente e de modo restrito no levantamento de requisitos inicial.
C) Ambas são essencialmente técnicas exclusivas pertencentes ao escopo dos testes de desempenho não funcionais.
D) A Validação avalia única e exclusivamente a qualidade semântica do código-fonte, englobando a caixa branca e refatorações puras, e a Verificação avalia testes finais estressantes.
E) A Verificação é obrigatoriamente de responsabilidade absoluta dos gerentes de projeto, enquanto a Validação é dos programadores júniores em codificação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A) A alternativa está correta. Esta é a famosa máxima definida por Barry Boehm. A Verificação foca nos processos e em atestar que as fases e o produto aderem às especificações técnicas descritas (Estamos construindo o produto do jeito certo?). A Validação avalia o software pronto diante das necessidades e expectativas subjetivas originais do negócio do cliente (Estamos construindo o produto certo para o cliente?).
B) A alternativa está incorreta. As duas correm em paralelo ao longo de quase todo o ciclo, seja de maneira contínua no Ágil ou com marcos delimitados nos modelos tradicionais.
C) A alternativa está incorreta. Ambas são dimensões que englobam a totalidade dos esforços de testes e qualidade, ultrapassando questões meramente dimensionadas ao desempenho.
D) A alternativa está incorreta. Na verdade a verificação detém o maior foco em códigos e documentações internas (garantir padrões técnicos/caixa branca). A validação recai primordialmente no teste do comportamento aos olhos do cliente/caixa preta ou aceitação.
E) A alternativa está incorreta. Não se pode isolar e definir arbitrariamente por nível hierárquico (como gerentes x júniores) papéis que fluem organicamente envolvendo Dev, QA e PO no processo produtivo da organização.
</details>

---

### Questão 15 (FCC - 2022 - TRT 5ª Região (BA) - Analista Judiciário - TI)
Dentre as abordagens especializadas e complexas de garantia de qualidade na engenharia de testes, o teste estrutural denominado "Teste de Mutação" é empregado visando:
A) validar constantemente se os requisitos operacionais que não influenciam no produto mudaram de escopo e sentido ao longo do tempo.
B) avaliar, com viés métrico, a real eficácia do conjunto de casos de teste automatizados existente introduzindo intencionalmente pequenas falhas isoladas ("mutantes") no código de produção.
C) monitorar intermitentemente as instabilidades e como o binário se comporta diante das intensas mutações contínuas provenientes de falhas de hardware no servidor de infraestrutura.
D) realizar testes visuais em série na interface do usuário (UI/UX) avaliando sua resiliência a dispositivos móveis flutuantes e mutações de tela responsivas (media queries).
E) fornecer ferramentas de orquestração automatizada para converter testes unitários antigos e complexos (caixa branca) para testes macro e puros de sistema e aceitação (caixa preta).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) A alternativa está incorreta. A atividade de validar mudanças em requisitos de projeto não remete a um tipo de testagem baseada em mutação, mas sim na gestão de ciclo de vida e requisitos de mudança corporativa.
B) A alternativa está correta. O Teste de Mutação atua no âmago da avaliação qualitativa dos próprios casos de teste existentes. Pequenos bugs cirúrgicos (alterar um '+' por um '-') são plantados e chamados de "mutantes". Roda-se os testes: o que passar está errado, e o teste que falhar e capturar a discrepância "matou o mutante". Testes blindados matam todos eles.
C) A alternativa está incorreta. Fatorar e analisar instabilidades em hardwares ou dependências na borda da infra refere-se a engenharia de confiabilidade (Chaos Engineering ou testes robustez), mas não ao rigor do "Teste de Mutação".
D) A alternativa está incorreta. Essa afirmação confunde o escopo voltando para validação da Interface de Usuário adaptativa ou responsiva para web, algo absolutamente distinto de alterar o código de produção logicamente de forma intencional para verificação da suíte.
E) A alternativa está incorreta. Na engenharia é virtualmente impossível orquestrar uma mudança estrutural (caixa branca, lógica condicional) de modo linear para um teste comportamental orientado à tela de usuário sem um alto nível de interpretação, e o Teste de Mutação não tem esse papel tradutório na sua essência.
</details>


