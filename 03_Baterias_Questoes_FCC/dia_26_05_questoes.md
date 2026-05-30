# Bateria de Questões FCC — Terça-feira 26/05

## 📝 TEMA 1: Arquitetura de Software e Padrões de Projeto

### Questão 1 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - Tecnologia da Informação)
No padrão de arquitetura MVC (Model-View-Controller), o componente responsável por intermediar as requisições enviadas pelo usuário através da View, manipular os dados no Model e retornar a resposta adequada é o:
A) Front Controller.
B) Model.
C) Controller.
D) View.
E) DAO (Data Access Object).
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. O Front Controller é um padrão de projeto estrutural (frequentemente usado junto ao MVC em sistemas web para interceptar todas as requisições em um ponto central), mas não é o componente padrão do MVC clássico definido para as funções essenciais descritas na questão.
B) Incorreta. O Model (Modelo) é responsável pela lógica de negócios, gestão do estado da aplicação e acesso aos dados. Ele não faz o intermédio entre as requisições da View e ele mesmo.
C) Correta. O Controller (Controlador) atua de fato como o mediador/intermediador. Ele recebe a entrada (evento/requisição) da View, processa as regras de controle ou solicita as ações necessárias ao Model e atualiza a View com o resultado.
D) Incorreta. A View (Visão) é responsável puramente pela interface com o usuário e pela apresentação visual dos dados, não intermediando as requisições nem manipulando os dados diretamente no Model.
E) Incorreta. O DAO (Data Access Object) é um padrão que provê uma interface abstrata para acesso a dados, ocultando detalhes do banco de dados, sem qualquer responsabilidade de intermediar lógicas de interface do MVC.
</details>

---

### Questão 2 (FCC - 2019 - TRF 3ª Região - Analista Judiciário - Informática)
Na utilização de padrões de projeto (Design Patterns) do catálogo GoF (Gang of Four), existe um padrão estrutural que fornece uma interface unificada para um conjunto de interfaces em um subsistema, definindo uma interface de nível mais alto que torna o subsistema mais fácil de ser usado. Trata-se do padrão:
A) Decorator.
B) Adapter.
C) Proxy.
D) Facade.
E) Composite.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A) Incorreta. O Decorator serve para anexar responsabilidades adicionais a um objeto de forma dinâmica, fornecendo uma alternativa viável ao uso de subclasses para estender funcionalidades, não unificando interfaces de um subsistema.
B) Incorreta. O Adapter converte a interface de uma classe existente em outra interface esperada pelos clientes, permitindo que classes com interfaces diferentes trabalhem em conjunto, o que não cria uma interface de nível mais alto para múltiplos subsistemas.
C) Incorreta. O Proxy fornece um substituto ou um marcador (placeholder) para outro objeto a fim de controlar o acesso a ele.
D) Correta. O padrão Facade (Fachada) tem exatamente essa função estrutural no GoF: ele mascara a complexidade de um subsistema inteiro ao fornecer uma única interface unificada e simplificada (de alto nível) para que os clientes interajam.
E) Incorreta. O Composite serve para compor objetos em estruturas de árvore que representam hierarquias partes-todo, permitindo o tratamento de classes individuais e composições uniformemente.
</details>

---

### Questão 3 (FCC - 2017 - TRE-SP - Analista Judiciário - Análise de Sistemas)
Um dos padrões de projeto comportamentais do GoF define uma dependência um-para-muitos entre objetos, de maneira que, quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente. Esse padrão é conhecido como:
A) Strategy.
B) Command.
C) Observer.
D) State.
E) Mediator.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. O Strategy encapsula uma família de algoritmos e os torna intercambiáveis, focando na flexibilidade da escolha do algoritmo em tempo de execução.
B) Incorreta. O Command encapsula solicitações como objetos paramétricos, permitindo criar filas de requisições, log e suporte para operações de desfazer/refazer.
C) Correta. O Observer estabelece uma típica arquitetura de publicador e assinantes (Publisher/Subscriber). Nele há o "Subject" que, quando sofre alteração de estado interno, realiza um broadcast automático de notificação para seus dependentes (Observers).
D) Incorreta. O State permite a um objeto mudar seu comportamento dependendo de alterações ocorridas no seu estado interno, de modo que parece que o próprio objeto trocou de classe.
E) Incorreta. O Mediator define um objeto central para encapsular como um conjunto de objetos interagem entre si, reduzindo o acoplamento excessivo (many-to-many) promovendo comunicação isolada através dele.
</details>

---

### Questão 4 (FCC - 2022 - TRT 22ª Região - Analista Judiciário - TI)
A arquitetura de microsserviços é uma abordagem para desenvolver um aplicativo único como um conjunto de pequenos serviços autônomos. Uma das características que a distingue de uma arquitetura monolítica tradicional é:
A) A utilização de um único banco de dados centralizado obrigatoriamente compartilhado por todos os microsserviços do sistema.
B) O alto e forte acoplamento entre os módulos em código-fonte, visando otimizar a performance por chamadas na mesma memória.
C) A implantação de todos os componentes da aplicação condensados em um único processo físico.
D) A governança de dados descentralizada, em que cada serviço isola e gerencia seu próprio banco de dados e esquema.
E) A padronização corporativa restrita de uma única linguagem de programação obrigatória para toda a solução.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A) Incorreta. Os microsserviços desencorajam fortemente bancos de dados unificados (Shared Database Pattern), pois isso cria pontos únicos de falha e acoplamento forte entre serviços.
B) Incorreta. A meta máxima dos microsserviços é garantir um BAIXO acoplamento. A comunicação geralmente ocorre por rede, o que reduz performance bruta, mas eleva a flexibilidade.
C) Incorreta. Empacotar tudo em um único processo e diretório define essencialmente um padrão arquitetural monolítico, o oposto de microsserviços.
D) Correta. Em microsserviços, preconiza-se a gestão de dados descentralizada. Se há o serviço de Pagamentos e o de Clientes, cada um deles detém posse, autonomia e isolamento de seus respectivos bancos de dados.
E) Incorreta. A arquitetura de microsserviços apoia fortemente o uso de "tecnologias poliglotas", permitindo que cada serviço adote a stack (linguagem/banco) que melhor resolva seu domínio específico.
</details>

---

### Questão 5 (FCC - 2018 - TRT 2ª Região - Analista Judiciário - TI)
Na arquitetura REST (Representational State Transfer), o princípio fundamental denominado de "Stateless" (sem estado) determina que:
A) As sessões e histórico dos clientes devem ser salvos persistentemente no cache interno do servidor web.
B) A arquitetura requer que o servidor retenha em memória todos os atributos de estado entre cada requisição feita pelo cliente.
C) Cada requisição do cliente para o servidor deve conter todas as informações contextuais necessárias para sua interpretação e processamento.
D) O cliente perde o estado atual da aplicação, restando ao servidor a exclusiva responsabilidade de gerar interfaces fixas.
E) É proibido ao servidor alterar os dados mantidos no banco de dados, configurando serviços estritamente de leitura.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. Armazenar estado da sessão do cliente no servidor viola diretamente o requisito de que o servidor deve ser stateless.
B) Incorreta. Assim como a alternativa A, reter contexto de estado na memória do servidor para amarrar requisições cria forte dependência, impossibilitando escalabilidade facilitada, o que o REST proíbe.
C) Correta. Pelo princípio Stateless, o servidor não armazena nenhuma sessão em memória a respeito do cliente. Logo, toda requisição feita pelo cliente (como pedir um saldo ou gerar um relatório) deve enviar também o estado (tokens de autenticação, parâmetros de busca etc.) necessário para executá-la isoladamente.
D) Incorreta. É o cliente (e não o servidor) que deve manter em suas mãos o estado transitório da sessão ou tela (Client-Side State).
E) Incorreta. O servidor gerencia os "Recursos" do sistema e pode, sim, alterar o banco de dados livremente (através de POST, PUT, DELETE, etc.). O termo "sem estado" aplica-se ao estado conversacional da comunicação, e não aos dados reais.
</details>

---

## 📝 TEMA 2: Integração Contínua e DevOps

### Questão 6 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - TI)
A Integração Contínua (Continuous Integration - CI) é uma prática de desenvolvimento de software em que a equipe integra e valida o código frequentemente. Dentre as exigências para o sucesso da Integração Contínua, destaca-se:
A) O uso estrito de branches de desenvolvimento isoladas por longos meses, integrando o código uma única vez antes da entrega.
B) A automação da compilação e execução de testes após cada commit efetuado no repositório de controle de versão.
C) A não utilização de suítes de testes unitários para priorizar construções rápidas e delegar a verificação aos testadores manuais no fim do ciclo.
D) A proibição de deploys automatizados, assegurando que toda construção de código dependa de revisões físicas demoradas e complexas.
E) A implantação e liberação automática para os usuários finais (Continuous Deployment) sempre que houver falhas no pipeline para forçar correções emergenciais.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) Incorreta. O uso de "Long-lived branches" (ramificações longas e raramente mescladas) culmina em pesados problemas de conflitos de código ("Integration Hell"), sendo uma prática avessa à CI, que pede integrações diárias ou várias vezes ao dia.
B) Correta. A essência do CI é a verificação automática de integração cada vez que um desenvolvedor submete um novo código. O servidor de CI detecta a mudança, compila (build) a aplicação, executa os testes automatizados e retorna um feedback rápido em caso de quebras.
C) Incorreta. Os testes automatizados (unitários, integração) são o pilar da verificação do CI. Remover esses testes destrói a segurança da prática e impede a validação real de que nada foi quebrado.
D) Incorreta. Processos demorados e estritamente manuais sem automação quebram a cultura de agilidade e feedback contínuo.
E) Incorreta. Uma liberação automática para produção só ocorre no "Continuous Deployment" e somente se TODAS as etapas (compilação e testes) passarem sem erros. Falhas bloqueiam o processo imediatamente, impedindo entregas danosas ao usuário.
</details>

---

### Questão 7 (FCC - 2019 - TRF 3ª Região - Técnico Judiciário - Informática)
O Docker popularizou a virtualização baseada em contêineres na indústria. Sobre os conceitos fundamentais desta tecnologia em ambientes DevOps, é correto afirmar:
A) A Imagem Docker é uma instância transiente e em execução de um Contêiner empacotado.
B) O Contêiner Docker usa emulação de hardware, encapsulando um kernel hospedeiro inteiro com um Guest OS pesado.
C) O arquivo Dockerfile consiste em um documento textual determinístico que contém as instruções para o Docker construir uma Imagem.
D) Contêineres Docker são projetados de forma a não possuir nenhum tipo de isolamento de processos nem de redes, operando exatamente como processos nativos compartilhados.
E) O Docker Compose é utilizado primariamente para construir e gerenciar grandes clusters multimáquinas geodistribuídos em ambientes cloud.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. A definição está propositalmente invertida: o Contêiner é que é a instância (em execução) derivada de uma Imagem Docker (que é o template estático, inativo).
B) Incorreta. O Docker não realiza emulação de hardware com um Sistema Operacional Convidado (Guest OS) para cada contêiner — isso é feito pelas Máquinas Virtuais (VMs). O Docker compartilha o Kernel do Sistema Operacional nativo do Host.
C) Correta. O Dockerfile é uma receita de instruções sequenciais (`FROM`, `RUN`, `COPY`, `CMD` etc.) utilizadas pela engine do Docker para criar as camadas de uma nova Imagem de maneira automatizada e documentada.
D) Incorreta. Embora sejam mais leves, os contêineres Docker fornecem um altíssimo grau de isolamento em nível de SO (usando `namespaces` e `cgroups` do Linux) separando processos, montagens e redes.
E) Incorreta. O Docker Compose é usado para orquestrar múltiplos contêineres apenas em ambientes de máquina única (single-host) para desenvolvimento. Para clusters em múltiplos nós e nuvem, usa-se Docker Swarm ou Kubernetes.
</details>

---

### Questão 8 (FCC - 2021 - TRT 6ª Região - Analista Judiciário - TI)
No Kubernetes (K8s), a orquestração de ambientes conteinerizados escaláveis requer conhecimentos de seus componentes. A menor unidade atômica computacional que pode ser implantada, criada e gerenciada nativamente pela plataforma e que representa um conjunto de um ou mais contêineres é chamada de:
A) ReplicaSet.
B) Pod.
C) Node.
D) Ingress.
E) Cluster.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) Incorreta. O ReplicaSet gerencia a garantia da existência e replicação em execução de um número "X" especificado daquela unidade atômica.
B) Correta. O "Pod" é o menor e mais básico objeto dentro do universo Kubernetes. O Kubernetes não implanta ou interage diretamente com "contêineres individuais", mas empacota um (mais comum) ou múltiplos contêineres estreitamente acoplados num único Pod, compartilhando volumes de rede e de armazenamento (mesmo IP e localhost).
C) Incorreta. O Node (Nó) representa a máquina (virtual ou física) do cluster, onde o agente Kubelet opera e hospeda fisicamente a alocação dos Pods.
D) Incorreta. Ingress é um objeto que gerencia as regras de acesso externo (como HTTP/HTTPS, balanceamento de carga, terminação SSL) para alcançar os serviços internos.
E) Incorreta. O Cluster é toda a junção do Control Plane (Gerência central) mais os inúmeros Nodes de processamento.
</details>

---

### Questão 9 (FCC - 2022 - TRT 22ª Região - Analista Judiciário - TI)
Como uma das práticas avançadas no pilar de automação da cultura DevOps, a Infraestrutura como Código (Infrastructure as Code - IaC) apresenta diversos benefícios. Um dos objetivos diretos e corretos do emprego de ferramentas de IaC (como Terraform ou Ansible) é:
A) Substituir os processos diários de backup de bancos de dados por códigos declarativos nos servidores.
B) Reduzir drasticamente o controle de versão para os artefatos de infraestrutura, garantindo independência do setor de operações.
C) Centralizar toda a gestão de configurações através de pesadas e lentas intervenções via interface gráfica de painéis em Cloud (ClickOps).
D) Possibilitar que ambientes inteiros sejam provisionados de forma rápida, repetível, idempotente e documentada em arquivos legíveis por humanos e máquinas.
E) Impedir implantações automatizadas em ambientes híbridos, bloqueando integração de serviços on-premise com recursos em nuvem pública.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A) Incorreta. O IaC gerencia infraestrutura (redes, instâncias, firewall), mas a garantia e o plano de continuidade de rotinas de backup de dados gerados pelos sistemas (dados de tabelas) vão muito além do mero IaC.
B) Incorreta. O IaC baseia-se exatamente NO AUMENTO DO USO do controle de versão (Git) aplicado às operações (GitOps), trazendo o rigor do código fonte para a infraestrutura.
C) Incorreta. A Infraestrutura como Código combate radicalmente as intervenções e gestões via click (ClickOps). O uso de painéis lentos e guiados por interface web são desencorajados em prol de scripts executáveis e automatizados.
D) Correta. A essência do IaC é fornecer ambientes seguros. Se um ambiente de desenvolvimento precisar ser levado para testes, basta executar o mesmo script, o que provê repetibilidade confiável, auditoria, segurança e documentação da infraestrutura vigente (idempotência nas ferramentas declarativas).
E) Incorreta. O IaC lida perfeitamente bem com ambientes multiplataformas, híbridos e multi-cloud. O Terraform, por exemplo, dispõe de centenas de "Providers" que cobrem redes tanto na AWS quanto em VMware interno na organização.
</details>

---

### Questão 10 (FCC - 2017 - TST - Analista Judiciário - Suporte em TI)
Em um pipeline completo sob os paradigmas do DevOps, é essencial diferenciar "Entrega Contínua" (Continuous Delivery) de "Implantação Contínua" (Continuous Deployment). A diferença conceitual mais expressiva e correta entre essas duas esteiras automatizadas é que:
A) Na Entrega Contínua o código é liberado para produção sem intervenção humana, enquanto a Implantação Contínua paralisa o código no teste unitário.
B) Na Implantação Contínua os testes devem ser executados apenas manualmente por analistas de qualidade (QA), em contraste com a Entrega Contínua.
C) A Implantação Contínua envia o artefato homologado automática e diretamente para a produção caso todos os testes passem, não existindo aprovação humana, enquanto na Entrega Contínua o deploy em produção necessita de aprovação e acionamento humano explícito.
D) A Entrega Contínua foca unicamente em infraestruturas baseadas em contêineres (Docker), ignorando o pipeline lógico, diferentemente da Implantação Contínua.
E) Ambos possuem rigorosamente o mesmo significado na literatura ágil, sendo o termo "Deployment" usado exclusivamente no Brasil.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. A definição exposta na afirmativa inverte frontalmente o conceito. O que ocorre sem intervenção (automático) é a Implantação Contínua.
B) Incorreta. Tanto CD (Entrega) quanto CD (Implantação) requerem baterias massivas de testes automatizados e desprezam a validação totalmente manual como via de regra de pipeline.
C) Correta. A principal linha divisória é a aprovação humana de liberação em negócios. Continuous Delivery garante que sua aplicação PODE ser implantada na produção a qualquer momento de forma segura (botão disponível). Continuous Deployment vai além: a implantação na produção É a última etapa da esteira automatizada sem clicar de botões, confiando-se 100% no suite de testes.
D) Incorreta. As práticas citadas dizem respeito à engenharia de liberação de software de forma independente da tecnologia final adotada (contêineres, VMs, Serverless etc).
E) Incorreta. Existe uma clara divergência conceitual e técnica formal em âmbito internacional no papel humano de aceite final (Release) perante a engenharia de software e os guias DevOps.
</details>

---

## 📝 TEMA 3: Direito Constitucional

### Questão 11 (FCC - 2018 - TRT 15ª Região - Técnico Judiciário - Área Administrativa)
Um servidor público necessita de acesso a informações e registros referentes à sua própria pessoa constantes de um complexo banco de dados pertencente a um órgão governamental, mas o órgão se recusa ilicitamente a fornecer a informação. Conforme os direitos e garantias fundamentais previstos na Constituição Federal de 1988 (Art. 5º), o remédio constitucional apto para sanar este tipo de lesão é o:
A) Mandado de Injunção.
B) Habeas Corpus.
C) Mandado de Segurança.
D) Habeas Data.
E) Ação Civil Pública.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A) Incorreta. O Mandado de Injunção é utilizado quando há omissão legislativa total ou parcial (falta de norma regulamentadora) que torne inviável o exercício de direitos previstos constitucionalmente.
B) Incorreta. O Habeas Corpus tem o escopo exclusivo de combater ou ameaçar combater violências e coações contra a liberdade de locomoção (direito de ir e vir).
C) Incorreta. O Mandado de Segurança protege direito líquido e certo não amparado por *Habeas Corpus* nem por *Habeas Data*. É uma regra residual e subsidiária perante informações pessoais, visto que existe ação específica.
D) Correta. Nos termos do art. 5º, inciso LXXII, CF/88, o Habeas Data será concedido para assegurar o conhecimento de informações relativas à pessoa do impetrante (informações personalíssimas), constantes de registros ou bancos de dados de entidades governamentais ou de caráter público. 
E) Incorreta. A Ação Civil Pública é promovida (frequentemente pelo Ministério Público) com o fim de proteger direitos difusos e coletivos perante meio-ambiente, consumidor etc., não informações sobre indivíduo em específico.
</details>

---

### Questão 12 (FCC - 2019 - TRF 4ª Região - Analista Judiciário - Área Judiciária)
Em regra geral expressa no Art. 37 da Constituição Federal acerca da Administração Pública, veda-se estritamente a acumulação remunerada de cargos públicos. No entanto, a referida norma exsurge com exceções pontuais onde a acumulação lícita é autorizada, desde que observada rigorosamente a compatibilidade de horários, como, por exemplo, na acumulação de:
A) Um cargo técnico do Judiciário com um cargo isolado em comissão de livre nomeação.
B) Dois cargos ou empregos unicamente privativos de profissionais de saúde, possuindo ambos profissões regulamentadas.
C) Três cargos na esfera do magistério estadual e municipal.
D) Um cargo de médico em uma fundação pública com outros dois cargos em autarquias em municípios vizinhos.
E) Um mandato de Prefeito Municipal concomitantemente com os vencimentos de proventos de dois cargos inativos de segurança.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A) Incorreta. O exercício em cargo comissionado por quem possui cargo técnico efetivo implica dedicação ao cargo comissionado (não se trata de acumular duas matrículas para desempenhos simultâneos, o servidor afasta-se para exercer o comissionado com opção de remuneração ditada na lei do ente).
B) Correta. O artigo 37, inciso XVI, "c" da Constituição Federal autoriza de forma expressa a acumulação de "dois cargos ou empregos privativos de profissionais de saúde, com profissões regulamentadas". 
C) Incorreta. O limite máximo da norma para magistério não admite três vínculos, mas sim a estrita de "dois cargos de professor" (art. 37, XVI, "a").
D) Incorreta. Estaríamos diante de três cargos para profissionais de saúde (um médico e outros dois), o que extrapola a baliza rígida de "dois cargos". Tripla acumulação para esta categoria é vedada pelo STF.
E) Incorreta. Conforme o Art. 38, o agente investido em mandato de Prefeito precisará licenciar-se de seu cargo originário e exercer a escolha opcional de remuneração, sendo vetada também qualquer quebra do teto remuneratório em acumulações anômalas com Segurança.
</details>

---

### Questão 13 (FCC - 2021 - TRT 6ª Região - Técnico Judiciário - Área Administrativa)
A Constituição da República de 1988 dotou o Supremo Tribunal Federal (STF) da importante prerrogativa de editar Súmulas Vinculantes (Art. 103-A), ferramenta criada na Emenda Constitucional nº 45. Sobre este instrumento, é pertinente afirmar que:
A) Pode versar sobre matéria puramente infraconstitucional, em caso de severas divergências nas justiças estaduais.
B) Obriga estritamente e exime de sua aplicação imediata todos os demais órgãos do Poder Judiciário, mas não incide o seu poder na administração pública do Poder Executivo estadual e municipal.
C) Exige-se que sua aprovação, bem como sua posterior revisão ou mesmo cancelamento no plenário, seja respaldada por um quórum de dois terços dos seus membros constituintes (oito Ministros).
D) A edição não poderá, sob nenhuma hipótese, ser provocada, mas será executada de ofício, com caráter monopolista de iniciativa, de forma irretratável, por seu Presidente.
E) O Defensor Público Geral da União consta nas opções entre os legitimados sem permissão para propor, revisar ou editar.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A) Incorreta. A súmula vinculante, de acordo com o texto da Constituição, só tem cabimento acerca de interpretações válidas atinentes a matéria unicamente "constitucional".
B) Incorreta. A súmula terá efeito perante todos os "órgãos do Poder Judiciário" e abrange totalmente a "Administração Pública direta e indireta nas esferas federal, estadual e municipal" (mas não vincula o Poder Legislativo na sua função legiferante).
C) Correta. A aprovação, revisão ou o cancelamento da Súmula Vinculante pelo STF será feita somente se acatada pela ampla e qualificada maioria de dois terços dos seus membros (dois terços de onze membros = 8 Ministros da Corte).
D) Incorreta. As Súmulas podem ser aprovadas "de ofício ou por provocação". O poder de proposição da súmula vinculante existe na lei para entes arrolados no art. 103.
E) Incorreta. A Lei 11.417/2006 explicitou os legitimados e o art. 103-A remete à Constituição a indicação da ampla gama daqueles que detêm a possibilidade de provocar este recurso, incluído a Defensoria.
</details>

---

### Questão 14 (FCC - 2017 - TST - Técnico Judiciário - Área Administrativa)
No que tange aos direitos de Nacionalidade (art. 12 da Constituição Federal), entende-se por critério válido, sendo considerados brasileiros natos:
A) Os originários de países de língua portuguesa, como Angola, que possuam de forma comprovada idoneidade moral, além da residência ininterrupta no Brasil por longos dois anos.
B) Os que nasceram na República Federativa do Brasil, filhos exclusivos de pais estrangeiros, desde que ambos esses genitores alienígenas estejam prestando serviços ao seu país de origem em uma representação consular em São Paulo.
C) Os cidadãos de Portugal, após cinco anos ininterruptos residentes nos estados da união com requisição aprovada junto ao ministério de Relações Exteriores e Justiça.
D) Os nascidos no estrangeiro, sendo de pai brasileiro ou de mãe brasileira, desde que qualquer um dos pais esteja oficialmente a serviço da República Federativa do Brasil.
E) Os nascidos em território estrangeiro de pai brasileiro, não sendo registrados na respectiva embaixada ou repartição consular e que decidam jamais retornar nem vir ao Brasil possuindo assim cidadania transnacional por mera descendência sanguínea.
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A) Incorreta. Indivíduos enquadrados neste aspecto não detêm o pódio de brasileiros natos, e sim de brasileiros naturalizados (naturalização ordinária de países lusófonos - um ano apenas).
B) Incorreta. Se nascer no Brasil de pais estrangeiros que estejam ambos prestando serviços ou trabalhando pelo respectivo país em terras tupiniquins (diplomatas), não receberá a nacionalidade nata (exceção à regra do *jus soli* fixada no art. 12, I, a).
C) Incorreta. Os portugueses recebem tratamento próprio em lei que gera equiparação legal e reciprocidade com sua naturalização, não sendo por óbvio "brasileiros natos".
D) Correta. Trata-se do clássico e explícito critério "jus sanguinis + critério funcional" contido na alínea "b" do art. 12, I, em que o filho de brasileiros que preste qualquer ofício ao Brasil (esferas ou estados da federação e suas entidades) no exterior é, desde já e para sempre, considerado um brasileiro nato.
E) Incorreta. Não basta descendência para os demais sem a filiação formal (registro na repartição consular) ou, caso ausente a última, a futura vinda a residir no Brasil com subsequente opção formal pelo título nos tribunais maiores (alínea "c").
</details>

---

### Questão 15 (FCC - 2018 - TRT 2ª Região - Analista Judiciário - Área Administrativa)
Considerando a organização dos poderes e órgãos constitucionais pátrios (Das Funções Essenciais à Justiça), qual instituição encontra-se expressamente amparada pela definição permanente, incumbida fundamentalmente da orientação jurídica de necessitados e responsável pela promoção dos direitos humanos, defendendo as frentes judiciais e extrajudiciais dos direitos individuais e coletivos, de forma integral e totalmente gratuita aos cidadãos de menor renda?
A) O Ministério Público.
B) O Conselho Nacional de Justiça.
C) O Ministério da Justiça e Cidadania da União.
D) A Defensoria Pública.
E) A Advocacia e Ordem dos Advogados (OAB).
<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A) Incorreta. O Ministério Público foca precipuamente na defesa e vigia da ordem jurídica geral, o resguardo do regime democrático de direitos, mas não foca a sua missão institucional direta na advocacia gratuita orientadora de "necessitados" em caráter exclusivo. 
B) Incorreta. O Conselho Nacional de Justiça atua precipuamente visando controle e controle disciplinar, não desempenhando jamais a função de procuradoria ou advocatícia para hipossuficientes.
C) Incorreta. Trata-se do ramo do executivo focado nas macropolíticas criminais, mas que não advoga gratuita nem compõe as Funções Essenciais descritas nesse texto normativo de defesa da população sem renda.
D) Correta. O comando da questão espelha de forma absolutamente idêntica a disposição trazida no art. 134, *caput*, da CF/88, o qual coroa e estabelece perfeitamente o escopo total que cabe à Defensoria Pública como um instrumento promotor da democracia e assistência jurídica integral a todos que comprovem carência econômica.
E) Incorreta. Os advogados são essenciais também, mas a OAB é uma entidade particular e de classe que não carrega a exigência magna institucional para o ônus financeiro gratuito contínuo nos estados providos por orçamentos em prol dos necessitados.
</details>
