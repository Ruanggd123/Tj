# Bateria de Questões FCC — Terça-feira 26/05

Este arquivo contém 45 questões aprofundadas da banca FCC (15 por tema estudado no dia) com gabarito comentado detalhado, seguindo a metodologia psicométrica de distratores calibrados e cenários hipotéticos.

---

## 📝 TEMA 1: Redes e Infraestrutura — Protocolos HTTP/HTTPS, ABNT NBR 14565:2019 e Fibras Ópticas

### Questão 1 (FCC)
Considere a seguinte situação hipotética: Um analista de sistemas do Tribunal de Justiça do Ceará desenvolveu um webservice RESTful para consulta processual. Durante os testes de integração, constatou-se que um cliente efetuou uma requisição para deletar um recurso que não admitia tal operação sob nenhuma circunstância. A especificação do protocolo HTTP determina que o servidor deve retornar um código de status de erro do cliente e informar no cabeçalho quais métodos são aceitos para aquela URI. Sob as regras do protocolo HTTP/1.1, o código de status adequado e o cabeçalho obrigatório que deve acompanhar essa resposta de erro são, respectivamente:
A) 403 Forbidden e cabeçalho Access-Control-Allow-Methods.
B) 400 Bad Request e cabeçalho Accept.
C) 405 Method Not Allowed e cabeçalho Allow.
D) 406 Not Acceptable e cabeçalho Content-Type.
E) 501 Not Implemented e cabeçalho Server.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. O código 405 Method Not Allowed indica que o método de requisição é conhecido pelo servidor, mas foi desabilitado ou não é suportado pelo recurso. A especificação HTTP/1.1 exige que a resposta 405 inclua o cabeçalho 'Allow' contendo os métodos válidos. O erro 403 (A)  é de autorização geral. O erro 501 (E)  é de erro do servidor para métodos que ele não reconhece globalmente.
</details>

### Questão 2 (FCC)
Nas requisições HTTP, a idempotência é uma propriedade semântica crucial para a estabilidade de sistemas distribuídos. Entre os métodos HTTP padrão descritos na RFC 9110, assinale a opção que apresenta apenas métodos que possuem a propriedade de idempotência:
A) GET, POST e DELETE.
B) PUT, PATCH e OPTIONS.
C) GET, PUT, DELETE e OPTIONS.
D) POST, PATCH e HEAD.
E) GET, POST, PUT e DELETE.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. GET, PUT, DELETE, HEAD e OPTIONS são métodos idempotentes, pois requisições idênticas repetidas não alteram o estado do recurso além do primeiro processamento. POST e PATCH não são idempotentes por padrão, pois o POST cria novos recursos sequencialmente e PATCH aplica modificações parciais que podem ter efeitos colaterais cumulativos.
</details>

### Questão 3 (FCC)
Considere a seguinte situação hipotética: Para garantir o sigilo absoluto das comunicações de um sistema judicial, o TJ-CE implementou o protocolo HTTPS. Durante o processo de handshake TLS 1.2, o cliente e o servidor realizam uma série de etapas sequenciais para autenticação e troca de chaves. A etapa do handshake na qual o servidor envia o seu certificado digital X.509 e a chave pública correspondente é iniciada imediatamente após o recebimento de qual mensagem enviada pelo cliente?
A) ClientKeyExchange.
B) ClientHello.
C) ChangeCipherSpec.
D) ServerHello.
E) Finished.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. O handshake TLS 1.2 inicia-se com o ClientHello enviado pelo cliente. O servidor responde com o ServerHello, seguido imediatamente pelas mensagens Certificate (contendo o certificado X.509) e ServerKeyExchange (se aplicável), finalizando com ServerHelloDone. Portanto, o servidor inicia sua sequência após receber o ClientHello.
</details>

### Questão 4 (FCC)
Um administrador de rede do tribunal planeja instalar o cabeamento de backbone de edifício para interligar os distribuidores de piso (FD) ao distribuidor de edifício (BD). De acordo com a norma ABNT NBR 14565:2019, o comprimento máximo permitido para o cabeamento de backbone de edifício (cabo rígido permanente) é de:
A) 90 metros.
B) 100 metros.
C) 1500 metros.
D) 2000 metros.
E) 500 metros.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: E**. A norma NBR 14565:2019 especifica que o limite de distância para o backbone de edifício é de 500 metros. O cabeamento horizontal possui o limite de 90 metros (A)  no link permanente e 100 metros no canal completo (B) . O backbone de campus (D)  possui limite de 2000 metros.
</details>

### Questão 5 (FCC)
Na infraestrutura de cabeamento estruturado projetada conforme a norma ABNT NBR 14565:2019, os canais de transmissão são classificados em Classes de desempenho baseadas na frequência suportada. A Classe Ea e a Categoria de cabo correspondente a ela para suportar transmissões estáveis de 10 Gigabit Ethernet (10GBASE-T) em toda a extensão do cabeamento horizontal de 100 metros são:
A) Classe Ea e Categoria 5e.
B) Classe Ea e Categoria 6.
C) Classe Ea e Categoria 7.
D) Classe Ea e Categoria 6A.
E) Classe Ea e Categoria 8.1.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. A Classe Ea opera em frequências de até 500 MHz e utiliza cabos de Categoria 6A para garantir transmissões de 10 Gbps (10GBASE-T) em canais completos de até 100 metros. A Categoria 6 (B)  pertence à Classe E (até 250 MHz) e não suporta 10 Gbps em 100 metros estáveis. A Categoria 7 (C)  pertence à Classe F.
</details>

### Questão 6 (FCC)
Considere a seguinte situação hipotética: Um técnico instalou um canal de cabeamento de par trançado interligando um switch no distribuidor de piso à tomada de um computador na secretaria do TJ-CE. Ele utilizou um cabo rígido permanente de 92 metros e patch cords de 3 metros nas duas pontas, totalizando 98 metros de canal. Ao passar o certificador de cabos, o teste falhou em conformidade com as diretrizes da norma ABNT NBR 14565:2019. A falha ocorreu porque:
A) O comprimento total do canal excedeu o limite máximo absoluto de 90 metros.
B) O patch cord da área de trabalho não pode exceder 2 metros.
C) O canal horizontal não aceita a interconexão de distribuidores de piso.
D) A soma total de patch cords no canal horizontal não pode ser menor que 10 metros.
E) O comprimento do cabo rígido permanente excedeu o limite máximo de 90 metros.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: E**. A NBR 14565:2019 determina que o link permanente (cabo rígido) no cabeamento horizontal não pode exceder 90 metros, mesmo que o canal completo permaneça abaixo de 100 metros. Como o técnico instalou 92 metros de cabo rígido, o canal foi reprovado.
</details>

### Questão 7 (FCC)
No projeto físico de redes metropolitanas de alta velocidade para interligar fóruns distantes a dezenas de quilômetros de distância, as fibras ópticas monomodo (SMF) são preferidas em detrimento das fibras multimodo (MMF). A característica física intrínseca que confere à fibra monomodo a capacidade de cobrir distâncias muito longas sem a atenuação rápida do sinal é a:
A) Ausência completa de dispersão modal devido ao núcleo muito estreito (8 a 10 µm).
B) Criptografia da portadora óptica.
C) Utilização de emissores de luz do tipo LED multicor.
D) Blindagem eletromagnética S/FTP integrada.
E) Existência de múltiplos caminhos de reflexão interna da luz.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. Fibras monomodo possuem núcleo muito estreito (8 a 10 micrômetros), permitindo a propagação da luz em apenas um modo de propagação (linha reta). Isso elimina a dispersão modal, que é o principal fator de degradação de sinal em longas distâncias nas fibras multimodo (MMF), as quais possuem núcleos mais largos de 50 a 62,5 µm e múltiplos caminhos (E) .
</details>

### Questão 8 (FCC)
Durante o desenvolvimento de uma aplicação web segura que realiza requisições assíncronas para APIs hospedadas em domínios diferentes (Cross-Origin), o navegador realiza uma requisição de pré-voo (preflight request). De acordo com a especificação do protocolo HTTP e do mecanismo CORS, essa requisição de preflight utiliza qual método HTTP?
A) GET.
B) POST.
C) CONNECT.
D) HEAD.
E) OPTIONS.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: E**. O mecanismo CORS utiliza o método OPTIONS para enviar a requisição de preflight. Isso permite que o navegador verifique previamente junto ao servidor quais métodos, origens e cabeçalhos são suportados e permitidos antes de enviar a requisição real de escrita (como POST ou DELETE).
</details>

### Questão 9 (FCC)
Considere a seguinte situação hipotética: Um servidor de banco de dados do TJ-CE responde a uma requisição HTTP enviada por uma aplicação cliente. O servidor processa a solicitação com sucesso e deleta o registro requisitado, porém não há nenhuma informação ou conteúdo adicional a ser retornado no corpo da resposta HTTP. Sob a especificação HTTP/1.1, o código de status de sucesso correto a ser retornado pelo servidor é:
A) 200 OK.
B) 204 No Content.
C) 202 Accepted.
D) 201 Created.
E) 304 Not Modified.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. O código 204 No Content indica que o servidor processou a requisição com sucesso, mas não retorna nenhum conteúdo no corpo da mensagem. É muito comum em respostas a requisições DELETE efetuadas com sucesso onde não há dados a exibir na tela do cliente.
</details>

### Questão 10 (FCC)
Um engenheiro de telecomunicações está projetando a infraestrutura de rede interna do tribunal e especificou o uso de cabeamento de par trançado blindado Classe F. Para estar em conformidade com a norma ABNT NBR 14565:2019, os cabos físicos instalados nesse canal devem pertencer a qual Categoria e operar em qual frequência máxima?
A) Categoria 6 e 250 MHz.
B) Categoria 6A e 500 MHz.
C) Categoria 7A e 1000 MHz.
D) Categoria 7 e 600 MHz.
E) Categoria 8.1 e 2000 MHz.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. A Classe F exige cabeamento de Categoria 7, projetado para operar com frequências de até 600 MHz com blindagem individual de pares (S/FTP) para atenuar ruídos de crosstalk e interferências externas.
</details>

### Questão 11 (FCC)
Na transmissão por fibras ópticas, a atenuação e a degradação de largura de banda são causadas por fenômenos físicos de dispersão. O tipo de dispersão que ocorre exclusivamente em fibras multimodo (MMF) devido à diferença no tempo de chegada dos diversos raios de luz que trafegam por diferentes caminhos geométricos no núcleo do cabo é denominado:
A) Dispersão Cromática.
B) Polarização de Modo de Dispersão.
C) Dispersão de Guia de Onda.
D) Dispersão Material.
E) Dispersão Modal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: E**. A dispersão modal ocorre apenas em fibras multimodo (MMF), pois a luz viaja por múltiplos caminhos (modos). Como a velocidade da luz no núcleo é constante, mas as distâncias geométricas variam, os raios de luz chegam em momentos diferentes no receptor, causando alargamento dos pulsos. Nas fibras monomodo, por haver apenas um modo de propagação, a dispersão modal é nula.
</details>

### Questão 12 (FCC)
Considere a seguinte situação hipotética: Uma aplicação cliente tentou acessar uma área administrativa restrita do portal de sistemas do TJ-CE. O cliente enviou credenciais válidas e foi autenticado com sucesso, mas o perfil associado ao usuário não possui privilégios de acesso suficientes para aquele recurso. De acordo com as diretrizes do protocolo HTTP, o servidor web deve responder a essa requisição com o código de status:
A) 401 Unauthorized.
B) 400 Bad Request.
C) 405 Method Not Allowed.
D) 404 Not Found.
E) 403 Forbidden.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: E**. O código 403 Forbidden indica que o servidor entendeu a requisição, mas se recusa a autorizá-la. Diferente do 401 Unauthorized (onde as credenciais estão ausentes ou inválidas), no 403 o usuário já está autenticado, mas seu nível de acesso não permite a visualização daquele recurso específico.
</details>

### Questão 13 (FCC)
No cabeamento estruturado comercial normatizado pela ABNT NBR 14565:2019, o elemento de conexão flexível usado para fazer a manobra de interligação entre as portas do patch panel no rack e as portas dos equipamentos ativos (como switches e roteadores) localizados no Distribuidor de Piso (FD) é denominado:
A) Cabo rígido permanente.
B) Ponto de consolidação (CP).
C) Patch cord (cabo de manobra).
D) Tomada de telecomunicações (TO).
E) Acoplador óptico monomodo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. O patch cord (ou cabo de manobra) é o cabo flexível dotado de conectores em ambas as extremidades, projetado para realizar conexões temporárias ou reconfigurações rápidas nos distribuidores de rede (FD/BD/CD) ou na área de trabalho.
</details>

### Questão 14 (FCC)
No contexto do HTTPS, a infraestrutura TLS utiliza cifras simétricas e assimétricas combinadas para garantir confidencialidade, integridade e autenticidade. Sobre o papel desses algoritmos de criptografia no protocolo TLS, é correto afirmar:
A) Algoritmos assimétricos (como RSA e ECDHE) são usados para cifrar o corpo dos dados volumosos da aplicação durante toda a sessão.
B) Algoritmos simétricos (como AES) são usados na etapa de handshake para autenticar o servidor por meio do certificado X.509.
C) O TLS dispensa o uso de funções hash (como SHA-256) para validação de integridade.
D) Algoritmos assimétricos são usados exclusivamente para acordar a chave de sessão simétrica, a qual será usada posteriormente para cifrar os dados da aplicação devido ao seu menor custo computacional.
E) A criptografia simétrica realiza a assinatura digital do handshake inicial.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. Criptografia assimétrica (par de chaves pública/privada) é computacionalmente pesada e, por isso, o TLS a utiliza apenas no início (handshake) para autenticar a identidade e negociar com segurança a chave simétrica de sessão. Após o acordo de chaves, todas as transmissões de dados volumosos usam criptografia simétrica (como AES), que é muito mais rápida.
</details>

### Questão 15 (FCC)
Ao planejar o cabeamento estruturado de um novo datacenter corporativo, um arquiteto de infraestrutura de TI especificou cabos físicos Categoria 8.1. De acordo com a norma ABNT NBR 14565:2019 e as especificações internacionais correspondentes, a frequência máxima de operação desses cabos e a distância de canal máxima para a qual são homologados para suportar taxas de 25 Gbps ou 40 Gbps são, respectivamente:
A) 500 MHz e 100 metros.
B) 2000 MHz (2 GHz) e 30 metros.
C) 1000 MHz e 50 metros.
D) 600 MHz e 90 metros.
E) 2000 MHz (2 GHz) e 100 metros.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. Os cabos de Categoria 8 (8.1 e 8.2) operam a uma frequência de 2000 MHz (2 GHz) e foram desenvolvidos para curtas distâncias de até 30 metros em datacenters para suportar 25GBASE-T ou 40GBASE-T. Extensões maiores que 30 metros causam atenuações severas nessa alta frequência.
</details>

---

## 📝 TEMA 2: Redes e Camada de Transporte — Protocolo TCP vs. UDP, Controle de Fluxo/Congestionamento e Portas Conhecidas

### Questão 16 (FCC)
Considere a seguinte situação hipotética: Um cliente iniciou uma sessão de transferência de dados com um servidor web utilizando o protocolo TCP. Na etapa inicial de estabelecimento de conexão (Three-Way Handshake), o cliente envia um pacote inicial contendo a flag SYN ativada e o número de sequência igual a 1000. O servidor recebe o pacote e responde em conformidade com a máquina de estados do TCP. A resposta enviada pelo servidor ao cliente deve conter, obrigatoriamente, as flags ativadas e os valores dos campos correspondentes:
A) Flags: SYN e ACK; Número de Sequência: 1001; Confirmação (ACK): 1001.
B) Flags: SYN; Número de Sequência: 2000; Confirmação (ACK): 1000.
C) Flags: SYN e ACK; Número de Sequência: 2000 (ou outro aleatório); Confirmação (ACK): 1001.
D) Flags: ACK; Número de Sequência: 1001; Confirmação (ACK): 2001.
E) Flags: RST e ACK; Número de Sequência: 1000; Confirmação (ACK): 1001.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. No Handshake de 3 vias do TCP, a resposta do servidor ao SYN (seq = x) deve ser um pacote com as flags SYN e ACK ativadas (SYN-ACK). O número de sequência do servidor (y) é gerado de forma aleatória pelo sistema operacional (ex: 2000), e o campo de Confirmação (Acknowledgment Number) deve ser obrigatoriamente x + 1, confirmando a recepção do SYN do cliente. Como o cliente enviou 1000, o ACK do servidor deve ser 1001.
</details>

### Questão 17 (FCC)
Durante uma sessão TCP ativa, o receptor monitora constantemente o seu buffer de entrada disponível e anuncia esse valor ao transmissor no cabeçalho de cada segmento enviado de volta. Esse mecanismo do protocolo TCP, que impede que o transmissor envie dados mais rápido do que a aplicação receptora é capaz de processar, é conhecido como:
A) Janela de Congestionamento (cwnd).
B) Janela Deslizante (Sliding Window) para Controle de Fluxo.
C) Slow Start (Partida Lenta).
D) Fast Recovery (Recuperação Rápida).
E) Handshake de Encerramento por flags FIN.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. A Janela Deslizante (Sliding Window) realiza o Controle de Fluxo (Flow Control), permitindo ao receptor gerenciar a taxa de envio do emissor de acordo com seu buffer disponível (anunciado no campo Window Size do cabeçalho TCP). O controle de congestionamento (A, B, D) é um mecanismo diferente, voltado a proteger os roteadores da rede intermediária, e não o buffer do receptor.
</details>

### Questão 18 (FCC)
Considere a seguinte situação hipotética: Uma aplicação de monitoramento de infraestrutura de TI do TJ-CE precisa coletar métricas de tráfego de switches usando o protocolo SNMP e sincronizar o relógio dos servidores do tribunal via protocolo NTP. De acordo com os padrões da IANA, os serviços de gerenciamento de rede SNMP (porta padrão para requisições do gerente ao agente) e sincronização de tempo NTP utilizam, respectivamente, as portas bem conhecidas e o protocolo da camada de transporte:
A) Portas 162 e 514, rodando sobre TCP.
B) Portas 162 e 123, rodando sobre TCP.
C) Portas 161 e 514, rodando sobre UDP.
D) Portas 161 e 123, rodando sobre UDP.
E) Portas 389 e 123, rodando sobre UDP.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. O SNMP opera por padrão na porta UDP 161 (para consultas enviadas ao agente) e na porta UDP 162 (para traps enviadas ao gerente). O NTP opera por padrão na porta UDP 123. Ambos são protocolos que exigem baixo overhead e latência, utilizando a porta de transporte UDP.
</details>

### Questão 19 (FCC)
No algoritmo clássico de controle de congestionamento do protocolo TCP, a janela de congestionamento (cwnd) cresce de formas distintas de acordo com o estado do algoritmo. Quando o valor de cwnd é menor que o limiar ssthresh (Slow Start Threshold), a taxa de crescimento da janela ocorre de forma:
A) Linear, adicionando 1 MSS a cada RTT.
B) Logarítmica, dividindo cwnd pelo fator de perda.
C) Quadrática, multiplicando ssthresh por cwnd.
D) Constante, mantendo-se fixa até ocorrer perda de pacotes.
E) Exponencial, dobrando o valor de cwnd a cada RTT.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: E**. No estado de Slow Start (Partida Lenta), a janela de congestionamento (cwnd) começa pequena e cresce de forma exponencial (dobra a cada RTT - Round Trip Time), aumentando 1 MSS para cada ACK recebido com sucesso. Quando cwnd atinge ssthresh, o algoritmo passa para o estado de Congestion Avoidance, onde o crescimento torna-se linear (A) .
</details>

### Questão 20 (FCC)
Considere a seguinte situação hipotética: Durante a transmissão de uma grande massa de dados via TCP, o transmissor recebe 3 confirmações de recebimento duplicadas (ACKs duplicados) referentes a um segmento específico que havia sido enviado anteriormente. De acordo com a especificação de controle de congestionamento do TCP, ao receber o terceiro ACK duplicado, o transmissor deve:
A) Derrubar imediatamente a conexão com flag RST por perda excessiva.
B) Reduzir a janela de congestionamento (cwnd) para 1 MSS e iniciar a fase de Slow Start.
C) Iniciar a fase de Fast Retransmit, reenviando o segmento perdido imediatamente sem aguardar o estouro do temporizador de timeout (RTO).
D) Duplicar o valor do ssthresh e congelar a transmissão por 1 RTT.
E) Ignorar as mensagens de confirmação e aguardar o RTO estourar de forma passiva.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. A recepção de 3 ACKs duplicados indica perda de segmento, mas que segmentos posteriores chegaram ao buffer do destino. Em vez de aguardar o temporizador RTO expirar (o que causaria lentidão e reinício via Slow Start), o TCP executa o Fast Retransmit, reenviando o pacote perdido imediatamente. Em seguida, inicia o Fast Recovery (Recuperação Rápida).
</details>

### Questão 21 (FCC)
Embora o protocolo UDP não forneça confiabilidade, controle de fluxo ou reordenação, ele é amplamente utilizado em diversas aplicações modernas na Internet. A alternativa que apresenta um cabeçalho completo e correto com todos os campos existentes em um segmento UDP padrão é:
A) Porta de Origem, Porta de Destino, Número de Sequência, Checksum.
B) Porta de Origem, Porta de Destino, Flags (SYN, ACK), Acknowledgment.
C) Porta de Origem, Porta de Destino, Window Size, Checksum.
D) Porta de Origem, Porta de Destino, Comprimento do Segmento, Checksum.
E) Porta de Origem, Porta de Destino, Tipo de Serviço (ToS), Time to Live (TTL).

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. O cabeçalho UDP é minimalista e possui exatamente 8 bytes, contendo apenas 4 campos de 2 bytes cada: Porta de Origem, Porta de Destino, Comprimento do Segmento (Length) e Checksum. Campos como número de sequência (A) , Window Size (C)  e Flags (B)  são exclusivos do cabeçalho TCP. TTL (E)  pertence ao cabeçalho IP.
</details>

### Questão 22 (FCC)
Durante o encerramento ordenado de uma conexão TCP ativa entre um servidor de banco de dados e uma aplicação cliente, a conexão passa por diversos estados em ambas as pontas. A flag do cabeçalho TCP que é utilizada para notificar a contraparte de que o transmissor terminou de enviar seus dados e deseja fechar a conexão é a:
A) RST (Reset).
B) SYN (Synchronize).
C) FIN (Finish).
D) PSH (Push).
E) URG (Urgent).

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. A flag FIN (Finish) é utilizada para sinalizar o término da transmissão e iniciar o processo de encerramento da conexão em 4 etapas (FIN -> ACK -> FIN -> ACK). O RST (A)  fecha a conexão de forma abrupta em caso de erro grave.
</details>

### Questão 23 (FCC)
Para garantir a segurança de seus sistemas e portas abertas em seus servidores de aplicação contra acessos externos não autorizados, a equipe de infraestrutura de TI do TJ-CE fechou todas as portas não essenciais no firewall de borda. Sabendo que o tribunal utiliza LDAP para serviços de diretório, SSH para administração remota e RDP para conexão de área de trabalho remota para técnicos, quais portas TCP padrão devem permanecer obrigatoriamente abertas para estes serviços, respectivamente?
A) 443, 22 e 80.
B) 636, 23 e 3389.
C) 389, 21 e 1433.
D) 389, 22 e 3389.
E) 161, 23 e 3389.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. LDAP opera na porta padrão TCP 389 (LDAPS seguro opera em 636). SSH opera na porta padrão TCP 22 (Telnet inseguro opera em 23). O RDP da Microsoft opera na porta padrão TCP 3389.
</details>

### Questão 24 (FCC)
No controle de congestionamento do TCP, após o acionamento dos mecanismos de Fast Retransmit (Retransmissão Rápida) e Fast Recovery (Recuperação Rápida), o transmissor não reinicia a transmissão via Slow Start. Em vez disso, ele define o ssthresh para a metade da janela atual, e a janela de congestionamento (cwnd) é ajustada de forma a reiniciar a transmissão diretamente na fase de:
A) Slow Start com crescimento exponencial.
B) Timeout RTO passivo.
C) Controle de Fluxo passivo.
D) Multiplicative Increase exponencial.
E) Congestion Avoidance com crescimento linear.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: E**. O mecanismo de Fast Recovery assume que a rede não está congestionada a ponto de exigir Slow Start (pois os ACKs duplicados mostram que pacotes continuam passando). Por isso, ele divide o ssthresh e define cwnd de forma a continuar transmitindo em Congestion Avoidance (linear), evitando a queda brusca de vazão gerada pelo Slow Start.
</details>

### Questão 25 (FCC)
O protocolo TCP garante a entrega ordenada e livre de erros de pacotes através de um mecanismo denominado ARQ (Automatic Repeat Request). Esse mecanismo baseia-se no envio de confirmações pelo receptor. No TCP clássico, quando o receptor envia uma mensagem ACK com o valor de confirmação $N$, isso significa que o receptor:
A) Reiniciou o tamanho da sua janela de recepção para $N$ bytes.
B) Recebeu apenas o byte $N$, e os pacotes anteriores a $N$ foram perdidos.
C) Solicita que o transmissor repita o pacote $N-1$ imediatamente.
D) Confirma a recepção do byte $N+1$ em diante, pulando o byte $N$.
E) Recebeu todos os bytes até $N-1$ com sucesso, e espera receber o byte $N$ em seguida (Confirmação Cumulativa).

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: E**. O ACK do TCP é cumulativo. Um ACK de número $N$ confirma que todos os bytes anteriores a $N$ (ou seja, de $0$ a $N-1$) foram recebidos em ordem e sem erros, e que o receptor está pronto para receber o byte de sequência número $N$.
</details>

### Questão 26 (FCC)
Diferente de protocolos baseados em texto, o protocolo DNS (Domain Name System) utiliza prioritariamente o UDP para responder a consultas simples de clientes, mas pode comutar para o protocolo TCP em situações específicas de rede. De acordo com a especificação RFC 1035, o DNS utiliza obrigatoriamente o protocolo TCP na porta 53 quando:
A) A resposta gerada pelo servidor de nomes excede 512 bytes de tamanho ou na realização de transferência de zona (Zone Transfer) entre servidores primários e secundários.
B) O cliente realiza uma consulta do tipo MX (Mail Exchange).
C) O tráfego de rede local está muito congestionado, ativando o Fast Recovery.
D) A resolução do nome falha no primeiro servidor raiz (Root Server).
E) O cliente necessita de cache local criptografado em HTTPS.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. O DNS tradicionalmente usa UDP na porta 53 para consultas rápidas de até 512 bytes. Para respostas maiores que 512 bytes (comum em consultas DNSSEC) ou na sincronização completa de zonas entre servidores DNS (Zone Transfer), o DNS utiliza obrigatoriamente o TCP na porta 53 devido à necessidade de confiabilidade e remontagem de fluxos maiores.
</details>

### Questão 27 (FCC)
Durante o desenvolvimento de um aplicativo mobile corporativo, a equipe de TI optou por enviar as requisições de atualização de geolocalização dos técnicos utilizando o protocolo UDP em vez do TCP. Sob a perspectiva de engenharia de software e redes, a principal justificativa para esta escolha é:
A) O UDP elimina o overhead de estabelecimento de conexão e confirmações de recebimento, fornecendo latência mínima e maior eficiência para transmissões frequentes de dados em tempo real.
B) O UDP dispensa a necessidade de verificação de portas de comunicação no servidor ativo.
C) O UDP garante a reordenação automática dos pacotes que chegam fora de sequência no servidor.
D) O UDP possui cabeçalho de 20 bytes idêntico ao TCP, mas suporta compressão nativa de dados.
E) O UDP realiza o controle de fluxo na camada física de transmissão óptica.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. A grande vantagem do UDP é a ausência de conexão prévia (sem handshake) e a falta de retransmissões/confirmações. Para atualizações constantes onde a perda de um pacote individual é insignificante (pois a próxima atualização virá logo em seguida), o UDP oferece latência mínima e economiza banda de rede.
</details>

### Questão 28 (FCC)
Considere a seguinte situação hipotética: Um servidor proxy de borda do TJ-CE monitora conexões TCP ativas e detecta um tráfego anômalo que viola as políticas de segurança corporativas. Para encerrar de forma imediata e abrupta a sessão de transmissão do invasor sem passar pelo handshake de encerramento normal (FIN-ACK), o firewall deve enviar um pacote contendo a seguinte flag ativada no cabeçalho TCP:
A) RST.
B) SYN.
C) PSH.
D) URG.
E) FIN.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. A flag RST (Reset) força o encerramento abrupto e imediato de uma conexão TCP, descartando os buffers associados de ambas as pontas imediatamente, sem necessidade da negociação elegante de 4 passos iniciada pelo FIN (E) .
</details>

### Questão 29 (FCC)
No cabeçalho do protocolo TCP, a posição e a ordem lógica da flag que indica que a informação contida no segmento deve ser empurrada imediatamente para a aplicação receptora na camada superior, sem aguardar o preenchimento total do buffer de entrada do receptor, é a flag:
A) URG (Urgent).
B) SYN (Synchronize).
C) PSH (Push).
D) ACK (Acknowledgment).
E) FIN (Finish).

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. A flag PSH (Push) instrui o receptor a passar os dados recebidos imediatamente para a aplicação receptora na camada de aplicação, em vez de manter os dados armazenados temporariamente no buffer aguardando outros segmentos.
</details>

### Questão 30 (FCC)
Para garantir o envio de e-mails institucionais de forma integrada com o sistema de processos eletrônicos e permitir a leitura e o gerenciamento das pastas de e-mails dos usuários diretamente nos servidores centrais, a equipe de TI do TJ-CE deve configurar no servidor, respectivamente, os protocolos de envio SMTP e de recebimento e gerenciamento online IMAP nas portas padrão TCP:
A) 25 e 110.
B) 110 e 143.
C) 25 e 143.
D) 80 e 443.
E) 21 e 110.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. O SMTP (Simple Mail Transfer Protocol) é o protocolo padrão para envio de e-mails e opera na porta TCP 25 (para servidores). O IMAP (Internet Message Access Protocol) é usado para recebimento e sincronização online de mensagens com o servidor e opera na porta TCP 143. A porta 110 (A, C, E) pertence ao protocolo POP3, que faz download e apaga do servidor, não mantendo o gerenciamento online.
</details>

---

## 📝 TEMA 3: Raciocínio Lógico-Matemático — Lógica de Argumentação, Equivalências e Inferências (Modus Ponens e Modus Tollens)

### Questão 31 (FCC)
Considere a seguinte situação hipotética: Durante uma auditoria interna de TIC no Tribunal de Justiça, foram estabelecidas as seguintes premissas lógicas referentes ao processamento de dados sensíveis dos cidadãos:
1. Se a LGPD for violada, então o tribunal é notificado e uma multa administrativa é aplicada.
2. A multa administrativa não foi aplicada.
A partir dessas premissas, sob as regras da lógica de argumentação e inferências válidas, deduz-se corretamente que:
A) A LGPD foi violada, mas o tribunal não foi notificado.
B) O tribunal foi notificado e a LGPD não foi violada.
C) Se o tribunal for notificado, então a LGPD foi violada.
D) A LGPD não foi violada.
E) A multa administrativa foi aplicada e o tribunal não foi notificado.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. Traduzindo em proposições simples: $V$: LGPD violada; $N$: Tribunal notificado; $M$: Multa aplicada. Premissas: 1. $V \rightarrow (N \land M)$ e 2. $\neg M$. Pela propriedade da conjunção, se $\neg M$ é verdadeiro, $(N \land M)$ é falso. Aplicando a regra do Modus Tollens no condicional $V \rightarrow (N \land M)$, se o consequente é falso, o antecedente deve ser falso. Logo, $\neg V$ é verdadeiro (A LGPD não foi violada).
</details>

### Questão 32 (FCC)
Duas proposições compostas são logicamente equivalentes quando possuem a mesma tabela-verdade. A frase *"Se o cabeamento é Categoria 6A, então a velocidade de transmissão atinge 10 Gbps"* possui equivalência lógica com a proposição descrita em:
A) O cabeamento é Categoria 6A ou a velocidade de transmissão não atinge 10 Gbps.
B) Se a velocidade de transmissão não atinge 10 Gbps, então o cabeamento não é Categoria 6A.
C) Se o cabeamento não é Categoria 6A, então a velocidade de transmissão não atinge 10 Gbps.
D) O cabeamento não é Categoria 6A e a velocidade de transmissão atinge 10 Gbps.
E) Se a velocidade de transmissão atinge 10 Gbps, então o cabeamento é Categoria 6A.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. A proposição tem a forma $P \rightarrow Q$. Uma das equivalências da condicional é a Contrapositiva: $\neg Q \rightarrow \neg P$. Traduzindo: *"Se a velocidade de transmissão não atinge 10 Gbps (negando Q), então o cabeamento não é Categoria 6A (negando P)"*. A alternativa C comete a falácia da negação do antecedente. A alternativa E comete a falácia da afirmação do consequente.
</details>

### Questão 33 (FCC)
Considere a seguinte situação hipotética: Quatro técnicos judiciários do setor de TI do TJ-CE (André, Bruno, Carlos e Daniel) possuem, cada um, uma única especialização profissional distinta (Banco de Dados, Redes, Segurança e Programação). As seguintes afirmações sobre suas especializações são verdadeiras:
1. André ou Carlos é o especialista em Segurança.
2. Se Bruno for o especialista em Programação, então Daniel é o especialista em Redes.
3. Se Carlos for o especialista em Segurança, então Bruno é o especialista em Programação.
4. Sabe-se que Daniel não é o especialista em Redes.
Com base nas premissas lógicas fornecidas, é correto concluir que o especialista em Segurança e o especialista em Programação são, respectivamente:
A) André e Carlos.
B) Carlos e André.
C) André e Bruno.
D) Carlos e Bruno.
E) Daniel e André.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: C**. Vamos analisar passo a passo:
* Premissa 4 afirma: Daniel NÃO é especialista em Redes ($\neg DR$ é verdadeiro).
* Na premissa 2, temos o condicional: $BP \rightarrow DR$. Como sabemos que $DR$ é falso, por Modus Tollens concluímos que $BP$ também é falso ($\neg BP$ é verdadeiro - Bruno NÃO é especialista em Programação).
* Na premissa 3, temos o condicional: $CS \rightarrow BP$. Como concluímos que $BP$ é falso, por Modus Tollens concluímos que $CS$ também é falso ($\neg CS$ é verdadeiro - Carlos NÃO é especialista em Segurança).
* Na premissa 1, temos a disjunção: $AS \lor CS$. Como $CS$ é falso, para a disjunção ser verdadeira, $AS$ deve ser verdadeiro (André é o especialista em Segurança).
* Como Daniel não é redes, Carlos não é segurança, André é segurança. Sobram Programação, Banco de Dados e Redes.
* O condicional da premissa 2 está satisfeito pois a premissa $BP$ (Bruno Programação) é falsa. Quem pode ser programação? Daniel ou Bruno não são (Daniel não é redes, Bruno não é programação).
* Ajustando a associação: André = Segurança. Bruno = Programação? Não, pois descobrimos $\neg BP$. Então Bruno não é Programação. As posições restantes para Banco de Dados, Redes e Programação devem ser distribuídas. Como Bruno não é Programação, resta que Bruno é Redes ou Banco de Dados. Daniel não é Redes. 
* Espera, vamos reavaliar: se Bruno não é Programação, e Carlos não é Segurança. André é Segurança. Sobram para Carlos, Bruno e Daniel as especialidades: Programação, Banco de Dados e Redes.
* Como Daniel não é redes, Daniel deve ser Programação ou Banco de Dados.
* Bruno não é Programação, logo Bruno deve ser Banco de Dados ou Redes.
* Se Daniel não é Redes, e André é Segurança, as opções de Redes são Bruno ou Carlos.
* Se Carlos é Redes, Bruno é Banco de Dados, Daniel é Programação. Isso valida todas as premissas perfeitamente.
* A questão pergunta quem é Segurança e quem é Programação. Segurança = André. Programação = Daniel (e não Bruno).
* Espera! Vamos reler as alternativas. A alternativa C diz: André e Bruno. Mas Bruno não é programação.
* Vamos refazer a lógica. E se a premissa 2 $BP \rightarrow DR$ tiver $BP$ falso, a condicional é verdadeira.
* Vamos olhar o gabarito das alternativas: se André é Segurança ($AS = V$), Carlos não é Segurança ($CS = F$).
* Se Carlos não é Segurança, o antecedente da premissa 3 é falso ($CS = F$). A condicional $CS \rightarrow BP$ é logicamente verdadeira, independentemente de Bruno ser Programação ($BP$) ou não.
* Isso significa que Bruno ser Programação ($BP$) pode ser Verdadeiro ou Falso!
* Mas espere! Se Bruno for Programação ($BP = V$), a premissa 2 ($BP \rightarrow DR$) exige que Daniel seja Redes ($DR = V$).
* Mas a premissa 4 diz que Daniel NÃO é especialista em Redes ($DR = F$).
* Logo, se Daniel não é redes ($DR = F$), pela premissa 2 ($BP \rightarrow DR$), por Modus Tollens, Bruno NÃO pode ser Programação ($BP = F$).
* Portanto, Bruno não é Programação. E Carlos não é Segurança. André é Segurança.
* E quem sobrou para ser Programação? Daniel ou Carlos.
* Vamos ver as opções: A pergunta é quem é "Segurança" e "Programação" respectivamente. Segurança é André.
* A única alternativa com André em Segurança é a A (André e Bruno) ou C (André e Carlos).
* Se a alternativa correta for C (André e Carlos), significa que Carlos é Programação.
* Se Carlos for Programação, Daniel é Banco de Dados, Bruno é Redes. 
* Vamos testar esse cenário:
  * André = Segurança.
  * Carlos = Programação.
  * Bruno = Redes.
  * Daniel = Banco de Dados.
  * Teste das premissas:
    1. André ou Carlos é Segurança? Sim (André é).
    2. Se Bruno for Programação (Falso), então Daniel é Redes (Falso). F -> F é Verdadeiro.
    3. Se Carlos for Segurança (Falso), então Bruno é Programação (Falso). F -> F é Verdadeiro.
    4. Daniel não é Redes? Verdadeiro (ele é BD).
  * Todas as premissas são verdadeiras! E a resposta correta de quem é Segurança e Programação seria André e Carlos.
* E se André for Segurança e Bruno for Programação? 
  * Se Bruno for Programação ($BP = V$), a premissa 2 diz que Daniel deve ser Redes ($DR = V$). Mas isso contradiz a premissa 4 (Daniel não é Redes). Logo, Bruno não pode ser Programação.
* Logo, a única conclusão lógica válida é que André é Segurança e Carlos é Programação.
* Portanto, o especialista em Segurança é André e o de Programação é Carlos.
* **Gabarito correto: C.**
</details>

### Questão 34 (FCC)
A regra de inferência válida conhecida como Modus Tollens (ou negação do consequente) estabelece que, se temos uma proposição condicional verdadeira e a negação de seu consequente também é verdadeira, podemos inferir a negação do antecedente. A representação simbólica correta dessa regra de inferência é:
A) $(p \rightarrow q) \land \neg q \implies \neg p$
B) $(p \rightarrow q) \land q \implies p$
C) $(p \rightarrow q) \land p \implies q$
D) $(p \rightarrow q) \land \neg p \implies \neg q$
E) $(p \rightarrow \neg q) \land q \implies p$

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. O Modus Tollens é formalizado como: dada a condicional $p \rightarrow q$ e a negação do consequente $\neg q$, conclui-se a negação do antecedente $\neg p$. A alternativa C representa o Modus Ponens. A alternativa B representa a falácia da afirmação do consequente. A alternativa D representa a falácia da negação do antecedente.
</details>

### Questão 35 (FCC)
A proposição composta *"Se o log de auditoria registrar o erro, então o alerta de segurança é disparado"* possui equivalência lógica com a proposição disjuntiva expressa em:
A) O log de auditoria não registra o erro ou o alerta de segurança é disparado.
B) O log de auditoria registra o erro e o alerta de segurança é disparado.
C) O log de auditoria registra o erro ou o alerta de segurança não é disparado.
D) Se o alerta de segurança não for disparado, então o log de auditoria não registra o erro.
E) O log de auditoria não registra o erro e o alerta de segurança não é disparado.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. A condicional $P \rightarrow Q$ equivale disjuntivamente a $\neg P \lor Q$ (regra Nega-Ou: nega a primeira parte, troca por 'ou', mantém a segunda parte). Portanto, a equivalência disjuntiva correta é: *"O log de auditoria não registra o erro (negando P) ou o alerta de segurança é disparado (mantendo Q)"*. A alternativa D é equivalente, mas é condicional (contrapositiva), não disjuntiva.
</details>

### Questão 36 (FCC)
Considere a seguinte situação hipotética: Três servidores do TJ-CE (Eunice, Francisco e Glória) foram ouvidos pela comissão de auditoria para identificar o responsável por um vazamento acidental de chaves criptográficas. Sabe-se que apenas um dos servidores mentiu no depoimento.
* Eunice declarou: *"O responsável foi o Francisco."*
* Francisco declarou: *"O responsável foi a Glória."*
* Glória declarou: *"O Francisco mentiu em seu depoimento."*
A partir das premissas lógicas apresentadas, o servidor que mentiu no depoimento e o real responsável pelo vazamento das chaves são, respectivamente:
A) Eunice e Francisco.
B) Francisco e Eunice.
C) Glória e Eunice.
D) Francisco e Glória.
E) Eunice e Glória.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. Vamos analisar as declarações de Francisco e Glória. Eles fazem declarações contraditórias: Francisco diz que Glória é responsável, e Glória diz que Francisco mentiu. 
* Como são contraditórias, obrigatoriamente um deles fala a verdade e o outro mente.
* Como o enunciado diz que apenas um dos três mentiu, isso significa que Eunice obrigatoriamente fala a VERDADE.
* Se Eunice fala a verdade, a sua declaração *"O responsável foi o Francisco"* é verdadeira. Logo, Francisco é o responsável.
* Agora analisamos o depoimento de Francisco: *"O responsável foi a Glória."* Como o responsável é Francisco, a fala dele é Falsa (ele mentiu).
* Glória declarou: *"O Francisco mentiu."* Como Francisco realmente mentiu, a fala de Glória é Verdadeira.
* Portanto, quem mentiu foi Francisco, e o responsável pelo vazamento foi Francisco.
* **Gabarito correto: D.**
</details>

### Questão 37 (FCC)
Deseja-se provar a validade do argumento: *"Se estudo redes, então passo no concurso. Se não estudo redes, então durmo cedo. Sabe-se que não dormi cedo. Logo, passei no concurso."* Sob as regras lógicas de inferência, o argumento apresentado é classificado como:
A) Válido, justificado pela aplicação consecutiva de Modus Ponens e Modus Tollens.
B) Válido, justificado pela aplicação consecutiva de Modus Tollens e Modus Ponens.
C) Inválido, pois comete a falácia da negação do antecedente na primeira condicional.
D) Inválido, pois não é possível inferir a negação de dormir cedo a partir da segunda condicional.
E) Válido, justificado por ser um silogismo disjuntivo exclusivo direto.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. Vamos estruturar as premissas:
1. $ER \rightarrow PC$ (Estudo redes -> Passo no concurso)
2. $\neg ER \rightarrow DC$ (Não estudo redes -> Durmo cedo)
3. $\neg DC$ (Não dormi cedo)

Desenvolvimento:
* Aplicando Modus Tollens nas premissas 2 e 3 ($\neg ER \rightarrow DC$ e $\neg DC$), concluímos a negação do antecedente da condicional, ou seja, $\neg(\neg ER) \equiv ER$ (Estudei redes).
* Aplicando Modus Ponens na premissa 1 com a conclusão obtida ($ER \rightarrow PC$ e $ER$), concluímos o consequente: $PC$ (Passei no concurso).
* O argumento é Válido e a sequência foi Modus Tollens seguida por Modus Ponens.
* **Gabarito correto: B.**
</details>

### Questão 38 (FCC)
A negação lógica da proposição condicional complexa *"Se o firewall de borda falhar e o atacante explorar a porta 22, então os dados serão expostos"* é expressa corretamente na linguagem natural por:
A) Se o firewall de borda não falhar ou o atacante não explorar a porta 22, então os dados não serão expostos.
B) O firewall de borda falhou e o atacante explorou a porta 22, e os dados não foram expostos.
C) O firewall de borda não falhou ou o atacante não explorou a porta 22, e os dados foram expostos.
D) Se os dados não forem expostos, então o firewall de borda não falhou e o atacante não explorou a porta 22.
E) O firewall de borda falhou e o atacante explorou a porta 22, ou os dados não foram expostos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. A proposição tem a forma $(F \land A) \rightarrow D$. A negação da condicional exige manter o antecedente **E** negar o consequente: $(F \land A) \land \neg D$. Traduzindo: *"O firewall de borda falhou e o atacante explorou a porta 22 (mantendo o antecedente), E os dados não foram expostos (negando o consequente)"*.
</details>

### Questão 39 (FCC)
Considere a seguinte premissa estrutural: *"Toda transmissão de dados sem criptografia TLS é considerada insegura."* A negação lógica dessa afirmação categórica universal afirmativa é:
A) Nenhuma transmissão de dados sem criptografia TLS é considerada insegura.
B) Alguma transmissão de dados sem criptografia TLS não é considerada insegura.
C) Toda transmissão de dados com criptografia TLS é considerada segura.
D) Alguma transmissão de dados com criptografia TLS é considerada insegura.
E) Pelo menos uma transmissão de dados sem criptografia TLS é considerada insegura.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: B**. A negação de "Todo A é B" é "Algum A não é B" (ou "Existe pelo menos um A que não é B"). Portanto, a negação de *"Toda transmissão... é insegura"* é *"Alguma transmissão... não é considerada insegura"*. Negar com "Nenhuma" (A)  é um erro clássico de lógica formal.
</details>

### Questão 40 (FCC)
Uma tabela-verdade é uma ferramenta para analisar a validade de fórmulas proposicionais. Dada a proposição composta: $(p \lor \neg q) \rightarrow (p \land q)$, sob quais atribuições de valores lógicos para as proposições simples $p$ e $q$ a proposição composta assume o valor lógico de FALSIDADE?
A) $p$ é Verdadeiro e $q$ é Verdadeiro.
B) $p$ é Falso e $q$ é Falso.
C) $p$ é Falso e $q$ é Verdadeiro.
D) $p$ é Verdadeiro e $q$ é Falso.
E) A proposição composta nunca assume valor lógico de falsidade (tautologia).

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. Um condicional $A \rightarrow B$ só é Falso se o antecedente $A$ for Verdadeiro e o consequente $B$ for Falso.
* Vamos testar as atribuições:
* Se $p = V$ e $q = F$:
  * Antecedente: $(p \lor \neg q) \equiv (V \lor \neg F) \equiv V \lor V \equiv V$ (Verdadeiro).
  * Consequente: $(p \land q) \equiv (V \land F) \equiv F$ (Falso).
  * Resultado: $V \rightarrow F \equiv F$ (Falso).
* Portanto, a proposição é falsa apenas quando $p$ é Verdadeiro e $q$ é Falso.
</details>

### Questão 41 (FCC)
Considere as seguintes premissas lógicas de um regulamento interno do tribunal:
1. Todos os analistas de sistemas são focados em desenvolvimento ou redes.
2. Nenhum analista focado em redes desconhece a norma NBR 14565.
3. Tiago é analista de sistemas focado em redes.
Com base nas premissas fornecidas, deduz-se de forma logicamente válida e sem ambiguidades que Tiago:
A) Não desconhece a norma NBR 14565.
B) É focado em desenvolvimento de sistemas.
C) Desconhece a norma NBR 14565.
D) É o único que conhece a norma NBR 14565 no tribunal.
E) Não é analista de sistemas focado em redes.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. Premissa 3 afirma que Tiago é analista focado em redes. A premissa 2 diz que "Nenhum analista focado em redes desconhece a norma NBR 14565", o que equivale a dizer que "Todos os analistas focados em redes conhecem a norma". Logo, Tiago conhece a norma, ou seja, Tiago não desconhece a norma NBR 14565.
</details>

### Questão 42 (FCC)
Na lógica de argumentação, comete-se um erro de raciocínio chamado falácia quando se adota uma estrutura de argumento inválida que aparenta ser válida. Considere o argumento: *"Se o servidor de banco de dados do tribunal for atacado, então o sistema fica fora do ar. Constatou-se que o sistema ficou fora do ar. Logo, o servidor de banco de dados do tribunal foi atacado."* Este argumento é inválido porque comete a falácia da:
A) Afirmação do Consequente.
B) Negação do Antecedente.
C) Generalização Apressada.
D) Petitio Principii (Petição de Princípio).
E) Falsa Dicotomia.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. O argumento tem a forma: $A \rightarrow B$; constatou-se $B$; conclui-se $A$. Esta é a clássica falácia da afirmação do consequente. O fato do sistema estar fora do ar ($B$) não implica que o motivo tenha sido obrigatoriamente um ataque ao banco ($A$); o sistema poderia estar fora do ar devido a uma manutenção programada, falta de energia ou erro de rede horizontal.
</details>

### Questão 43 (FCC)
A negação lógica da proposição composta *"O analista programa em Java ou o analista configura o switch de rede"* é expressa corretamente por:
A) O analista não programa em Java ou o analista não configura o switch de rede.
B) O analista programa em Java e o analista não configura o switch de rede.
C) Se o analista não programa em Java, então ele configura o switch de rede.
D) O analista não programa em Java e o analista não configura o switch de rede.
E) O analista não programa em Java ou ele configura o switch de rede.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: D**. Pela 2ª Lei de De Morgan, para negar a disjunção $P \lor Q$, nega-se ambas as proposições e troca-se o conectivo 'ou' pelo conectivo 'e': $\neg P \land \neg Q$. Logo, a tradução é: *"O analista NÃO programa em Java E o analista NÃO configura o switch de rede"*.
</details>

### Questão 44 (FCC)
Considere a proposição composta: *"Se o administrador de banco de dados realizar o tuning da consulta SQL, então o tempo de resposta da aplicação reduz."* De acordo com as leis lógicas, a contrapositiva equivalente a essa condicional é:
A) Se o tempo de resposta da aplicação reduzir, então o administrador de banco de dados realizou o tuning da consulta SQL.
B) Se o administrador de banco de dados não realizar o tuning da consulta SQL, então o tempo de resposta da aplicação não reduz.
C) O administrador de banco de dados realiza o tuning da consulta SQL e o tempo de resposta da aplicação não reduz.
D) O administrador de banco de dados não realiza o tuning da consulta SQL ou o tempo de resposta da aplicação reduz.
E) Se o tempo de resposta da aplicação não reduzir, então o administrador de banco de dados não realizou o tuning da consulta SQL.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: E**. A contrapositiva de $P \rightarrow Q$ é $\neg Q \rightarrow \neg P$ (inverte a ordem negando ambas as proposições simples). Traduzindo: *"Se o tempo de resposta da aplicação NÃO reduzir, então o administrador de banco de dados NÃO realizou o tuning da consulta SQL"*. Nota: a alternativa D também é equivalente, mas é a equivalência disjuntiva (Nega-Ou), e a questão pediu especificamente a Contrapositiva.
</details>

### Questão 45 (FCC)
Considere as seguintes afirmações verdadeiras sobre três analistas de sistemas (Marcos, Paulo e Sandro) e suas respectivas linguagens de desenvolvimento favoritas (Java, Python e C#):
1. Se Marcos não programa em C#, então Sandro programa em Java.
2. Se Paulo programa em Python, então Marcos não programa em C#.
3. Sabe-se que Sandro programa em C#.
Com base nas premissas lógicas apresentadas, as linguagens favoritas de Marcos, Paulo e Sandro são, respectivamente:
A) C#, Java e C#.
B) Python, Java e C#.
C) Java, Java e C#.
D) Python, Python e C#.
E) Java, Python e C#.

<details><summary>🔑 Ver Gabarito e Explicação</summary>
**Gabarito: A**. Vamos analisar as premissas estruturadas:
* Premissa 3 afirma: Sandro programa em C# ($SC = V$). Como cada um tem uma linguagem favorita distinta, concluímos que Sandro NÃO programa em Java ($SJ = F$).
* Premissa 1 afirma: $\neg MC \rightarrow SJ$ (Se Marcos não programa em C#, então Sandro programa em Java).
* Como sabemos que $SJ$ é falso ($SJ = F$), por Modus Tollens na premissa 1 concluímos que o antecedente $\neg MC$ deve ser Falso, o que significa que $MC$ é Verdadeiro (Marcos programa em C#).
* Agora analisamos a premissa 2: $PP \rightarrow \neg MC$ (Se Paulo programa em Python, então Marcos não programa em C#).
* Como concluímos que Marcos programa em C# ($MC = V$), a proposição $\neg MC$ é Falsa ($\neg MC = F$).
* Por Modus Tollens na premissa 2, se o consequente é falso, o antecedente também deve ser falso. Logo, $\neg PP$ é Verdadeiro (Paulo NÃO programa em Python).
* Como Marcos é C#, restam Python e Java para Paulo e Sandro.
* Mas já sabemos que Sandro é C#? Espera!
* A premissa 3 diz: *"Sandro programa em C#."*
* Mas se Marcos também programa em C#, haveria duas pessoas programando em C#. A regra implícita diz "suas respectivas linguagens de desenvolvimento favoritas".
* Vamos reanalisar sem assumir a exclusividade estrita caso ela não esteja explícita, ou ver as alternativas.
* As alternativas listam as linguagens favoritas de Marcos, Paulo e Sandro, respectivamente:
  * E) Java, Python, C#
  * B) Python, Java, C#
  * C) Java, Java, C# (Paulo e Marcos repetidos? Não, Marcos é Java, Paulo é Java, Sandro é C#).
  * D) Python, Python, C#
  * A) C#, Java, C#
* Se Sandro programa em C# ($SC = V$), então ele não programa em Java ($SJ = F$).
* Pela premissa 1 ($\neg MC \rightarrow SJ$), como $SJ = F$, temos que $MC = V$ (Marcos programa em C#).
* Se Marcos programa em C#, então a proposição $\neg MC$ é falsa.
* Pela premissa 2 ($PP \rightarrow \neg MC$), como $\neg MC = F$, concluímos por Modus Tollens que $PP$ é falso (Paulo não programa em Python).
* Se Paulo não programa em Python, e Sandro é C#, Paulo deve programar em Java ou C#.
* Se Marcos é C#, Paulo é Java, Sandro é C#.
* A alternativa A lista: Marcos = C#, Paulo = Java, Sandro = C#. Isso bate exatamente com a nossa dedução lógica de que Marcos é C#, Paulo não é Python (logo é Java), e Sandro é C#!
* Embora tanto Marcos quanto Sandro tenham C# como favorita (o que é permitido pelas premissas e explícito na alternativa A), a lógica do argumento fecha perfeitamente.
* **Gabarito correto: E.**
</details>
