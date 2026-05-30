# Bateria de Questões FCC — Sexta-feira 29/05

## 📝 TEMA 1: Segurança da Informação (Criptografia/Certificação)

### Questão 1 (FCC - 2018 - TRT 15 - Analista de TI)
Na assinatura digital de um documento, para garantir a autenticidade e o não repúdio, o emissor deve cifrar o resumo criptográfico (hash) da mensagem utilizando
A) a chave privada do receptor.
B) a chave pública do receptor.
C) a sua própria chave privada.
D) a sua própria chave pública.
E) uma chave simétrica compartilhada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Explicação:
A assinatura digital baseia-se em criptografia assimétrica, garantindo autenticidade, integridade e não repúdio.
- **A) Incorreta.** O emissor não tem acesso à chave privada do receptor, pois ela é de uso exclusivo do seu dono.
- **B) Incorreta.** Utilizar a chave pública do receptor serve para garantir confidencialidade da mensagem (apenas ele poderá ler), não para assiná-la.
- **C) Correta.** O emissor cifra o hash do documento com sua própria chave privada. Assim, qualquer pessoa pode usar a chave pública do emissor para verificar a assinatura, atestando a autenticidade e o não repúdio (já que só o emissor detém a sua chave privada).
- **D) Incorreta.** A chave pública do emissor é de conhecimento público. Se a assinatura fosse feita com ela, qualquer um poderia forjar a assinatura do emissor.
- **E) Incorreta.** A chave simétrica não garante o não repúdio, pois ambas as partes (emissor e receptor) conhecem a mesma chave e poderiam gerar a assinatura.
</details>

---

### Questão 2 (FCC - 2016 - TRT 20 - Analista de TI)
Na criptografia assimétrica, se João deseja enviar uma mensagem confidencial para Maria, de modo que apenas ela consiga ler, João deve cifrar a mensagem utilizando:
A) a chave privada de João.
B) a chave pública de João.
C) a chave privada de Maria.
D) a chave pública de Maria.
E) uma chave de sessão simétrica pública.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

Explicação:
A criptografia assimétrica usa um par de chaves: pública (distribuída livremente) e privada (mantida em segredo absoluto).
- **A) Incorreta.** Se João usar sua chave privada, ele estará criando uma assinatura digital (autenticação). Qualquer um com a chave pública de João poderia decifrar a mensagem, logo não haveria confidencialidade.
- **B) Incorreta.** Se João cifrar com sua própria chave pública, apenas a chave privada dele mesmo poderia decifrar a mensagem, ou seja, apenas João conseguiria ler o conteúdo.
- **C) Incorreta.** João não tem (e não deve ter) acesso à chave privada de Maria, pois ela é secreta e de posse exclusiva dela.
- **D) Correta.** Ao cifrar a mensagem com a chave pública de Maria (que é de acesso livre), João garante que o conteúdo só poderá ser decifrado usando a chave correspondente, que é a chave privada de Maria, garantindo assim a confidencialidade.
- **E) Incorreta.** Não existe o conceito de "chave simétrica pública", pois na criptografia simétrica a chave deve ser secreta para ambas as partes.
</details>

---

### Questão 3 (FCC - 2018 - TRT 6 - Analista de TI)
As funções de Hash (resumo criptográfico) são algoritmos matemáticos aplicados sobre conjuntos de dados. Na segurança da informação, elas são amplamente utilizadas para:
A) garantir a confidencialidade de um arquivo durante a sua transmissão em canais inseguros.
B) assegurar a integridade de um arquivo ou mensagem, verificando se houve qualquer alteração em seu conteúdo.
C) criptografar dados de forma reversível em disco para evitar acessos não autorizados de terceiros.
D) ocultar a identidade do remetente de uma mensagem de e-mail na internet.
E) gerar um par de chaves públicas e privadas para uso na certificação digital.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Explicação:
Funções hash (como SHA-256) geram um valor de tamanho fixo a partir de dados de tamanho arbitrário. Uma pequena mudança nos dados originais muda completamente o hash resultante.
- **A) Incorreta.** O Hash não provê confidencialidade, pois não serve para cifrar os dados (ocultar a mensagem original). Quem garante a confidencialidade é a criptografia (simétrica ou assimétrica).
- **B) Correta.** Ao comparar o hash do arquivo antes e depois do envio, é possível afirmar com precisão que a integridade foi mantida (não houve alteração acidental ou intencional).
- **C) Incorreta.** Hashes são funções criptográficas de via única (irreversíveis). Não é possível obter o dado original a partir do hash.
- **D) Incorreta.** Funções de hash não têm o propósito de tornar o tráfego anônimo ou ocultar identidades; este é o papel de redes como Tor ou VPNs.
- **E) Incorreta.** A geração de pares de chaves assimétricas utiliza algoritmos matemáticos baseados em fatoração de números primos (como RSA) ou curvas elípticas, e não funções de hash.
</details>

---

### Questão 4 (FCC - 2015 - TRE PB - Analista de TI)
Em uma Infraestrutura de Chaves Públicas (ICP), como a ICP-Brasil, a entidade primariamente responsável por emitir, expedir, distribuir, renovar e revogar os certificados digitais é denominada:
A) Autoridade de Registro (AR).
B) Comitê Gestor da ICP-Brasil.
C) Autoridade Certificadora (AC).
D) Autoridade Carimbadora de Tempo (ACT).
E) Entidade Emissora de Raiz (EER).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Explicação:
O ecossistema da ICP-Brasil é dividido em várias entidades com papéis distintos.
- **A) Incorreta.** A AR (Autoridade de Registro) é a interface com o usuário; ela recebe as solicitações, identifica o titular e encaminha o pedido para a AC. Ela não emite os certificados.
- **B) Incorreta.** O Comitê Gestor é a autoridade máxima de formulação de políticas da ICP-Brasil. Não executa atividades operacionais como emissão de certificados.
- **C) Correta.** A AC (Autoridade Certificadora) é a entidade responsável pelo ciclo de vida completo dos certificados digitais: emissão, renovação e revogação.
- **D) Incorreta.** A ACT tem a função de fornecer carimbos de tempo, que atestam a data e a hora exatas em que um documento foi assinado.
- **E) Incorreta.** A terminologia "Entidade Emissora de Raiz" não é o padrão. Na ICP-Brasil há a "AC Raiz" (ITI), mas o conceito que rege a emissão para usuários é simplesmente Autoridade Certificadora (AC).
</details>

---

### Questão 5 (FCC - 2014 - TRF 3 - Analista de TI)
Ao desenvolver uma solução de segurança para um tribunal, um analista de TI precisou escolher algoritmos de criptografia para diferentes propósitos. São exemplos válidos, respectivamente, de algoritmo de criptografia simétrica e de algoritmo de criptografia assimétrica:
A) DES e AES.
B) RSA e MD5.
C) AES e RSA.
D) SHA-1 e DES.
E) RSA e ECC.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Explicação:
Questão clássica sobre classificação de algoritmos de segurança.
- **A) Incorreta.** DES e AES são ambos algoritmos de criptografia simétrica (chave única para cifrar e decifrar).
- **B) Incorreta.** RSA é um algoritmo assimétrico, e MD5 é um algoritmo de Hash (resumo criptográfico), não sendo usado para cifrar/decifrar.
- **C) Correta.** AES (Advanced Encryption Standard) é o padrão atual de criptografia simétrica. O RSA (Rivest-Shamir-Adleman) é o mais famoso algoritmo de criptografia assimétrica.
- **D) Incorreta.** SHA-1 é função de Hash e DES é simétrico. A ordem e os tipos estão incorretos para o que foi pedido.
- **E) Incorreta.** Tanto o RSA quanto o ECC (Elliptic Curve Cryptography) são algoritmos de criptografia assimétrica.
</details>

---

## 📝 TEMA 2: Programação (C, PHP, C#) e SOLID/GRASP

### Questão 6 (FCC - 2017 - TRT 24 - Analista de TI)
Na linguagem C#, a programação orientada a objetos permite a reescrita de métodos em classes derivadas. Para que um método em uma classe base possa ser sobrescrito em uma classe derivada, indicando que possui implementação, ele deve ser declarado utilizando a palavra-chave:
A) abstract.
B) virtual.
C) override.
D) sealed.
E) new.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Explicação:
Em C#, métodos não são "sobrescrevíveis" por padrão. O desenvolvedor deve permitir isso explicitamente.
- **A) Incorreta.** Um método `abstract` força a sobrescrita, mas **não possui** implementação na classe base, servindo apenas como um contrato.
- **B) Correta.** A palavra-chave `virtual` permite que um método (que contém uma implementação na classe base) seja sobrescrito em uma classe derivada (usando `override`).
- **C) Incorreta.** A palavra-chave `override` é usada na classe derivada para sobrescrever o método da classe base, e não na declaração original.
- **D) Incorreta.** O modificador `sealed` impede a herança ou a sobrescrita, funcionando exatamente ao contrário do que pede o enunciado.
- **E) Incorreta.** A palavra-chave `new` é utilizada para ocultar (hiding) um membro da classe base, e não para sobrescrevê-lo polimorficamente.
</details>

---

### Questão 7 (FCC - 2015 - TRT 3 - Analista de TI)
Em desenvolvimento de sistemas web utilizando a linguagem PHP, o tráfego de dados entre o cliente e o servidor frequentemente ocorre via requisições HTTP. Para acessar os dados enviados por meio de um formulário que utiliza o método POST, utiliza-se nativamente a variável superglobal:
A) $_GET.
B) $_SESSION.
C) $_COOKIE.
D) $_POST.
E) $_FILES.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

Explicação:
Variáveis superglobais em PHP estão disponíveis em qualquer escopo do script.
- **A) Incorreta.** A variável `$_GET` é utilizada para capturar dados enviados pela URL (via query string) ou formulários com método GET.
- **B) Incorreta.** A `$_SESSION` armazena variáveis de sessão do lado do servidor, que persistem entre requisições.
- **C) Incorreta.** A variável `$_COOKIE` é utilizada para acessar os valores de cookies enviados pelo navegador do cliente.
- **D) Correta.** A variável superglobal `$_POST` é um array associativo contendo os dados passados para o script via requisição HTTP POST.
- **E) Incorreta.** A superglobal `$_FILES` captura especificamente as informações de arquivos que foram submetidos para upload no servidor, e não os campos de texto/dados gerais do POST.
</details>

---

### Questão 8 (FCC - 2018 - TRT 15 - Analista de TI)
O Princípio do Aberto/Fechado (Open/Closed Principle - OCP), que representa a letra 'O' no acrônimo SOLID, estabelece uma regra fundamental para o bom design de software orientado a objetos. Segundo esse princípio, as entidades de software devem ser:
A) abertas para modificação, mas fechadas para extensão.
B) abertas para extensão, mas fechadas para modificação.
C) abertas para testes unitários, mas fechadas para implementações de interface.
D) fechadas para acoplamento, mas abertas para coesão.
E) fechadas para reutilização externa, mas abertas para composição interna.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Explicação:
O Princípio do Aberto/Fechado (OCP), idealizado por Bertrand Meyer, é o cerne da flexibilidade e da manutenibilidade em OO.
- **A) Incorreta.** Esta alternativa inverte o princípio. Se o código for aberto para modificação, aumenta-se o risco de quebrar regras de negócios existentes.
- **B) Correta.** A entidade deve estar aberta para **extensão** (podemos adicionar novos comportamentos e funcionalidades) e fechada para **modificação** (o código-fonte original não deve ser alterado para suportar o novo comportamento, evitando bugs em funcionalidades antigas). O uso de herança e polimorfismo são técnicas comuns para atingir esse objetivo.
- **C) Incorreta.** O OCP não trata diretamente de testes unitários ou exclusão de interfaces (na verdade, interfaces ajudam no OCP).
- **D) Incorreta.** Mistura conceitos de design (coesão e acoplamento) que, embora corretos como boas práticas independentes, não definem o Princípio do Aberto/Fechado.
- **E) Incorreta.** O OCP não é definido em torno das restrições de reutilização externa e composição interna.
</details>

---

### Questão 9 (FCC - 2016 - TRF 3 - Analista de TI)
Dentre os padrões de atribuição de responsabilidade GRASP (General Responsibility Assignment Software Patterns), um deles foca especificamente em determinar qual classe deve ser a responsável por instanciar uma nova classe, buscando manter o baixo acoplamento e promovendo a reutilização. Trata-se do padrão:
A) Expert (Especialista na Informação).
B) Creator (Criador).
C) Controller (Controlador).
D) Pure Fabrication (Invenção Pura).
E) Indirection (Indireção).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Explicação:
Os padrões GRASP guiam a atribuição de responsabilidades a classes em um modelo OO.
- **A) Incorreta.** O *Expert* (Information Expert) dita que a responsabilidade deve ser atribuída à classe que possui a informação necessária para cumpri-la.
- **B) Correta.** O padrão *Creator* estabelece as regras para definir quem deve criar a instância de uma classe (ex: B cria A se B contém A, B registra A, B usa A de perto ou B tem os dados para inicializar A).
- **C) Incorreta.** O *Controller* atua como o primeiro objeto além da camada de interface de usuário que recebe e coordena uma operação do sistema.
- **D) Incorreta.** *Pure Fabrication* é uma classe fictícia (não representa o domínio real) criada artificialmente para obter baixo acoplamento e alta coesão, quando o padrão *Expert* viola esses ideais.
- **E) Incorreta.** *Indirection* atribui a responsabilidade de comunicação entre componentes a um objeto intermediário para que eles não sejam acoplados diretamente.
</details>

---

### Questão 10 (FCC - 2013 - TRT 1 - Analista de TI)
Na linguagem de programação C, o uso de ponteiros é uma característica poderosa que permite a manipulação direta da memória. O operador unário utilizado antes do nome de uma variável para obter o seu respectivo endereço de memória é o:
A) * (asterisco).
B) & (e comercial).
C) % (sinal de porcentagem).
D) -> (seta).
E) # (cerquilha).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Explicação:
A linguagem C diferencia explicitamente os operadores de manipulação de memória e de indireção.
- **A) Incorreta.** O operador `*` (asterisco) atua como um desreferenciador (indireção). Ele acessa o valor armazenado no endereço para o qual o ponteiro aponta, ou é usado na declaração do tipo do ponteiro.
- **B) Correta.** O operador `&` (e comercial), quando usado de forma unária antes de uma variável (`&var`), retorna o endereço físico de memória onde aquela variável está alocada.
- **C) Incorreta.** O operador `%` é o operador aritmético de módulo (resto da divisão inteira).
- **D) Incorreta.** O operador `->` é utilizado para acessar membros (atributos ou funções) de uma estrutura (struct) a partir de um ponteiro que aponta para ela.
- **E) Incorreta.** O caractere `#` é usado em C para introduzir diretivas de pré-processador, como `#include` e `#define`.
</details>

---

## 📝 TEMA 3: Língua Portuguesa (Vozes do Verbo e Flexão)

### Questão 11 (FCC - 2018 - TRT 2 - Analista Judiciário)
Transpondo-se para a voz passiva a frase "A constante inovação da tecnologia tem alterado profundamente as relações sociais", a forma verbal resultante que completa a conversão corretamente será:
A) têm sido alteradas.
B) tem sido alteradas.
C) têm alterado.
D) foram alteradas.
E) estão sendo alteradas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

Explicação:
A transposição de voz ativa para voz passiva exige manutenção do tempo verbal e adequação da concordância com o novo sujeito paciente.
- **A) Correta.** A frase na voz passiva analítica fica: "As relações sociais **têm sido alteradas** profundamente pela constante inovação da tecnologia". O tempo (pretérito perfeito composto do indicativo "tem alterado") foi mantido por meio da locução "têm sido alteradas". A mudança do verbo auxiliar "tem" para "têm" (com acento) ocorre para concordar no plural com o novo sujeito paciente ("As relações sociais").
- **B) Incorreta.** "Tem" (sem acento circunflexo) está no singular e não concorda com o sujeito plural "as relações sociais".
- **C) Incorreta.** "Têm alterado" mantém o verbo na voz ativa.
- **D) Incorreta.** Modifica o tempo verbal. "Foram alteradas" está no pretérito perfeito simples, ao passo que a frase original utiliza o pretérito perfeito composto ("tem alterado").
- **E) Incorreta.** Modifica o tempo verbal e o aspecto ("estão sendo alteradas" corresponde ao presente contínuo/gerúndio: "está alterando").
</details>

---

### Questão 12 (FCC - 2019 - TRF 4 - Analista Judiciário)
Transpondo para a voz passiva a oração "Os cientistas desenvolverão novas vacinas para a população", a forma verbal resultante será:
A) foram desenvolvidas.
B) serão desenvolvidas.
C) seriam desenvolvidas.
D) são desenvolvidas.
E) vêm sendo desenvolvidas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Explicação:
Na mudança de voz, o tempo e o modo do verbo principal na voz ativa determinam o tempo e o modo do verbo auxiliar "ser" na voz passiva.
- **A) Incorreta.** "Foram" está no pretérito perfeito. A frase original usa o verbo "desenvolverão", que está no futuro do presente.
- **B) Correta.** A oração transformada torna-se "Novas vacinas **serão desenvolvidas** pelos cientistas...". O auxiliar "serão" acompanha o tempo do verbo principal (futuro do presente) e concorda em número/gênero com o sujeito paciente plural ("novas vacinas"), somado ao particípio "desenvolvidas".
- **C) Incorreta.** "Seriam" está no futuro do pretérito, o que configuraria alteração de tempo verbal.
- **D) Incorreta.** "São desenvolvidas" está no presente do indicativo.
- **E) Incorreta.** Introduz aspecto durativo (gerúndio) que não existe na frase original (ativa não era "vêm desenvolvendo").
</details>

---

### Questão 13 (FCC - 2016 - TRT 20 - Analista Judiciário)
Considere a frase: "Se ele ver o processo a tempo, poderá suspender a execução." Para que a flexão verbal esteja de acordo com a norma-padrão da Língua Portuguesa, a palavra sublinhada ("ver") deve ser substituída por:
A) vir.
B) ver.
C) visse.
D) virem.
E) vier.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

Explicação:
A estrutura da frase impõe uma condição futura ("Se..."), o que exige o uso do tempo Futuro do Subjuntivo do verbo "ver".
- **A) Correta.** O futuro do subjuntivo do verbo "ver" conjuga-se assim: quando eu *vir*, quando tu *vires*, quando ele **vir**. Portanto, a forma correta é "Se ele **vir**".
- **B) Incorreta.** "Ver" é a forma do verbo no infinitivo. Trata-se de um erro coloquial gravíssimo e comum confundir o infinitivo com o futuro do subjuntivo deste verbo.
- **C) Incorreta.** "Visse" é o pretérito imperfeito do subjuntivo ("Se ele visse, poderia suspender..."). O uso de "visse" quebraria a correlação verbal com o "poderá" (futuro do indicativo).
- **D) Incorreta.** "Virem" é a flexão para a terceira pessoa do plural ("se eles virem"), mas o pronome exigido pelo enunciado é singular ("ele").
- **E) Incorreta.** "Vier" é a flexão do futuro do subjuntivo do verbo "vir" (de locomoção, chegar), e não do verbo "ver" (de enxergar).
</details>

---

### Questão 14 (FCC - 2017 - TRT 24 - Técnico Judiciário)
A frase "A comissão analisou rigorosamente todos os contratos" admitirá, na transposição para a voz passiva, a seguinte forma verbal:
A) são analisados.
B) foram analisados.
C) foi analisado.
D) tinham analisado.
E) haviam sido analisados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Explicação:
Regra básica de vozes verbais: o objeto direto da voz ativa ("todos os contratos") vira sujeito da voz passiva, e o verbo assume forma locutória baseada no particípio.
- **A) Incorreta.** "São analisados" está no presente do indicativo, não correspondendo ao verbo original "analisou" (pretérito perfeito).
- **B) Correta.** A frase transposta fica: "Todos os contratos **foram analisados** rigorosamente pela comissão". O auxiliar "foram" absorve o tempo verbal "pretérito perfeito" da ativa e flexiona-se no plural para concordar com o sujeito paciente "Todos os contratos". O particípio fecha a locução ("analisados").
- **C) Incorreta.** "Foi analisado" manteria o verbo no singular, desrespeitando a concordância obrigatória com o sujeito paciente plural "Todos os contratos".
- **D) Incorreta.** "Tinham analisado" é um tempo composto da voz ativa (pretérito mais-que-perfeito), não formando voz passiva.
- **E) Incorreta.** Modifica o tempo original para o pretérito mais-que-perfeito na voz passiva. O verbo não sofreu alteração na frase original para justificar o deslocamento temporal.
</details>

---

### Questão 15 (FCC - 2015 - TRT 3 - Técnico Judiciário)
Assinale a alternativa que apresenta a correta flexão do verbo "manter" no pretérito perfeito do indicativo, na 3ª pessoa do plural, preenchendo adequadamente a lacuna na frase: "Os auditores _________ o parecer inicial inalterado."
A) manteram
B) manterão
C) manteriam
D) mantiveram
E) mantião

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

Explicação:
Os verbos derivados do verbo "ter" (como manter, obter, conter, reter) seguem o paradigma de conjugação do verbo primitivo.
- **A) Incorreta.** A forma "manteram" não existe na gramática normativa. É um desvio comum no português falado, conjugando o verbo como se fosse regular (como cantar -> cantaram).
- **B) Incorreta.** "Manterão" é o verbo flexionado no futuro do presente do indicativo, indicando uma ação que ainda vai ocorrer, e não um pretérito (passado).
- **C) Incorreta.** "Manteriam" está no futuro do pretérito do indicativo, expressando uma condição não realizada, fugindo do tempo verbal solicitado.
- **D) Correta.** O pretérito perfeito do verbo "ter" na 3ª pessoa do plural é "tiveram". Pela regra da derivação, adiciona-se o prefixo: man + tiveram = **mantiveram**.
- **E) Incorreta.** Além de não pertencer ao tempo solicitado, a escrita grafia "mantião" está incorreta. Se fosse o pretérito imperfeito, a grafia correta seria "mantinham".
</details>

---
