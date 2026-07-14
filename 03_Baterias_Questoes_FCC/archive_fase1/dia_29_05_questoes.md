# Bateria de Questões FCC — Sexta-feira 29/05

## 📝 TEMA 1: Segurança da Informação (Criptografia/Certificação)

### Questão 1 (FCC - 2018 - TRT 15 - Analista Judiciário - Tecnologia da Informação)
A assinatura digital é um mecanismo fundamental na segurança da informação, pois garante, simultaneamente, autenticidade, integridade e não repúdio a documentos eletrônicos. Do ponto de vista técnico, a geração de uma assinatura digital sobre um documento ocorre:
A) Cifrando o documento completo com a chave pública do destinatário.
B) Cifrando o resumo criptográfico (hash) do documento com a chave privada do remetente.
C) Cifrando o resumo criptográfico (hash) do documento com a chave pública do remetente.
D) Cifrando o documento completo com a chave privada do destinatário.
E) Cifrando o documento e o seu hash com uma chave simétrica temporária compartilhada entre os envolvidos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Para criar uma assinatura digital, o emissor passa o documento por uma função de espalhamento (hash), gerando um resumo de tamanho fixo. Em seguida, esse hash é criptografado com a sua própria **chave privada** (do remetente). 

- **A está incorreta:** Cifrar com a chave pública do destinatário provê confidencialidade (apenas ele poderá ler), não assinatura digital (autenticidade). Além disso, não se cifra o documento completo para assinar, e sim o hash (por eficiência).
- **B está correta:** É exatamente este o processo. Cifrar o hash com a chave privada garante quem foi o emissor, pois só ele a possui (autenticidade/não repúdio).
- **C está incorreta:** Cifrar algo com a chave pública não faz sentido para autenticação, pois qualquer pessoa tem acesso à chave pública e poderia forjar o documento.
- **D está incorreta:** Ninguém tem acesso à chave privada do destinatário, exceto o próprio destinatário. O remetente jamais poderia usá-la.
- **E está incorreta:** A assinatura digital provém da criptografia assimétrica. A chave simétrica provê apenas confidencialidade entre duas partes que a conhecem, não garantindo o não repúdio (já que ambas as partes possuem a mesma chave e poderiam gerar a mensagem).
</details>

---

### Questão 2 (FCC - 2016 - TRT 20 - Técnico Judiciário - Tecnologia da Informação)
Um certificado digital do tipo X.509 é um documento eletrônico emitido por uma entidade confiável. Sua finalidade central é atrelar de forma segura uma identidade a uma chave pública. A garantia de que os dados do certificado são válidos e de que aquela chave pública pertence àquela identidade é atestada matematicamente pela presença de:
A) Uma assinatura feita com a chave privada do titular do certificado, validada pela Autoridade de Registro.
B) Uma assinatura feita com a chave pública do titular, referendada pela Autoridade Certificadora.
C) Uma assinatura feita com a chave privada da Autoridade Certificadora emissora.
D) Um registro cifrado com a chave simétrica de sessão compartilhada entre o servidor e o cliente.
E) Uma assinatura digital feita com a chave pública da Autoridade Certificadora Raiz da infraestrutura.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Um certificado digital é essencialmente a chave pública de um usuário assinada pela Autoridade Certificadora (AC) que o emitiu. 

- **A está incorreta:** O certificado não é assinado com a chave privada do titular. Quem atesta a veracidade é a entidade certificadora, não o próprio indivíduo (isso seria auto-assinado e não confiável no contexto de uma ICP).
- **B está incorreta:** Assinaturas digitais são feitas usando chaves privadas, nunca chaves públicas.
- **C está correta:** A AC pega as informações do usuário (nome, validade) + a chave pública desse usuário, gera um hash e cifra esse hash com a SUA chave privada (da AC). O navegador do usuário usa a chave pública da AC para validar o certificado.
- **D está incorreta:** Chaves de sessão simétricas são para tráfego seguro de rede (ex: TLS), não para a estrutura de um certificado digital.
- **E está incorreta:** A assinatura é feita com a chave PRIVADA da AC emissora (seja ela intermediária ou raiz). Não se usa chave pública para gerar assinaturas, apenas para verificá-las.
</details>

---

### Questão 3 (FCC - 2018 - TRT 2 - Analista Judiciário - Tecnologia da Informação)
No âmbito da Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil), diferentes entidades desempenham papéis específicos. A Autoridade de Registro (AR) é a entidade operacional responsável por:
A) Emitir, expedir, distribuir e revogar os certificados digitais dos usuários finais.
B) Assinar o certificado digital da Autoridade Certificadora Raiz.
C) Armazenar as chaves privadas dos usuários de forma centralizada para viabilizar a recuperação em caso de perda.
D) Receber, validar, identificar presencialmente ou remotamente os solicitantes, e encaminhar as solicitações de emissão e revogação de certificados.
E) Determinar as Políticas de Certificado (PC) e as Declarações de Práticas de Certificação (DPC) de todas as ACs brasileiras.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A ICP-Brasil é rigorosa na separação de papéis. A AR (Autoridade de Registro) lida com o público, enquanto a AC (Autoridade Certificadora) cuida da criptografia pesada (emissão de fato).

- **A está incorreta:** Quem emite, expede e revoga é a Autoridade Certificadora (AC). A AR apenas *solicita* isso à AC após validar o usuário.
- **B está incorreta:** O certificado da AC Raiz (ITI) é auto-assinado. A AR não tem nenhuma relação com a assinatura da raiz.
- **C está incorreta:** Na ICP-Brasil, a chave privada do usuário é de controle exclusivo dele (gerada no próprio token, smartcard ou computador). Ela não fica armazenada centralmente pela AR.
- **D está correta:** A AR é a interface (o "balcão"). Ela identifica o usuário, confere documentos, realiza a biometria e manda a solicitação aprovada para a AC emitir o certificado.
- **E está incorreta:** Quem normatiza e aprova as políticas é o Comitê Gestor da ICP-Brasil (CG ICP-Brasil) e as próprias ACs redigem suas DPCs aprovadas pela AC Raiz.
</details>

---

### Questão 4 (FCC - 2017 - TRE PR - Analista Judiciário - Apoio Especializado - Análise de Sistemas)
Os algoritmos de criptografia são classicamente divididos em duas grandes famílias: simétricos e assimétricos. Sobre essas categorias e seus respectivos algoritmos, é correto afirmar:
A) O algoritmo AES é do tipo assimétrico, destacando-se pela velocidade em processos de autenticação.
B) Na criptografia assimétrica, utiliza-se um par de chaves complementares: o que uma cifra, apenas a outra pode decifrar.
C) RSA, DES e ECC são todos exemplos clássicos e vigentes de algoritmos simétricos robustos.
D) A criptografia simétrica sofre com gargalos de desempenho computacional, sendo muito mais lenta que a assimétrica.
E) Algoritmos simétricos resolvem de forma nativa e isolada o problema da distribuição segura de chaves pela internet.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A criptografia assimétrica trabalha com o conceito de par de chaves (Pública e Privada) matematicamente vinculadas.

- **A está incorreta:** O AES (Advanced Encryption Standard) é o padrão ouro moderno para criptografia *simétrica* (chave única), não assimétrica.
- **B está correta:** Esta é a definição fundamental da criptografia assimétrica. Se eu cifro com a Pública, decifro com a Privada (Confidencialidade). Se eu cifro (um hash) com a Privada, decifro com a Pública (Assinatura digital).
- **C está incorreta:** RSA e ECC (Curvas Elípticas) são assimétricos. DES é simétrico (e obsoleto por questões de segurança de tamanho de chave).
- **D está incorreta:** É o exato oposto. A criptografia simétrica (operações de matrizes, XORs lógicos) é milhares de vezes mais rápida que a assimétrica (fatoração de primos imensos, logaritmos discretos).
- **E está incorreta:** O grande problema da criptografia simétrica é justamente o problema da distribuição de chaves (como mandar a chave simétrica secreta para a outra ponta de forma segura em um meio inseguro?). A assimétrica resolve isso.
</details>

---

### Questão 5 (FCC - 2014 - TRT 16 - Analista Judiciário - Tecnologia da Informação)
Para garantir exclusivamente a **confidencialidade** no envio de um e-mail com dados sigilosos, e sabendo que remetente (Alice) e destinatário (Bob) dispõem de pares de chaves assimétricas, o processo de cifragem desse e-mail por Alice deve utilizar:
A) A chave privada de Alice.
B) A chave pública de Alice.
C) A chave privada de Bob.
D) A chave pública de Bob.
E) Uma função de espalhamento (hash) sem o uso de chaves.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão cobra a aplicação prática da propriedade de **confidencialidade** na criptografia de chave pública.

- **A está incorreta:** Se Alice usar sua própria chave privada, qualquer pessoa no mundo, usando a chave pública de Alice (que é acessível a todos), poderia abrir e ler a mensagem. Isso não garante confidencialidade.
- **B está incorreta:** A chave pública de Alice não serve para que Bob consiga abrir a mensagem (ele precisaria da privada de Alice, o que seria uma falha fatal de segurança se a possuísse).
- **C está incorreta:** A chave privada de Bob está sob posse apenas de Bob, é impossível Alice tê-la para cifrar a mensagem. 
- **D está correta:** Para que APENAS Bob leia a mensagem, Alice deve empacotar a mensagem em um cofre cuja fechadura só a chave particular (privada) de Bob abre. Para isso, ela cifra a mensagem usando a **chave pública de Bob**.
- **E está incorreta:** Hash provê apenas verificação de integridade, não garante confidencialidade, além de ser um processo irreversível (Bob não conseguiria recuperar a mensagem original).
</details>

---

### Questão 6 (FCC - 2013 - TRT 1 - Analista Judiciário - Tecnologia da Informação)
No padrão brasileiro da ICP-Brasil, há distinção normativa entre os tipos de certificados. Em particular, a diferença técnica principal entre certificados do tipo A1 e do tipo A3 reside no fato de que:
A) O certificado A1 é gerado exclusivamente em hardware (token ou smartcard) e possui validade máxima de um ano.
B) O certificado A3 é gerado e armazenado em meio físico criptográfico dedicado (token, smartcard ou HSM) e sua chave privada não pode ser exportada ou extraída.
C) O certificado A3 é emitido unicamente para Pessoas Jurídicas (e-CNPJ), enquanto o A1 destina-se a Pessoas Físicas (e-CPF).
D) O certificado A1 exige renovação presencial a cada 3 anos, enquanto o A3 é vitalício se não for revogado.
E) O certificado A3 baseia-se em criptografia simétrica com validade de 5 anos, e o A1 em criptografia assimétrica de 1 ano.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Os certificados "A" significam Assinatura (existem também S para Sigilo e T para Carimbo do Tempo). O número indica o nível de segurança e tipo de mídia.

- **A está incorreta:** O A1 é gerado em software (no computador do próprio usuário) e armazenado no disco rígido/navegador como um arquivo (pode ter extensão .pfx ou .p12). Tem validade de 1 ano.
- **B está correta:** Os certificados do tipo A3 oferecem maior segurança porque a geração das chaves ocorre dentro de um chip criptográfico (smartcard ou token USB). A chave privada do A3 é "in-exportável"; ela nunca sai do dispositivo, os cálculos criptográficos ocorrem dentro do próprio token. Tem validade máxima usual de 3 anos.
- **C está incorreta:** Ambos (A1 e A3) estão disponíveis tanto para Pessoa Física (e-CPF) quanto para Pessoa Jurídica (e-CNPJ).
- **D está incorreta:** A1 tem validade de 1 ano. Nenhum deles é vitalício.
- **E está incorreta:** Todos os certificados digitais da ICP-Brasil usam criptografia assimétrica de chave pública (Padrão X.509).
</details>

---

### Questão 7 (FCC - 2015 - TRE PB - Analista Judiciário - Análise de Sistemas)
As funções de resumo criptográfico (hash functions) são essenciais em diversos protocolos de segurança. Para que uma função hash seja considerada criptograficamente segura na atualidade, ela deve possuir diversas propriedades. Dentre elas, a característica que afirma ser computacionalmente inviável encontrar duas mensagens distintas $M_1$ e $M_2$ tais que $Hash(M_1) = Hash(M_2)$ recebe o nome de:
A) Irreversibilidade (One-way).
B) Efeito Avalanche.
C) Resistência fraca à colisão (Second pre-image resistance).
D) Resistência forte à colisão (Collision resistance).
E) Assimetria linear determinística.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão trata das propriedades formais de uma função hash.

- **A está incorreta:** Irreversibilidade significa que, dado um hash H, é inviável achar a mensagem original M. Não trata de mensagens diferentes com o mesmo hash.
- **B está incorreta:** Efeito avalanche significa que a alteração de 1 bit na entrada M altera drasticamente (cerca de 50% dos bits) o hash de saída.
- **C está incorreta:** Resistência *fraca* (segunda pré-imagem) significa que, dada uma mensagem **específica** $M_1$, é inviável encontrar uma $M_2$ diferente que gere o mesmo hash. 
- **D está correta:** A resistência *forte* a colisão significa que é inviável encontrar **quaisquer duas** mensagens aleatórias $M_1$ e $M_2$ que, ao passarem pelo algoritmo, resultem no mesmo hash. É a garantia de que colisões (mesma saída para entradas diferentes) não podem ser geradas propositalmente.
- **E está incorreta:** Termo inventado sem aderência técnica com os requisitos de funções hash.
</details>

---

### Questão 8 (FCC - 2022 - TRT 22 - Analista Judiciário - Tecnologia da Informação)
No tocante ao uso de algoritmos de criptografia simétrica modernos, o AES (Advanced Encryption Standard) desponta como o padrão mais adotado globalmente. Uma característica técnica que define corretamente a arquitetura do AES é:
A) Operar utilizando uma arquitetura de cifras de fluxo (stream cipher), criptografando os dados bit a bit em tempo real.
B) Possuir tamanhos de bloco flexíveis de 64, 128 e 256 bits, acoplados unicamente a chaves de 128 bits.
C) Operar sobre blocos de dados de 128 bits e suportar tamanhos de chave de 128, 192 ou 256 bits.
D) Basear sua segurança matemática na dificuldade de resolver o problema do logaritmo discreto sobre curvas elípticas.
E) Substituir a estrutura tradicional de rede de permutação por redes de substituição do tipo Feistel em 64 rodadas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

O AES foi o vencedor do concurso do NIST para substituir o antigo DES.

- **A está incorreta:** O AES é uma cifra de bloco (block cipher), e não de fluxo (stream cipher como o RC4). Ele processa blocos inteiros de dados de uma vez.
- **B está incorreta:** O AES possui um tamanho fixo de bloco de **128 bits**, independentemente do tamanho da chave. (No original Rijndael, o bloco variava, mas na padronização AES travou-se o bloco em 128 bits).
- **C está correta:** O AES processa blocos de entrada de 128 bits. A complexidade de segurança é definida pela chave, que pode ser de 128, 192 ou 256 bits (o que altera o número de rodadas internas de substituição e permutação: 10, 12 ou 14 rodadas, respectivamente).
- **D está incorreta:** Essa é a base matemática da criptografia ECC (Curvas Elípticas), que é assimétrica. O AES usa substituição e permutação (Rijndael).
- **E está incorreta:** O DES usava estrutura de rede de Feistel. O AES abandonou o modelo Feistel e usa uma Rede de Substituição-Permutação (SPN).
</details>

---

### Questão 9 (FCC - 2017 - TRT 11 - Analista Judiciário - Tecnologia da Informação)
Em um sistema de folha de pagamento do tribunal, um analista precisa garantir o atributo da irretratabilidade de uma aprovação sistêmica executada por um gestor. Na segurança da informação, a irretratabilidade (ou não repúdio) implica que:
A) A comunicação entre o computador do gestor e o servidor nunca caia durante a transação, assegurando alta disponibilidade.
B) Uma vez gerada a assinatura, o arquivo do pagamento ficará travado em modo leitura não sendo permitida nenhuma manipulação (integridade de hardware).
C) O sistema utilize criptografia puramente simétrica com chaves rodadas mensalmente pelas regras de negócio.
D) O gestor, posteriormente à aprovação, não possa negar legitimamente que ele foi o autor ou remetente daquela transação.
E) Uma terceira parte certificadora mantenha uma cópia em texto claro da mensagem caso ocorra disputa judicial, caracterizando sigilo recuperável.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A irretratabilidade/não repúdio é um dos cinco pilares fundamentais da segurança da informação (CIA-NA: Confidencialidade, Integridade, Disponibilidade, Não repúdio, Autenticidade).

- **A está incorreta:** Garantir que a conexão não caia remete à Disponibilidade (Availability).
- **B está incorreta:** Arquivo travado trata de controles de acesso no nível do SO ou aplicação, não define não repúdio.
- **C está incorreta:** Criptografia simétrica *sozinha* é insuficiente para garantir não repúdio, pois duas partes têm a mesma chave, logo qualquer uma poderia forjar a mensagem e botar a culpa na outra.
- **D está correta:** A essência do não repúdio é impedir que o emissor legue autoria falsa de uma ação ou mensagem. Como a assinatura é feita com a chave privada (exclusiva dele), fica impossível para ele argumentar perante terceiros (como um juiz) que "não fui eu que enviei".
- **E está incorreta:** A Autoridade Certificadora nunca deve armazenar as mensagens em texto claro enviadas entre partes (isso violaria a confidencialidade e a privacidade); a AC atesta apenas o vínculo da identidade com a chave pública.
</details>

---

### Questão 10 (FCC - 2019 - TRF 3 - Técnico Judiciário - Informática)
Considere os seguintes métodos e algoritmos voltados à criptografia e proteção de dados:
I. AES
II. RSA
III. SHA-256
IV. Curvas Elípticas (ECC)

Assinale a alternativa que classifica, correta e respectivamente, a categoria desses algoritmos na segurança da informação:
A) Simétrico, Assimétrico, Função de Hash e Assimétrico.
B) Assimétrico, Simétrico, Assimétrico e Função de Hash.
C) Simétrico, Assimétrico, Função de Hash e Simétrico.
D) Função de Hash, Assimétrico, Simétrico e Assimétrico.
E) Simétrico, Simétrico, Assimétrico e Função de Hash.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

Vamos classificar cada um individualmente baseados no mercado e na doutrina.

- **I. AES (Advanced Encryption Standard):** É o padrão atual para cifra *simétrica* de blocos. Substituiu o antigo DES/3DES. Usa uma chave única compartilhada.
- **II. RSA (Rivest-Shamir-Adleman):** É o algoritmo de criptografia *assimétrica* (chave pública e privada) mais estudado e utilizado no mundo. Baseia-se na fatoração de grandes números primos.
- **III. SHA-256 (Secure Hash Algorithm de 256 bits):** É uma *função de hash* criptográfico, unidirecional, que emite um resumo de 256 bits, utilizado na assinatura digital.
- **IV. ECC (Elliptic Curve Cryptography):** É um poderoso algoritmo de criptografia *assimétrica* que garante o mesmo nível de segurança do RSA, mas exigindo chaves muito menores (ótimo para dispositivos móveis).

Portanto, a única sequência correta (Simétrico, Assimétrico, Hash, Assimétrico) está na alternativa **A**. As demais (B, C, D e E) misturam essas classificações ou invertem simétrico com assimétrico no AES/RSA.
</details>

---

### Questão 11 (FCC - 2021 - DPE RR - Analista de Sistemas)
A relação entre tamanho de chave e segurança provida varia conforme o tipo de algoritmo criptográfico empregado. Ao comparar algoritmos modernos, para obter-se um nível de segurança equivalente (resistência teórica similar contra força bruta e evolução computacional), constata-se que:
A) As chaves usadas no AES devem ser sensivelmente maiores que as usadas no RSA.
B) O algoritmo RSA e o de Curvas Elípticas (ECC) exigem chaves exatamente do mesmo tamanho.
C) O algoritmo RSA necessita de chaves consideravelmente maiores do que algoritmos simétricos, como o AES, para oferecer segurança equivalente.
D) Algoritmos de hash, como o MD5, exigem chaves assimétricas de pelo menos 1024 bits para funcionarem sem colisões.
E) A segurança do algoritmo independe do tamanho da chave, baseando-se unicamente no sigilo matemático de seu código-fonte.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

O tamanho das chaves é pautado pela matemática por trás do algoritmo. Algoritmos simétricos resistem bem a ataques, exigindo que a quebra ocorra por busca exaustiva (força bruta). Algoritmos assimétricos lidam com matemática dedutível (fatores de primos, etc.), onde supercomputadores usam algoritmos de peneira (ex: GNFS) atalhando a quebra.

- **A está incorreta:** A relação é inversa. O AES é muito seguro com chaves curtas (ex: 256 bits).
- **B está incorreta:** A grande vantagem mercadológica do ECC (Curvas Elípticas) é prover o mesmo nível de segurança do RSA, mas usando chaves muito *menores* (ex: uma chave ECC de 256 bits equivale em segurança a um RSA de 3072 bits).
- **C está correta:** Para obter uma segurança considerada adequada hoje (aproximadamente 128 bits de "segurança bruta"), o AES precisa de uma chave de 128 bits, enquanto o RSA requer uma chave de pelo menos 2048 ou 3072 bits. 
- **D está incorreta:** Funções de Hash tradicionais não usam chaves de encriptação (são "keyless"). Além disso, o MD5 possui colisões provadas e está obsoleto.
- **E está incorreta:** Isso fere a máxima de Kerckhoffs. Um algoritmo criptográfico seguro deve ter seu funcionamento totalmente público (sem sigilo de código), recaindo a segurança **exclusivamente no tamanho e sigilo da chave**.
</details>

---

### Questão 12 (FCC - 2016 - TRT 23 - Analista Judiciário - Tecnologia da Informação)
No uso da internet bancária (Home Banking), o protocolo HTTPS entra em cena estabelecendo um túnel TLS/SSL que fornece comunicação segura entre o navegador e o servidor do banco. Em relação aos métodos criptográficos usualmente empregados nesse cenário híbrido (TLS), é correto afirmar:
A) O tráfego intenso de transferência de dados (como extratos e faturas baixadas) é cifrado usando apenas criptografia assimétrica (RSA).
B) O protocolo TLS dispensa o uso de certificados digitais, baseando a autenticação do banco apenas num pré-compartilhamento de chaves simétricas.
C) A criptografia assimétrica é utilizada prioritariamente no início da conexão (handshake) para autenticação do servidor e estabelecimento de uma chave secreta compartilhada (simétrica).
D) O cliente é obrigado a possuir e apresentar seu próprio certificado digital X.509 em todos os acessos via HTTPS para se autenticar no banco.
E) O sigilo é garantido inteiramente pela assinatura digital do pacote IP usando o algoritmo SHA-1 embarcado no navegador.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Os sistemas modernos usam a criptografia de forma híbrida para usufruir do melhor de dois mundos (segurança da assimétrica + velocidade da simétrica).

- **A está incorreta:** A criptografia assimétrica é pesada e lerda. Usá-la para cifrar tráfego volumoso (extratos, stream, imagens) sobrecarregaria as CPUs. O tráfego de dados (payload) é cifrado com cifra simétrica (como AES).
- **B está incorreta:** O TLS/HTTPS depende visceralmente do envio do certificado digital X.509 do servidor (para o navegador checar se está falando com o banco verdadeiro ou um site falso de phishing).
- **C está correta:** No "handshake" TLS, a criptografia assimétrica (e chaves contidas no certificado) é usada para as partes se apresentarem com segurança e acordarem, nos bastidores, uma chave simétrica temporária. Uma vez que os dois têm a chave simétrica combinada (session key), todo o envio pesado de dados passa a usá-la.
- **D está incorreta:** O HTTPS padrão exige apenas a autenticação de uma das vias (do Servidor para o Cliente). O cliente normal acessando um site não precisa de um certificado (o navegador não envia um cert do usuário), ele fará o login com usuário e senha após o túnel subir.
- **E está incorreta:** SHA-1 é função de hash e provê apenas integridade. Ele não cifra dados, então não tem capacidade de garantir sigilo/confidencialidade.
</details>

---

### Questão 13 (FCC - 2014 - TRT 19 - Analista Judiciário - Tecnologia da Informação)
Ao receber um documento assinado digitalmente que garanta integridade, um sistema computacional realiza, em "background", a verificação daquela assinatura. Se durante a transmissão do documento, um atacante interceptar e alterar intencionalmente apenas um caractere do texto do documento M original (sem quebrar a cifra da assinatura), o que resultará na etapa final da validação?
A) O certificado digital do remetente será marcado como revogado na LCR imediatamente, já que a quebra foi detectada pela Autoridade de Registro.
B) O algoritmo falhará ao tentar decifrar a assinatura digital, travando a máquina destino com um erro de acesso a bloco não encriptado.
C) O hash local calculado pelo software do destinatário sobre o documento M modificado será completamente diferente do hash recuperado da assinatura, invalidando o documento.
D) A assinatura continuará válida, pois ela verifica primariamente a autenticidade da chave pública, mas o sistema alertará que o texto sofreu atualização temporal.
E) O destinatário solicitará via protocolo OCSP uma verificação reversa usando a chave simétrica da sessão para reescrever o texto ao original.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

O processo de validação de assinatura digital de um software ocorre em duas vias simultâneas:
1) O software pega o documento M (que chegou e que o usuário pode ler livremente) e aplica um algoritmo de hash localmente (ex: SHA-256), gerando um Resumo A.
2) O software pega a Assinatura Digital anexada e a decifra utilizando a chave Pública do remetente, o que revela o resumo original feito lá na origem (Resumo B).

- **A está incorreta:** Falha de integridade em uma mensagem não causa revogação do certificado do usuário. A revogação ocorre por quebra da chave privada ou perda do token.
- **B está incorreta:** A decifragem da assinatura com a chave pública do remetente funcionará perfeitamente e devolverá o hash original intocado. 
- **C está correta:** O coração da integridade repousa aqui. Como o texto sofreu alteração na rota (um caractere mudado), o Hash local calculado (Resumo A) dará completamente diferente do Hash da assinatura original decifrada (Resumo B). Logo, o software avisa: "Assinatura inválida / Documento alterado".
- **D está incorreta:** A alteração de 1 byte no arquivo é detectada e a assinatura é imediatamente invalidada na checagem final.
- **E está incorreta:** O protocolo OCSP (Online Certificate Status Protocol) serve para checar em tempo real se um certificado foi revogado (em alternativa à LCR). Não tem nenhuma relação com "consertar texto modificado" ou gerar hashes.
</details>

---

### Questão 14 (FCC - 2015 - TRT 4 - Analista Judiciário - Tecnologia da Informação)
Na cadeia de confiança da Infraestrutura de Chaves Públicas do Brasil (ICP-Brasil), a entidade responsável precípua pela formulação das diretrizes políticas normativas, definição de regras, autorização e credenciamento e auditoria das Autoridades Certificadoras é o(a):
A) Secretaria de Governo Digital (SGD).
B) Comitê Gestor da ICP-Brasil (CG ICP-Brasil).
C) Autoridade Certificadora Raiz (AC Raiz - exercida pelo ITI).
D) Agência Nacional de Telecomunicações (ANATEL).
E) Autoridade de Registro de Primeiro Nível (AR-BR).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A hierarquia da ICP-Brasil tem três níveis clássicos em relação a poder e operação:
1. Comitê Gestor (normatiza e dita as regras/políticas - Poder diretivo).
2. AC Raiz - papel exercido pelo Instituto Nacional de Tecnologia da Informação - ITI (Credencia e emite certificados apenas para as ACs debaixo dela - Poder operacional superior).
3. ACs de 1º/2º Nível e ARs (Fazem o trabalho perante o público, empresas e cidadãos - Poder operacional ponta).

- **A está incorreta:** Embora a SGD trabalhe com governança digital e plataformas gov.br, a estrutura legal e as normas exclusivas da ICP-Brasil cabem ao seu Comitê Gestor.
- **B está correta:** O Comitê Gestor da ICP-Brasil é quem tem o poder normativo, responsável por estabelecer as políticas, ditar normas e aprovar os procedimentos técnicos e operacionais de toda a ICP-Brasil.
- **C está incorreta:** O ITI é o órgão executor, ele obedece às normas do Comitê Gestor. O papel principal do ITI como AC Raiz é auditar as outras ACs e emitir a chave criptográfica que confere validade às ACs inferiores.
- **D está incorreta:** A ANATEL regula telecomunicações no país, não a infraestrutura pública de criptografia e certificação digital.
- **E está incorreta:** Não existe a figura de "Autoridade de Registro de Primeiro Nível" determinando regras. AR apenas executa cadastro de usuário (identificação).
</details>

---

### Questão 15 (FCC - 2015 - TRT 3 - Analista Judiciário - Informática)
Em virtude da perda ou suspeita de comprometimento da chave privada em um token USB, o proprietário do certificado digital solicita o imediato bloqueio e invalidação desse certificado antes do fim natural do seu prazo de validade. Esse processo, na nomenclatura e na arquitetura de certificação digital, é chamado de:
A) Suspensão da Chave Pública, operado exclusivamente pelo cartório de títulos.
B) Renovação Criptográfica Compulsória, efetuado pela própria máquina afetada e publicado via DNSSEC.
C) Revogação de Certificado, no qual o número de série desse certificado é publicado na LCR (Lista de Certificados Revogados).
D) Bloqueio de Assinatura Assimétrica, que apaga a chave da base de dados do Comitê Gestor.
E) Exclusão Lógica de Identidade, onde a chave privada do usuário é invalidada pelo repositório interno da Autoridade de Registro.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Quando há roubo, comprometimento de senha do token, morte do titular, alteração de dados da empresa, etc., o certificado deve ser "cancelado" prematuramente. 

- **A está incorreta:** A terminologia de mercado para a invalidação definitiva é "revogação". E isso é mantido pelas Autoridades Certificadoras, e não por cartórios físicos convencionais de títulos.
- **B está incorreta:** "Renovação" é emitir um novo. O procedimento do cancelamento não se chama renovação e tampouco usa a estrutura de DNSSEC (esta protege infraestrutura de DNS e não publica revogação pessoal).
- **C está correta:** É a Revogação. O certificado afetado entra na Lista de Certificados Revogados (LCR / CRL - Certificate Revocation List) disponibilizada publicamente na internet pela Autoridade Certificadora que o emitiu. Sistemas modernos consultam a LCR ou disparam OCSP para ver se o certificado ainda é digno de confiança.
- **D está incorreta:** O Comitê Gestor não possui base de dados com as chaves ou dados de usuários finais (quem tem a base operacional é a AC). E o processo se chama Revogação.
- **E está incorreta:** Conforme pontuado nas questões anteriores, a Autoridade de Registro (AR) atua na identificação; ela não mantém o repositório de chaves e de listas, ela apenas envia o pedido de revogação até a AC, que faz a publicação formal na LCR.
</details>

---


## 📝 TEMA 2: Programação (C, PHP, C#) e SOLID/GRASP

### Questão 1 (FCC - 2019 - TRF 4ª Região - Analista Judiciário - Sistemas da Informação)
No contexto dos princípios SOLID, o Princípio do Aberto/Fechado (Open/Closed Principle) estabelece que as entidades de software devem ser:
A) abertas para extensão e fechadas para modificação.
B) abertas para modificação e fechadas para extensão.
C) abertas para extensão e abertas para modificação.
D) abertas para substituição e fechadas para herança.
E) abertas para instanciação e fechadas para composição.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

O Princípio do Aberto/Fechado (Open/Closed Principle - OCP) estabelece que as entidades de software (classes, módulos, funções, etc.) devem ser abertas para extensão, mas fechadas para modificação.
- **A) Correta.** É a exata definição de Bertrand Meyer para o Princípio do Aberto/Fechado, indicando que novos comportamentos podem ser adicionados (extensão) sem alterar o código-fonte existente (modificação).
- **B) Incorreta.** Inverte totalmente os conceitos de aberto e fechado. Se fosse aberto para modificação, quebraríamos os sistemas dependentes sempre que houvesse mudança.
- **C) Incorreta.** Aberto para modificação contraria o objetivo do princípio, que é proteger o código funcional testado.
- **D) Incorreta.** Substituição é relacionada ao Princípio de Substituição de Liskov (LSP). Fechadas para herança também contraria o princípio, pois a herança é uma das formas de extensão (embora a composição seja frequentemente preferida).
- **E) Incorreta.** Instanciação e composição não são os eixos definidos pelo OCP, o qual foca em extensão e modificação.
</details>

---

### Questão 2 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - Tecnologia da Informação)
A linguagem C# suporta diversos modificadores de acesso que definem o escopo de visibilidade de tipos e membros. O modificador `internal` determina que o acesso é limitado:
A) ao assembly atual em que o código está sendo compilado.
B) apenas à classe onde foi declarado.
C) à classe onde foi declarado e às classes derivadas.
D) ao namespace onde foi declarado, independentemente do assembly.
E) ao projeto atual e a todos os projetos que o referenciam através de herança global.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

Em C#, modificadores de acesso ditam a visibilidade. O modificador `internal` torna o tipo ou membro acessível por qualquer código dentro do mesmo assembly, mas não a partir de outro assembly.
- **A) Correta.** O nível de acesso `internal` restringe o uso do membro apenas a arquivos no mesmo assembly (.dll ou .exe).
- **B) Incorreta.** Restringir o acesso apenas à classe onde foi declarado é a função do modificador `private`.
- **C) Incorreta.** Permitir acesso à classe e às classes derivadas é a função do modificador `protected`.
- **D) Incorreta.** A restrição não se dá pelo namespace. Um namespace pode abranger múltiplos assemblies. O modificador `internal` é estritamente vinculado ao assembly em que foi compilado.
- **E) Incorreta.** Não há o conceito de herança global em C# ou em projetos dependentes para `internal`. Qualquer assembly referenciador externo não enxerga tipos ou membros `internal`.
</details>

---

### Questão 3 (FCC - 2018 - TRT 2ª Região - Analista Judiciário - Tecnologia da Informação)
Na linguagem PHP, a partir da versão 5.4, introduziu-se um mecanismo de reutilização de código que permite aos desenvolvedores reutilizarem conjuntos de métodos livremente em várias classes independentes, que vivem em diferentes hierarquias de classes. Esse mecanismo é conhecido como:
A) Interfaces.
B) Traits.
C) Namespaces.
D) Mixins.
E) Abstract Classes.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Os *Traits* em PHP permitem criar blocos de código que podem ser embutidos dentro de múltiplas classes sem depender da herança clássica.
- **A) Incorreta.** Interfaces servem como contratos em que as classes definem as assinaturas dos métodos que devem implementar, não contêm implementações (em versões clássicas) para promover reutilização de lógica de código.
- **B) Correta.** Traits foram criados exatamente com esse propósito em PHP (desde a versão 5.4): possibilitar o uso de múltiplos métodos sem necessitar de herança múltipla, contornando a restrição de "herança simples" da linguagem.
- **C) Incorreta.** Namespaces resolvem o problema de colisão de nomes de classes, funções e constantes em projetos grandes, não para reutilização de métodos.
- **D) Incorreta.** Embora o conceito seja similar aos Mixins em outras linguagens, o termo técnico correto para esta feature em PHP é *Trait*.
- **E) Incorreta.** Classes abstratas servem de classe base, forçando a implementação de métodos, mas caem na limitação de herança simples do PHP, não sendo viáveis para classes independentes de diferentes hierarquias simultâneas.
</details>

---

### Questão 4 (FCC - 2017 - TST - Analista Judiciário - Tecnologia da Informação)
Em C, ao declarar um ponteiro, o símbolo utilizado para obter o endereço de uma variável na memória é:
A) *
B) &
C) %
D) #
E) $

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Na linguagem C, ponteiros operam diretamente sob endereços de memória, usando dois operadores primários: o de desreferência e o "endereço de".
- **A) Incorreta.** O asterisco (*) é o operador de indireção ou desreferência, usado na declaração para indicar que a variável é um ponteiro ou para acessar o valor apontado por ele.
- **B) Correta.** O e-comercial (&) é o operador "endereço de", o qual retorna o endereço de memória de seu operando, permitindo que um ponteiro aponte para essa variável.
- **C) Incorreta.** A porcentagem (%) é o operador de módulo (resto da divisão) em cálculos matemáticos ou formatador de string (ex: `%d`).
- **D) Incorreta.** A cerquilha (#) é usada como diretiva de pré-processador (ex: `#include`, `#define`).
- **E) Incorreta.** O cifrão ($) não é um operador padrão do C para tratar ponteiros ou variáveis.
</details>

---

### Questão 5 (FCC - 2016 - TRT 20ª Região - Analista Judiciário - Tecnologia da Informação)
Os padrões GRASP (General Responsibility Assignment Software Patterns) consistem em diretrizes para atribuição de responsabilidades a classes e objetos em projetos orientados a objetos. O padrão que estabelece que se deve atribuir a responsabilidade de criar uma instância da classe A a uma classe B, se B contiver ou agregar A, é o:
A) Controller (Controlador).
B) Pure Fabrication (Invenção Pura).
C) Creator (Criador).
D) Information Expert (Especialista na Informação).
E) High Cohesion (Alta Coesão).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

O GRASP possui 9 padrões fundamentais. A questão aborda o padrão referente à instanciação de novos objetos.
- **A) Incorreta.** O Controller foca em lidar com eventos de sistema ou mensagens de interface. É responsável por repassar requisições aos componentes internos.
- **B) Incorreta.** Pure Fabrication é uma classe que não representa um conceito do domínio do problema, criada artificialmente para alcançar baixa dependência ou alta coesão (ex: utilitários, classes de serviço).
- **C) Correta.** O Creator sugere as diretrizes sobre quem deve instanciar objetos. Uma classe B deve criar um objeto A se B tem dados de inicialização de A, se B contém/agrega A, se B usa A proximamente.
- **D) Incorreta.** Information Expert determina que se atribua a responsabilidade de uma tarefa à classe que detém a informação necessária para completá-la.
- **E) Incorreta.** High Cohesion é um padrão avaliativo que recomenda manter os objetos e módulos altamente focados, compreendendo operações relacionadas.
</details>

---

### Questão 6 (FCC - 2016 - TRF 3ª Região - Analista Judiciário - Informática)
Considere os princípios SOLID. O Princípio da Inversão de Dependência (Dependency Inversion Principle) prega que:
A) classes derivadas devem poder ser substituídas por suas classes bases sem alterar a corretude do programa.
B) módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.
C) uma classe deve ter um, e somente um, motivo para mudar.
D) clientes não devem ser forçados a depender de interfaces que não utilizam.
E) uma classe deve depender diretamente da implementação detalhada de outra classe e não de abstrações genéricas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

O princípio da Inversão de Dependência (DIP) guia o desacoplamento de software, baseando-se na estabilidade de abstrações (interfaces/classes abstratas).
- **A) Incorreta.** Trata-se da definição do Princípio de Substituição de Liskov (LSP).
- **B) Correta.** DIP define que "Módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de abstrações. Abstrações não devem depender de detalhes, detalhes devem depender de abstrações."
- **C) Incorreta.** Trata-se da definição do Princípio da Responsabilidade Única (SRP).
- **D) Incorreta.** Trata-se da definição do Princípio da Segregação de Interface (ISP).
- **E) Incorreta.** Esta alternativa prega justamente o oposto do DIP. Depender de implementações diretas aumenta acoplamento.
</details>

---

### Questão 7 (FCC - 2017 - TRE-PR - Analista Judiciário - Análise de Sistemas)
No padrão GRASP, o padrão Controlador (Controller) é responsável por:
A) acessar diretamente o banco de dados e garantir a persistência dos objetos do sistema.
B) receber e coordenar eventos de sistema em operações vindas do nível da interface com o usuário para o sistema.
C) maximizar o acoplamento entre a interface de usuário e a lógica de negócios.
D) instanciar todas as classes de domínio presentes na aplicação orientada a objetos.
E) representar um objeto que possui as informações necessárias para preencher os dados de uma interface gráfica.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

O Controller do GRASP (não deve ser confundido com MVC) é o primeiro objeto além da camada de apresentação (interface) que recebe e coordena os eventos de um sistema.
- **A) Incorreta.** Acessar diretamente banco de dados não é sua responsabilidade, mas geralmente de objetos de acesso a dados (DAO / Repositórios) e Pure Fabrications.
- **B) Correta.** O Controller é atribuído para gerenciar requisições da interface de usuário que são roteadas para o domínio. Ele não executa a regra em si necessariamente, mas "controla" a execução encaminhando para os especialistas corretos.
- **C) Incorreta.** O objetivo do Controller é justamente o oposto: desacoplar a interface de usuário e a lógica de negócios, minimizando o acoplamento.
- **D) Incorreta.** Quem instancia as classes de domínio é o padrão Creator.
- **E) Incorreta.** Representar dados que preenchem interface é frequentemente o papel de DTOs, não do padrão Controller.
</details>

---

### Questão 8 (FCC - 2015 - TRT 3ª Região - Analista Judiciário - Tecnologia da Informação)
Sobre a linguagem C#, na manipulação de exceções, qual bloco é sempre executado, independentemente de uma exceção ter sido lançada ou não?
A) try
B) catch
C) finally
D) throw
E) exception

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

No gerenciamento estruturado de exceções (try/catch/finally), alguns blocos têm comportamentos de controle de fluxo de erros específicos.
- **A) Incorreta.** O bloco `try` encapsula o código que pode gerar erro. Se uma exceção ocorrer no início dele, o restante do bloco é abortado (logo, nem tudo do try é sempre executado).
- **B) Incorreta.** O bloco `catch` só será executado se, e somente se, uma exceção correspondente for lançada dentro do `try`.
- **C) Correta.** O bloco `finally` é sempre executado, independentemente do sucesso do `try` ou da ocorrência de uma exceção capturada pelo `catch`. Ele é utilizado tipicamente para limpeza e liberação de recursos, como fechar arquivos ou conexões com banco.
- **D) Incorreta.** `throw` não é um bloco de controle de fluxo, mas um comando para gerar explicitamente uma exceção.
- **E) Incorreta.** `Exception` é a classe base para tratamento de erros no .NET, não um bloco sintático de execução forçada.
</details>

---

### Questão 9 (FCC - 2014 - TRT 16ª Região - Analista Judiciário - Tecnologia da Informação)
Na linguagem C, um array de caracteres terminado com o caractere nulo ('\0') é utilizado para representar:
A) um ponteiro dinâmico.
B) uma string.
C) um caractere único constante.
D) um número em ponto flutuante.
E) uma matriz bidimensional estrita.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Em C, não há um tipo nativo predefinido como as classes "String" em C# ou Java. Strings são interpretadas por arranjos de chars.
- **A) Incorreta.** Um ponteiro dinâmico (`malloc`, `calloc`) aloca memória na heap. Apesar de arrays terminados em nulo poderem usar ponteiros (ex. `char *str`), não definem o conceito de ponteiro em si.
- **B) Correta.** Uma sequência (array) de caracteres onde o último elemento é um terminador nulo (`\0`) é a forma idiomática da linguagem C para representar e tratar strings. Funções como `strlen` ou `strcpy` dependem deste `\0`.
- **C) Incorreta.** Um caractere constante é apenas `char c = 'a';`, não sendo um array terminado em null.
- **D) Incorreta.** Ponto flutuante é representado pelos tipos `float` e `double`.
- **E) Incorreta.** Uma matriz bidimensional de `char` precisaria de duas dimensões, ex: `char mat[2][3]`, o que não é o conceito de um array linear de caracteres.
</details>

---

### Questão 10 (FCC - 2019 - TRF 3ª Região - Analista Judiciário - Informática)
Na linguagem PHP, a abstração para acesso a bancos de dados, que fornece uma interface uniforme para acessar várias bases de dados diferentes, é a extensão:
A) mysqli.
B) OCI8.
C) pgsql.
D) PDO (PHP Data Objects).
E) sqlite3.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

Trabalhar com múltiplos bancos exige flexibilidade de conexão e queries sem mudar a infraestrutura inteira do código.
- **A) Incorreta.** `mysqli` é a extensão melhorada, mas funciona exclusivamente para o banco de dados MySQL.
- **B) Incorreta.** `OCI8` é o driver exclusivo de PHP para se comunicar com bases de dados Oracle.
- **C) Incorreta.** `pgsql` é a interface de comunicação do PHP apenas para o PostgreSQL.
- **D) Correta.** O PDO (PHP Data Objects) provê uma camada de abstração de acesso a dados. Pode-se usar as mesmas funções e métodos para emitir queries e buscar dados não importando o banco (MySQL, SQLite, SQL Server, etc).
- **E) Incorreta.** `sqlite3` é exclusiva para manipular o banco SQLite e não serve como interface genérica.
</details>

---

### Questão 11 (FCC - 2017 - TRT 24ª Região - Analista Judiciário - Tecnologia da Informação)
De acordo com os princípios SOLID, se o cliente A precisa de apenas um método e o cliente B precisa de outros três métodos diferentes, é uma má prática forçá-los a implementar uma única interface genérica contendo todos os métodos. Isso se refere ao Princípio da:
A) Segregação de Interfaces.
B) Responsabilidade Única.
C) Substituição de Liskov.
D) Inversão de Dependência.
E) Coesão de Métodos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

Interfaces devem ser granulares.
- **A) Correta.** O Princípio da Segregação de Interfaces (ISP - Interface Segregation Principle) determina que "Clientes não devem ser forçados a depender de interfaces (métodos) que eles não utilizam". Criar interfaces menores e mais específicas é a recomendação.
- **B) Incorreta.** A Responsabilidade Única (SRP) aborda os motivos para mudar uma classe ("uma classe deve ter um e apenas um motivo para mudar"). Foca no comportamento interno.
- **C) Incorreta.** Substituição de Liskov (LSP) dita que subtipos devam ser substituíveis pelos seus tipos bases.
- **D) Incorreta.** Inversão de Dependência (DIP) aborda abstrações em oposição a implementações diretas.
- **E) Incorreta.** "Coesão de Métodos" não é um dos cinco princípios do acrônimo SOLID, embora ter métodos coesos seja uma meta arquitetural secundária.
</details>

---

### Questão 12 (FCC - 2018 - TRT 6ª Região - Analista Judiciário - Tecnologia da Informação)
No GRASP, o padrão que diz que uma responsabilidade deve ser atribuída à classe que possui a informação necessária para cumpri-la é chamado de:
A) Indirection (Indireção).
B) Polymorphism (Polimorfismo).
C) Creator (Criador).
D) Information Expert (Especialista na Informação).
E) Protected Variations (Variações Protegidas).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

Uma das primeiras decisões no design OO é: "Qual objeto deve fazer o quê?". O GRASP formalizou isso.
- **A) Incorreta.** Indireção (Indirection) cria um intermediário para desacoplar dois ou mais componentes, reduzindo acoplamento.
- **B) Incorreta.** Polimorfismo aborda o tratamento flexível e extensível de alternativas de comportamento baseado em tipo de objeto através de operações em classes distintas.
- **C) Incorreta.** O Criador (Creator) guia a atribuição de responsabilidades para a instanciação e criação de objetos, não para cumprir lógica de negócio genérica.
- **D) Correta.** O Especialista na Informação (Information Expert) é o padrão primário para atribuição de responsabilidades gerais: delega a tarefa à classe que contém (é especialista) nos dados para realizá-la.
- **E) Incorreta.** Variações Protegidas (Protected Variations) protege os elementos das variações criando abstrações (interfaces/herança).
</details>

---

### Questão 13 (FCC - 2015 - TRE-AP - Analista Judiciário - Tecnologia da Informação)
A linguagem C# introduziu o recurso LINQ (Language-Integrated Query) que permite realizar consultas em diferentes fontes de dados. Qual palavra-chave do LINQ é utilizada para filtrar os resultados de uma consulta baseada em uma condição?
A) select
B) from
C) where
D) group
E) orderby

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

O LINQ unifica e flexibiliza as consultas usando sintaxe similar à linguagem SQL no .NET.
- **A) Incorreta.** A cláusula `select` no LINQ dita como projetar os elementos e seus tipos de saída, qual formato a resposta terá, mas não faz a filtragem.
- **B) Incorreta.** A cláusula `from` introduz a fonte dos dados e o nome da variável de range (ex: `from p in Pessoas`), mas não filtra os itens.
- **C) Correta.** A cláusula `where` atua como um filtro com predicado booleano, permitindo que apenas os itens que satisfaçam a condição sejam retornados na query.
- **D) Incorreta.** A cláusula `group` é usada para organizar e agrupar elementos que compartilhem uma chave comum.
- **E) Incorreta.** A cláusula `orderby` determina a ordenação dos resultados produzidos na fonte em ordens crescentes ou decrescentes.
</details>

---

### Questão 14 (FCC - 2016 - TRT 23ª Região - Analista Judiciário - Tecnologia da Informação)
No contexto de PHP, quando se deseja utilizar classes com o mesmo nome em diferentes bibliotecas, evita-se colisão de nomes através do uso de:
A) scopes.
B) namespaces.
C) traits.
D) interfaces.
E) static properties.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Projetos grandes costumam utilizar múltiplas bibliotecas externas (via Composer, por exemplo).
- **A) Incorreta.** Em PHP, o termo scope (escopo) refere-se ao tempo de vida de uma variável e sua visibilidade, não para agrupar identificadores e bibliotecas.
- **B) Correta.** Namespaces são projetados especificamente para resolver dois problemas: colisão de nomes com classes, funções ou constantes do PHP ou pacotes de terceiros, bem como para estruturar, encadear e organizar código.
- **C) Incorreta.** Traits são para reuso de métodos para sanar limitações da falta de herança múltipla do PHP.
- **D) Incorreta.** Interfaces servem como contratos de classe.
- **E) Incorreta.** Propriedades estáticas pertencem à classe, mas não previnem colisão entre classes homônimas em arquivos diferentes.
</details>

---

### Questão 15 (FCC - 2017 - TRE-SP - Analista Judiciário - Programação de Sistemas)
O princípio de Substituição de Liskov (Liskov Substitution Principle - LSP) estabelece que:
A) as abstrações não devem depender de detalhes, e os detalhes não devem depender de abstrações.
B) uma classe derivada deve poder ser substituída por sua classe base sem alterar a corretude do programa.
C) os módulos devem ser coesos e fracamente acoplados entre si.
D) uma classe deve possuir apenas um motivo para ser modificada.
E) as interfaces devem ser pequenas, com o menor número possível de operações, para evitar poluição de dependência.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Criado por Barbara Liskov, este princípio rege as regras do uso semântico da herança em Orientação a Objetos.
- **A) Incorreta.** Esse enunciado mistura conceitos do Inversion of Dependency Principle (DIP). O correto de DIP é abstrações não devem depender de detalhes, detalhes devem depender de abstrações.
- **B) Correta.** O Princípio da Substituição de Liskov define que objetos de uma superclasse (base) devem ser substituíveis por objetos de suas subclasses (derivada) sem quebrar a aplicação (corretude e funcionalidade).
- **C) Incorreta.** Isto se refere a conceitos gerais de design (Alta Coesão e Baixo Acoplamento), não especificamente ao LSP.
- **D) Incorreta.** Refere-se à Responsabilidade Única (SRP - Single Responsibility Principle).
- **E) Incorreta.** Refere-se à Segregação de Interfaces (ISP - Interface Segregation Principle).
</details>


## 📝 TEMA 3: Língua Portuguesa

### Questão 1 (FCC - 2022 - TRT 22ª Região - Analista Judiciário)
O sinal indicativo de crase está empregado corretamente em:
A) Devido a forte chuva, o evento ao ar livre foi sumariamente cancelado.
B) O juiz fez referência a leis trabalhistas muito antigas na audiência.
C) O candidato dedicou-se à redigir um bom texto para a prova discursiva.
D) A solicitação de recurso foi encaminhada à Vossa Excelência ontem.
E) Os pesquisadores chegaram àquela conclusão após muitos testes de campo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**

**Explicação detalhada:**
- **A) Incorreta.** Faltou o sinal de crase. Como "forte chuva" é uma expressão feminina determinada e o termo anterior "Devido a" exige preposição, deveria ser "Devido à forte chuva".
- **B) Incorreta.** Não ocorre crase antes de palavras no plural se o "a" estiver no singular ("a leis"). Para que houvesse crase, deveria ser "às leis". O termo em "a" aqui é apenas preposição.
- **C) Incorreta.** É regra básica: não se usa sinal indicativo de crase antes de verbos ("redigir"), visto que não admitem artigo feminino.
- **D) Incorreta.** Pronomes de tratamento como "Vossa Excelência", "Vossa Senhoria", "Sua Majestade" não admitem crase, pois repudiam o artigo feminino.
- **E) Correta.** A regência nominal/verbal de "chegar" exige a preposição "a" (quem chega, chega **a** algo). Essa preposição se fundiu com a primeira vogal do pronome demonstrativo "aquela" (a + aquela = àquela).
</details>

---

### Questão 2 (FCC - 2023 - TRT 18ª Região - Técnico Judiciário)
A concordância verbal está plenamente respeitada na frase:
A) Espera-se que hajam novas oportunidades de crescimento econômico no próximo ano.
B) Fazem muitos anos que a tecnologia transformou o mercado de trabalho brasileiro.
C) Tratam-se de questões fundamentais para o desenvolvimento sustentável da sociedade.
D) Coube aos pesquisadores a responsabilidade de apresentar os novos dados.
E) Deve existir muitos obstáculos até a conclusão definitiva do projeto de expansão.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Explicação detalhada:**
- **A) Incorreta.** O verbo "haver" no sentido de existir é impessoal e deve permanecer na 3ª pessoa do singular: "Espera-se que **haja** novas oportunidades".
- **B) Incorreta.** O verbo "fazer" indicando tempo decorrido também é impessoal, devendo ficar no singular: "**Faz** muitos anos".
- **C) Incorreta.** Na estrutura com pronome "se" servindo de índice de indeterminação do sujeito (quem trata, trata **de** algo), o verbo deve ficar na 3ª pessoa do singular: "**Trata-se** de questões fundamentais".
- **D) Correta.** O sujeito da oração é "a responsabilidade de apresentar os novos dados", que é singular. O verbo "coube" concorda corretamente com o núcleo "responsabilidade" no singular.
- **E) Incorreta.** O verbo principal da locução é "existir", que possui sujeito ("muitos obstáculos"). Assim, o verbo auxiliar "dever" precisa flexionar no plural para concordar com o sujeito: "**Devem** existir muitos obstáculos".
</details>

---

### Questão 3 (FCC - 2021 - TRT 15ª Região - Analista Judiciário)
Para que os segmentos sublinhados na frase "O diretor *entregou o relatório* aos conselheiros, mas antes precisou *revisar as planilhas*" sejam substituídos por pronomes de modo correto e de acordo com a norma-padrão, deve-se escrever:
A) entregou-lhe / revisá-las.
B) entregou-o / revisá-las.
C) entregou-lhes / revisar-lhes.
D) entregou-o / revisar-lhas.
E) entregou-no / revisá-las.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Explicação detalhada:**
- **A) Incorreta.** O pronome "lhe" substitui objetos indiretos regidos de preposição (a, para). "O relatório" é objeto direto (quem entrega, entrega algo), exigindo os pronomes o, a, os, as.
- **B) Correta.** "entregar" é verbo transitivo direto e indireto. Ao substituir o objeto direto "o relatório", usamos o pronome "o" (entregou-o). Já o verbo "revisar" é transitivo direto. Ao substituir "as planilhas" (objeto direto), usa-se o pronome "as". Como "revisar" termina em "r", corta-se a consoante e acrescenta-se "L" ao pronome: revisá-las.
- **C) Incorreta.** Ambos os objetos destacados são diretos, logo, a substituição por "lhes" (que exerce função de objeto indireto) é indevida. 
- **D) Incorreta.** "lhas" é a contração de lhes + as. Não há objeto indireto a ser substituído junto com o direto no segundo caso.
- **E) Incorreta.** O pronome "no/na/nos/nas" é usado quando a forma verbal termina em som nasal (-m, -ão, -õe). Como "entregou" termina em ditongo oral ("u"), deve-se usar apenas "o" (entregou-o).
</details>

---

### Questão 4 (FCC - 2022 - TRT 14ª Região - Técnico Judiciário)
A frase cuja pontuação está inteiramente correta é:
A) Os funcionários, que solicitaram folga, terão seus pedidos, analisados pelo RH.
B) Embora a reunião, tenha sido longa, os principais pontos da pauta foram discutidos.
C) O projeto, de modernização do sistema judiciário, será implementado no próximo mês.
D) Muitos acreditam que a inteligência artificial, trará grandes benefícios à humanidade.
E) Os documentos solicitados na semana passada, segundo informou o setor de protocolo, já estão disponíveis.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**

**Explicação detalhada:**
- **A) Incorreta.** Há uma vírgula separando o substantivo ("pedidos") de seu adjunto adnominal/predicativo ("analisados"), o que é proibido pela norma-padrão.
- **B) Incorreta.** O uso da vírgula separando o sujeito ("a reunião") de seu verbo ("tenha sido") está incorreto.
- **C) Incorreta.** As vírgulas estão isolando "de modernização do sistema judiciário", que é um adjunto adnominal restritivo, o que fere a norma culta.
- **D) Incorreta.** A vírgula entre "a inteligência artificial" (sujeito) e "trará" (verbo) quebra a regra básica e absoluta de não separar o sujeito do seu predicado com vírgula.
- **E) Correta.** As vírgulas foram perfeitamente utilizadas para isolar a oração intercalada e adverbial conformativa ("segundo informou o setor de protocolo"). O sujeito "Os documentos..." liga-se ao predicado "...já estão disponíveis" apenas sofrendo a devida interrupção dessa intercalação.
</details>

---

### Questão 5 (FCC - 2019 - TRF 3ª Região - Analista Judiciário)
Transpondo-se para a voz passiva a oração "O tribunal julgaria os recursos na próxima sessão", a forma verbal resultante será:
A) teriam sido julgados.
B) julgar-se-ão.
C) foram julgados.
D) seriam julgados.
E) serão julgados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Explicação detalhada:**
- **A) Incorreta.** O tempo "teriam sido julgados" equivale a um tempo composto, o que não reflete a estrutura simples de "julgaria".
- **B) Incorreta.** "julgar-se-ão" está no Futuro do Presente ("julgarão"), enquanto o original "julgaria" está no Futuro do Pretérito.
- **C) Incorreta.** "foram julgados" é Pretérito Perfeito (passado). A frase original está num tempo futuro (Futuro do Pretérito).
- **D) Correta.** Na transposição para a voz passiva analítica, o verbo ser (auxiliar) deve ficar no exato tempo e modo do verbo ativo. Como "julgaria" está no Futuro do Pretérito do Indicativo, usamos "seriam" + particípio "julgados". Resulta em: "Os recursos **seriam julgados** pelo tribunal na próxima sessão".
- **E) Incorreta.** "serão julgados" é Futuro do Presente (que corresponderia a "O tribunal julgará"). 
</details>

---

### Questão 6 (FCC - 2023 - TRT 11ª Região - Analista Judiciário)
"**Conquanto** houvesse forte resistência de alguns diretores, a nova política interna foi aprovada."
O termo destacado introduz no período uma noção de:
A) causa.
B) conformidade.
C) concessão.
D) consequência.
E) condição.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Explicação detalhada:**
- **A) Incorreta.** Para indicar causa, usaríamos "como", "porque", "já que". Ex: Já que havia resistência, a política NÃO foi aprovada.
- **B) Incorreta.** Para indicar conformidade, usaríamos "conforme", "segundo", "consoante".
- **C) Correta.** A conjunção "conquanto" é tipicamente concessiva e equivale a "embora", "mesmo que", "ainda que". Exprime uma oposição que não é suficiente para anular a ação principal (resistiram, mas a política foi aprovada mesmo assim).
- **D) Incorreta.** Consequência seria introduzida por "de modo que", "tanto que".
- **E) Incorreta.** Condição usa conjunções como "caso", "se", "contanto que".
</details>

---

### Questão 7 (FCC - 2018 - TRT 2ª Região - Técnico Judiciário)
O verbo indicado entre parênteses deverá flexionar-se de modo a concordar obrigatoriamente no **plural** para preencher corretamente a lacuna da frase:
A) Não (caber) aos cidadãos comuns resolver um problema tão complexo sozinho.
B) (Verificar)-se, durante a rigorosa fiscalização, irregularidades na prestação de contas.
C) Hoje (fazer) exatamente duas semanas que o novo sistema eletrônico entrou no ar.
D) Sempre (haver) motivos infundados para os funcionários discordarem das regras.
E) (Surgir) de repente, no meio da reunião, uma ideia inovadora para solucionar o impasse.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Explicação detalhada:**
- **A) Incorreta.** O verbo "caber" tem como sujeito a oração "resolver um problema...". Sujeitos oracionais forçam o verbo a ficar na 3ª pessoa do singular. Correção: "Não cabe...".
- **B) Correta.** A partícula "se" apassiva o verbo transitivo direto "verificar". O sujeito paciente é "irregularidades", termo no plural. Portanto, o verbo obrigatoriamente vai para o plural: "Verificaram-se irregularidades".
- **C) Incorreta.** O verbo "fazer", marcando tempo transcorrido, é impessoal. Fica apenas na 3ª pessoa do singular: "Hoje faz exatamente duas semanas...".
- **D) Incorreta.** O verbo "haver", empregado com o sentido de existir, é impessoal e só pode ser conjugado na 3ª pessoa do singular. Correção: "Sempre haverá/houve/há motivos...".
- **E) Incorreta.** O sujeito é "uma ideia inovadora", que está no singular. O verbo fica no singular: "Surgiu...".
</details>

---

### Questão 8 (FCC - 2021 - TRT 15ª Região - Técnico Judiciário)
A regência do verbo destacado e o emprego do pronome relativo estão adequados à norma-padrão em:
A) O valioso livro histórico **cujas as** páginas estão rasgadas precisa de reparos.
B) A pacata cidade **onde** nasci passou por grandes e importantes transformações.
C) O cargo de gerência **que** aspiro exige muita dedicação aos estudos e à prática.
D) As testemunhas do caso **com quem** conversei confirmou toda a história narrada.
E) A inusitada conclusão **que** chegaram foi surpreendente para os pesquisadores.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Explicação detalhada:**
- **A) Incorreta.** O uso de artigo feminino plural "as" após o pronome relativo "cujo" (e suas flexões) é totalmente proibido pela norma-padrão. O correto é "cujas páginas".
- **B) Correta.** O pronome relativo "onde" está perfeitamente empregado, pois refere-se a lugar fixo (cidade). Além disso, a regência de "nascer" é de quem nasce, nasce **em** algum lugar ("em" + "que" = "onde" / nasci na cidade).
- **C) Incorreta.** O verbo "aspirar", no sentido de desejar, almejar, exige a preposição "a". O correto seria o cargo **ao qual** ou **a que** aspiro.
- **D) Incorreta.** Há um erro de concordância (não de regência) que inviabiliza a frase: "As testemunhas [...] *confirmou*". O correto é "confirmaram".
- **E) Incorreta.** O verbo "chegar" (no sentido de alcançar) é intransitivo e exige a preposição "a". Quem chega, chega **a** algo. O correto seria a conclusão **a que** (ou **à qual**) chegaram.
</details>

---

### Questão 9 (FCC - 2022 - TRT 14ª Região - Analista Judiciário)
A correlação entre os tempos e modos verbais está inteiramente correta na frase:
A) Se o projeto for aprovado hoje, nós começaríamos os testes na próxima semana.
B) Caso o governo investisse mais em educação, os índices de pobreza diminuirão consideravelmente.
C) Quando os novos equipamentos chegarem, a equipe técnica iniciará a instalação imediatamente.
D) Embora o diretor da empresa tenha exigido pontualidade, os funcionários chegassem atrasados.
E) Se todos os setores colaborarem com a pesquisa, nós poderíamos entregar o relatório no prazo estipulado.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Explicação detalhada:**
- **A) Incorreta.** O Futuro do Subjuntivo ("for") articula-se corretamente com o Futuro do Presente do Indicativo ("começaremos"), e não com o Futuro do Pretérito ("começaríamos").
- **B) Incorreta.** O Pretérito Imperfeito do Subjuntivo ("investisse") exige, para sua correta correlação, o Futuro do Pretérito do Indicativo ("diminuiriam"), e não o Futuro do Presente ("diminuirão").
- **C) Correta.** Há uma perfeita correlação temporal e modal: "chegarem" (Futuro do Subjuntivo - expressando fato provável no futuro) correlaciona-se ao verbo "iniciará" (Futuro do Presente do Indicativo - expressando ação que se realizará após a condição satisfeita).
- **D) Incorreta.** "tenha exigido" (Pretérito Perfeito Composto do Subjuntivo) não se harmoniza com "chegassem" (Pretérito Imperfeito do Subjuntivo). O certo seria "chegaram" (Pretérito Perfeito do Indicativo): Embora o diretor tenha exigido, eles chegaram.
- **E) Incorreta.** O Futuro do Subjuntivo ("colaborarem") demanda o Futuro do Presente do Indicativo ("poderemos"), não "poderíamos".
</details>

---

### Questão 10 (FCC - 2018 - TRT 6ª Região - Analista Judiciário)
A crase está empregada de acordo com a norma-padrão da Língua Portuguesa na alternativa:
A) O juiz declarou-se favorável à medidas mais severas durante o julgamento do réu.
B) O processo confidencial foi entregue à um funcionário recém-chegado ao setor.
C) Passo à passo, o novo projeto de infraestrutura foi ganhando forma e consistência.
D) O relatório trimestral foi imediatamente submetido à apreciação da diretoria executiva.
E) O habilidoso advogado fez referência à artigos muito antigos da Constituição Federal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Explicação detalhada:**
- **A) Incorreta.** Não ocorre crase de um "a" no singular antes de uma palavra no plural ("medidas"). Para a crase ser correta, seria necessário o artigo no plural: "às medidas".
- **B) Incorreta.** Não se usa crase antes de pronomes ou artigos indefinidos masculinos, como "um".
- **C) Incorreta.** Não ocorre crase entre palavras repetidas e unidas por preposição, sejam elas masculinas (passo a passo) ou femininas (face a face).
- **D) Correta.** A expressão "submetido" pede a preposição "a" (submetido **a**). A palavra "apreciação" é feminina e admite o artigo feminino "a". A contração de preposição + artigo exige o acento grave indicador de crase (à).
- **E) Incorreta.** Assim como na alternativa A, temos a preposição "a" no singular antes de um substantivo plural ("artigos"). Ademais, "artigos" é palavra masculina, o que por si só já inviabiliza a crase nesse contexto.
</details>

---

### Questão 11 (FCC - 2023 - TRE SP - Técnico Judiciário)
O elemento sublinhado tem o mesmo valor semântico e a mesma função sintática do pronome "se" em "Ainda *se* observam as mesmas falhas no sistema" na seguinte frase:
A) A coordenadora *se* arrependeu de ter deixado o cargo prematuramente no ano passado.
B) Construiu-*se* um novo prédio anexo para abrigar todas as secretarias do órgão público.
C) Precisa-*se* urgentemente de profissionais qualificados no setor de tecnologia da informação.
D) O funcionário descuidado machucou-*se* durante o manuseio da máquina de triturar papel.
E) As duas antigas colegas de turma abraçaram-*se* emocionadas no saguão do aeroporto.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Explicação detalhada:**
O enunciado traz a frase "Ainda se observam as mesmas falhas", em que o **"se" é Partícula Apassivadora**. A prova de que é apassivadora é a possibilidade de conversão para a voz passiva analítica: "As mesmas falhas são observadas".
- **A) Incorreta.** Aqui, o "se" é Parte Integrante do Verbo, pois o verbo é pronominal "arrepender-se" (ninguém "arrepende" alguém).
- **B) Correta.** O "se" também é Partícula Apassivadora. "Construiu-se um novo prédio" = "Um novo prédio foi construído". 
- **C) Incorreta.** O "se" funciona como Índice de Indeterminação do Sujeito, pois acompanha verbo transitivo indireto (precisar de) na 3ª pessoa do singular. 
- **D) Incorreta.** O "se" é um Pronome Reflexivo, indicando que a ação feita pelo funcionário recaiu sobre ele mesmo (ele machucou a si próprio).
- **E) Incorreta.** O "se" é um Pronome Recíproco, indicando uma ação mútua entre as amigas (uma abraçou a outra).
</details>

---

### Questão 12 (FCC - 2019 - TRF 4ª Região - Técnico Judiciário)
A colocação pronominal atende plenamente às rígidas regras da norma-padrão em:
A) Lhe disseram que o prazo improrrogável para recurso de apelação havia terminado.
B) Nunca revelaram-me os verdadeiros e sombrios motivos daquela demissão em massa.
C) Os dedicados servidores que dedicaram-se intensamente ao projeto foram homenageados.
D) Dar-te-ei a resposta definitiva sobre o caso assim que o processo for julgado no plenário.
E) Em tratando-se de complexas questões jurídicas, o veterano advogado é especialista.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Explicação detalhada:**
- **A) Incorreta.** A norma-padrão proíbe que se inicie uma oração ou período com um pronome átono. O correto é usar ênclise: "Disseram-lhe...".
- **B) Incorreta.** O advérbio "Nunca" atua como palavra atrativa, exigindo, obrigatoriamente, o uso da próclise (pronome antes do verbo). O correto seria: "Nunca **me** revelaram".
- **C) Incorreta.** O pronome relativo "que" é um poderoso atrator de pronomes átonos, exigindo próclise. O correto seria: "...que **se** dedicaram...".
- **D) Correta.** Há mesóclise (pronome no meio do verbo). A mesóclise é obrigatória quando o verbo está no futuro do presente ("darei") ou do pretérito ("daria"), e desde que não haja palavra atrativa exigindo próclise antes do verbo. Portanto, "Dar-te-ei" está perfeito.
- **E) Incorreta.** Com verbo no gerúndio precedido pela preposição "em", ocorre próclise obrigatória. O correto é: "Em **se** tratando de...".
</details>

---

### Questão 13 (FCC - 2018 - TRT 15ª Região - Técnico Judiciário)
Sem nenhum prejuízo para a correção gramatical e o sentido original da frase "As empresas faliram *porque* não houve um planejamento adequado", o elemento sublinhado pode ser substituído por:
A) conquanto.
B) visto que.
C) por conseguinte.
D) a fim de que.
E) ainda que.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Explicação detalhada:**
O termo "porque", neste contexto, introduz a causa de as empresas terem falido, possuindo valor causal.
- **A) Incorreta.** "Conquanto" é uma conjunção concessiva (equivale a "embora"), o que alteraria drasticamente o sentido.
- **B) Correta.** "Visto que" é uma clássica locução conjuntiva de valor causal, sendo perfeita sinônima de "porque", "já que", "dado que", "uma vez que".
- **C) Incorreta.** "Por conseguinte" é conjunção conclusiva (portanto, logo).
- **D) Incorreta.** "A fim de que" exprime finalidade (para que).
- **E) Incorreta.** "Ainda que" é uma locução conjuntiva concessiva, sinônimo de "embora".
</details>

---

### Questão 14 (FCC - 2021 - TRT 11ª Região - Analista Judiciário)
Está plenamente adequada às regras de pontuação a seguinte frase:
A) Aqueles pesquisadores que chegaram recentemente da Europa, apresentarão seus estudos em breve.
B) O problema central, afirmou o diretor financeiro, não é a falta de recursos, mas sim o planejamento falho.
C) Quando os resultados da pesquisa, foram divulgados a população começou a questionar as ações do prefeito.
D) O respeitado tribunal, durante a sessão matutina de ontem decidiu, absolver o réu das graves acusações de corrupção.
E) Todos os antigos funcionários do departamento de recursos humanos, foram convocados para a reunião de emergência.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Explicação detalhada:**
- **A) Incorreta.** Há uma vírgula separando indevidamente o sujeito ("Aqueles pesquisadores que chegaram recentemente da Europa") do verbo principal ("apresentarão").
- **B) Correta.** A oração intercalada "afirmou o diretor financeiro" está perfeitamente isolada por duas vírgulas. E a vírgula antes de "mas sim" está correta para separar a conjunção adversativa.
- **C) Incorreta.** A vírgula após "pesquisa" separa o sujeito de seu verbo passivo ("foram divulgados"). Além disso, falta a vírgula obrigatória antes de "a população", para separar a oração adverbial temporal que veio deslocada no início do período.
- **D) Incorreta.** A vírgula após "decidiu" separa o verbo transitivo de seu objeto direto oracional ("absolver o réu..."). 
- **E) Incorreta.** A vírgula está separando o sujeito inteiro ("Todos os antigos funcionários do departamento de recursos humanos") do verbo da oração ("foram convocados"). Essa é uma quebra brutal da norma-padrão.
</details>

---

### Questão 15 (FCC - 2022 - TRT 4ª Região - Analista Judiciário)
Considerando a norma-padrão, as lacunas da frase "*_____* dias que não o vejo; disseram-me que ele se opôs tenazmente *_____* propostas da nova diretoria, o que gerou *_____* confusão no departamento" devem ser preenchidas, correta e respectivamente, por:
A) Fazem / as / bastantes
B) Faz / às / bastante
C) Fazem / às / bastante
D) Faz / as / bastantes
E) Faz / às / bastantes

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Explicação detalhada:**
A resolução envolve três análises:
1. **Fazer:** O verbo fazer indicando tempo decorrido (tempo passado) é verbo impessoal. Não admite plural, ficando obrigatoriamente na terceira pessoa do singular. Logo, o correto é **Faz** (e não "Fazem").
2. **Crase:** O verbo "opor-se" exige a preposição "a" (quem se opõe, opõe-se **a** algo). O substantivo feminino "propostas" admite o artigo feminino plural "as". A junção (a + as) gera a crase **às**.
3. **Bastante:** A palavra "bastante", nesse contexto, está modificando o substantivo "confusão" (que é feminino singular), funcionando como pronome adjetivo. Ele deve concordar em gênero e número com o substantivo. Como "confusão" está no singular, usa-se **bastante**. (Dica: é substituível por "muita"). Se fosse plural, seria "bastantes", mas não é o caso.

Portanto, o preenchimento correto, em ordem, é: **Faz / às / bastante**.
</details>

---


