# Bateria de Questões FCC — Quarta-feira 27/05

## 📝 TEMA 1: Programação Web Java/Spring

### Questão 1 (FCC - 2022 - TRT 22ª Região (PI) - Analista Judiciário - TI)
No contexto da criação de API REST com Spring Boot, qual anotação combina a funcionalidade das anotações `@Controller` e `@ResponseBody`, indicando que os dados retornados por cada método serão gravados diretamente no corpo da resposta (response body) no formato JSON ou XML em vez de renderizar um template (view)?
A) @ApiResource
B) @RestController
C) @WebMapping
D) @Controller
E) @ResponseBody

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A alternativa correta é a **B**, pois a anotação `@RestController` é uma anotação de conveniência no Spring Framework que é internamente anotada com `@Controller` e `@ResponseBody`. Essa junção simplifica a criação de controladores RESTful, garantindo que o retorno dos métodos vá diretamente para o corpo da resposta HTTP (em JSON, XML, etc.), não sendo necessário anotar cada método individualmente com `@ResponseBody`.

Análise das demais alternativas:
- **A) @ApiResource:** Essa anotação não é um padrão do Spring Framework para criação de controladores. Ela se assemelha mais a anotações de outras bibliotecas ou de frameworks em outras linguagens.
- **C) @WebMapping:** Não existe tal anotação no Spring. As anotações de mapeamento padrão são `@RequestMapping`, `@GetMapping`, `@PostMapping`, etc.
- **D) @Controller:** Embora seja usada para criar controladores, o padrão é retornar uma "View" (template HTML). Para criar uma API REST retornando JSON, seria necessário adicionar `@ResponseBody` em cima de cada método ou da própria classe separadamente. Portanto, ela sozinha não combina as duas funções exigidas no enunciado.
- **E) @ResponseBody:** Esta anotação indica que o valor retornado do método será inserido no corpo da resposta da web. No entanto, ela não marca a classe como um controlador (componente gerenciado pelo Spring MVC). Ela é uma das partes que compõem o `@RestController`.
</details>

---

### Questão 2 (FCC - 2018 - TRT 6ª Região (PE) - Analista Judiciário - TI)
Em uma aplicação Java utilizando Spring Data JPA, a interface base primária fornecida pelo framework que provê métodos padronizados para realizar operações genéricas de CRUD (Create, Read, Update, Delete) em uma entidade específica é a:
A) SessionFactory
B) JpaOperations
C) CrudRepository
D) EntityManager
E) TransactionTemplate

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A alternativa correta é a **C**. A interface `CrudRepository` é fornecida pelo Spring Data para implementar rapidamente operações CRUD de forma genérica para as entidades da aplicação. Através de métodos embutidos como `save()`, `findById()`, `findAll()` e `delete()`, o desenvolvedor não precisa escrever código SQL ou JPQL repetitivo para as ações básicas.

Análise das demais alternativas:
- **A) SessionFactory:** Pertence ao Hibernate nativo, servindo como uma fábrica de sessões para comunicação com o banco de dados. Não é a interface de CRUD do Spring Data JPA.
- **B) JpaOperations:** Não é uma interface utilizada como base para repositórios. No Spring, interfaces como `JpaRepository` estendem `PagingAndSortingRepository`, que por sua vez estende `CrudRepository`.
- **C) EntityManager:** É uma interface da especificação JPA (Java Persistence API) responsável por gerenciar o ciclo de vida das entidades. O Spring Data abstrai o uso direto do EntityManager utilizando os repositórios (como o CrudRepository).
- **D) EntityManager:** Resposta repetida por equívoco na formulação desta justificativa, sua explicação está no item C.
- **E) TransactionTemplate:** Trata-se de uma classe do Spring focada no gerenciamento programático de transações, não em operações de persistência CRUD.
</details>

---

### Questão 3 (FCC - 2016 - TRT 20ª Região (SE) - Analista Judiciário - TI)
No ecossistema do Spring Framework, a injeção de dependência (Dependency Injection) é o conceito central da Inversão de Controle (IoC). A anotação padrão do Spring que permite injetar as dependências automaticamente (autowiring) em um bean a partir de atributos, construtores ou métodos setter, é a:
A) @Dependency
B) @InjectBean
C) @ResourceInject
D) @Autowired
E) @WireBean

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A alternativa correta é a **D**. A anotação `@Autowired` é a assinatura registrada do Spring para marcar onde uma injeção de dependência deve ocorrer. O Spring tentará encontrar um Bean compatível no ApplicationContext e associá-lo automaticamente no atributo, construtor ou método anotado.

Análise das demais alternativas:
- **A) @Dependency:** Esta anotação não existe na API padrão do Spring.
- **B) @InjectBean:** Anotação fictícia. Na especificação padrão CDI (Java EE), a anotação para injeção é `@Inject`, não `@InjectBean`.
- **C) @ResourceInject:** Não existe. A anotação do Java EE que tem o comportamento semelhante e que é suportada pelo Spring é `@Resource` (da JSR-250), que resolve a dependência prioritariamente pelo nome, não "ResourceInject".
- **E) @WireBean:** É uma anotação fictícia, não presente nas APIs nativas do framework Spring.
</details>

---

### Questão 4 (FCC - 2019 - TRF 3ª Região - Analista Judiciário - Informática)
Na utilização conjunta dos frameworks Hibernate e Spring Data JPA, é necessário mapear as classes de domínio da aplicação em tabelas de um banco de dados relacional. Para marcar explicitamente uma classe de domínio como sendo uma entidade persistente da JPA, utiliza-se a anotação:
A) @Table
B) @Document
C) @Column
D) @JPAEntity
E) @Entity

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**

A alternativa correta é a **E**. Na especificação da JPA, a anotação `javax.persistence.Entity` (ou `jakarta.persistence.Entity` em versões mais recentes) é obrigatória para indicar que a classe representa uma tabela no banco de dados e será gerenciada pelo EntityManager e repassada pelo Spring Data JPA.

Análise das demais alternativas:
- **A) @Table:** É utilizada *em conjunto* com `@Entity` quando se deseja especificar configurações exclusivas da tabela no banco, como alterar o nome padrão da tabela gerada ou definir índices, mas não marca isoladamente a classe como uma entidade persistente.
- **B) @Document:** Esta anotação é usada pelo Spring Data MongoDB para mapear objetos em documentos NoSQL, e não em bancos relacionais (JPA).
- **C) @Column:** Mapeia um campo ou propriedade específica (atributo) da classe para uma coluna da tabela, não podendo ser utilizada na classe em si.
- **D) @JPAEntity:** Anotação fictícia. A anotação formal adotada pela especificação é apenas `@Entity`.
</details>

---

### Questão 5 (FCC - 2022 - TRT 22ª Região (PI) - Analista Judiciário - TI)
O Spring Boot simplifica o desenvolvimento de aplicações baseadas no ecossistema Spring. Um de seus principais recursos é a provisão de dependências do tipo "starter", que reúnem diversas bibliotecas de um mesmo contexto. Para desenvolver uma aplicação web comum (incluindo RESTful), usando o Spring MVC e que inclui por padrão o Tomcat como servidor embutido, deve-se incluir a dependência:
A) spring-boot-starter-tomcat
B) spring-boot-starter-web
C) spring-boot-starter-rest
D) spring-boot-starter-mvc
E) spring-boot-starter-webmvc

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A alternativa correta é a **B**. O `spring-boot-starter-web` é o starter fundamental no Spring Boot para o desenvolvimento de sistemas web ou APIs RESTful. Ao incluí-lo, o Spring Boot auto-configura as bibliotecas necessárias, incluindo o Spring MVC, Jackson (para conversão de JSON), validações padrão e embutindo, de forma transitiva, o Apache Tomcat como container web padrão.

Análise das demais alternativas:
- **A) spring-boot-starter-tomcat:** Esse starter existe, porém a finalidade dele é lidar exclusivamente com as bibliotecas do servidor Tomcat. Ele não embute toda a stack do MVC. Inclusive, ao incluir o `starter-web`, ele já embute automaticamente o `starter-tomcat`.
- **C) spring-boot-starter-rest:** Anotação fictícia. O Spring não possui um starter oficial com este nome para prover o ambiente de APIs REST; isso é englobado no `starter-web`.
- **D) spring-boot-starter-mvc:** O nome correto para o ecossistema MVC é englobado pela dependência `starter-web`. Não existe uma "starter-mvc".
- **E) spring-boot-starter-webmvc:** Não existe como starter autônomo na especificação oficial do Spring Boot. A nomenclatura oficial consolidou todas essas bibliotecas no "spring-boot-starter-web".
</details>

---

## 📝 TEMA 2: Testes de Software

### Questão 6 (FCC - 2022 - TRT 11ª Região - Analista Judiciário - TI)
Na engenharia de software, a fase de testes na qual o objetivo principal é verificar se unidades de software ou componentes já desenvolvidos e validados separadamente funcionam corretamente em conjunto, identificando falhas na comunicação entre eles, recebe o nome de:
A) Teste de Unidade
B) Teste de Sistema
C) Teste de Regressão
D) Teste de Aceitação
E) Teste de Integração

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**

A alternativa correta é a **E**. O Teste de Integração tem o foco principal em aferir a interface e a comunicação entre duas ou mais unidades/componentes (como módulos, métodos complexos, microsserviços) que já foram submetidos e validados individualmente. O intuito é garantir que dados trocados entre essas camadas estejam corretos e sem causar conflito.

Análise das demais alternativas:
- **A) Teste de Unidade:** Avalia a menor parte testável de forma individualizada e isolada (um método, uma classe), portanto, não avalia a comunicação conjunta das unidades.
- **B) Teste de Sistema:** Avalia o sistema em sua totalidade de ponta-a-ponta após o teste de integração, assegurando que este cumpre as especificações de requisitos como um produto concluído.
- **C) Teste de Regressão:** Destina-se a retestar o software após alguma modificação para assegurar que partes que funcionavam anteriormente não deixaram de funcionar, sem foco exclusivo em comunicação de unidades recém-compostas.
- **D) Teste de Aceitação:** Feito pelo usuário final ou cliente em ambiente que simula a produção para decidir se aceita o software para implantação, estando fora da esfera técnica de comunicação entre classes/módulos.
</details>

---

### Questão 7 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - TI)
A técnica de teste de software também conhecida como teste funcional ou baseado no comportamento, na qual os casos de teste são criados a partir da especificação de requisitos e o testador avalia as saídas produzidas pelas entradas sem analisar a estrutura interna ou código-fonte do programa, é denominada:
A) Teste de Caixa-Branca
B) Teste de Caminho Básico
C) Teste de Caixa-Preta
D) Teste de Fluxo de Dados
E) Teste de Mutação

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A alternativa correta é a **C**. Nos Testes de Caixa-Preta (Black-Box Testing), ignora-se a arquitetura e os mecanismos lógicos da aplicação. O foco é alimentar o sistema com entradas e validar se as saídas coincidem com os resultados esperados especificados pelos requisitos (Testes Funcionais).

Análise das demais alternativas:
- **A) Teste de Caixa-Branca:** Técnica que baseia a criação de testes no conhecimento do código-fonte, analisando if/else, laços e estrutura lógica subjacente. É diametralmente o oposto do caixa-preta.
- **B) Teste de Caminho Básico:** Essa é uma técnica de Teste de Caixa-Branca proposta por Tom McCabe, em que o testador elabora os testes cobrindo os caminhos independentes do fluxo de execução do código-fonte.
- **D) Teste de Fluxo de Dados:** Também é uma abordagem de Caixa-Branca voltada ao ciclo de vida (declaração, uso e exclusão) das variáveis e caminhos de dados no código, sendo impossível de executar sem acesso e análise estrutural.
- **E) Teste de Mutação:** É um método voltado para medir a qualidade de suites de teste existentes inserindo intencionalmente falhas no código-fonte para checar se os testes o descobrem, o que demanda interação técnica estrutural.
</details>

---

### Questão 8 (FCC - 2019 - TRF 3ª Região - Analista Judiciário - Informática)
Durante o ciclo de vida do software, é comum que a introdução de novos recursos ou a correção de bugs provoque falhas em funcionalidades que anteriormente operavam de maneira correta. Os testes executados especificamente com o intuito de descobrir esses defeitos colaterais recém-introduzidos são denominados testes:
A) de Regressão
B) de Fumaça (Smoke testing)
C) Estruturais
D) de Aceitação
E) de Carga

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A alternativa correta é a **A**. A principal função do Teste de Regressão é evitar o "efeito colateral" de uma nova implementação ou de uma manutenção corretiva. Ao modificar o sistema, uma bateria de testes reavalia o software para assegurar que ele não regrediu para um estado falho naquelas funcionalidades que já estavam finalizadas.

Análise das demais alternativas:
- **B) de Fumaça (Smoke testing):** É uma abordagem superficial executada imediatamente após uma compilação (build) ser concluída (geralmente automatizada), para confirmar que as funções primárias do software rodam de forma mínima antes de repassar a compilação para testes profundos. Não tem a função profunda focada nas colisões entre manutenções e o sistema legado.
- **C) Estruturais:** São conhecidos como caixa-branca, que avaliam o código interno. Uma regressão pode englobar caixa-branca e caixa-preta.
- **D) de Aceitação:** Realizado pelo usuário final para aceitar o produto entregue em ambiente de negócio final.
- **E) de Carga:** Um tipo de teste não funcional que tem como propósito avaliar os limites de processamento do software injetando alto número de interações ou requisições; nada tem a ver com avaliar introdução de defeitos nas regras de negócio preexistentes.
</details>

---

### Questão 9 (FCC - 2018 - TRT 6ª Região (PE) - Analista Judiciário - TI)
O Desenvolvimento Orientado a Testes (Test-Driven Development - TDD) é uma abordagem de desenvolvimento de software em que os casos de teste dão base e antecipam a escrita do código-fonte da aplicação. O ciclo de micro-iteração amplamente divulgado nesta prática é estabelecido pelos passos sequenciais de:
A) Design, Code, Test
B) Plan, Do, Check, Act
C) Write, Test, Fix
D) Red, Green, Refactor
E) Define, Measure, Analyze, Improve, Control

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A alternativa correta é a **D**. TDD é norteado pelo ciclo *Red-Green-Refactor* criado por Kent Beck. Primeiro, escrevemos um teste para uma funcionalidade que ainda não existe, ele deve inicialmente falhar (estado **Red**). Em seguida, implementa-se o código de produção mais simples apenas o suficiente para fazê-lo passar (estado **Green**). Por fim, o código recém-aprovado é otimizado e limpo, sem quebrar os testes (estado **Refactor**).

Análise das demais alternativas:
- **A) Design, Code, Test:** Um ciclo clássico de metodologias preditivas ou do padrão tradicional de desenvolvimento cascata/iterativo, que cria o teste no final da fase de codificação.
- **B) Plan, Do, Check, Act:** Conhecido como Ciclo PDCA de Deming, é uma matriz de melhoria contínua de processos administrativos e de gestão de qualidade, não sendo a tríade base do TDD.
- **C) Write, Test, Fix:** É uma descrição rústica de como se escrevia código de maneira convencional ("Codifica e Testa"), inversamente à filosofia de desenhar o teste antes de codificar (test-first).
- **E) Define, Measure, Analyze, Improve, Control:** É a espinha dorsal (DMAIC) do modelo do Seis Sigma utilizado para gestão e melhoria de qualidade organizacional e na manufatura corporativa, longe de práticas de codificação orientada a teste.
</details>

---

### Questão 10 (FCC - 2016 - TRT 20ª Região (SE) - Analista Judiciário - TI)
A técnica de teste baseada em examinar exaustivamente a estrutura lógica, fluxo de controle e os detalhes de implementação de um programa ou de suas rotinas internas, incluindo a elaboração de matrizes de cobertura de decisões (if/else) e desvios de condição, é classicamente conhecida como:
A) Teste de Desempenho
B) Teste de Caixa-Branca
C) Teste de Usabilidade
D) Teste de Caixa-Preta
E) Teste de Stress

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A alternativa correta é a **B**. O Teste de Caixa-Branca (também chamado de Caixa-de-Vidro ou Teste Estrutural) permite ao testador olhar "através da caixa" diretamente para o código interno do sistema. Esse conhecimento estrutural é o que permite projetar testes destinados a cobrir 100% de linhas de comandos, desvios ou blocos de decisão iterativos/lógicos contidos no código-fonte de um artefato.

Análise das demais alternativas:
- **A) Teste de Desempenho:** Avalia a rapidez e eficiência do sistema no tempo de resposta durante condições designadas, sem focar na execução linha a linha da lógica matemática do código.
- **C) Teste de Usabilidade:** Verifica se a interface de usuário (UI/UX) é intuitiva, de fácil uso e atende a aspectos ergonômicos da interação homem-máquina.
- **D) Teste de Caixa-Preta:** Focado unicamente na regra de negócio (entradas e saídas) descritas nos requisitos funcionais; o testador tem total ignorância do código implementado sob os panos.
- **E) Teste de Stress:** É uma ramificação de desempenho em que se força o software além de sua capacidade nominal a fim de avaliar suas rotinas de falha, tratamento de erro, ou colapso estrutural na sobrecarga.
</details>

---

## 📝 TEMA 3: Direito Administrativo

### Questão 11 (FCC - 2022 - TRT 4ª Região (RS) - Técnico Judiciário - Área Administrativa)
No que diz respeito aos poderes administrativos conferidos às autoridades estatais para a defesa do interesse público, o poder pelo qual a Administração tem competência legal para apurar infrações e aplicar, diretamente, sanções punitivas aos servidores públicos e a demais agentes atrelados aos quadros hierárquicos e à disciplina funcional denomina-se:
A) Poder Regulamentar
B) Poder de Polícia
C) Poder Disciplinar
D) Poder Hierárquico
E) Poder Vinculado

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A alternativa correta é a **C**. O Poder Disciplinar baseia-se na faculdade de apurar a ocorrência de infrações e aplicar sanções a quem esteja sujeito à disciplina interna da Administração Pública. Tais sanções incidem primariamente sobre servidores públicos estatutários ou pessoas particulares que possuam um vínculo jurídico especial/específico com a Administração.

Análise das demais alternativas:
- **A) Poder Regulamentar:** Refere-se à prerrogativa inerente aos Chefes de Executivo (Presidente, Governadores, Prefeitos) de editarem decretos ou regulamentos de modo a fiar a correta execução e operacionalização de uma Lei.
- **B) Poder de Polícia:** Apura e pune o particular, focado na coerção para frear direitos e liberdades do cidadão comum a fim de garantir a ordem e o bem-estar da coletividade como um todo, não restrito a vínculos internos.
- **D) Poder Hierárquico:** Consiste no dever-poder de distribuir e escalonar as funções de órgãos públicos e servidores, delegar, avocar competências, e ordenar ordens internamente. Embora fundamentem sanções de forma transversal, o ato de punir per se brota do poder Disciplinar.
- **E) Poder Vinculado:** É um limite legal à atuação administrativa. Não é propriamente um "poder" de punir, mas o enquadramento de que o administrador deve obedecer cegamente ao disposto em lei e sem deixar margem a liberdade de conveniência de atuação.
</details>

---

### Questão 12 (FCC - 2023 - TRT 18ª Região (GO) - Analista Judiciário - Área Administrativa)
Conforme estabelece expressamente a Lei nº 14.133/2021 (Nova Lei de Licitações e Contratos Administrativos), é modalidade de licitação obrigatória para a aquisição de bens e serviços classificados como comuns, adotando primordialmente os critérios de julgamento de menor preço ou de maior desconto:
A) Pregão
B) Concorrência
C) Diálogo Competitivo
D) Leilão
E) Concurso

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A alternativa correta é a **A**. Pela redação da Lei 14.133/2021 (art. 6º, inciso XLI, c/c art. 29), o Pregão é definido como a modalidade de licitação obrigatória para aquisição de bens e serviços comuns. Além disso, determina de forma expressa que no Pregão serão adotados sempre os critérios de julgamento por menor preço ou por maior desconto.

Análise das demais alternativas:
- **B) Concorrência:** Na nova lei, é utilizada para contratação de bens e serviços especiais, ou de obras e serviços comuns/especiais de engenharia. Utiliza os critérios: menor preço, melhor técnica ou conteúdo artístico, técnica e preço, maior retorno econômico e maior desconto.
- **C) Diálogo Competitivo:** Modalidade nova destinada à contratação de inovações tecnológicas ou técnicas, obras e serviços em que a Administração não possui viabilidade técnica de descrever o objeto por conta própria e precisa debater e obter ideias com os competidores do mercado antes de fechar a proposta.
- **D) Leilão:** É restrita de forma absoluta à alienação (venda/transferência) de bens imóveis ou bens móveis inservíveis ou legalmente apreendidos, sob o critério de maior lance.
- **E) Concurso:** Destinado apenas à escolha de trabalho com caráter técnico, de pesquisa, científico, ou artístico para concessão de remuneração preestabelecida na forma de prêmios ou honorários à figura do vencedor.
</details>

---

### Questão 13 (FCC - 2019 - TRF 4ª Região - Técnico Judiciário - Área Administrativa)
Ao longo do curso de validade de um ato administrativo, este reflete as prerrogativas peculiares e superiores do Estado. A qualidade que viabiliza que um ato administrativo imponha restrições e crie obrigações jurídicas de forma coercitiva aos administrados, independentemente de sua concordância ou vontade prévia de cumpri-lo, refere-se ao atributo da:
A) Presunção de legitimidade
B) Autoexecutoriedade
C) Legalidade
D) Imperatividade
E) Tipicidade

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A alternativa correta é a **D**. A imperatividade, também cunhada de coercibilidade pela doutrina, é o atributo segundo o qual a Administração constitui de forma unilateral os atos jurídicos em desfavor dos cidadãos. Estes devem aceitar e se submeter à vontade do Estado, mesmo que sejam avessos ou a refutem.

Análise das demais alternativas:
- **A) Presunção de legitimidade:** Atributo que sustenta que até provado o contrário de forma cabal ou anulatória, todo ato se presume redigido e criado sob as rigorosas exigências da lei e de modo lícito (verdadeiro e verossímil).
- **B) Autoexecutoriedade:** Reflete a capacidade conferida ao administrador público de executar atos com as próprias forças e poder do Estado diretamente (exemplo: multar, embargar uma obra), sem a obrigatoriedade de solicitar ordem judicial a um Juízo primeiramente.
- **C) Legalidade:** Representa um princípio balizador macro em que a administração pública somente atua onde a lei autoriza. Ele não compõe o escopo clássico do que se categoriza explicitamente como um "atributo do ato" na doutrina pátria (PATI).
- **E) Tipicidade:** Relaciona-se com a exigência formal de que o ato praticado tenha prévia e exata tipificação legal para seu nascimento (desenvolvido por Maria Sylvia Di Pietro); isso garante proteção aos cidadãos para que o Estado não cometa arbítrios que fujam da lei.
</details>

---

### Questão 14 (FCC - 2021 - TRT 15ª Região (SP) - Analista Judiciário - Área Administrativa)
No topo das regras constitucionais que regem e solidificam o Estado de Direito, a Administração Pública tem sua atuação norteada e vinculada pelos princípios caput do Art. 37 da Constituição da República. Assinale a alternativa que elenca de forma correta e expressa o preceito normativo dessa carta magna para a administração direta e indireta em quaisquer dos Poderes:
A) Legalidade, impessoalidade, razoabilidade, publicidade e eficiência.
B) Legalidade, finalidade, moralidade, publicidade e eficiência.
C) Supremacia do interesse público, impessoalidade, moralidade, publicidade e continuidade.
D) Legalidade, impessoalidade, motivação, publicidade e eficiência.
E) Legalidade, impessoalidade, moralidade, publicidade e eficiência.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**

A alternativa correta é a **E**. O art. 37, *caput*, da Constituição Federal estabelece os cinco pilares expressos, nacionalmente memorizados sob o mnemônico **LIMPE**: **L**egalidade, **I**mpessoalidade, **M**oralidade, **P**ublicidade e **E**ficiência (este último adicionado pela emenda n° 19/98).

Análise das demais alternativas:
- **A) razoabilidade:** É um princípio implícito/reconhecido em âmbito administrativo jurisprudencial e legal da esfera federal (art. 2º da Lei 9.784), mas não está expressamente redigido no *caput* do art. 37 da CF/88.
- **B) finalidade:** Embora seja um pilar central correlacionado à impessoalidade, trata-se de um princípio não expresso no art. 37 da CF/88. É sim expresso na Lei federal 9.784/99.
- **C) Supremacia do interesse público e continuidade:** São essenciais como princípios gerais (pedras de toque de todo o Direito Administrativo de Hely Lopes), mas não integram expressamente o texto do art. 37.
- **D) motivação:** A exigência de fundamentação e motivo dos atos está positivada em outras legislações, mas na letra exata da carta magna no art. 37 não é elencada formalmente.
</details>

---

### Questão 15 (FCC - 2022 - TRT 22ª Região (PI) - Analista Judiciário - Área Administrativa)
A Administração Pública em sua matriz indireta é fracionada em várias categorias, cada qual sujeita a um regime específico visando descentralizar a prestação de serviços. A entidade descrita pela doutrina clássica como o ente provido de personalidade jurídica de direito público, que necessariamente advém de autorização criadora por lei específica e que detém e executa funções próprias de Estado (livres de vertente mercantil) em gestão autônoma é a:
A) Empresa Pública
B) Fundação Pública de Direito Privado
C) Sociedade de Economia Mista
D) Autarquia
E) Organização Social

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A alternativa correta é a **D**. As Autarquias são as únicas entidades da Administração Indireta que detêm, originariamente, personalidade jurídica de Direito Público e são **criadas diretamente por lei**, com o objetivo de executar atribuições típicas de Estado sem buscar fins econômicos industriais (ex: INSS, BACEN, Ibama).

Análise das demais alternativas:
- **A) Empresa Pública:** Possui estritamente a personalidade jurídica de Direito Privado (ex: Correios, Caixa). Além disso, não é criada diretamente por lei, e sim tem a sua criação "autorizada" pela norma e seu registro e estatuto firmados como empresas mercantis.
- **B) Fundação Pública de Direito Privado:** Tem sua criação autorizada, e não estabelecida prontamente na lei primária instituidora, não correspondendo aos ditames da pergunta que invoca pessoa jurídica de direito público.
- **C) Sociedade de Economia Mista:** É uma S.A., e assim como as empresas públicas, goza sempre de natureza de Direito Privado, destinada comumente para prestar serviço público por meio de capital misto entre governo (majoritário) e o mercado corporativo ou sociedade em geral.
- **E) Organização Social (OS):** Pertence ao denominado Terceiro Setor (parcerias e fomento de caráter público-privado), não compondo o organograma da Administração Pública Indireta.
</details>

---
