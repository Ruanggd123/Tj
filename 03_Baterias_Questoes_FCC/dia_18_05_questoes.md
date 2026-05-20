# Bateria de Questões FCC — Segunda-feira 18/05

Este arquivo contém 45 questões da banca FCC (15 por tema estudado) com gabarito comentado ocultável.

---

## 📝 TEMA 1: Infraestrutura e Redes — Modelo OSI (7 Camadas)

### Questão 1 (FCC - TRT 11ª Região - Analista Judiciário - TI)
No modelo de referência ISO/OSI, a camada responsável por realizar o roteamento de pacotes através de múltiplos nós de rede, determinando o melhor caminho físico que os dados devem percorrer, é a camada de:
A) Transporte.
B) Enlace.
C) Rede.
D) Sessão.
E) Física.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A camada de **Rede** (Camada 3) é responsável pelo endereçamento lógico (IP) e pelo roteamento (escolha do melhor caminho para o tráfego de pacotes entre a origem e o destino através de redes distintas).
</details>

---

### Questão 2 (FCC - TRT 24ª Região - Analista - Tecnologia da Informação)
No contexto do modelo OSI, a camada que trata do controle de acesso ao meio físico (MAC), da detecção e correção opcional de erros ocorridos no link de comunicação física, agrupando os bits em quadros (frames), é a camada de:
A) Rede.
B) Enlace.
C) Física.
D) Transporte.
E) Apresentação.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A camada de **Enlace de Dados** (Camada 2) divide-se nas subcamadas LLC e MAC. Ela transforma o meio de transmissão físico bruto em um link confiável, agrupando bits em **quadros (frames)** e controlando o fluxo e erros locais (hop-to-hop).
</details>

---

### Questão 3 (FCC - TRF 3ª Região - Analista)
Em relação às Unidades de Dados de Protocolo (PDUs) nas diferentes camadas do modelo OSI, a associação correta é:
A) Camada Física ➔ Pacotes.
B) Camada de Enlace ➔ Segmentos.
C) Camada de Rede ➔ Quadros (Frames).
D) Camada de Transporte ➔ Segmentos (no TCP) ou Datagramas (no UDP).
E) Camada de Aplicação ➔ Bits.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** A associação correta das PDUs é:
- Camada Física ➔ **Bits**
- Camada de Enlace ➔ **Quadros (Frames)**
- Camada de Rede ➔ **Pacotes (Packets) / Datagramas IP**
- Camada de Transporte ➔ **Segmentos (TCP) / Datagramas (UDP)**
- Camadas superiores ➔ **Dados (Data)**
</details>

---

### Questão 4 (FCC - Sabesp - Analista)
Um Switch convencional de Camada 2 (Layer 2 Switch) atua primariamente na camada OSI de:
A) Física, repetindo os sinais elétricos em todas as portas de saída.
B) Enlace de Dados, encaminhando quadros com base no endereço físico MAC.
C) Rede, analisando o cabeçalho IP dos pacotes para definir a sub-rede.
D) Transporte, gerenciando as portas de socket ativas.
E) Aplicação, realizando a tradução de protocolos HTTP.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Switches L2 operam na camada de **Enlace de Dados** (Camada 2). Eles leem o cabeçalho do quadro (especificamente o endereço MAC de destino) para encaminhar o tráfego apenas para a porta física correta, reduzindo colisões.
</details>

---

### Questão 5 (FCC - Assembleia Legislativa - PB)
A camada do modelo OSI que atua na tradução, formatação e representação dos dados, realizando serviços como compressão de dados, conversão de formatos de texto (ex: ASCII para EBCDIC) e criptografia, é a camada de:
A) Aplicação.
B) Sessão.
C) Apresentação.
D) Transporte.
E) Rede.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A camada de **Apresentação** (Camada 6) cuida da sintaxe e da representação dos dados entregues à aplicação. Compressão, criptografia e formatação (ex: JPEG, ASCII) ocorrem aqui.
</details>

---

### Questão 6 (FCC - PGE-CE - Analista)
Qual a principal diferença funcional entre o controle de erros realizado pela camada de **Enlace** e o realizado pela camada de **Transporte** no modelo OSI?
A) O da camada de Enlace é executado de ponta a ponta (end-to-end); o de Transporte é executado entre nós vizinhos (hop-to-hop).
B) O da camada de Enlace aplica-se a bits brutos; o de Transporte aplica-se a pacotes IP.
C) O da camada de Enlace é executado localmente entre dois nós adjacentes conectados fisicamente; o de Transporte é executado de ponta a ponta entre a aplicação de origem e a de destino.
D) O de Enlace utiliza o protocolo TCP; o de Transporte utiliza o protocolo ARP.
E) Não há diferença; ambas realizam exatamente o mesmo controle sobre a mesma PDU física.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A camada de Enlace garante a entrega livre de erros sobre o link físico direto (entre dois aparelhos adjacentes). A camada de Transporte abstrai a rede física intermediária e realiza o controle de erros de ponta a ponta (end-to-end, entre o host de origem e o de destino).
</details>

---

### Questão 7 (FCC - TRT 15ª Região - Analista)
Um Hub e um Roteador atuam, respectivamente, em quais camadas do modelo de referência OSI?
A) Física e Rede.
B) Enlace e Transporte.
C) Física e Enlace.
D) Rede e Aplicação.
E) Enlace e Rede.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** 
- **Hub:** É um repetidor elétrico burro de portas, operando na Camada 1 (**Física**).
- **Roteador:** Toma decisões com base no endereçamento IP, operando na Camada 3 (**Rede**).
</details>

---

### Questão 8 (FCC - TRT 6ª Região - TI)
A camada do modelo OSI que gerencia o diálogo entre aplicações de hosts diferentes, estabelecendo, controlando e sincronizando a comunicação (através de pontos de sincronização para recuperação de falhas), é a camada de:
A) Transporte.
B) Sessão.
C) Apresentação.
D) Rede.
E) Enlace.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A camada de **Sessão** (Camada 5) permite que usuários em diferentes máquinas estabeleçam sessões de comunicação entre si, oferecendo controle de diálogo (simplex, half-duplex ou full-duplex) e inserindo pontos de sincronização (checkpoints).
</details>

---

### Questão 9 (FCC - ARTESP - Especialista)
O processo pelo qual uma camada inferior adiciona informações de controle (na forma de cabeçalhos e rodapés) a uma PDU recebida da camada superior é denominado:
A) Modulação.
B) Segmentação.
C) Multiplexação.
D) Encapsulamento.
E) Roteamento.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** O **Encapsulamento** ocorre à medida que os dados descem na pilha de protocolos: cada camada envelopa a PDU da camada superior adicionando seu próprio cabeçalho (header) e, opcionalmente, rodapé (trailer).
</details>

---

### Questão 10 (FCC - MPE-RS - Analista)
Em uma transmissão de rede de dados, cabos de par trançado UTP Categoria 6, conectores RJ-45 e fibras ópticas monomodo são componentes padronizados pela camada OSI de nível:
A) 1.
B) 2.
C) 3.
D) 4.
E) 7.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** Conectores, cabos, propriedades elétricas e mecânicas dos meios de transmissão pertencem à Camada 1 (**Física**).
</details>

---

### Questão 11 (FCC - TRT 20ª Região - TI)
Durante a navegação na internet, o navegador do usuário envia dados requisitando uma página HTML. O sistema operacional encapsula a requisição HTTP. Quando esses dados chegam à placa de rede para transmissão de sinais elétricos ou ópticos, o fluxo de dados transformou-se em:
A) Pacotes IP.
B) Segmentos de bytes.
C) Sinais em formato de Bits.
D) Quadros Ethernet criptografados.
E) Tabelas de roteamento.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A placa de rede (no nível físico de transmissão de cabo/ar/fibra) transmite as informações como pulsos de tensão, luz ou ondas eletromagnéticas, o que equivale conceitualmente a **Bits** (Camada Física).
</details>

---

### Questão 12 (FCC - Sabesp - Analista de Sistemas)
A camada de **Transporte** (Camada 4) do modelo OSI tem como uma de suas funções primordiais:
A) O controle de acesso ao meio compartilhado usando CSMA/CD.
B) A multiplexação de múltiplas conexões de aplicações utilizando portas lógicas (sockets).
C) O mapeamento físico de endereços lógicos em endereços de hardware locais.
D) A renderização de tags de marcação XML e JSON.
E) O roteamento estático com base na distância de saltos (hops).

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A camada de Transporte realiza a **multiplexação/demultiplexação** de conexões através do uso de números de portas (Sockets), permitindo que múltiplos aplicativos em execução no mesmo computador enviem e recebam dados simultaneamente na rede.
</details>

---

### Questão 13 (FCC - TRT 9ª Região - TI)
Qual dispositivo de rede atua na Camada 3 do modelo OSI e impede que mensagens de Broadcast locais se propaguem para outras redes físicas?
A) Switch L2.
B) Hub.
C) Roteador.
D) Repetidor de Sinal.
E) Bridge (Ponte).

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O **Roteador** delimita o domínio de broadcast. Pacotes direcionados ao endereço de broadcast de uma rede local (ex: `255.255.255.255`) não são encaminhados por roteadores para outras redes.
</details>

---

### Questão 14 (FCC - TRT 15ª Região - Analista)
Em relação às camadas OSI, os protocolos HTTP, FTP e SMTP pertencem à camada de número:
A) 4.
B) 5.
C) 6.
D) 7.
E) 3.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** HTTP, FTP e SMTP interagem diretamente com o usuário e os softwares de aplicação, pertencendo à Camada 7 (**Aplicação**).
</details>

---

### Questão 15 (FCC - Sabesp - TI)
Uma falha na sincronização lógica de uma transação de longa duração entre dois sistemas corporativos distribuídos, em que o envio foi interrompido na metade e o sistema de recepção não sabe de qual ponto continuar a gravação de dados, aponta um problema de projeto relacionado primariamente à camada OSI de:
A) Apresentação.
B) Transporte.
C) Sessão.
D) Enlace.
E) Física.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A camada de **Sessão** cuida da reinicialização de conexões e sincronização lógica de diálogos complexos inserindo pontos de verificação (checkpoints) nas transmissões de grandes arquivos para evitar a retransmissão completa do zero.
</details>

---

## 📝 TEMA 2: Infraestrutura e Redes — TCP/IP e Sub-redes

### Questão 16 (FCC - TRT 11ª Região - Analista Judiciário - TI)
Sobre os protocolos da camada de transporte da pilha TCP/IP, TCP e UDP, é correto afirmar:
A) O TCP e o UDP são protocolos orientados a conexão que garantem a entrega de pacotes sem duplicidades.
B) O UDP possui menor overhead de cabeçalho (8 bytes) em comparação ao TCP (mínimo de 20 bytes), tornando-o mais rápido e adequado para transmissões em tempo real (como VoIP).
C) O TCP utiliza o mecanismo de "Three-Way Handshake" apenas para finalizar conexões ativas.
D) O UDP possui controle de congestionamento nativo que reduz a vazão de envio ao detectar perda de datagramas na rede.
E) Ambos utilizam a mesma estrutura de flags de controle como SYN, ACK e FIN.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O UDP não tem conexão, controle de fluxo ou retransmissão, o que resulta em um cabeçalho muito enxuto de apenas **8 bytes**. Isso o torna extremamente rápido e perfeito para streaming e VoIP. O TCP exige mais recursos, com cabeçalho de no mínimo **20 bytes**.
</details>

---

### Questão 17 (FCC - TRT 24ª Região - Analista)
Associe os protocolos da pilha TCP/IP com suas respectivas funções padrão:
1. **ARP**
2. **ICMP**
3. **DNS**
4. **DHCP**

( ) Traduz nomes de domínio legíveis por humanos em endereços IP.
( ) Atribui dinamicamente endereços IP e parâmetros de rede a hosts na inicialização.
( ) Descobre o endereço físico MAC a partir de um endereço IP conhecido na rede local.
( ) Utilizado para enviar mensagens de controle e relatórios de erro de roteamento (ex: ping).

A sequência correta de preenchimento dos parênteses, de cima para baixo, é:
A) 3 - 4 - 1 - 2.
B) 4 - 3 - 2 - 1.
C) 3 - 4 - 2 - 1.
D) 1 - 2 - 3 - 4.
E) 2 - 1 - 4 - 3.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** 
- DNS (3) realiza a resolução de nomes para IP.
- DHCP (4) distribui IPs dinamicamente.
- ARP (1) mapeia IP para endereço MAC físico.
- ICMP (2) é usado para testes de conectividade e reporte de erros de entrega.
</details>

---

### Questão 18 (FCC - TRF 3ª Região - Analista)
Considere as portas lógicas TCP padrão utilizadas por diferentes servidores de aplicação na internet. A porta padrão do protocolo de transferência de hipertexto seguro (HTTPS) e a porta padrão do servidor de nomes de domínio (DNS) são, respectivamente:
A) 80 e 53.
B) 443 e 53.
C) 443 e 80.
D) 22 e 25.
E) 80 e 110.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** 
- HTTPS ➔ **443** (TCP)
- DNS ➔ **53** (tipicamente UDP, podendo usar TCP para transferências de zona)
- HTTP comum utiliza a porta 80.
</details>

---

### Questão 19 (FCC - Sabesp - Analista)
A RFC 1918 define faixas de endereços IPv4 reservados para uso exclusivo em redes privadas (não roteáveis na internet pública). Qual dos seguintes endereços IPv4 pertence a uma dessas faixas privadas?
A) 192.169.10.1.
B) 172.31.254.10.
C) 10.256.0.1.
D) 127.0.0.1.
E) 224.0.0.1.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** As faixas privadas da RFC 1918 são:
- Classe A: `10.0.0.0` a `10.255.255.255`
- Classe B: `172.16.0.0` a `172.31.255.255`
- Classe C: `192.168.0.0` a `192.168.255.255`
O IP `172.31.254.10` está contido na faixa de classe B privada.
</details>

---

### Questão 20 (FCC - PGE-CE - Analista de Sistemas)
No endereçamento IPv6, os endereços possuem um comprimento de bits e um formato de representação composto por grupos hexadecimais separados por dois-pontos. Esse tamanho de endereço em bits e a quantidade máxima de grupos hexadecimais são, respectivamente:
A) 64 bits e 8 grupos.
B) 128 bits e 8 grupos.
C) 128 bits e 16 grupos.
D) 256 bits e 8 grupos.
E) 64 bits e 4 grupos.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O IPv6 utiliza endereços de **128 bits** divididos em **8 grupos** de 16 bits cada (hextetos), representados por caracteres hexadecimais separados por dois-pontos (ex: `2001:db8:0:0:0:0:2:1`).
</details>

---

### Questão 21 (FCC - Sabesp - TI)
Uma das principais diferenças funcionais no envio de dados no protocolo IPv6 em relação ao IPv4 é a eliminação completa do tipo de transmissão por:
A) Unicast.
B) Multicast.
C) Broadcast.
D) Anycast.
E) Point-to-Point.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O IPv6 **não utiliza transmissões por Broadcast**. No lugar, ele implementa transmissões por Multicast especializadas (como o endereço multicast de nó solicitado), o que otimiza o uso do meio físico evitando interrupções em hosts que não devem receber o pacote.
</details>

---

### Questão 22 (FCC - TRT 15ª Região - Analista)
Considere a simplificação de escrita de endereços IPv6 de acordo com a RFC 5952. O endereço original `2001:0db8:0000:0000:0000:ff00:0042:8329` pode ser simplificado de forma correta e minimal para:
A) `2001:db8::ff00:42:8329`
B) `2001:0db8::ff::42:8329`
C) `2001:db8:0:0:0:ff00:42:8329`
D) `2001:db8::ff00:0042:8329`
E) `2001:db8:::ff00:42:8329`

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** Regras de simplificação:
1. Remover zeros à esquerda de cada grupo: `2001:0db8` vira `2001:db8` e `0042` vira `42`.
2. Substituir a maior sequência contígua de grupos zerados por dois-pontos duplos `::`. Isso só pode ser feito **uma única vez** no endereço.
Resultado: `2001:db8::ff00:42:8329`.
</details>

---

### Questão 23 (FCC - TRT 20ª Região - Analista Judiciário)
Um administrador de rede configurou um servidor com o endereço IP `192.168.10.75` e a máscara de sub-rede `/26` (notação CIDR). O endereço lógico de rede (Network Address) e o endereço de Broadcast desta sub-rede específica são, respectivamente:
A) `192.168.10.0` e `192.168.10.255`
B) `192.168.10.64` e `192.168.10.127`
C) `192.168.10.64` e `192.168.10.128`
D) `192.168.10.32` e `192.168.10.95`
E) `192.168.10.0` e `192.168.10.63`

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** 
- A máscara `/26` divide a rede em sub-redes com blocos de $2^{32-26} = 2^6 = 64$ endereços cada.
- Sub-redes possíveis:
  - Sub-rede 0: `0` a `63`
  - Sub-rede 1: `64` a `127` (O IP `75` está nesta faixa)
  - Sub-rede 2: `128` a `191`...
- Para a sub-rede que contém o IP `75`:
  - Endereço de Rede (primeiro do bloco): `192.168.10.64`
  - Endereço de Broadcast (último do bloco): `192.168.10.127`
</details>

---

### Questão 24 (FCC - TRT 6ª Região - TI)
Uma sub-rede com máscara de rede `/29` permite configurar, no máximo, quantos endereços IP utilizáveis para hosts físicos conectados na rede local?
A) 8.
B) 6.
C) 14.
D) 30.
E) 2.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O total de IPs em um bloco `/29` é $2^{32-29} = 2^3 = 8$. Como devemos descontar obrigatoriamente 2 endereços (o de rede e o de broadcast), restam $8 - 2 = 6$ endereços utilizáveis para hosts.
</details>

---

### Questão 25 (FCC - ARTESP - Especialista)
Deseja-se dividir a rede `10.0.0.0/24` em 4 sub-redes de tamanho idêntico. A nova máscara CIDR de sub-rede que deve ser aplicada e a quantidade de hosts utilizáveis por sub-rede resultante são, respectivamente:
A) `/26` e 62 hosts.
B) `/28` e 14 hosts.
C) `/26` e 64 hosts.
D) `/25` e 126 hosts.
E) `/27` e 30 hosts.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** Para criar 4 sub-redes ($2^2$), precisamos tomar emprestados 2 bits da máscara original `/24`. A nova máscara será `/24 + 2 = /26`.
- Cada bloco terá $2^{32-26} = 2^6 = 64$ endereços.
- Descontando os endereços de rede e broadcast, temos $64 - 2 = 62$ hosts utilizáveis por sub-rede.
</details>

---

### Questão 26 (FCC - MPE-RS - Analista)
O protocolo TCP garante a entrega ordenada e confiável dos dados na rede. Qual mecanismo de controle é utilizado pelo transmissor para enviar múltiplos segmentos antes de receber uma confirmação (ACK), ajustando dinamicamente o fluxo com base na capacidade informada pelo receptor?
A) Handshake de 3 vias.
B) Janela Deslizante (Sliding Window).
C) Algoritmo de Dijkstra.
D) Timeout de Retransmissão Fixo.
E) Controle de Acesso ao Meio Físico CSMA/CA.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O mecanismo de **Janela Deslizante** permite ao TCP controlar o fluxo de dados, evitando que o transmissor sobrecarregue o buffer do receptor (Flow Control). O receptor envia o tamanho da janela livre no cabeçalho do ACK.
</details>

---

### Questão 27 (FCC - TRF 3ª Região - Analista)
Em uma infraestrutura de rede corporativa, o protocolo responsável por converter dinamicamente os pacotes com IPs privados internos para um IP público válido na internet no momento em que saem pelo roteador de borda é o:
A) DHCP.
B) DNS.
C) NAT (Network Address Translation).
D) OSPF.
E) ARP.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O **NAT** traduz endereços de IPs privados locais em endereços IPs públicos globais válidos para tráfego na internet, economizando escassos IPs IPv4 públicos.
</details>

---

### Questão 28 (FCC - Sabesp - TI)
Durante o processo de resolução de nomes realizado pelo sistema de DNS, quando o servidor DNS local da instituição não conhece o IP correspondente ao endereço digitado e realiza consultas sucessivas a outros servidores externos (como Root Servers, TLD Servers e Autoridade do domínio) repassando o resultado intermediário, a consulta é denominada:
A) Consulta Recursiva.
B) Consulta Iterativa.
C) Consulta Direta Cacheada.
D) Resolução Reversa Invertida.
E) Requisição de Zona Estática.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Na consulta **Iterativa**, o servidor consultado não resolve ele mesmo, mas indica para qual servidor o cliente DNS local deve perguntar a seguir. O servidor local gerencia o processo. (Na recursiva, o servidor consultado assume a responsabilidade de obter a resposta final e entregá-la ao cliente).
</details>

---

### Questão 29 (FCC - TRT 9ª Região - Tecnologia da Informação)
O comando do sistema operacional Windows ou Linux que utiliza o envio de mensagens do protocolo ICMP do tipo *Echo Request* para verificar se um determinado host remoto está ativo e respondendo na rede é o:
A) ipconfig.
B) ping.
C) nslookup.
D) netstat.
E) route.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O comando **ping** envia pacotes ICMP *Echo Request* (Tipo 8) e aguarda respostas do tipo ICMP *Echo Reply* (Tipo 0) do host destino para medir latência e perda de pacotes.
</details>

---

### Questão 30 (FCC - TRT 15ª Região - Analista)
Uma empresa recebeu a faixa IP `192.168.1.0/24`. O administrador dividiu a rede de modo a obter sub-redes com máscara `255.255.255.240`. O número total de sub-redes criadas e a máscara em notação CIDR correspondente são:
A) 8 sub-redes e `/27`
B) 16 sub-redes e `/28`
C) 32 sub-redes e `/29`
D) 4 sub-redes e `/26`
E) 16 sub-redes e `/27`

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** 
- A máscara `255.255.255.240` possui no último octeto o valor binário `11110000` ($128+64+32+16=240$).
- Logo, a máscara CIDR possui $24 + 4 = 28$ bits ativos (`/28`).
- Como a rede original era `/24` e agora é `/28`, foram usados 4 bits adicionais para sub-redes, totalizando $2^4 = 16$ sub-redes.
</details>

---

## 📝 TEMA 3: Raciocínio Lógico-Matemático — Estruturas Lógicas (Proposições e Conectivos)

### Questão 31 (FCC - TRT 23ª Região - Analista - TI)
De acordo com os princípios da lógica matemática proposicional clássica, qual das seguintes sentenças representa uma proposição lógica?
A) Que dia maravilhoso para fazer provas de tribunal!
B) O processo eletrônico do TJ-CE será atualizado amanhã?
C) Desenvolva o código do módulo de segurança imediatamente.
D) O número 101 é um número primo.
E) Ele é um excelente analista de sistemas de informação.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** Uma proposição lógica deve ser uma sentença declarativa, afirmativa, de sentido completo, que possa ser classificada de forma única como Verdadeira (V) ou Falsa (F).
- A é exclamativa.
- B é interrogativa.
- C é imperativa (ordem).
- E possui sujeito indefinido ("Ele"), sendo uma sentença aberta (não proposição).
- D é uma declaração matemática completa e fechada (pode ser valorada como F ou V).
</details>

---

### Questão 32 (FCC - TRT 14ª Região - Analista)
Considere a proposição composta: *"Se o servidor de banco de dados cair ou a rede física ficar lenta, então o sistema de processos ficará fora do ar."*
Identifique os conectivos lógicos presentes nessa proposição composta na ordem de leitura:
A) Conjunção, Condicional.
B) Disjunção Inclusiva, Condicional.
C) Disjunção Exclusiva, Bicondicional.
D) Conjunção, Bicondicional.
E) Disjunção Inclusiva, Conjunção.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** 
- *"ou"* representa a **Disjunção Inclusiva** ($\lor$).
- *"Se... então"* representa o conectivo **Condicional** ($\rightarrow$).
</details>

---

### Questão 33 (FCC - TRF 3ª Região - Analista Judiciário)
Dadas as proposições simples:
- $p$: O switch está configurado.
- $q$: A rede está ativa.

A tradução para a linguagem simbólica matemática da sentença *"O switch não está configurado e a rede está ativa"* é dada por:
A) $p \land q$
B) $\sim p \lor q$
C) $\sim p \land q$
D) $p \rightarrow \sim q$
E) $\sim(p \land q)$

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** 
- *"não está configurado"* ➔ $\sim p$ (negação)
- *"e"* ➔ $\land$ (conjunção)
- *"a rede está ativa"* ➔ $q$
Resultado: $\sim p \land q$.
</details>

---

### Questão 34 (FCC - Sabesp - Analista)
Na lógica proposicional clássica, a conjunção de duas proposições quaisquer, $A \land B$, é valorada como Verdadeira (V) somente quando:
A) Pelo menos uma das proposições simples for Verdadeira.
B) Ambas as proposições simples forem Falsas.
C) Ambas as proposições simples forem Verdadeiras.
D) A proposição $A$ for Verdadeira e a proposição $B$ for Falsa.
E) A proposição $A$ for Falsa, independente do valor de $B$.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A tabela-verdade do conectivo "E" (conjunção $\land$) exige que **todas** as proposições envolvidas sejam Verdadeiras para que a sentença total resulte em Verdadeiro.
</details>

---

### Questão 35 (FCC - Assembleia Legislativa - PB)
A proposição composta do tipo Condicional, representado simbolicamente por $p \rightarrow q$ ("Se $p$, então $q$"), assume valor lógico Falso (F) em uma única linha de sua tabela-verdade. Essa situação ocorre quando:
A) $p$ é Falso e $q$ é Verdadeiro.
B) $p$ é Verdadeiro e $q$ é Falso.
C) Tanto $p$ quanto $q$ são Verdadeiros.
D) Tanto $p$ quanto $q$ são Falsos.
E) O valor lógico de $q$ for o dobro do valor lógico de $p$.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O conectivo condicional ($\rightarrow$) só é falso na situação clássica apelidada de "Vera Fischer" (Antecedente Verdadeiro $\rightarrow$ Consequente Falso). Nas demais combinações (V$\rightarrow$V, F$\rightarrow$V, F$\rightarrow$F), a condicional é Verdadeira.
</details>

---

### Questão 36 (FCC - PGE-CE - Analista)
Considere a proposição composta: *"Carlos é programador ou Ana é analista de testes, mas não ambos."* O conectivo lógico que representa esta estrutura gramatical é denominado:
A) Disjunção Inclusiva.
B) Disjunção Exclusiva (ou...ou).
C) Conjunção Condicional.
D) Bicondicional (se e somente se).
E) Negação da Conjunção.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A expressão *"ou um ou outro, mas não ambos"* define a **Disjunção Exclusiva** (símbolo $\underline{\lor}$ ou $\oplus$), onde a proposição composta só é verdadeira se as proposições simples tiverem valores lógicos opostos.
</details>

---

### Questão 37 (FCC - TRT 15ª Região - Analista)
Qual a valoração lógica da proposição composta dada pela sentença: *"Se $3 + 2 = 7$, então $5 \times 2 = 10$"?*
A) Falsa, pois a premissa inicial ($3+2=7$) é matematicamente incorreta.
B) Verdadeira, pois o consequente ($5\times2=10$) é verdadeiro, e uma condicional com antecedente falso é sempre verdadeira.
C) Invalida, pois não é possível associar lógica clássica a fórmulas da aritmética básica.
D) Falsa, porque a conjunção de equações aritméticas resulta em nulo.
E) Indeterminada, dependendo do referencial numérico adotado.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** 
- Antecedente: $3 + 2 = 7$ (Falso).
- Consequente: $5 \times 2 = 10$ (Verdadeiro).
- Tabela-verdade da condicional: F $\rightarrow$ V resulta em **Verdadero** (V).
</details>

---

### Questão 38 (FCC - TRT 6ª Região - TI)
A tabela-verdade do conectivo **Bicondicional** ($p \leftrightarrow q$, "se e somente se") é caracterizada por ser Verdadeira somente quando:
A) O antecedente $p$ for falso e o consequente $q$ for verdadeiro.
B) Pelo menos uma das proposições for verdadeira.
C) Ambas as proposições simples tiverem o mesmo valor lógico (ambas V ou ambas F).
D) As proposições simples apresentarem valorações lógicas alternadas e contrárias.
E) Nenhuma das proposições simples possuir valor definido.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O conectivo bicondicional determina que a equivalência lógica é verdadeira se e somente se ambas as partes compartilham da mesma verdade ou da mesma falsidade (V$\leftrightarrow$V = V; F$\leftrightarrow$F = V).
</details>

---

### Questão 39 (FCC - ARTESP - Especialista)
Sabendo que a proposição simples $A$ é Verdadeira e que a proposição $B$ é Falsa, assinale a alternativa que apresenta uma proposição composta de valor lógico Falso:
A) $A \lor B$
B) $\sim B \rightarrow A$
C) $A \leftrightarrow \sim B$
D) $A \land B$
E) $\sim(A \land B)$

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** 
- A) V $\lor$ F = V.
- B) V $\rightarrow$ V = V.
- C) V $\leftrightarrow$ V = V.
- D) V $\land$ F = **F** (Gabarito).
- E) $\sim$(F) = V.
</details>

---

### Questão 40 (FCC - MPE-RS - Analista)
Quantas linhas possui a tabela-verdade completa de uma proposição composta que contém 4 proposições simples independentes (ex: $p, q, r, s$)?
A) 8.
B) 16.
C) 4.
D) 32.
E) 12.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O número de linhas da tabela-verdade de uma proposição composta contendo $n$ proposições simples é dado pela fórmula matemática $2^n$. Como temos 4 proposições simples, temos $2^4 = 16$ linhas.
</details>

---

### Questão 41 (FCC - TRT 20ª Região - TI)
A sentença *"Se João estuda engenharia de software, então ele sabe codificar em Java"* possui como antecedente e consequente, respectivamente:
A) João estuda engenharia de software / ele sabe codificar em Java.
B) João sabe codificar em Java / ele estuda engenharia de software.
C) João estuda / ele sabe codificar.
D) Se João / então ele sabe.
E) Não existem antecedente e consequente em proposições condicionais.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** Na condicional $p \rightarrow q$:
- A cláusula que vem após o "Se" ($p$) é o **antecedente** (premissa).
- A cláusula que vem após o "então" ($q$) é o **consequente** (conclusão).
</details>

---

### Questão 42 (FCC - Sabesp - Analista de Sistemas)
A negação lógica de uma proposição simples $P$ (representada por $\sim P$) tem como propriedade fundamental:
A) Manter o valor lógico original da proposição em qualquer cenário.
B) Inverter o valor lógico da proposição (se $P$ é V, $\sim P$ é F; se $P$ é F, $\sim P$ é V).
C) Transformar a frase em uma pergunta.
D) Anular a estrutura da sentença proposicional, convertendo-a em sentença aberta.
E) Multiplicar a quantidade de proposições por dois.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A negação ($\sim$ ou $\neg$) é um operador unário que altera a valoração lógica de uma proposição para o seu exato oposto no sistema binário clássico (Princípio do Terceiro Excluído).
</details>

---

### Questão 43 (FCC - TRT 9ª Região - TI)
Considere a seguinte frase em linguagem natural: *"Não é verdade que Lucas é administrador e Mariana não é engenheira."*
Representando por $p$ a proposição "Lucas é administrador" e por $q$ "Mariana é engenheira", a tradução simbólica correta dessa frase é:
A) $\sim(p \land q)$
B) $\sim p \land \sim q$
C) $\sim(p \land \sim q)$
D) $\sim p \rightarrow q$
E) $\sim(p \lor \sim q)$

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** 
- *"Lucas é administrador"* ➔ $p$
- *"Mariana não é engenheira"* ➔ $\sim q$
- *"Lucas é administrador e Mariana não é engenheira"* ➔ $p \land \sim q$
- *"Não é verdade que..."* nega a conjunção inteira ➔ $\sim(p \land \sim q)$.
</details>

---

### Questão 44 (FCC - TRT 15ª Região - Analista)
Na lógica de proposições, qual conectivo possui precedência de resolução padrão mais alta em expressões lógicas complexas sem parênteses?
A) Condicional ($\rightarrow$).
B) Bicondicional ($\leftrightarrow$).
C) Disjunção ($\lor$).
D) Negação ($\sim$).
E) Conjunção ($\land$).

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** A ordem de precedência padrão dos operadores lógicos na ausência de parênteses delimitadores é:
1. **Negação** ($\sim$)
2. **Conjunção** ($\land$) e **Disjunção** ($\lor$) (resolvidas da esquerda para a direita)
3. **Condicional** ($\rightarrow$)
4. **Bicondicional** ($\leftrightarrow$)
</details>

---

### Questão 45 (FCC - Sabesp - TI)
Qual das seguintes alternativas não constitui uma proposição válida da lógica bivalente clássica?
A) O Sol é uma estrela de nêutrons fria.
B) Todos os computadores do tribunal possuem Linux instalado.
C) Que Deus te acompanhe nesta jornada de estudos!
D) O número 2 é o único número primo que é par.
E) A capital do estado do Ceará é a cidade de Fortaleza.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A alternativa C expressa um desejo, uma bênção/exclamação (sentença optativa/exclamativa). Sentenças desse tipo não possuem caráter declarativo e não podem ser avaliadas como V ou F, logo, não são proposições.
</details>
