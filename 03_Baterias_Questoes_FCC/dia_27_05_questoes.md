# Bateria de Questões FCC — Quarta-feira 27/05

## 📝 TEMA 1: Programação Web Java/Spring

### Questão 1 (FCC - 2018 - TRT 15 - Analista Judiciário - TI)
No Spring MVC, a anotação `@RestController` é, em si, uma anotação de conveniência que combina as anotações:
A) `@Controller` e `@ResponseBody`
B) `@Controller` e `@RequestMapping`
C) `@Component` e `@ResponseBody`
D) `@Service` e `@RequestMapping`
E) `@Service` e `@Controller`

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A anotação `@RestController` é uma especialização do `@Controller` que já inclui automaticamente a anotação `@ResponseBody`.
- **A) Correta.** `@RestController` = `@Controller` + `@ResponseBody`. Isso instrui o Spring a converter a resposta dos métodos diretamente para o corpo da resposta HTTP (ex: JSON), e não buscar uma view (HTML).
- **B) Incorreta.** `@RequestMapping` é usado para mapear URIs em classes e métodos, e não está embutido no `@RestController`.
- **C) Incorreta.** Embora `@Controller` herde de `@Component`, a definição técnica e funcional de `@RestController` é a união estrita de `@Controller` e `@ResponseBody`.
- **D) Incorreta.** `@Service` é restrito para a camada de negócios, não de apresentação.
- **E) Incorreta.** `@Service` e `@Controller` têm propósitos semânticos distintos e não são combinados assim.
</details>

---

### Questão 2 (FCC - 2019 - TRF 3 - Técnico Judiciário - Informática)
No Spring Boot, os *starters* são:
A) plugins do Maven ou Gradle responsáveis pela geração do pacote final (.jar ou .war).
B) dependências descritoras que agrupam outras dependências comuns para um determinado tipo de aplicação, facilitando a configuração.
C) classes de configuração Java onde são definidos os beans a serem gerenciados pelo contêiner do Spring.
D) anotações utilizadas para inicializar a aplicação web a partir de um método principal.
E) servidores de aplicação embutidos, como o Tomcat ou Jetty, configurados para iniciar junto com a aplicação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Os *starters* do Spring Boot foram introduzidos para evitar a fadiga de gerenciar dezenas de dependências isoladas com diferentes versões.
- **A) Incorreta.** Plugins de build (como `spring-boot-maven-plugin`) empacotam o artefato final, mas não são denominados *starters*.
- **B) Correta.** *Starters* são descritores de dependências ("BOMs" ou *pom.xml* agrupadores) que reúnem um conjunto testado e compatível de dependências (ex: `spring-boot-starter-web` para aplicações REST com Spring MVC, Tomcat e Jackson).
- **C) Incorreta.** Classes de configuração utilizam a anotação `@Configuration`.
- **D) Incorreta.** A inicialização ocorre por meio da anotação `@SpringBootApplication` em uma classe com o método `main`.
- **E) Incorreta.** Embora alguns *starters* (como o de web) agreguem um servidor Tomcat embutido, o conceito de *starter* refere-se à dependência em si, não ao servidor.
</details>

---

### Questão 3 (FCC - 2018 - TRT 2 - Analista Judiciário - TI)
No ecossistema Spring Data JPA, para criar um repositório que fornece métodos para realizar operações CRUD em uma entidade, a interface criada pelo desenvolvedor geralmente estende:
A) `JpaRepository` ou `CrudRepository`.
B) `EntityManagerFactory`.
C) `JpaTemplate`.
D) `HibernateTemplate`.
E) `SessionFactory`.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

O Spring Data JPA revoluciona o acesso a dados fornecendo implementações automáticas para interfaces.
- **A) Correta.** O desenvolvedor cria uma interface e estende `CrudRepository`, `PagingAndSortingRepository` ou, na maioria das vezes para JPA, `JpaRepository`. O Spring fornece instâncias transparentes (proxies) que realizam operações de banco.
- **B) Incorreta.** `EntityManagerFactory` é parte da especificação nativa do JPA que gera o `EntityManager` a nível de fábrica.
- **C) Incorreta.** `JpaTemplate` é um modelo de classe depreciado herdado do Spring Framework clássico para remover boilerplate do JPA, abandonado em favor do Spring Data.
- **D) Incorreta.** `HibernateTemplate` tem o mesmo propósito legado do anterior, mas para projetos puramente Hibernate pré-JPA.
- **E) Incorreta.** `SessionFactory` pertence unicamente à API original e nativa do Hibernate.
</details>

---

### Questão 4 (FCC - 2017 - TST - Analista Judiciário - TI)
O Spring Framework suporta fortemente o princípio de Injeção de Dependência (DI). Uma das anotações principais utilizadas para marcar um construtor, um campo ou um método de configuração a ser autoligado pelas dependências mapeadas do Spring é:
A) `@InjectDependency`
B) `@ResourceAutowired`
C) `@Autowired`
D) `@Dependency`
E) `@Wire`

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A injeção de dependência via anotações no Spring é governada primariamente pelo `@Autowired`.
- **A) Incorreta.** O nome da anotação não existe na API do Spring.
- **B) Incorreta.** Invenção com fusão de dois termos. A API oficial do Java oferece `@Resource`, mas não combinada com Autowired.
- **C) Correta.** A anotação `@Autowired` é a forma padrão do Spring para instruir o IoC Container (Inversion of Control) a preencher dependências em campos, construtores ou métodos setter com base no tipo (*by type*).
- **D) Incorreta.** `@Dependency` não é parte do ecossistema para injeção.
- **E) Incorreta.** Não há uma anotação com o nome `@Wire`.
</details>

---

### Questão 5 (FCC - 2018 - TRT 6 - Analista Judiciário - TI)
A anotação `@SpringBootApplication` é frequentemente utilizada na classe principal de um projeto Spring Boot. Ela encapsula três outras anotações fundamentais, que são:
A) `@Configuration`, `@EnableAutoConfiguration` e `@ComponentScan`.
B) `@Controller`, `@Service` e `@Repository`.
C) `@Component`, `@Autowired` e `@Qualifier`.
D) `@Configuration`, `@EnableWebMvc` e `@ComponentScan`.
E) `@EnableAutoConfiguration`, `@EntityScan` e `@EnableJpaRepositories`.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

O Spring Boot favorece a convenção sobre a configuração, simplificando com meta-anotações.
- **A) Correta.** A documentação oficial do Spring Boot descreve que a anotação `@SpringBootApplication` é um atalho que abrange as funcionalidades do `@Configuration` (permite registro de *beans* extras), `@EnableAutoConfiguration` (ativa o mecanismo que auto-configura *beans* baseando-se no classpath) e `@ComponentScan` (escaneia o pacote atual e subpacotes por componentes do Spring).
- **B) Incorreta.** Estas formam as clássicas anotações de estereótipo do pacote, e não compõem a anotação de boot.
- **C) Incorreta.** Tratam apenas de injeção de dependências e definições de componentes atômicos.
- **D) Incorreta.** `@EnableWebMvc` desativa parte da autoconfiguração Web do Spring Boot caso declarada. Portanto, ela definitivamente não faz parte do pacote embutido do `@SpringBootApplication`.
- **E) Incorreta.** As anotações relacionadas estritamente aos pacotes de persistência JPA não fazem parte do metadado genérico da aplicação.
</details>

---

### Questão 6 (FCC - 2016 - TRT 20 - Analista Judiciário - TI)
Na Java Persistence API (JPA), utilizada frequentemente com o ecossistema Spring, para mapear uma chave primária composta de múltiplas colunas, a classe que representa essa chave deve ser anotada preferencialmente ou utilizar uma anotação específica na entidade. Dentre as opções abaixo, quais anotações são corretas para essa finalidade?
A) `@CompositeKey`
B) `@IdClass` ou `@EmbeddedId`
C) `@PrimaryKeyJoinColumn`
D) `@Embedded`
E) `@ElementCollection`

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

O mapeamento de chaves primárias compostas na JPA requer que a chave seja representada por uma classe avulsa (que deve implementar `Serializable`, e sobrepor `equals()` e `hashCode()`).
- **A) Incorreta.** Não há uma anotação `@CompositeKey` definida pelo padrão JPA.
- **B) Correta.** Existem duas formas aprovadas na especificação JPA: 1) Usar a anotação `@IdClass` sobre a definição da Entidade, mantendo os campos `@Id` em seu corpo normalmente; 2) Usar a anotação `@EmbeddedId` num campo da Entidade que seja do tipo da classe que representa a chave (anotada com `@Embeddable`).
- **C) Incorreta.** É utilizada apenas para mapeamento de herança nas entidades filhas (tipo JOINED).
- **D) Incorreta.** `@Embedded` indica que os campos de uma classe injetada devem ser traduzidos para as colunas da entidade que a injetou, mas isoladamente não tem poder semântico de transformá-la numa Chave Primária.
- **E) Incorreta.** Utilizado em coleções de tipos primitivos ou *embeddables* puros para mapear tabelas fracas no estilo 1:N.
</details>

---

### Questão 7 (FCC - 2018 - TRT 15 - Analista Judiciário - TI)
Em uma aplicação baseada no Spring MVC, para extrair valores dinâmicos da URI em que uma requisição foi mapeada (por exemplo, obter o valor '123' da URL `/usuarios/123`), o desenvolvedor deve utilizar a anotação:
A) `@RequestParam`
B) `@PathVariable`
C) `@UriParameter`
D) `@RequestAttribute`
E) `@PathParam`

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

O Spring MVC utiliza modelos de padrões de URI (*URI Templates*).
- **A) Incorreta.** O `@RequestParam` liga os argumentos de um método aos parâmetros de *query* (ex: `/usuarios?id=123`) ou formulários postados.
- **B) Correta.** A anotação `@PathVariable` extrai pedaços contidos no caminho da URL definidos entre chaves na rota mapeada, como `@RequestMapping("/usuarios/{id}")`.
- **C) Incorreta.** Esta anotação não existe no framework Spring.
- **D) Incorreta.** `@RequestAttribute` serve para resgatar atributos internos anexados à requisição por *interceptors* ou *filters* na própria execução no lado do servidor, e não na URL.
- **E) Incorreta.** `@PathParam` desempenha uma função idêntica a `@PathVariable`, porém ela é exclusiva da API concorrente `JAX-RS` (Java EE).
</details>

---

### Questão 8 (FCC - 2015 - TRT 3 - Analista Judiciário - TI)
No desenvolvimento de aplicações Web em Java, os *Servlets* possuem um ciclo de vida estrito que é gerenciado pelo contêiner Web (como Tomcat, Jetty ou Undertow). Os métodos fundamentais que compõem as fases desse ciclo de vida na interface principal Servlet são:
A) `create()`, `execute()` e `destroy()`
B) `start()`, `run()` e `stop()`
C) `init()`, `service()` e `destroy()`
D) `doGet()`, `doPost()` e `doDelete()`
E) `load()`, `process()` e `unload()`

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

O ciclo de vida básico de qualquer artefato da API *Servlet* é estritamente regrado em três passos oficiais da interface pai `javax.servlet.Servlet` (atualmente `jakarta.servlet.Servlet`).
- **A) Incorreta.** O modelo de criação foge à nomenclatura da especificação.
- **B) Incorreta.** Nomeia estados padrão associados a *Threads* em Java (classe `Thread` e interface `Runnable`), e não a componentes Web.
- **C) Correta.** `init()` é ativado apenas na criação da primeira instância; `service()` atende toda requisição que entra processando a requisição e devolvendo a resposta; `destroy()` limpa a instância da memória ao desligar o servidor ou remover a aplicação.
- **D) Incorreta.** A classe `HttpServlet` estende a interface e implementa o `service()`, dividindo e direcionando a rota para métodos específicos do protocolo HTTP como `doGet`, `doPost`, mas estes não compõem os estágios "raiz" do ciclo de vida definidos pela própria infraestrutura Web.
- **E) Incorreta.** Falso, não há qualquer registro formal com essa nomenclatura no *Java EE*.
</details>

---

### Questão 9 (FCC - 2019 - TRF 4 - Analista Judiciário - TI)
No Spring Framework, a anotação `@Transactional` é amplamente utilizada para definir os limites de uma transação no banco de dados. Quando aplicada a um método, qual é o comportamento padrão do Spring caso ocorra uma exceção de tempo de execução (`RuntimeException`) não tratada dentro desse método?
A) O Spring realiza o *commit* da transação imediatamente antes do lançamento da exceção ao chamador.
B) A transação é suspensa e mantida aberta até que seja retomada manualmente pelo servidor de aplicação.
C) O comportamento padrão do Spring é realizar o *rollback* (desfazer) das operações da transação no banco de dados.
D) O Spring ignora a exceção, não interferindo no status da transação em andamento.
E) Apenas as operações de leitura são desfeitas (*rollback*); operações de escrita que já passaram com sucesso são confirmadas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

As transações do Spring funcionam sob um mecanismo de Aspectos (AOP) que inspecionam o retorno ou interrupção do método.
- **A) Incorreta.** Lançar um erro interrompe a continuidade de dados sadios, forçando um cancelamento (*rollback*), e não um salvamento de dados com falha.
- **B) Incorreta.** As conexões não ficam permanentemente pendentes esperando intervenção externa; o bloco tem escopo e finalização imediatos.
- **C) Correta.** O aspecto do Spring, interceptando uma `RuntimeException` ou instância de `Error`, considera como uma falha fatal nas regras de negócio e aciona nativamente um *rollback* no `PlatformTransactionManager`, protegendo a integridade dos dados. (Lembrando que Exceções Verificadas – *Checked Exceptions* – por padrão NÃO fazem *rollback*, a não ser que declaradas como `rollbackFor=Exception.class`).
- **D) Incorreta.** O *Proxy* de transação fica de plantão e analisa toda exceção ocorrida no escopo do método decorado.
- **E) Incorreta.** A atomicidade (A de ACID) garante a diretriz "tudo ou nada". Logo, todo tipo de operação efetuada na transação corrente, leitura ou escrita, será descartada em conjunto.
</details>

---

### Questão 10 (FCC - 2022 - TRT 22 - Analista Judiciário - TI)
No contexto do ecossistema de segurança e autenticação com Spring Security, a interface principal frequentemente implementada pelo desenvolvedor, responsável exclusivamente por buscar e carregar os dados específicos do usuário (como nome, senha gerada, e permissões) a partir de uma base de dados externa ou interna, é a:
A) `UserDetailsService`.
B) `AuthenticationManager`.
C) `SecurityContextHolder`.
D) `GrantedAuthority`.
E) `PasswordEncoder`.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

O processo de autenticação é decomposto em vários pequenos serviços especializadas e intercambiáveis.
- **A) Correta.** A interface `UserDetailsService` deve possuir apenas a implementação de `loadUserByUsername(String username)`. Sua principal função é consultar o repositório de dados desejado para retornar um objeto encapsulado do tipo `UserDetails` (que guarda informações do login a serem checadas).
- **B) Incorreta.** `AuthenticationManager` é o componente superior central, responsável por iniciar o processo de *login* e acionar os mecanismos que verificarão a autenticidade das credenciais (senhas recebidas).
- **C) Incorreta.** O `SecurityContextHolder` se limita ao papel de armazenador contextual em memória (utilizando *ThreadLocal* por padrão) dos dados de autenticação de quem já fez o acesso.
- **D) Incorreta.** `GrantedAuthority` é uma interface que representa puramente o direito cedido a um objeto, como os perfis de acesso (ex. "ROLE_ADMIN").
- **E) Incorreta.** O `PasswordEncoder` aplica algoritmos de embaralhamento e de saltos (como BCrypt ou PBKDF2) para validação unidirecional, ou seja, verifica se a string digitada equivale ao _hash_ registrado.
</details>

---

### Questão 11 (FCC - 2014 - TRT 16 - Analista Judiciário - TI)
No Spring Framework, os escopos de configuração (*scopes*) definem o ciclo de vida e a visibilidade dos *beans* que serão gerenciados pelo contêiner de Injeção de Dependência. O escopo definido como **padrão** (*default*) estabelecido pelo framework, no qual é criada e controlada apenas uma única instância do *bean* para ser compartilhada por todo o contêiner, é o:
A) *prototype*
B) *singleton*
C) *request*
D) *session*
E) *global-session*

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Os beans no Spring operam por padrão na máxima economia de memória, compartilhando os mesmos objetos, a menos que precisem possuir estados variantes para instâncias individuais (não-*stateless*).
- **A) Incorreta.** O escopo *prototype* cria o oposto do padrão: cada solicitação ao contêiner gerará uma nova alocação e objeto independentes da mesma classe.
- **B) Correta.** O *singleton* do escopo de Spring é o default. O contêiner retém a cópia da instância no escopo global da aplicação (`ApplicationContext`) e qualquer injeção deste tipo referenciará o exato mesmo objeto alocado daquela configuração.
- **C) Incorreta.** *Request* é restrito a aplicações que rodam numa extensão do contexto *Web* (WebApplicationContext), instanciando objetos cujas vivências terminam no final do processamento da chamada HTTP que as criaram.
- **D) Incorreta.** Igualmente válido no ambiente Web, esse escopo vincula e guarda os dados no cache de uma instância enquanto uma Sessão de usuário Web for considerada ativa.
- **E) Incorreta.** Um escopo restrito voltado ao falecido cenário de Portlets Web; atualmente ineficaz em implantações regulares de serviços.
</details>

---

### Questão 12 (FCC - 2016 - TRT 20 - Analista Judiciário - TI)
A tecnologia JSP frequentemente utiliza a biblioteca de base estrutural da JSTL (*JSP Standard Tag Library*) para evitar ao máximo a escrita pesada de código Java embutido em *scriptlets*. A biblioteca *core* da JSTL (normalmente registrada sob o prefixo "c") inclui uma *tag* projetada especificamente para iterar sobre coleções de dados, como listas oriundas dos *Servlets*. Essa *tag* iteradora padrão é a:
A) `<c:iterate>`
B) `<c:for>`
C) `<c:forEach>`
D) `<c:loop>`
E) `<c:repeat>`

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Para diminuir as tags `<% ... %>` (Scriptlets puros), as *Custom Tags* da JSTL assumiram o trabalho limpo e voltado ao HTML.
- **A) Incorreta.** A tag de nome `<logic:iterate>` foi famosa, porém no histórico do framework Apache Struts, anterior ou simultâneo ao pleno uso da JSTL.
- **B) Incorreta.** É um conceito derivado direto do laço padrão do Java (o bloco nativo `for`), inexistente com esse nome na JSTL.
- **C) Correta.** `<c:forEach>` é a *tag* oficial presente na API JSTL Core. Opera varrendo a coleção definida em `items`, provendo o elemento atual por meio da variável expressa em `var`.
- **D) Incorreta.** A tag em inglês de "loop" nunca fez parte dos nomes oficiais do padrão Jakarta.
- **E) Incorreta.** Sem suporte funcional, o conceito de repeate pertence mais frequentemente a frameworks de UI no ecossistema JSF, como `<ui:repeat>`.
</details>

---

### Questão 13 (FCC - 2017 - TRE PR - Analista Judiciário - TI)
Na infraestrutura base de bancos de dados da Java Persistence API (JPA), as instâncias das entidades mapeadas podem assumir diferentes estados contínuos de ciclo de vida. Quando o método `persist()` de um objeto ativo `EntityManager` é chamado passando uma nova entidade como parâmetro, o estado lógico dessa entidade sofre diretamente a mudança de:
A) *Managed* para *Detached*.
B) *New (Transient)* para *Managed*.
C) *Detached* para *Removed*.
D) *Managed* para *Removed*.
E) *Transient* para *Detached*.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Os estados do ciclo de vida são 4 clássicos na literatura JPA: *New* (ou Transient), *Managed*, *Detached* e *Removed*.
- **A) Incorreta.** Entrar em estado *Detached* ocorre quando instâncias previamente *Managed* são desanexadas do contexto (ao fazer *clear()*, *close()* do escopo).
- **B) Correta.** Um objeto puramente alocado no Java por meio da instrução `new` (sem associação alguma com o banco de dados até aquele momento) encontra-se em um estado efêmero e transitório conhecido como *Transient / New*. O ato de acionar o `em.persist(entidade)` obriga o JPA (ex: Hibernate) a alocar o objeto dentro do Contexto de Persistência, transacionando-o para *Managed* e eventualmente disparando os inserts.
- **C) Incorreta.** Entidades separadas não assumem remoção automaticamente; uma reanexação (*merge*) antecede as operações.
- **D) Incorreta.** O estado de *Managed* para *Removed* ocorre com o método inverso `em.remove(entidade)`.
- **E) Incorreta.** Não há mecanismo no ecossistema que mova uma entidade do nada (Nova) diretamente à desanexação, pulando todo o processo de mapeamento transacional gerenciado.
</details>

---

### Questão 14 (FCC - 2018 - TRT 15 - Analista Judiciário - TI)
No Spring Framework, as chamadas "anotações de estereótipo" são aplicadas sobre as classes para classificar e indicar semanticamente o papel dos componentes perante o projeto. A anotação genérica e primária para qualquer componente no Spring é o `@Component`. As anotações especializadas do Spring (que herdam deste estereótipo base) e que servem para designar as camadas de **apresentação (web)**, **negócio (serviços)** e de **persistência (acesso direto a dados)** são, respectivamente:
A) `@View`, `@Business` e `@Dao`.
B) `@Controller`, `@Service` e `@Repository`.
C) `@Web`, `@Logic` e `@Database`.
D) `@RestController`, `@AppService` e `@Entity`.
E) `@RequestMapping`, `@Transactional` e `@PersistenceContext`.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A injeção semântica orientada ao *Domain-Driven Design* permite ao Spring tratar cada classe conforme as exigências da camada.
- **A) Incorreta.** Os três termos não fazem parte da árvore de estereótipos base da estrutura de módulos Spring Context.
- **B) Correta.** As sub-anotações oficias estendidas do `@Component` são: `@Controller` para roteamentos e MVC, `@Service` para lógicas agregadoras de negócios e escopos de segurança/transacionais, e o `@Repository` em DAOs para realizar acessos nativos e traduzir/padronizar automaticamente o emaranhado das exceções legadas geradas por bancos SQL e drivers JDBC.
- **C) Incorreta.** Tratam-se de nomes intuitivos na indústria de desenvolvimento que, entretanto, não foram aderidos como anotações reais do ecossistema do Spring.
- **D) Incorreta.** A primeira integra parte da camada de apresentação (REST), porém é filha de Controller. A segunda não é padrão do ecossistema. A última pertence ao concorrente/acoplador JPA, mapeando tabelas.
- **E) Incorreta.** Como exposto, as anotações representadas nessa alternativa dizem respeito a mapeamento de propriedades e restrições metodológicas (`RequestMapping` para rotas; `Transactional` para controle ACID de banco; e `PersistenceContext` para injeção específica do *Manager* JPA).
</details>

---

### Questão 15 (FCC - 2016 - TRT 14 - Analista Judiciário - TI)
No desenvolvimento de aplicações distribuídas com serviços *RESTful* em Java, utilizando estritamente a especificação oficial JAX-RS (*Java API for RESTful Web Services*), as anotações encarregam-se de mapear requisições. A anotação padrão utilizada para expor e indicar que um método HTTP deve responder especificamente a interações clientes do tipo de inserção/envio de informações com **POST** é a:
A) `@Post`
B) `@HttpPost`
C) `@POST`
D) `@RequestMapping(method="POST")`
E) `@WebMethod(action="POST")`

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Para garantir conformidade de implementações de terceiros (como Jersey, RESTEasy e CXF), as marcações da Jakarta/JAX-RS seguem um padrão explícito e simples, presente no pacote *javax.ws.rs* ou *jakarta.ws.rs*.
- **A) Incorreta.** O Java é *case-sensitive*, e a API JAX-RS estabeleceu que os verbos seriam capitalizados totalmente.
- **B) Incorreta.** Remete aos modelos de classes do componente legados nativos de requisições do pacote Apache *HttpClient*.
- **C) Correta.** A anotação `@POST` reflete inteiramente e exclusivamente o verbo do protocolo HTTP suportado. As demais, logicamente, são: `@GET`, `@PUT`, `@DELETE`, etc.
- **D) Incorreta.** Esta sintaxe exata refere-se ao recurso do Spring Framework/MVC (onde o próprio verbo viria com `RequestMethod.POST`).
- **E) Incorreta.** `@WebMethod` remonta a especificação concorrente para serviços SOAP baseados em XML, o JAX-WS, que trabalha em paradigmas e formatos não inerentes ao esquema RESTful.
</details>


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


## 📝 TEMA 3: Direito Administrativo

### Questão 1 (FCC - 2023 - TRT 18 - Técnico Judiciário - Área Administrativa)
No tocante aos princípios aplicáveis à Administração Pública, o princípio da impessoalidade tem como um de seus aspectos a ideia de que:
A) a Administração não pode atuar com vistas a prejudicar ou beneficiar pessoas determinadas.
B) as competências dos órgãos públicos devem ser definidas previamente por lei, sem influência pessoal.
C) os atos administrativos devem ser sempre publicados em órgão oficial para conhecimento de todos.
D) as decisões administrativas devem ser motivadas e embasadas em pareceres técnicos imparciais.
E) a eficiência na prestação do serviço independe das características pessoais do agente público.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A alternativa **A** é a correta, pois o princípio da impessoalidade apresenta dupla vertente no Direito Administrativo: a primeira é a vedação à promoção pessoal do agente público (art. 37, § 1º, da CF), garantindo que as realizações sejam imputadas ao Estado; a segunda impõe que a atuação estatal deve ter como objetivo o interesse público, não podendo beneficiar ou prejudicar indevidamente pessoas específicas. Portanto, a opção descreve o aspecto finalístico da impessoalidade.
A alternativa **B** está incorreta, pois a estrita submissão dos órgãos e competências ao que está previsto em lei diz respeito ao princípio da legalidade (o agente público só faz o que a lei permite).
A alternativa **C** está incorreta porque a obrigatoriedade de publicação oficial dos atos visa dar conhecimento ao público e marcar o início de sua eficácia, sendo um reflexo direto do princípio da publicidade, e não da impessoalidade.
A alternativa **D** está incorreta, pois fundamentar as decisões em parâmetros técnicos é uma exigência do princípio da motivação. Embora a motivação ajude no controle da impessoalidade, ela é um instituto autônomo.
A alternativa **E** está incorreta, visto que o alcance de produtividade e otimização de recursos refere-se primordialmente ao princípio da eficiência (incluído no art. 37, caput, da CF pela EC 19/98).
</details>

---

### Questão 2 (FCC - 2022 - TRT 22 - Analista Judiciário - Área Administrativa)
Sobre a organização administrativa da União, as autarquias são compreendidas como:
A) pessoas jurídicas de direito público, criadas por lei, com capacidade de autoadministração, para o desempenho de serviço público descentralizado.
B) pessoas jurídicas de direito privado, cuja criação é autorizada por lei, voltadas à exploração de atividade econômica.
C) entes da administração direta, com personalidade jurídica própria, criados por lei específica.
D) órgãos despersonalizados criados por lei para exercerem poder de polícia, subordinados diretamente ao Ministério respectivo.
E) entidades privadas autorizadas por lei a prestar serviços sociais não exclusivos do Estado.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A alternativa **A** é a correta. As autarquias compõem a Administração Indireta, ostentam personalidade jurídica de direito público e são criadas diretamente por lei específica, não necessitando de registro de seus atos constitutivos (art. 37, XIX, CF e art. 5º do Decreto-Lei 200/67). Possuem autonomia financeira e administrativa para executar atividades típicas de Estado, operando a descentralização por serviços (outorga).
A alternativa **B** é incorreta. O texto descreve as sociedades de economia mista e empresas públicas, que pertencem à Administração Indireta, mas possuem personalidade jurídica de direito privado e dependem de autorização legal seguida de registro para nascerem.
A alternativa **C** é incorreta porque autarquias fazem parte da Administração Indireta, e não da Direta (que é composta pela União, Estados, DF e Municípios, e seus órgãos).
A alternativa **D** é incorreta. Autarquias possuem personalidade jurídica própria. Órgãos são centros de competência despersonalizados que integram a estrutura das pessoas jurídicas (como os Ministérios ou Secretarias). Além disso, a autarquia não é subordinada, mas sim vinculada (sofre controle finalístico) ao Ministério respectivo.
A alternativa **E** é incorreta, pois se refere às entidades do Terceiro Setor (ex: serviços sociais autônomos, como o Sistema S), que não integram a Administração Pública.
</details>

---

### Questão 3 (FCC - 2023 - TRT 11 - Técnico Judiciário - Área Administrativa)
No exercício do poder de polícia, a Administração Pública ostenta atributos, dentre os quais o que permite que a decisão seja posta em prática pela própria Administração, sem a necessidade de prévia intervenção do Poder Judiciário. Trata-se do atributo da:
A) discricionariedade.
B) imperatividade.
C) autoexecutoriedade.
D) coercibilidade.
E) presunção de legitimidade.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A alternativa **C** está correta. A autoexecutoriedade é o atributo do poder de polícia (e dos atos administrativos em geral) que permite que a Administração execute materialmente as suas próprias decisões sem precisar recorrer previamente às vias judiciais, podendo inclusive usar a força se necessário (exemplo clássico: apreensão de mercadorias estragadas).
A alternativa **A** está incorreta. Discricionariedade é a margem de escolha que a lei confere ao agente público para, num caso concreto, aferir a conveniência e oportunidade da medida (ex: decidir a gravidade da penalidade dentro dos limites legais).
A alternativa **B** está incorreta. Imperatividade é a qualidade de impor obrigações aos administrados independentemente de sua concordância, criando uma restrição na esfera jurídica de terceiros, mas não se confunde com a "execução material direta".
A alternativa **D** está incorreta. Embora a coercibilidade garanta o uso legítimo da força para obrigar o cumprimento do ato, o comando da questão ("posta em prática pela própria Administração... sem o Judiciário") é a definição doutrinária exata da autoexecutoriedade.
A alternativa **E** está incorreta. Presunção de legitimidade significa apenas que, até prova em contrário, entende-se que o ato foi emitido em conformidade com a lei e que os fatos alegados pelo Estado são verdadeiros (presunção de veracidade).
</details>

---

### Questão 4 (FCC - 2018 - TRT 15 - Analista Judiciário - Área Administrativa)
Um determinado ato administrativo possui um vício de legalidade insanável. De acordo com o entendimento sumulado do Supremo Tribunal Federal (Súmula 473) e a legislação aplicável, a Administração:
A) deve revogar o ato, respeitados os direitos adquiridos e ressalvada, em todos os casos, a apreciação judicial.
B) deve convalidar o ato, caso este já tenha produzido efeitos perante terceiros de boa-fé, independentemente do vício.
C) pode anular seus próprios atos, quando eivados de vícios que os tornam ilegais, porque deles não se originam direitos.
D) não pode invalidar o ato de ofício, dependendo de prévia provocação do particular interessado ou decisão judicial.
E) deve anular o ato com efeitos ex nunc, a fim de garantir a segurança jurídica das relações consolidadas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A alternativa **C** é a correta. Ela reflete a literalidade da Súmula 473 do STF (que consagra o princípio da autotutela): "A administração pode anular seus próprios atos, quando eivados de vícios que os tornam ilegais, porque deles não se originam direitos; ou revogá-los, por motivo de conveniência ou oportunidade, respeitados os direitos adquiridos, e ressalvada, em todos os casos, a apreciação judicial".
A alternativa **A** é incorreta. A revogação é o instrumento adequado para extinguir atos válidos (sem vício de legalidade), mas inoportunos ou inconvenientes. Atos ilegais são anulados.
A alternativa **B** é incorreta. Atos com vícios insanáveis (como defeito de finalidade, motivo, ou forma essencial) não comportam convalidação. Apenas vícios sanáveis (competência não exclusiva e forma não essencial) podem ser convalidados.
A alternativa **D** é incorreta. Pelo princípio da autotutela, a Administração Pública tem o dever (e o poder) de rever e invalidar seus próprios atos ilegais de ofício, não dependendo do Poder Judiciário nem de provocação de terceiro.
A alternativa **E** é incorreta. A anulação fundamenta-se na ilegalidade originária e opera efeitos, em regra, *ex tunc* (retroativos), retroagindo para desfazer os efeitos do ato viciado, ao passo que a revogação gera efeitos *ex nunc*.
</details>

---

### Questão 5 (FCC - 2022 - TRT 5 - Técnico Judiciário - Área Administrativa)
Segundo a Lei nº 14.133/2021 (Nova Lei de Licitações e Contratos), o diálogo competitivo é modalidade de licitação aplicável para contratação de:
A) obras, serviços e compras, em que os licitantes disputam por meio de propostas e lances sucessivos de forma presencial.
B) bens e serviços especiais, quando não for possível o atendimento à necessidade do órgão sem a adaptação de soluções disponíveis no mercado.
C) serviços e compras de grande vulto que envolvam recursos de financiamento internacional ou inovação tecnológica padronizada.
D) parcerias público-privadas onde haja necessidade de se aferir o menor preço global mediante disputa em lances abertos.
E) bens ou serviços comuns, cujo critério de julgamento poderá ser o menor preço ou o maior desconto, em certame restrito a grandes empresas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A alternativa **B** está correta. Nos moldes do art. 32 da Lei 14.133/21, a modalidade de Diálogo Competitivo é voltada para situações de alta complexidade em que a Administração não possui as condições técnicas iniciais para descrever a solução adequada e, por isso, dialoga com o mercado em busca de soluções que envolvem inovação tecnológica/técnica, impossibilidade de atendimento sem adaptação de soluções existentes no mercado ou inviabilidade da especificação objetiva integral.
A alternativa **A** está incorreta. Licitação comum que admite lances e propostas não caracteriza o diálogo competitivo, cuja ênfase é o debate e o desenvolvimento de alternativas prévias às propostas finais, sendo uma modalidade para bens/serviços complexos, e não de menor preço puro presencial.
A alternativa **C** está incorreta, visto que inovações padronizadas ou serviços de prateleira podem ser adquiridos via concorrência ou pregão (desde que sejam comuns). O diálogo existe para o que NÃO for padronizado.
A alternativa **D** está incorreta, pois as PPPs possuem lei própria e o principal foco do diálogo não é apenas "menor preço global" via lances, mas sim o critério de técnica e preço ou melhor técnica, após estruturar o edital.
A alternativa **E** está incorreta, porque bens e serviços comuns são obrigatoriamente licitados pela modalidade Pregão, jamais pelo diálogo competitivo.
</details>

---

### Questão 6 (FCC - 2023 - TRE SP - Técnico Judiciário - Área Administrativa)
A responsabilidade civil do Estado brasileiro, nos termos previstos no art. 37, §6º da Constituição Federal:
A) adota, como regra principal, a teoria da culpa administrativa ou falta do serviço.
B) exige, para a condenação do ente público a reparar o dano, a comprovação de dolo ou culpa de seu agente por parte do particular.
C) adota a teoria do risco integral em todas as situações que envolvam prestação de serviço público essencial.
D) é de natureza objetiva para as pessoas jurídicas de direito público e as de direito privado prestadoras de serviços públicos.
E) restringe-se às condutas comissivas, não incidindo em nenhuma hipótese sobre casos de omissões da autoridade pública.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A alternativa **D** é a correta. O art. 37, §6º da Constituição Federal estabelece que as pessoas jurídicas de direito público (União, Estados, Municípios, Autarquias, Fundações Públicas) e as de direito privado prestadoras de serviços públicos (Concessionárias, Empresas Públicas prestadoras de serviço) responderão pelos danos causados por seus agentes a terceiros, baseando-se na responsabilidade civil objetiva (Teoria do Risco Administrativo).
A alternativa **A** está incorreta, pois a regra constitucional da teoria adotada é o Risco Administrativo, configurando responsabilidade objetiva. A teoria da culpa administrativa exige a prova de falha do serviço e aplica-se subsidiariamente, não como regra.
A alternativa **B** está incorreta porque a natureza objetiva da responsabilidade significa que a vítima não precisa provar dolo ou culpa do Estado, bastando demonstrar o dano, a ação estatal e o nexo de causalidade.
A alternativa **C** é incorreta. A regra é a Teoria do Risco Administrativo, que admite atenuantes/excludentes (ex.: culpa exclusiva da vítima, força maior). O risco integral (onde não cabem excludentes) só se aplica no Brasil em hipóteses excepcionalíssimas (ex: dano nuclear e dano ambiental), e não na prestação de todo serviço público essencial.
A alternativa **E** é incorreta. O Estado também responde civilmente por omissões (em regra, de forma subjetiva; e, em casos de guarda e dever de vigilância, de forma objetiva), não estando sua responsabilidade limitada a condutas comissivas (ativas).
</details>

---

### Questão 7 (FCC - 2019 - TRF 4 - Analista Judiciário)
Considerando o regime jurídico instituído pela Lei nº 8.112/1990, a investidura em cargo público efetivo ocorre com:
A) a aprovação em concurso público homologado.
B) a nomeação, independentemente de qualquer outro ato formal por parte do Estado.
C) a posse do candidato, assinando o respectivo termo.
D) o exercício efetivo das atribuições típicas do cargo no local de lotação.
E) a publicação do ato de nomeação no Diário Oficial da União, tornando-se irrevogável.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A alternativa **C** é a correta. Nos termos literais do art. 7º da Lei 8.112/1990, "A investidura em cargo público ocorrerá com a posse". É na posse, com a assinatura do respectivo termo, que o candidato manifesta expressamente a sua aceitação das atribuições, direitos e deveres, passando formalmente à condição de servidor público.
A alternativa **A** é incorreta. A aprovação gera o direito subjetivo à nomeação (caso esteja nas vagas do edital), mas não preenche o cargo por si só, faltando as etapas de convocação.
A alternativa **B** é incorreta. A nomeação é apenas o ato unilateral originário do Estado chamando o indivíduo aprovado; ela não consuma a relação jurídica bilateral exigida para assumir o cargo, que depende da aceitação (posse).
A alternativa **D** é incorreta. O exercício (início efetivo das atividades laborais) decorre da posse. Se o servidor tomar posse e não entrar em exercício, será exonerado, mas a sua investidura já havia ocorrido previamente no ato da posse.
A alternativa **E** é incorreta, pois a publicação no Diário Oficial é uma exigência de publicidade para eficácia do ato de nomeação, mas não perfaz a investidura, devendo o sujeito apresentar-se para a posse no prazo de 30 dias.
</details>

---

### Questão 8 (FCC - 2021 - TRT 15 - Técnico Judiciário)
O ato de concessão inicial de aposentadoria de um servidor público federal, para ser considerado definitivo e plenamente exequível, submete-se à apreciação do Tribunal de Contas da União, que realizará o exame de legalidade para fins de registro. À luz da doutrina prevalente e da jurisprudência do STF, este ato classifica-se como:
A) ato simples.
B) ato complexo.
C) ato composto.
D) ato bilateral.
E) ato negocial.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A alternativa **B** está correta. A jurisprudência consolidada do STF pacificou o entendimento de que a concessão de aposentadoria (ou pensão e reforma) é um ato administrativo complexo. Ele se forma pela conjugação de vontades originárias e autônomas de órgãos diversos (a vontade do órgão ao qual o servidor se vincula e a vontade do Tribunal de Contas que promove o registro). Só quando o TCU registra o ato é que a aposentadoria passa a ser considerada um ato finalizado, perfeito.
A alternativa **A** está incorreta. Ato simples é aquele que decorre da declaração de vontade de um único órgão governamental, seja ele singular ou colegiado.
A alternativa **C** está incorreta. No ato composto, há duas vontades: uma principal e outra acessória/instrumental (homologação, visto ou aprovação). A aposentadoria poderia até se assemelhar estruturalmente, mas a classificação do STF consagrou que as duas manifestações formam a existência do ato principal, tratando-se, pois, de ato complexo, não composto.
A alternativa **D** é incorreta. Atos bilaterais são os contratos administrativos, baseados em acordo de vontades e interesses contrapostos (Estado e particular).
A alternativa **E** é incorreta. Os atos negociais representam declarações de vontade do Estado em harmonia com os interesses particulares (ex.: licença, permissão), mas a aposentadoria não é um negócio de interesse privado outorgado de forma precária, e sim o reconhecimento de um direito estatutário submetido a crivo complexo de validade.
</details>

---

### Questão 9 (FCC - 2022 - TRT 9 - Analista Judiciário)
Com relação às disposições da Lei de Improbidade Administrativa (Lei nº 8.429/1992, profundamente alterada pela Lei nº 14.230/2021), configura ato de improbidade:
A) a conduta meramente culposa do agente público que gera prejuízo ao erário, se o dano for de grande vulto financeiro.
B) a divergência na interpretação de lei, quando o agente, munido de dolo, busca finalidade expressamente lícita e amparada em jurisprudência.
C) a ação ou omissão dolosa que importe em enriquecimento ilícito do agente público em detrimento dos cofres públicos.
D) o exercício irregular do cargo que gere ineficiência nos serviços, mesmo na ausência de dolo e de enriquecimento próprio.
E) qualquer ação omissiva do agente que venha a violar os princípios constitucionais da Administração de forma exclusivamente culposa.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A alternativa **C** é a correta, figurando exatamente no art. 9º da Lei de Improbidade. Com a Lei nº 14.230/2021, passou a ser requisito inafastável para todas as modalidades (enriquecimento ilícito, prejuízo ao erário e atentado aos princípios) a presença do elemento subjetivo dolo, ou seja, a vontade livre e consciente de alcançar o resultado ilícito tipificado (dolo específico).
A alternativa **A** é incorreta. A alteração promovida em 2021 pela Lei 14.230 extinguiu a punição por atos de improbidade na modalidade culposa, inclusive nos casos de lesão ao erário (antigo art. 10 que admitia culpa). O dolo é sempre exigido, independentemente do vulto do dano.
A alternativa **B** é incorreta, pois o art. 1º, § 8º da Lei nº 8.429/92 expressamente exime o ato de improbidade em casos de mera divergência interpretativa da lei, fundamentada em jurisprudência ainda que não pacificada.
A alternativa **D** é incorreta. A ineficiência e as falhas gerenciais desprovidas de intenção de locupletamento ou de causar lesão intencional não se tipificam como improbidade administrativa, embora possam atrair punição disciplinar severa.
A alternativa **E** é incorreta, pois, assim como nas demais modalidades, os atos que atentam contra os princípios da Administração (art. 11) exigem estritamente comprovação de dolo com fim ilícito, jamais punindo a modalidade culposa.
</details>

---

### Questão 10 (FCC - 2023 - TRT 18 - Analista Judiciário)
A Administração Pública resolve conceder a uma empresa particular o direito de prestar um serviço público de transporte coletivo municipal, transferindo a sua execução por prazo determinado. O contrato administrativo pelo qual o Estado delega a prestação de serviços públicos, mediante licitação, à pessoa jurídica ou consórcio de empresas que demonstre capacidade para seu desempenho, por sua conta e risco, é tecnicamente denominado:
A) Autorização.
B) Concessão.
C) Permissão.
D) Consórcio público.
E) Franquia.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A alternativa **B** é a correta. De acordo com o art. 2º, inc. II, da Lei nº 8.987/1995 (Lei de Concessões e Permissões), a "concessão de serviço público" é a delegação da sua prestação, feita pelo poder concedente, mediante licitação (tradicionalmente na modalidade de concorrência, agora incluindo o diálogo competitivo pela Lei 14.133), à pessoa jurídica ou consórcio de empresas que demonstre capacidade para seu desempenho, por sua conta e risco e por prazo determinado.
A alternativa **A** está incorreta. A autorização de serviço público é ato administrativo (e não contrato bilateral), unilateral, discricionário e precário, não sendo precedido da formalidade de um contrato para prestação continuada de transporte regular e volumoso de grande porte.
A alternativa **C** está incorreta. Embora seja delegação de serviço público, a Permissão é contrato de adesão firmado a título precário, e sua lei admite a prestação por pessoa física ou jurídica (a concessão é estritamente a PJ/consórcio).
A alternativa **D** está incorreta. Consórcio público (Lei nº 11.107/05) é pessoa jurídica criada da união entre entes federativos (União, Estados, Municípios) para realização de objetivos comuns na administração, não constituindo um contrato de prestação por conta e risco voltado para o particular.
A alternativa **E** está incorreta. O contrato de Franquia é típico de Direito Privado (empresarial), regulamentando negócios de marcas e tecnologia. No setor público, sua aplicação (como no caso dos Correios) é uma exceção e não configura o mecanismo geral de delegação de transporte, regido primariamente pela concessão.
</details>

---

### Questão 11 (FCC - 2018 - TRT 2 - Técnico Judiciário)
No que se refere ao controle da Administração Pública exercido na República Federativa do Brasil, o julgamento sistemático das contas dos administradores e de demais responsáveis por dinheiros, bens e valores públicos, da administração direta e indireta, constitui competência constitucional do(a):
A) Ministério Público Federal, que atua como instância administrativa punitiva.
B) Controladoria-Geral da União, através de processos de auditoria vinculante.
C) Poder Judiciário Federal, exercendo controle preventivo, repressivo e de mérito das contas.
D) Tribunal de Contas respectivo, no exercício da sua competência de controle externo.
E) Congresso Nacional, privativamente, exercendo julgamento contábil sem o auxílio de qualquer outro órgão estatal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A alternativa **D** está correta. A Constituição Federal, no art. 71, inciso II, estabelece que compete ao Tribunal de Contas da União (extensível aos congêneres estaduais e municipais) "julgar as contas dos administradores e demais responsáveis por dinheiros, bens e valores públicos". Esse julgamento reveste-se da qualidade de atuação como órgão independente e técnico ligado à atividade de controle externo.
A alternativa **A** está incorreta. O Ministério Público instaura inquéritos e promove ações cíveis ou penais em casos de irregularidades, não julgando contas da Administração (ato que é de competência do TCU).
A alternativa **B** está incorreta. A CGU é o órgão máximo de controle interno do Poder Executivo Federal. Ela audita e fiscaliza, mas não tem competência jurisdicional de contas ou condão de julgamento que atinja gestores das estatais. O julgamento técnico das contas (que impõe devolução ao erário e gera títulos executivos) é prerrogativa do Tribunal de Contas.
A alternativa **C** está incorreta. O controle jurisdicional do Judiciário é provocado e rege-se pelo princípio da inafastabilidade, operando em regra na análise de legalidade repressiva. O Judiciário não possui competência constitucional para emitir julgamento originário das prestações contábeis mensais de órgãos executivos e apreciar mérito de escolhas administrativas lícitas.
A alternativa **E** está incorreta. O Poder Legislativo (Congresso Nacional, Assembleias) apenas detém a competência privativa de julgar politicamente as contas globais do Chefe do Poder Executivo, e isso ocorre com o indispensável auxílio técnico e parecer prévio emitido pelo Tribunal de Contas. As contas dos demais administradores são julgadas diretamente pelo TCU.
</details>

---

### Questão 12 (FCC - 2017 - TRE PR - Analista Judiciário)
O desfazimento de um ato administrativo que se formou perfeito e válido pela própria Administração Pública, tão somente em razão de ele ter se tornado inconveniente ou inoportuno perante o interesse público superveniente, opera-se de ofício mediante a:
A) Anulação, que produzirá efeitos ex tunc, apagando o ato da ordem jurídica.
B) Cassação, que produzirá efeitos ex nunc e aplicará a devida sanção.
C) Revogação, que produzirá efeitos ex tunc em função do princípio da razoabilidade.
D) Revogação, que produzirá efeitos ex nunc, respeitando os direitos já adquiridos.
E) Anulação, que produzirá efeitos ex nunc em proteção aos terceiros de boa-fé envolvidos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A alternativa **D** é a correta. Quando a Administração desfaz um ato porque ele deixou de atender à conveniência e à oportunidade (reapreciação do mérito), ela se vale da Revogação. O ato era legalmente expedido; logo, seus efeitos gerados no passado foram perfeitamente lícitos e não podem ser apagados, razão pela qual a revogação não tem poder retroativo, ou seja, gera efeitos apenas prospectivos (*ex nunc* — "daqui para frente"), preservando os direitos adquiridos e situações consolidadas.
A alternativa **A** é incorreta. A anulação é a forma jurídica de extinção reservada exclusivamente para sanar vício de legalidade, originando-se de um defeito na origem, operando, em regra, com efeitos retroativos (*ex tunc*).
A alternativa **B** é incorreta. A cassação de um ato ocorre como espécie de punição, em que o particular, após beneficiar-se do ato válido de concessão, comete falta legal posterior que extingue o benefício (ex.: hotel que passa a abrigar atividades ilícitas e tem o alvará cassado).
A alternativa **C** é incorreta, porque a revogação nunca surte efeitos retroativos (*ex tunc*). A finalidade da revogação é amparada nos critérios de conveniência/oportunidade, que não podem desrespeitar os atos do passado validamente ocorridos.
A alternativa **E** é incorreta. A anulação aplica-se à ilegalidade, e a regra na anulação (salvo hipóteses excepcionais de modulação pautadas na segurança jurídica) são os efeitos *ex tunc*, não havendo correspondência com a extinção por conveniência e oportunidade, que atrai o instituto da revogação.
</details>

---

### Questão 13 (FCC - 2021 - TRT 15 - Analista Judiciário)
Em relação aos consórcios públicos regulamentados pela Lei nº 11.107/2005, que tratam da cooperação federativa no Brasil, assinale a afirmativa correta.
A) Os consórcios públicos poderão adquirir personalidade jurídica de direito público ou de direito privado.
B) Apenas a União, os Estados e os Municípios podem integrar consórcio público, sendo vedada a participação expressa do Distrito Federal.
C) A criação de um consórcio público exige, inexoravelmente, a prévia edição de lei complementar por todos os entes consorciados.
D) Caso o consórcio adquira personalidade de direito privado, seus empregados serão regidos pelo regime jurídico único dos servidores estatutários de sua sede.
E) A União não poderá firmar convênio com consórcios públicos, mas apenas com os entes federados individualmente para a descentralização de recursos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A alternativa **A** está correta e espelha perfeitamente a literalidade do art. 1º, §1º, da Lei 11.107/2005. Ao ser criado, o consórcio público constituirá associação pública, se adquirir personalidade jurídica de direito público (passando a integrar a administração indireta de todos os entes da Federação consorciados), ou será constituído sob a forma de pessoa jurídica de direito privado.
A alternativa **B** é incorreta, porque o Distrito Federal, como ente federativo autônomo, está expressamente autorizado a figurar em consórcios públicos e participar ativamente da cooperação regional.
A alternativa **C** é incorreta. A adesão ao consórcio e ratificação do protocolo de intenções deve ser feita por meio de edição de Lei Ordinária de cada ente, não existindo imposição constitucional e legal para edição de Lei Complementar.
A alternativa **D** é incorreta. O art. 6º, §2º, estipula que a admissão de pessoal pelos consórcios públicos (tanto os de direito público quanto os de direito privado) ocorrerá unicamente pela égide das normas consolidadas de trabalho (regime celetista). Portanto, é proibida a adoção de regime estatutário (RJUs).
A alternativa **E** é incorreta. A lei que rege a matéria possibilita a celebração de convênios, contratos de repasse e instrumentos congêneres da União não só com entes individualizados, mas diretamente com os próprios consórcios públicos, garantindo captação eficiente de investimentos (art. 2º, § 1º, II).
</details>

---

### Questão 14 (FCC - 2022 - TRT 14 - Analista Judiciário)
Em tema de bens públicos integrantes do patrimônio da Administração, os rios navegáveis, mares, estradas estaduais, ruas e praças municipais são classificados, de acordo com o Código Civil brasileiro vigente, como:
A) bens dominicais, sendo imprescritíveis, mas passíveis de alienação imediata para arrecadação financeira.
B) bens de uso especial, afetados ao serviço público governamental e inalienáveis enquanto conservarem esta qualificação específica de segurança pública.
C) bens de uso comum do povo, sendo permitida sua utilização por toda coletividade, podendo estar sujeitos a cobrança mediante regulamentos e leis.
D) bens de posse privativa do Estado, não ostentando natureza pública, exceto se devidamente registrados em cartórios de imóveis como dominicais.
E) bens públicos classificados como indisponíveis por natureza perpétua, sendo juridicamente impossível qualquer processo de desafetação ao longo do tempo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A alternativa **C** está correta. Nos precisos termos do art. 99, inciso I, do Código Civil, os bens de uso comum do povo são "tais como rios, mares, estradas, ruas e praças", sendo que o uso é acessível e livre a todos os membros da coletividade, seja de forma gratuita ou de forma remunerada (a depender do que as leis fixarem — como os pedágios ou outorgas de uso sobre calçadas), e são inalienáveis enquanto preservarem essa afetação pública.
A alternativa **A** é incorreta. Bens dominicais (ou dominiais) formam o patrimônio de renda do Estado. São desafetados, destituídos de finalidade pública primária (como lotes vagos e fazendas desativadas), passíveis de alienação em processo formal, e não se prestam a classificar rios, mares e vias terrestres.
A alternativa **B** é incorreta. Bens de uso especial são aqueles afetados e destinados à prestação de um serviço administrativo particular da máquina pública ou ao suporte do Estado (ex.: prédio de delegacia, hospitais públicos, veículo viatura, biblioteca estadual). O mar e a praça não servem primariamente à repartição pública, mas diretamente à população em geral.
A alternativa **D** é incorreta. Todos esses itens (ruas, praças) gozam de natureza inteiramente de "bem público", não se misturando às regras do domínio meramente privado e, por fim, dispensando registro imobiliário para terem sua presunção de afetação por finalidade coletiva originária (nos casos de praias e mares).
A alternativa **E** é incorreta. A afetação ou o uso comum não são perpetuamente indisponíveis de forma insuperável. Uma praça ou rua pode, mediante estudo, conveniência pública e autorização de Lei formal respectiva, sofrer procedimento de desafetação. Após a perda desse atributo, passará a ser enquadrada como bem dominical, tornando-se, excepcionalmente, passível de alienação pelas regras licitatórias.
</details>

---

### Questão 15 (FCC - 2023 - TRT 12 - Técnico Judiciário)
Pelo princípio administrativo da razoabilidade (implícito na esfera federal e expresso em muitas Constituições Estaduais), um ato discricionário praticado pela autoridade administrativa pode ser perfeitamente invalidado pelo Poder Judiciário se:
A) não houver pertinência, adequação e proporcionalidade entre o fim constitucional almejado e os meios empregados, configurando evidente excesso ou desvio nas punições ou restrições impostas.
B) tiver sido exarado por agente administrativo sabidamente incompetente para o mister, independentemente da justiça e do mérito de sua finalidade.
C) carecer de prévia publicação na imprensa oficial para surtir efeitos imediatos e eficazes perante a rotina dos particulares afetados.
D) deixar de apresentar fundamentação fática pormenorizada ou argumentação analítica exaustiva em todas as suas laudas, como regra para validade de todo e qualquer despacho meramente ordinatório.
E) a lei que embasava o seu dispositivo legal vier a ser revogada antes da finalização total da execução continuada dos efeitos pretendidos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A alternativa **A** está correta. A essência do princípio da razoabilidade consiste na aferição da compatibilidade entre os meios empregados e os fins buscados na lei. Assim, ainda que o administrador atue dentro da margem de discricionariedade permitida pela norma, caso ele se exceda severamente (ou puna abusivamente quando medidas brandas seriam suficientes), a doutrina entende que houve violação dos contornos que formam o núcleo da finalidade, permitindo sua invalidação pelo Poder Judiciário em função do vício latente.
A alternativa **B** está incorreta. A invalidação em virtude de ser emitido por agente incompetente diz respeito à manifestação objetiva do vício atrelado ao princípio basilar da legalidade ou à falta dos requisitos constitutivos (competência, sujeito), e não toca, na gênese, à mensuração das balizas da razoabilidade no âmbito da escolha de mérito.
A alternativa **C** está incorreta. O vício na publicação em órgão oficial é defeito relativo ao princípio da publicidade ou um problema referente à eficácia (produção de efeitos do ato perante terceiros).
A alternativa **D** está incorreta. A justificativa técnica para as decisões está lastreada no princípio específico da motivação. Além disso, no Direito Administrativo não se exige que despachos de mero expediente (sem conteúdo decisório) tenham extensa argumentação, bastando motivação aos atos que alteram, criam ou restringem direitos.
A alternativa **E** está incorreta. Uma mudança legislativa futura em face de um ato passado que se encontrava dentro do comando de razoabilidade gera impasses associados a direito adquirido ou conflitos de aplicação temporal da lei (segurança jurídica e efeito repristinatório), não tendo vinculação intrínseca com o vício originário por descompasso na razoabilidade.
</details>


