# Bateria de Questões FCC — Sexta-feira 29/05
Este arquivo contém 45 questões altamente calibradas nos padrões da FCC, com alternativas de comprimento similar e distratores baseados em pegadinhas reais.

---
## 📝 TEMA 1: Segurança da Informação — Criptografia, Hashes, Certificados e Assinatura Digital
### Questão 1 (FCC)
Criptografia simétrica e assimétrica diferem essencialmente na forma de gerenciamento das chaves de segurança. Sobre essa diferença, é correto afirmar:
A) A criptografia simétrica utiliza um par de chaves em que a chave privada cifra os dados e a chave pública decifra os dados de forma exclusiva.
B) A criptografia assimétrica utiliza uma única chave secreta que deve ser distribuída previamente por canais físicos e seguros.
C) A criptografia simétrica utiliza uma única chave compartilhada para cifrar e decifrar os dados, enquanto a assimétrica utiliza um par de chaves (pública e privada).
D) A criptografia assimétrica possui menor custo computacional, sendo preferida para cifrar grandes volumes de dados de tráfego de rede.
E) A criptografia simétrica impede o não-repúdio de forma nativa, pois cada sessão possui um par de chaves públicas geradas dinamicamente.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 2 (FCC)
As funções de hash criptográfico desempenham um papel vital na segurança da informação. A propriedade que garante que é computacionalmente inviável encontrar dois inputs diferentes que gerem o mesmo valor de hash de saída é a:
A) Resistência à segunda pré-imagem
B) Resistência à pré-imagem
C) Resistência à colisão
D) Propriedade de efeito avalanche
E) Propriedade de integridade simétrica

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 3 (FCC)
Em relação aos algoritmos de criptografia simétrica clássicos e modernos, assinale a opção que apresenta um algoritmo considerado inseguro devido ao seu tamanho de chave e o algoritmo padrão que o substituiu, respectivamente:
A) AES (chave de 128 bits) e DES (chaves de 512 bits)
B) DES (chave de 56 bits) e AES (chaves de 128, 192 ou 256 bits)
C) RSA (chave de 1024 bits) e AES (chaves de 128 bits)
D) DES (chave de 56 bits) e RSA (chaves de 2048 bits)
E) MD5 (chave de 128 bits) e SHA-256 (chaves de 256 bits)

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 4 (FCC)
O algoritmo RSA é um dos sistemas de criptografia assimétrica mais conhecidos. Sua segurança fundamenta-se na dificuldade matemática de realizar a seguinte operação computacional:
A) Ordenação de chaves criptográficas em pilhas de dados recursivas orientadas.
B) Cálculo de logaritmos discretos em corpos finitos de curvas elípticas generalizadas.
C) Multiplicação matricial densa em bases de dados multidimensionais sem perdas.
D) Fatoração de números inteiros grandes que são produtos de dois números primos grandes.
E) Resolução de sistemas lineares de equações com múltiplas variáveis complexas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 5 (FCC)
Para garantir a integridade e o não-repúdio de um documento assinado digitalmente, a assinatura digital é gerada pelo remetente cifrando:
A) A chave simétrica de sessão temporária utilizando a chave privada da autoridade certificadora.
B) O documento original de forma completa utilizando a chave pública do destinatário final.
C) O resumo criptográfico (hash) do documento original utilizando a chave pública do destinatário.
D) O resumo criptográfico (hash) do documento original utilizando a chave privada do próprio remetente.
E) O documento original de forma completa utilizando a chave privada do destinatário final.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 6 (FCC)
Os certificados digitais baseados no padrão X.509 são utilizados para associar a identidade de um usuário a um par de chaves criptográficas. Um elemento que consta obrigatoriamente do certificado digital do usuário é:
A) A chave pública do usuário associada à assinatura digital da Autoridade Certificadora emissora.
B) A chave privada do usuário associada ao hash de validação gerado pelo navegador.
C) A chave privada da Autoridade Certificadora responsável pela emissão da chave do usuário.
D) A lista completa de senhas criptografadas do usuário em serviços públicos de diretório.
E) A chave simétrica acordada no início da sessão de handshake do protocolo HTTPS.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 7 (FCC)
Para conciliar a segurança do gerenciamento de chaves e a eficiência de processamento de dados, os sistemas modernos utilizam criptografia híbrida. Na criptografia híbrida:
A) O algoritmo de hash calcula o resumo digital, e a criptografia simétrica cifra o hash gerando a assinatura.
B) A criptografia simétrica é usada para compartilhar a chave pública, e a criptografia assimétrica é usada para cifrar os dados da mensagem.
C) As chaves simétrica e assimétrica são combinadas gerando uma única chave híbrida indivisível e permanente.
D) A criptografia assimétrica realiza a cifragem dos blocos de dados, e a criptografia simétrica garante o não-repúdio.
E) A criptografia assimétrica é usada para compartilhar a chave simétrica, e a criptografia simétrica é usada para cifrar os dados da mensagem.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 8 (FCC)
As funções hash da família SHA-2 são amplamente recomendadas para segurança de sistemas. Assinale a alternativa que apresenta apenas algoritmos válidos e pertencentes a essa família:
A) SHA-256, MD5 e SHA-3
B) SHA-1, SHA-2, SHA-3 e SHA-4
C) SHA-128, SHA-256 e SHA-512
D) SHA-224, SHA-256, SHA-384 e SHA-512
E) SHA-256, HMAC e SHA-1

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 9 (FCC)
No âmbito da Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil), a entidade que atua como o topo da cadeia (Autoridade Certificadora Raiz), credenciando e fiscalizando as demais Autoridades Certificadoras (ACs), é o:
A) ANPD (Autoridade Nacional de Proteção de Dados)
B) ITI (Instituto Nacional de Tecnologia da Informação)
C) CNJ (Conselho Nacional de Justiça)
D) MCTI (Ministério da Ciência, Tecnologia e Inovação)
E) SERPRO (Serviço Federal de Processamento de Dados)

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 10 (FCC)
Sobre os algoritmos de hash criptográfico clássicos MD5 e SHA-1, assinale a opção que descreve corretamente o seu status atual de segurança:
A) São os algoritmos simétricos padrão para cifragem de discos rígidos em servidores de datacenters modernos.
B) Permanecem totalmente seguros e são recomendados pela ICP-Brasil para assinaturas de processos eletrônicos judiciais.
C) São considerados inseguros para aplicações criptográficas de assinatura devido à descoberta de colisões práticas em tempo viável.
D) Foram unificados no algoritmo SHA-3 para formar um único hash de 512 bits resistente a computação quântica.
E) São restritos exclusivamente ao uso em redes locais com cabeamento estruturado de par trançado Classe F.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 11 (FCC)
Para verificar se um certificado digital X.509 de um servidor foi revogado antes de expirar a sua validade, o navegador cliente pode consultar periodicamente:
A) O banco de dados de chaves simétricas negociadas durante o handshake do protocolo HTTPS.
B) O repositório local de chaves privadas do sistema operacional ou o arquivo temporário de hosts DNS.
C) A Lista de Revogação de Certificados (LRC / CRL) ou utilizar o protocolo online OCSP (Online Certificate Status Protocol).
D) A Autoridade Certificadora Raiz através de uma requisição síncrona baseada em FTP.
E) O Comitê de Acessibilidade da ICP-Brasil responsável pelo credenciamento das Autoridades de Registro.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 12 (FCC)
Ao receber um arquivo assinado digitalmente, o destinatário verifica a assinatura realizando o seguinte procedimento técnico:
A) Calcula o hash do arquivo recebido e o compara com o hash obtido ao decifrar a assinatura com a sua própria chave privada.
B) Decifra o arquivo completo usando a sua própria chave privada e o compara com o texto plano original enviado.
C) Envia o arquivo para a Autoridade Certificadora autenticar usando a chave privada da autoridade.
D) Calcula o hash do arquivo recebido e o compara com o hash obtido ao decifrar a assinatura com a chave pública do remetente.
E) Decifra a assinatura digital usando a chave simétrica acordada no handshake do TLS.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 13 (FCC)
A Criptografia de Curvas Elípticas (ECC) possui uma vantagem técnica importante sobre os algoritmos assimétricos clássicos como o RSA:
A) Ser imune a qualquer ataque físico ou lógico mesmo que a chave privada seja exposta publicamente.
B) Funcionar sem a necessidade de chaves públicas, reduzindo o tráfego de dados na rede.
C) Ser um algoritmo de criptografia simétrica com suporte nativo a blocos dinâmicos de dados.
D) Garantir a integridade dos dados sem a necessidade de calcular funções hash adicionais.
E) Oferecer o mesmo nível de segurança criptográfica que o RSA utilizando tamanhos de chaves significativamente menores.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 14 (FCC)
Para validar a autenticidade de um certificado digital X.509 recebido de um servidor, o cliente realiza as seguintes verificações, com EXCEÇÃO de:
A) Confirmar se o certificado não consta em Listas de Revogação de Certificados (CRLs) atualizadas.
B) Verificar a validade do certificado comparando a data atual com o período de validade constante no documento.
C) Validar a assinatura digital do certificado utilizando a chave pública da Autoridade Certificadora que o emitiu.
D) Verificar se a chave privada do certificado do servidor corresponde à chave pública da Autoridade Certificadora emissora.
E) Verificar se o nome de domínio (Common Name - CN) do certificado corresponde ao endereço do website acessado.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 15 (FCC)
Em segurança da informação, o não-repúdio (irretratabilidade) é a garantia de que:
A) Os dados transmitidos não sofreram qualquer alteração acidental ou intencional durante o trânsito na rede.
B) O emissor de uma mensagem ou transação assinada digitalmente não pode negar a sua autoria ou criação.
C) Apenas usuários autorizados tenham acesso à leitura do conteúdo confidencial armazenado em servidores.
D) Os sistemas de rede estejam disponíveis e funcionais para os usuários legítimos em tempo integral.
E) O canal de comunicação simétrico impeça o acesso físico aos servidores e switches locais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

## 📝 TEMA 2: Engenharia de Software — Programação em PHP, C, C# e .NET, SOLID e GRASP
### Questão 16 (FCC)
O princípio SOLID da Responsabilidade Única (Single Responsibility Principle - SRP) estabelece que:
A) Uma classe só pode conter um único método público para realizar todas as operações do seu módulo.
B) Uma classe deve ter um, e apenas um, motivo para mudar, possuindo uma única responsabilidade no sistema.
C) Os componentes do sistema devem ser acoplados exclusivamente de forma síncrona na camada de apresentação.
D) Toda interface deve declarar apenas um método abstrato a ser implementado pelas classes herdeiras.
E) O banco de dados deve possuir apenas uma tabela associada a cada entidade de negócio do sistema.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 17 (FCC)
De acordo com o princípio SOLID Aberto-Fechado (Open-Closed Principle - OCP), as entidades de software (classes, módulos, funções) devem ser:
A) Abertas para extensão, mas fechadas para modificação.
B) Abertas para modificação externa, mas fechadas para herança.
C) Abertas para acesso público, mas fechadas para injeção de dependências.
D) Abertas para persistência em disco, mas fechadas para compilação local.
E) Abertas para alterações parciais no código, mas fechadas para refatorações.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 18 (FCC)
O princípio SOLID da Substituição de Liskov (Liskov Substitution Principle - LSP) determina que:
A) Toda classe derivada deve herdar diretamente de múltiplas superclasses abstratas simultaneamente.
B) Subclasses devem sobrescrever todos os métodos da superclasse para alterar a assinatura original e forçar o polimorfismo.
C) Objetos de uma superclasse devem ser substituíveis por objetos de suas subclasses sem que isso quebre o funcionamento correto do programa.
D) Interfaces não podem ser estendidas por outras interfaces para evitar conflitos de implementação múltipla.
E) Classes concretas devem substituir todas as referências a injeção de dependências por instanciação estática de objetos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 19 (FCC)
O princípio SOLID da Segregação de Interfaces (Interface Segregation Principle - ISP) preconiza que:
A) Interfaces de persistência de banco de dados devem ser separadas fisicamente de classes controladoras MVC.
B) Interfaces devem ser unificadas em um único arquivo de contrato para facilitar a manutenção de grandes sistemas Java ou C#.
C) Módulos de alto nível não devem herdar de interfaces abstratas criadas em pacotes de baixo nível.
D) Todas as interfaces do sistema devem declarar obrigatoriamente constantes estáticas e finais do tipo string.
E) Muitas interfaces específicas são melhores do que uma única interface de propósito geral, evitando que classes sejam forçadas a depender de métodos que não utilizam.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 20 (FCC)
O princípio SOLID da Inversão de Dependência (Dependency Inversion Principle - DIP) estabelece que:
A) Módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações. Abstrações não devem depender de detalhes; detalhes devem depender de abstrações.
B) Módulos de baixo nível devem gerenciar o ciclo de vida e a instanciação estática dos objetos de alto nível no Spring Framework.
C) As dependências do sistema devem ser invertidas fisicamente no disco através de links simbólicos de arquivos binários.
D) Classes concretas devem depender diretamente de outras classes concretas, reduzindo o uso excessivo de interfaces e abstrações.
E) A injeção de dependência deve ser realizada exclusivamente através do construtor de classes sem visibilidade pública.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 21 (FCC)
No conjunto de padrões GRASP para atribuição de responsabilidades em POO, o padrão **Controller** (Controlador) é responsável por:
A) Impedir que classes de domínio interajam com as classes de visualização através do acoplamento forte.
B) Garantir que uma classe tenha apenas uma única instância física carregada na memória da máquina virtual Java ou .NET.
C) Criar objetos de coleções complexas e encapsular o acesso físico a tabelas de banco de dados relacionais.
D) Definir a estrutura hierárquica de classes para simular a herança múltipla de comportamento em interfaces simples.
E) Receber eventos do sistema originados por elementos da interface do usuário (UI) e coordenar as operações de negócio adequadas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 22 (FCC)
De acordo com o padrão GRASP **Creator** (Criador), uma classe $A$ deve ser responsável pela criação de instâncias de uma classe $B$ se:
A) O desenvolvedor deseja aplicar o princípio SOLID da substituição de Liskov na instanciação de Beans.
B) A classe $B$ estende diretamente a classe $A$ através de herança simples ou múltipla de implementação.
C) A classe $A$ não possui atributos de instância e declara apenas métodos estáticos e abstratos.
D) A classe $A$ agrega, contém, registra ou usa de forma muito próxima as instâncias da classe $B$.
E) O banco de dados relacional possui uma chave estrangeira de $A$ apontando para a tabela $B$ correspondente.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 23 (FCC)
Na linguagem de programação C, o operador de desreferenciação `*` (asterisco) e o operador de endereço `&` (e comercial), quando aplicados a ponteiros e variáveis comuns, servem para, respectivamente:
A) Acessar o valor armazenado no endereço apontado pelo ponteiro, e obter o endereço de memória de uma variável comum.
B) Obter o endereço de memória de uma variável ponteiro, e realizar a multiplicação aritmética de dois inteiros.
C) Alocar espaço na memória heap do sistema operacional, e liberar o espaço em memória associado à variável local.
D) Declarar uma constante global em tempo de compilação, e verificar a igualdade lógica de dois valores booleanos.
E) Concatenar duas sequências de caracteres na memória dinâmica, e calcular a negação lógica de bits.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 24 (FCC)
Em PHP 8+, a declaração `namespace` e a utilização de ferramentas como o autoloader do Composer têm como finalidade principal:
A) Substituir o uso de classes de banco de dados por consultas SQL em formato binário indexado.
B) Compilar o código PHP em linguagem de máquina nativa do servidor, e gerenciar a segurança lógica de portas abertas.
C) Organizar e isolar o escopo de classes evitando conflitos de nomes, e carregar os arquivos de classes sob demanda de forma automática (lazy loading).
D) Exigir a declaração obrigatória de tipos dinâmicos para todas as variáveis globais da aplicação corporativa.
E) Importar bibliotecas em C++ compiladas diretamente no kernel do Apache Server sem passar pelo interpretador.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 25 (FCC)
Na linguagem C# e plataforma .NET, as variáveis são divididas em tipos de valor (value types) e tipos de referência (reference types). Sobre essa divisão, é correto afirmar:
A) O armazenamento de tipos de referência na pilha impede a ocorrência de exceções de estouro de memória (StackOverflowException).
B) Tipos de referência são armazenados na memória stack para garantir o acesso instantâneo e a liberação de espaço sem o Garbage Collector.
C) Tipos de valor são gerenciados pelo Garbage Collector da plataforma .NET de forma síncrona e obrigatória.
D) Classes em C# são classificadas como tipos de valor, enquanto as structs representam tipos de referência nativos.
E) Tipos de valor (como structs, int, bool) são armazenados diretamente na pilha (stack), enquanto tipos de referência (como classes, interfaces, objects) são armazenados na memória heap.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 26 (FCC)
Na linguagem C#, a instrução `using` (por exemplo, `using (var resource = new Resource()) { ... }`) é utilizada para garantir:
A) A liberação automática de recursos não gerenciados (como conexões de rede ou arquivos) ao final do bloco de código, chamando o método Dispose().
B) A importação de bibliotecas externas compiladas em C++ nativo e localizadas no diretório do sistema `/bin`.
C) A herança múltipla de interfaces por classes controladoras de dados da persistência do EF Core.
D) O tratamento obrigatório de exceções de divisão por zero e estouro de buffer em tempo de execução.
E) A compilação em lote de arquivos de código-fonte dinâmicos associados a namespaces corporativos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 27 (FCC)
Na linguagem de programação C, para alocar dinamicamente 10 inteiros na memória heap e, posteriormente, liberar esse espaço na memória de forma correta, o desenvolvedor deve utilizar, respectivamente, as funções:
A) malloc() e free()
B) new e delete
C) calloc() e remove()
D) alloc() e dispose()
E) malloc() e clean()

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 28 (FCC)
Em C#, as propriedades (properties) com sintaxes como `{ get; set; }` são utilizadas para:
A) Configurar o mapeamento objeto-relacional automático do framework Entity Framework sem anotações adicionais.
B) Definir que o atributo associado será armazenado exclusivamente na memória stack de acesso rápido.
C) Obrigar que a classe implemente herança de comportamento baseada em atributos públicos dinâmicos.
D) Bloquear o acesso de escrita por classes herdadas na mesma assembly em tempo de execução.
E) Implementar o encapsulamento de forma simplificada, abstraindo a criação manual de atributos privados e métodos getters/setters correspondentes.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 29 (FCC)
O padrão GRASP **Information Expert** (Especialista na Informação) dita que a responsabilidade de executar uma determinada tarefa deve ser atribuída para:
A) O módulo de persistência de dados encarregado do acesso ao banco de dados relacional.
B) A classe controladora que gerencia a interface visual do sistema operacional.
C) A classe abstrata que possui o maior número de subclasses concretas associadas.
D) A classe que possui as informações necessárias para realizar essa responsabilidade.
E) A interface que declara o maior número de métodos abstratos e propriedades genéricas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 30 (FCC)
O Garbage Collector (GC) da plataforma .NET atua de forma automática para gerenciar a memória da aplicação. A operação básica realizada pelo GC consiste em:
A) Autenticar os certificados digitais X.509 utilizados em requisições seguras ao banco de dados.
B) Mover todas as variáveis locais da memória stack para a memória heap para evitar erros de ponteiros nulos.
C) Compilar dinamicamente o código C# para linguagem intermediária (IL) durante a execução do programa.
D) Compactar fisicamente os arquivos executáveis gerados na pasta de publicação para economizar espaço em disco.
E) Monitorar a memória heap para liberar o espaço alocado por objetos que não possuem mais nenhuma referência ativa no programa.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

## 📝 TEMA 3: Língua Portuguesa — Flexão Nominal e Verbal, Vozes do Verbo e Transposição
### Questão 31 (FCC)
A transposição de uma oração da voz ativa para a voz passiva analítica exige a reestruturação dos termos sintáticos. A frase *'O analista do tribunal desenvolveu o novo sistema de segurança'* transposta para a voz passiva analítica assume a seguinte redação correta:
A) O novo sistema de segurança desenvolvera-se pelo analista do tribunal.
B) Desenvolveu-se o novo sistema de segurança pelo analista do tribunal.
C) O novo sistema de segurança foi desenvolvido pelo analista do tribunal.
D) O analista do tribunal tinha desenvolvido o novo sistema de segurança.
E) O novo sistema de segurança seria desenvolvido pelo analista do tribunal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 32 (FCC)
A voz passiva sintética (ou pronominal) caracteriza-se pelo uso do pronome apassivador 'se' associado a verbo transitivo direto. Assinale a frase que exemplifica corretamente o uso da voz passiva sintética:
A) Precisa-se de novos servidores estáveis na área de infraestrutura de TI.
B) Identificaram-se falhas graves de segurança nos servidores do tribunal.
C) Os técnicos assistiram ao deploy do novo módulo judicial na quarta-feira.
D) Eles referiram-se ao antigo banco de dados corporativo durante a reunião.
E) Trabalhou-se bastante durante o fim de semana para corrigir os bugs de rede.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 33 (FCC)
Na oração *'As novas regras de tratamento de dados pessoais foram estabelecidas pela ANPD'*, o termo *'pela ANPD'* desempenha a função sintática de:
A) Agente da passiva
B) Objeto direto preposicionado
C) Adjunto adnominal
D) Predicativo do sujeito
E) Complemento nominal

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 34 (FCC)
Transpondo a frase *'Os auditores analisarão todos os logs de acesso'* para a voz passiva sintética, obtém-se a forma correta:
A) Todos os logs de acesso serão analisados pelos auditores.
B) Analisar-se-ia todos os logs de acesso.
C) Analisar-se-ão todos os logs de acesso.
D) Teriam sido analisados todos os logs de acesso pelos auditores.
E) Analisaram-se todos os logs de acesso pelos auditores.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 35 (FCC)
Assinale a alternativa que apresenta a flexão verbal correta de acordo com a norma-padrão da língua portuguesa:
A) Se eles manterem os backups atualizados, o risco de perda de dados diminuirá.
B) Se eles mantiverem os backups atualizados, o risco de perda de dados diminuirá.
C) Quando a equipe ver o relatório de erros, tomará as devidas providências.
D) Se o diretor intervir a tempo, a falha crítica de rede não ocorrerá hoje.
E) Eles requiseram a exclusão definitiva dos prontuários médicos da base.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 36 (FCC)
O verbo intervir é derivado do verbo vir e deve seguir a sua conjugação. Assinale a alternativa que apresenta a flexão correta desse verbo no pretérito perfeito do indicativo:
A) Quando o comitê intervir na tomada de decisões, as falhas serão sanadas.
B) O comitê interviu na tomada de decisões estratégicas de segurança ontem.
C) Os analistas interviram na tomada de decisões estratégicas de segurança ontem.
D) Se o comitê intervisse na tomada de decisões, o projeto teria sucesso.
E) O comitê interveio na tomada de decisões estratégicas de segurança ontem.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 37 (FCC)
A voz reflexiva ocorre quando o sujeito pratica e sofre a ação verbal simultaneamente. A frase que exemplifica a voz reflexiva com pronome de reciprocidade (ação mútua) é:
A) Os técnicos queixaram-se do calor excessivo dentro da sala de servidores públicos.
B) O desenvolvedor cortou-se acidentalmente com a chapa de metal do rack de rede.
C) O sistema operacional atualizou-se automaticamente durante a madrugada.
D) Os dois analistas de sistemas parabenizaram-se mutuamente pelo deploy bem-sucedido.
E) Eles arrependeram-se de não ter migrado a base de dados para o PostgreSQL.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 38 (FCC)
Ao realizar a transposição de uma frase da voz ativa para a voz passiva analítica, o tempo e modo do verbo auxiliar da passiva deve corresponder exatamente ao tempo e modo do verbo principal da ativa. Na frase *'O switch transmitia os pacotes de dados'*, o verbo auxiliar correspondente na voz passiva analítica deve ser flexionado no:
A) Pretérito imperfeito do indicativo (eram)
B) Pretérito perfeito do indicativo (foram)
C) Futuro do pretérito do indicativo (seriam)
D) Pretérito mais-que-perfeito do indicativo (tinham sido)
E) Presente do indicativo (são)

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 39 (FCC)
Alguns verbos possuem dois particípios: um regular (terminado em -ado ou -ido), usado com os auxiliares ter ou haver, e outro irregular, usado com ser ou estar. Assinale a frase gramaticalmente correta em relação ao uso do particípio:
A) O documento de requisitos foi imprimido em papel timbrado pelo analista.
B) A proposta comercial de TI foi aceitada pela comissão de licitação do tribunal.
C) A equipe já tinha elegido o novo coordenador de segurança da informação.
D) O tribunal já havia aceitado todas as propostas comerciais enviadas pelas empresas.
E) Os servidores públicos já tinham chego ao prédio do fórum judicial de manhã.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**. A alternativa D descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 40 (FCC)
Na frase *'Não se tolerarão falhas graves no processamento de dados dos cidadãos'*, a função da palavra 'se' e a classificação de voz da oração são, respectivamente:
A) Conjunção subordinada condicional e voz ativa com sujeito composto.
B) Índice de indeterminação do sujeito e voz ativa com sujeito indeterminado.
C) Pronome reflexivo e voz reflexiva com sujeito simples.
D) Partícula expletiva de realce e voz ativa com sujeito oculto.
E) Pronome apassivador e voz passiva sintética.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**. A alternativa E descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 41 (FCC)
Assinale a alternativa que apresenta a flexão de plural correta do substantivo composto de acordo com a norma-padrão:
A) Os novos decretos estabeleceram diversos salário-famílias para os servidores.
B) Os novos decretos estabeleceram diversos salários-família para os servidores.
C) A comissão contratou dois analistas de sistemas recém-formados para os cargos-chaves.
D) Os técnicos instalaram os softwares-base em todos os computadores do fórum.
E) As partes assinaram os termos de cooperação com vários estados-membros.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 42 (FCC)
O verbo reaver é classificado como defectivo e deve ser conjugado apenas nas formas em que o verbo haver possui a letra 'v'. Assinale a alternativa que apresenta a flexão correta do verbo reaver:
A) Nós reavemos todos os arquivos de backups que haviam sido apagados da base.
B) Nós reouvemos todos os arquivos de backups que haviam sido apagados da base.
C) Se a equipe reaver os arquivos de backups, o sistema voltará a funcionar.
D) Eles reaveram o acesso físico aos servidores após a intervenção técnica.
E) Quando a comissão reaver os documentos de licitação, o processo continuará.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**. A alternativa A descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 43 (FCC)
A transposição para a voz passiva só é possível em orações que possuem objeto direto na voz ativa (verbos transitivos diretos ou transitivos diretos e indiretos). Assinale a frase que NÃO admite transposição para a voz passiva:
A) O analista de infraestrutura instalou o sistema operacional Linux no servidor.
B) Os técnicos de TI necessitam de novos switches gigabit ethernet de alto desempenho.
C) O comitê de acessibilidade analisou as barreiras físicas no prédio do fórum.
D) A empresa terceirizada entregou os cabos de manobra patch cord na terça-feira.
E) A ANPD aplicou uma advertência administrativa formal ao órgão público.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 44 (FCC)
Assinale a alternativa que apresenta o emprego correto do verbo no modo subjuntivo de acordo com a norma-padrão:
A) Caso a equipe requira o acesso ao banco de dados, o administrador concederá.
B) Caso a equipe requeira o acesso ao banco de dados, o administrador concederá.
C) Quando o diretor propor o novo planejamento de metas, todos concordarão.
D) Se o analista dispor de tempo livre hoje à tarde, revisará os requisitos.
E) Se nós medirmos a velocidade do canal de cabeamento, o teste falhará.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**. A alternativa B descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---

### Questão 45 (FCC)
Transpondo a frase *'A diretoria de TI vinha revisando os processos de deploy'* para a voz passiva analítica, obtém-se a forma correta:
A) Os processos de deploy tinham sido revisados pela diretoria de TI.
B) Os processos de deploy vinha sendo revisados pela diretoria de TI.
C) Os processos de deploy vinham sendo revisados pela diretoria de TI.
D) Os processos de deploy foram sendo revisados pela diretoria de TI.
E) Revisavam-se os processos de deploy pela diretoria de TI.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**. A alternativa C descreve corretamente a resposta com base na especificação técnica cobrada pela banca FCC.
</details>

---
