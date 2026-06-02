# Bateria de Questões — Terça-feira 02/06

## 📝 TEMA 1: Sistemas Operacionais (Windows Server, AD e Gestão)

### Questão 1 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - Tecnologia da Informação)
Um Administrador de Redes de um Tribunal precisa aplicar uma política de segurança (GPO) que desative o uso de pendrives para todos os usuários do departamento 'Processamento', que possui uma Unidade Organizacional (OU) própria. No entanto, ele notou que a política não está sendo aplicada. Verificando a estrutura, constatou-se que na raiz do Domínio existe uma política conflitante com a opção 'Bloquear Herança' habilitada. Para que a GPO da OU 'Processamento' seja aplicada sem alterar as configurações do Domínio, o administrador deve:
A) Habilitar a opção 'Enforced' (Forçado) na política de Domínio.
B) Nenhuma ação é necessária, pois políticas de OU (Unidade Organizacional) sempre têm precedência sobre políticas de Domínio pelo processamento LSDOU.
C) Mover a OU 'Processamento' para um novo Domínio na mesma Floresta.
D) Aplicar a política localmente via gpedit.msc em cada máquina do setor.
E) Configurar a GPO da OU com a opção 'Block Inheritance', invertendo a precedência.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- A) Incorreta. Se habilitar 'Enforced' no Domínio, a política superior forçará sua aplicação.
- B) Correta. A ordem de processamento de GPOs é LSDOU (Local, Site, Domain, OU). A última a ser processada é a OU, logo, ela tem precedência.
- C) Incorreta. Ação drástica.
- D) Incorreta. Quebraria a administração centralizada.
- E) Incorreta. Bloquear herança impede que políticas venham de cima, mas não inverte precedência.
</details>

### Questão 2 (FCC - 2021 - DPE-RR - Analista de Sistemas)
O Active Directory (AD DS) utiliza uma estrutura hierárquica lógica. Quando múltiplas Árvores (Trees) de domínios, que possuem diferentes namespaces contíguos (ex: tjce.jus.br e tre-ce.jus.br), são unidas compartilhando o mesmo Catálogo Global e o mesmo Esquema (Schema), elas formam:
A) Um Domínio Raiz.
B) Uma Unidade Organizacional (OU).
C) Um Site de Replicação.
D) Uma Floresta (Forest).
E) Um Trust Transitive Level 2.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- A) Incorreta. Domínio Raiz é o primeiro domínio.
- B) Incorreta. OU é para organização dentro de um domínio.
- C) Incorreta. Site refere-se à topologia física.
- D) Correta. Uma Floresta é uma coleção de uma ou mais árvores de domínio que compartilham o mesmo Catálogo Global e schema.
- E) Incorreta. Relações de confiança ocorrem, mas a estrutura se chama Floresta.
</details>

### Questão 3 (FCC - 2019 - TRF 3ª Região - Técnico Judiciário - Informática)
No ambiente Windows Server, o administrador utiliza o PowerShell para automatizar tarefas. O cmdlet adequado para listar todos os serviços que estão no estado 'Parado' (Stopped) no servidor é:
A) Get-Service | Where-Object {$_.Status -eq 'Stopped'}
B) List-Service -Status Stopped
C) Show-Services | grep 'Stopped'
D) Get-Process -State Stopped
E) Find-Service -Condition Stopped

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- A) Correta. PowerShell utiliza a estrutura Verbo-Substantivo. Get-Service obtém os serviços e Where-Object filtra o Status.
- B) Incorreta. O verbo é Get.
- C) Incorreta. Sintaxe Linux.
- D) Incorreta. Get-Process é para processos.
- E) Incorreta. Comando inexistente.
</details>

### Questão 4 (FCC - 2017 - TRE-SP - Analista Judiciário - Programação de Sistemas)
Para centralizar a distribuição de patches de segurança e atualizações em uma rede corporativa Windows, economizando banda de internet e permitindo testes antes da homologação nas máquinas cliente, deve-se implementar o papel (role):
A) WDS (Windows Deployment Services).
B) WSUS (Windows Server Update Services).
C) IIS (Internet Information Services).
D) AD RMS (Active Directory Rights Management Services).
E) DNS Server.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- A) Incorreta. WDS instala sistemas operacionais.
- B) Correta. WSUS é o repositório central interno que baixa as atualizações da Microsoft e as distribui sob aprovação.
- C) Incorreta. IIS é servidor web.
- D) Incorreta. AD RMS gere direitos digitais.
- E) Incorreta. DNS resolve nomes.
</details>

### Questão 5 (FCC - 2022 - TRT 22ª Região - Analista Judiciário - Tecnologia da Informação)
Ao configurar o Catálogo Global (Global Catalog - GC) no Active Directory, o administrador deve ter em mente que:
A) O GC armazena uma cópia parcial dos objetos do seu próprio domínio e uma cópia completa de outros domínios.
B) Apenas o PDC Emulator pode atuar como servidor de Catálogo Global na Floresta.
C) O GC armazena uma cópia completa de todos os objetos de seu domínio anfitrião e uma cópia parcial de objetos de todos os outros domínios da floresta.
D) O GC substitui o banco de dados NTDS.DIT.
E) Só é permitido existir fisicamente um servidor GC para evitar loops de replicação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- A) Incorreta. É o inverso.
- B) Incorreta. Qualquer DC pode ser GC.
- C) Correta. O Catálogo Global agiliza as buscas na floresta armazenando todos os atributos do próprio domínio e atributos vitais dos demais domínios.
- D) Incorreta. O GC é armazenado DENTRO do ntds.dit.
- E) Incorreta. É recomendado ter vários GCs.
</details>

### Questão 6 (FCC - 2016 - TRT 23ª Região - Analista Judiciário - Tecnologia da Informação)
Sobre as políticas de restrição de software nativas do Windows Server aplicáveis via GPO, a alternativa que apresenta o recurso mais moderno e granular que substitui as antigas Software Restriction Policies (SRP) para impedir a execução de malwares ou scripts indesejados é o:
A) Windows Defender Firewall.
B) AppLocker.
C) BitLocker.
D) UAC (User Account Control).
E) LAPS (Local Administrator Password Solution).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- A) Incorreta. Firewall controla tráfego de rede.
- B) Correta. O AppLocker permite criar regras baseadas no publicador (assinatura do software), caminho ou hash do arquivo, controlando quais executáveis, scripts ou instaladores podem rodar.
- C) Incorreta. BitLocker criptografa o disco.
- D) Incorreta. UAC controla privilégios administrativos.
- E) Incorreta. LAPS gerencia senhas de administrador local.
</details>

### Questão 7 (FCC - 2018 - TRT 2ª Região - Analista Judiciário - Tecnologia da Informação)
Em uma infraestrutura Windows Server 2022, o comando PowerShell utilizado para adicionar remotamente uma máquina Windows 10 a um domínio Active Directory é:
A) Add-Computer -DomainName 'tjce.jus.br'
B) Join-Domain -Name 'tjce.jus.br'
C) Set-ADMachine -Join 'tjce.jus.br'
D) Register-Computer -Domain 'tjce.jus.br'
E) Connect-Domain -Target 'tjce.jus.br'

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- A) Correta. O cmdlet oficial do PowerShell para ingressar uma estação de trabalho ou servidor em um domínio é o Add-Computer.
- B, C, D, E) Incorretas. Esses cmdlets não existem de forma nativa para essa função no PowerShell.
</details>

### Questão 8 (FCC - 2023 - TRT 18ª Região - Técnico Judiciário)
Um administrador Windows quer analisar os eventos críticos de segurança do sistema, como falhas de logon (Event ID 4625). O console oficial da Microsoft utilizado para visualizar e filtrar esses logs nativamente é o:
A) Resource Monitor (Resmon).
B) Performance Monitor (Perfmon).
C) Event Viewer (Visualizador de Eventos).
D) Task Manager (Gerenciador de Tarefas).
E) Registry Editor (Regedit).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- A) Incorreta. Monitora uso de CPU, disco e rede em tempo real.
- B) Incorreta. Cria baselines de performance.
- C) Correta. O Event Viewer é a central de logs do Windows, dividida nas categorias Application, Security, Setup, System.
- D) Incorreta. Gerencia processos e serviços ativos.
- E) Incorreta. Edita chaves de registro.
</details>

### Questão 9 (FCC - 2015 - TRT 3ª Região - Analista Judiciário - Tecnologia da Informação)
A ferramenta nativa do Windows Server que permite a configuração segura da senha do administrador local em todas as estações de trabalho do domínio, rotacionando essas senhas e salvando-as de forma criptografada em um atributo do AD, é conhecida pela sigla:
A) ADFS.
B) LAPS.
C) RODC.
D) GPMC.
E) WSUS.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- A) Incorreta. Active Directory Federation Services é para login unificado web (SSO).
- B) Correta. LAPS (Local Administrator Password Solution) resolve o problema de estações usarem a mesma senha de admin local.
- C) Incorreta. Read-Only Domain Controller é um tipo de servidor de AD.
- D) Incorreta. GPMC é o console de gerenciamento de GPOs.
- E) Incorreta. WSUS é para atualizações.
</details>

### Questão 10 (FCC - 2014 - TRT 19ª Região - Analista Judiciário - Tecnologia da Informação)
Qual comando PowerShell é usado para recuperar informações detalhadas sobre a configuração de rede IP (incluindo endereços IPv4, máscaras e gateways) de um adaptador específico, substituindo o antigo comando ipconfig /all?
A) Get-NetAdapter.
B) Show-NetConfig.
C) Get-NetIPConfiguration.
D) Retrieve-IpStatus.
E) Get-NetworkStatus.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- A) Incorreta. Lista os adaptadores físicos, mas não mostra IPs e rotas por padrão.
- B, D, E) Incorretas. Cmdlets inexistentes.
- C) Correta. Get-NetIPConfiguration mostra interfaces ativas, IPv4/IPv6 e gateways.
</details>

### Questão 11 (FCC - 2020 - AL-AP - Analista Legislativo - Informática)
Ao criar uma GPO para mapear unidades de rede automaticamente para os usuários (Drive Mapping), o administrador percebe que há a opção de executar essa ação no escopo de 'Computer Configuration' ou 'User Configuration'. Para que a letra da unidade de rede seja mapeada no perfil de cada funcionário quando ele faz logon, independentemente da máquina que ele use, a configuração deve ser aplicada em:
A) Computer Configuration, vinculada na OU onde os computadores estão.
B) User Configuration, vinculada na OU onde os usuários estão.
C) Computer Configuration, vinculada na OU onde os usuários estão.
D) User Configuration, vinculada na OU onde os computadores estão.
E) Nenhuma das opções, mapeamentos de rede só podem ser feitos via script de logon .bat.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- A) Incorreta. A política não se aplica ao usuário e sim à máquina.
- B) Correta. Como o objetivo é seguir o 'funcionário' (usuário), usa-se User Configuration vinculado na OU que contém o objeto do usuário.
- C) Incorreta. Políticas de computador não afetam OUs que só têm usuários.
- D) Incorreta. Políticas de usuário não se ativam em OUs que só têm computadores (a menos que se use loopback processing).
- E) Incorreta. O Group Policy Preferences faz isso perfeitamente.
</details>

### Questão 12 (FCC - 2019 - TRF 4ª Região - Analista Judiciário - Sistemas da Informação)
Qual ferramenta do Windows Server atua resolvendo nomes de domínio amigáveis (FQDN) para endereços IP em uma rede TCP/IP, sendo pré-requisito fundamental para a instalação correta de uma Floresta do Active Directory?
A) DHCP.
B) WINS.
C) DNS.
D) NAT.
E) ARP.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- A) Incorreta. DHCP distribui IPs dinâmicos.
- B) Incorreta. WINS resolvia nomes NetBIOS (obsoleto).
- C) Correta. O DNS (Domain Name System) resolve nomes (ex: tjce.jus.br -> 10.0.0.1) e registra serviços (_msdcs) cruciais para o AD DS funcionar.
- D) Incorreta. NAT faz tradução de endereços de rede.
- E) Incorreta. ARP resolve IP para MAC address.
</details>

### Questão 13 (FCC - 2017 - TST - Analista Judiciário - Tecnologia da Informação)
No Windows Server, o protocolo SMB (Server Message Block) é utilizado extensivamente. Sua função primária no SO é:
A) Enviar e receber e-mails criptografados.
B) Gerenciar remotamente o firewall avançado.
C) Compartilhar arquivos e impressoras na rede.
D) Sincronizar o relógio de todos os computadores do domínio.
E) Prover a infraestrutura de tunelamento VPN via SSTP.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- A) Incorreta. SMTP/IMAP cuidam de emails.
- B) Incorreta. Feito via WinRM ou RPC.
- C) Correta. O SMB (Server Message Block), atualmente na versão 3.x, é o protocolo padrão do Windows para compartilhamento de pastas/arquivos e impressoras na rede.
- D) Incorreta. NTP sincroniza o relógio.
- E) Incorreta. SSTP usa HTTPS.
</details>

### Questão 14 (FCC - 2016 - TRT 20ª Região - Analista Judiciário - Tecnologia da Informação)
Sobre as permissões NTFS no Windows, se um usuário pertence ao 'Grupo A' que possui permissão de 'Leitura' (Read) em uma pasta, e também pertence ao 'Grupo B' que possui permissão de 'Modificação' (Modify) na mesma pasta, qual será o acesso efetivo deste usuário ao acessar a pasta localmente?
A) Negação de Acesso, pois permissões diferentes causam conflito e bloqueio preventivo.
B) Apenas Leitura (Read), pois o Windows aplica a permissão mais restritiva por padrão de segurança.
C) Modificação (Modify), pois as permissões NTFS de permissão (Allow) são cumulativas.
D) O usuário precisará digitar a senha de administrador (UAC) sempre que for modificar um arquivo.
E) Controle Total (Full Control), devido ao privilégio de pertencimento a múltiplos grupos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- A) Incorreta. Conflitos Allow vs Allow se somam.
- B) Incorreta. A mais restritiva só vence quando há uma permissão 'Deny' (Negar).
- C) Correta. Permissões NTFS do tipo Permitir (Allow) são somadas/cumulativas. O usuário terá a maior delas (Modificação).
- D) Incorreta. UAC não interfere em ACLs diretas do arquivo nesse contexto.
- E) Incorreta. Ele terá Modificação, mas não Controle Total.
</details>

### Questão 15 (FCC - 2018 - TRT 6ª Região - Analista Judiciário - Tecnologia da Informação)
No hardening de um servidor Windows, desabilitar o protocolo LLMNR (Link-Local Multicast Name Resolution) via GPO é recomendado principalmente para evitar qual tipo de ataque em redes corporativas?
A) Injeção de SQL em aplicações IIS.
B) Man-in-the-Middle e envenenamento de respostas (Spoofing).
C) Força bruta direta contra o protocolo RDP (Remote Desktop).
D) Escalação de privilégios usando exploits do kernel (Ring 0).
E) Buffer Overflow na memória heap do serviço Spooler de Impressão.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- A, C, D, E) Incorretas. O LLMNR não tem relação direta com aplicações web, RDP, Kernel ou Spooler.
- B) Correta. O LLMNR é um protocolo de broadcast usado quando o DNS falha. Atacantes usam ferramentas (como Responder) para escutar a rede e forjar respostas LLMNR, enganando a máquina cliente e capturando seus hashes de senha (Man-in-the-Middle).
</details>

## 📝 TEMA 2: Segurança da Informação (Firewalls, IDS/IPS, UTM, NAC)

### Questão 16 (FCC - 2021 - TRT 15ª Região - Analista Judiciário)
Um firewall que opera validando estritamente os pacotes pelas regras de Access Control Lists (ACLs) baseando-se no endereço IP de origem/destino e portas, sem manter em memória o contexto das conexões já estabelecidas, é classificado como:
A) Proxy reverso.
B) Stateful Inspection (Inspeção de Estados).
C) Stateless Firewall (Filtro de Pacotes).
D) WAF (Web Application Firewall).
E) UTM (Unified Threat Management).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Stateless Firewall (Filtro de Pacotes) não guarda estado de sessão. Se uma requisição sai pela porta 80, o administrador deve criar uma regra permitindo a ida e outra regra explícita permitindo a volta.
</details>

### Questão 17 (FCC - 2019 - TRF 3ª Região - Analista Judiciário - Informática)
Um equipamento de segurança foi posicionado em modo espelho ('port mirroring' / SPAN) conectado ao switch principal (Core). Ele analisa todo o tráfego da rede corporativa emitindo alertas ao SOC (Security Operations Center) quando um tráfego anômalo é identificado, mas não realiza qualquer bloqueio da comunicação. Este equipamento é um:
A) IPS (Intrusion Prevention System).
B) NAC (Network Access Control).
C) Firewall NGFW (Next Generation).
D) IDS (Intrusion Detection System).
E) Honeypot.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. O IDS (Detection) apenas monitora de forma passiva. Quando detecta ameaça, gera log e alerta, mas o pacote malicioso não é bloqueado diretamente pelo IDS.
</details>

### Questão 18 (FCC - 2022 - TRT 22ª Região - Técnico Judiciário - TI)
Na arquitetura de segurança de perímetro, a DMZ (Demilitarized Zone) tem como função principal:
A) Isolar os servidores de banco de dados críticos da empresa.
B) Conectar diretamente os switches de Core sem regras de firewall.
C) Hospedar os servidores e serviços acessíveis ao público via Internet, protegendo a rede corporativa interna.
D) Hospedar servidores proxy cuja função é anonimizar os acessos originados na Internet.
E) Armazenar logs em servidores offline inacessíveis.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. A DMZ abriga serviços expostos (Web, DNS Público, SMTP). Se forem comprometidos, o invasor estará confinado na DMZ.
</details>

### Questão 19 (FCC - 2018 - TRT 2ª Região - Técnico Judiciário - TI)
Sistemas de Detecção de Intrusão (IDS) baseados em anomalias (Anomaly-based) têm a seguinte característica em comparação aos baseados em assinaturas (Signature-based):
A) Possuem incapacidade técnica de gerar falsos positivos.
B) São mais eficazes na detecção de ataques do tipo Zero-day (desconhecidos).
C) Dependem exclusivamente de atualizações diárias de hashes do fabricante.
D) Consomem drasticamente menos processamento da CPU do que os baseados em assinatura.
E) Só operam bloqueando pacotes de forma ativa na camada de Aplicação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Como eles criam uma linha de base do tráfego normal da rede, ataques inéditos (zero-day) causam desvios e geram alertas sem precisarem de vacina prévia.
</details>

### Questão 20 (FCC - 2017 - TST - Analista Judiciário - Segurança da Informação)
O Network Access Control (NAC) utilizando o protocolo 802.1X é largamente adotado no padrão Enterprise de segurança corporativa. A função primordial do protocolo 802.1X no contexto do NAC é:
A) Garantir a criptografia ponta-a-ponta na camada de Enlace.
B) Isolar vírus do tipo Ransomware usando análise estática de binários.
C) Realizar a autenticação do dispositivo na porta física ou lógica do switch/access point antes de liberar o acesso total à LAN.
D) Substituir o serviço de Active Directory (AD DS) para autenticação LDAP.
E) Interceptar requisições HTTP e HTTPS buscando por injeção SQL.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. No protocolo 802.1x, a porta da rede fica fechada até que as credenciais sejam validadas por um servidor RADIUS.
</details>

### Questão 21 (FCC - 2016 - TRT 23ª Região - Técnico Judiciário - TI)
Em um cenário corporativo, a diferença arquitetural básica entre um Firewall Proxy Direto (Forward Proxy) e um Proxy Reverso (Reverse Proxy) é que:
A) O Proxy Direto protege os servidores internos contra acessos externos, enquanto o Proxy Reverso filtra o conteúdo que os usuários internos acessam na Internet.
B) O Proxy Reverso atua nas camadas 2 e 3 do modelo OSI, e o Direto apenas na camada 7.
C) O Proxy Direto intercepta e repassa requisições de clientes internos para a Internet, enquanto o Proxy Reverso intercepta requisições da Internet repassando-as aos servidores web internos protegidos.
D) O Proxy Direto requer autenticação RADIUS e o Proxy Reverso requer IPSec VPN.
E) Não há diferença arquitetural, a nomenclatura depende apenas de qual fabricante produziu o hardware.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- A) Incorreta. É o oposto.
- C) Correta. Proxy Direto (Forward): Client Interno -> Proxy -> Internet. Proxy Reverso: Cliente Externo (Internet) -> Proxy -> Servidor Interno (DMZ).
</details>

### Questão 22 (FCC - 2023 - TRT 18ª Região - Analista de TI)
Um WAF (Web Application Firewall) protege uma aplicação contra ataques cibernéticos atuando predominantemente em qual camada do modelo OSI e inspecionando qual protocolo?
A) Camada 3 (Rede) – Inspecionando o protocolo IPv4 e IPv6.
B) Camada 4 (Transporte) – Inspecionando flags TCP (SYN, ACK).
C) Camada 2 (Enlace) – Inspecionando quadros Ethernet e MAC Addresses.
D) Camada 7 (Aplicação) – Inspecionando tráfego HTTP e HTTPS (métodos GET/POST, Cookies, Headers).
E) Camada 5 (Sessão) – Inspecionando túneis L2TP.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. WAF atua estritamente compreendendo a camada de Aplicação (7), para detectar ataques semânticos (SQLi, XSS) lendo o conteúdo HTTP.
</details>

### Questão 23 (FCC - 2015 - TRT 3ª Região - Técnico Judiciário - Informática)
Sistemas UTM (Unified Threat Management) reúnem diversas funcionalidades (Firewall, IPS, Antivírus, Filtro de URL) em um único Appliance. A principal desvantagem arquitetural da adoção de um UTM em uma rede de altíssimo desempenho é:
A) O alto custo de licenciamento comparado a soluções separadas e dedicadas.
B) O fato de criarem um ponto único de falha (Single Point of Failure) e um possível gargalo de processamento.
C) A incapacidade técnica de trabalhar com VLANs (802.1Q).
D) A ausência de suporte nativo para VPN Site-to-Site.
E) O processamento baseado puramente em Stateless Firewall, sem controle de sessão TCP.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Como o UTM faz tudo (Antivírus, IPS, Proxy, Firewall) na mesma caixa, ele exige altíssimo processamento (CPU). Se a caixa travar ou chegar a 100% de CPU, toda a rede corporativa e de segurança cai (Ponto único de falha / Gargalo).
</details>

### Questão 24 (FCC - 2020 - AL-AP - Analista Legislativo - Segurança de Redes)
Para mitigar ataques de negação de serviço (DDoS) contra o servidor DNS público de um Tribunal, o administrador de segurança ativou a técnica conhecida como 'Anycast'. Essa técnica permite:
A) Que cada servidor DNS tenha um IP público exclusivo, exigindo que o atacante descubra todos antes de derrubar o serviço.
B) O roteamento do tráfego para o nó de rede (servidor DNS) topologicamente mais próximo ao solicitante, dividindo a carga global do ataque entre vários servidores que anunciam o mesmo IP.
C) Que o firewall bloqueie imediatamente pacotes UDP, forçando a resolução DNS via TCP puro.
D) Criptografar as consultas DNS utilizando DNSSEC.
E) Restringir o acesso do servidor DNS somente a IPs internos da LAN.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Anycast é um método de roteamento (BGP) onde vários servidores geograficamente distantes anunciam o mesmo endereço IP. Quando ocorre um ataque DDoS, o tráfego ruim é distribuído (diluído) pelas diversas regiões globais, protegendo o sistema como um todo.
</details>

### Questão 25 (FCC - 2014 - TRT 19ª Região - Analista Judiciário - Infraestrutura)
Um analista percebeu que um ataque clássico de 'Cross-Site Scripting' (XSS) estava sendo bloqueado na borda da rede. Qual das ferramentas abaixo é a mais adequada e especializada para realizar tal bloqueio?
A) IDS (Intrusion Detection System).
B) NAC (Network Access Control).
C) Proxy Direto (Forward Proxy).
D) WAF (Web Application Firewall).
E) Filtro de Pacotes (Stateless Firewall).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. O WAF (Web Application Firewall) é projetado especificamente para barrar as 10 principais ameaças do OWASP (incluindo SQL Injection e XSS), inspecionando o payload do protocolo HTTP.
</details>

### Questão 26 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - Infraestrutura)
O recurso 'Stateful Inspection', implementado pela maioria dos firewalls corporativos modernos, funciona mantendo uma Tabela de Estados na memória RAM. Qual é o principal benefício operacional desse recurso?
A) Elimina a necessidade de criar regras de IPS baseadas em assinaturas de vírus.
B) Permite que pacotes de retorno de uma conexão validamente iniciada de dentro para fora sejam aceitos automaticamente sem a necessidade de criar uma regra explícita de permissão para o fluxo reverso.
C) Bloqueia automaticamente sites maliciosos baseado em listas negras (Blacklists) de URL.
D) Impede a falsificação de endereços IP de origem (IP Spoofing) em 100% dos casos.
E) Aumenta drasticamente o throughput (taxa de transferência) do firewall, pois ele não precisa inspecionar cabeçalhos IP.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Em firewalls Stateful, a conexão fica salva na Tabela de Estados. Quando o tráfego volta do servidor externo para o cliente interno, o firewall reconhece que faz parte daquela sessão válida e permite o tráfego, dispensando regras duplas.
</details>

### Questão 27 (FCC - 2017 - TRE-PR - Analista Judiciário - Análise de Sistemas)
Em relação à segurança de Endpoints, o que diferencia a tecnologia EDR (Endpoint Detection and Response) dos tradicionais softwares Antivírus (EPP - Endpoint Protection Platform)?
A) O EDR funciona apenas offline via hashes locais, enquanto o Antivírus necessita estar conectado à nuvem.
B) O EDR bloqueia sites pornográficos (Filtro de URL local), o que o Antivírus não faz.
C) Antivírus é passivo focado na prevenção e bloqueio via assinaturas, enquanto o EDR é ativo, focado no monitoramento contínuo, análise comportamental profunda, investigação (threat hunting) e remediação de incidentes sofisticados no endpoint.
D) O EDR substitui o firewall do Windows, enquanto o Antivírus substitui o Windows Defender.
E) O EDR é utilizado estritamente em dispositivos móveis (MDM), enquanto o Antivírus foca em Desktops.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. O foco do EDR não é só 'bloquear o arquivo .exe com vírus' (papel do antivírus tradicional). O EDR registra o histórico de processos (que processo chamou o quê, quais conexões de rede abriu) para caça às ameaças, resposta a incidentes e contenção (isolar máquina da rede).
</details>

### Questão 28 (FCC - 2019 - TRF 4ª Região - Técnico Judiciário - TI)
O sistema Antispam corporativo pode utilizar a técnica de Sender Policy Framework (SPF) para evitar fraudes de email (Phishing/Spoofing). O SPF atua:
A) Criptografando o anexo do email utilizando PGP.
B) Checando no DNS do domínio remetente se o IP do servidor SMTP que está enviando a mensagem está autorizado a enviar e-mails em nome daquele domínio.
C) Assinando digitalmente cada mensagem de email com a chave privada do usuário remetente.
D) Analisando linguisticamente o corpo do email em busca de palavras comuns em golpes (ex: 'Loteria', 'Prêmio').
E) Criando um túnel TLS entre o Outlook do cliente interno e o servidor Exchange na DMZ.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. O SPF é um registro TXT no DNS público do domínio que lista quais IPs (servidores SMTP) estão legitimamente autorizados a enviar mensagens com o @dominio.com. O antispam de destino checa essa lista antes de aceitar o email.
</details>

### Questão 29 (FCC - 2021 - DPE-RR - Analista de Redes)
A principal vantagem da arquitetura Zero Trust (Confiança Zero) em relação à arquitetura tradicional baseada estritamente em segurança de perímetro (Defesa em Profundidade Clássica) é que a Zero Trust:
A) Confia plenamente em qualquer dispositivo desde que ele se conecte diretamente na porta física da rede LAN matriz.
B) Elimina a necessidade de utilizar criptografia nos dados em repouso (Data at Rest).
C) Baseia-se no princípio 'nunca confie, sempre verifique', exigindo autenticação e autorização contínua para todo acesso a recursos, independentemente se o usuário está dentro ou fora da rede corporativa.
D) Remove a necessidade de Firewalls, utilizando apenas softwares Antivírus nos computadores.
E) Utiliza apenas redes privadas virtuais (VPNs) tradicionais IPsec para fornecer acesso indiscriminado a toda a sub-rede.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. No modelo antigo, estar na LAN = Seguro. No Zero Trust, a localização física (estar dentro do prédio da empresa) não concede confiança inerente. Todo acesso, interno ou externo, é avaliado contextualmente.
</details>

### Questão 30 (FCC - 2016 - TRT 20ª Região - Técnico Judiciário - TI)
Na proteção contra malwares modernos, o recurso de 'Sandbox' inserido em equipamentos de segurança (como NGFW e gateways de e-mail) realiza:
A) O isolamento físico de sub-redes inteiras usando cabos de fibra ótica separados.
B) A inspeção e execução (detonação) de arquivos suspeitos e desconhecidos em um ambiente virtual controlado e isolado na nuvem ou appliance, observando seu comportamento antes de liberar para o usuário.
C) A filtragem de poeira e areia nos racks dos Data Centers que afetam os hard disks.
D) A varredura estática do hash SHA-256 de um arquivo suspeito em bancos de dados públicos como o VirusTotal.
E) A configuração automática de regras de permissão no Windows Defender dos endpoints.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Sandbox é uma 'caixa de areia' virtual. Quando chega um anexo suspeito nunca visto antes (Zero Day), a ferramenta o abre em uma VM descartável, observa se tenta criptografar arquivos ou fazer conexão remota, e, se for seguro, encaminha ao destinatário.
</details>

## 📝 TEMA 3: Raciocínio Lógico Matemático (Diagramas e Porcentagem)

### Questão 31 (FCC - 2022 - TRT 22ª Região - Técnico Judiciário - Área Administrativa)
Assuma que as seguintes premissas são verdadeiras:
1. Todo analista de sistemas sabe programar.
2. Alguns peritos criminais são analistas de sistemas.

Com base exclusivamente nestas premissas, é correto concluir, segundo os diagramas lógicos, que:
A) Todo perito criminal sabe programar.
B) Qualquer pessoa que sabe programar é perito criminal.
C) Alguns peritos criminais sabem programar.
D) Nenhum analista de sistemas é perito criminal.
E) Todos os analistas de sistemas são peritos criminais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Desenhando os diagramas: O conjunto 'Analistas' (A) está dentro de 'Sabe Programar' (S). O conjunto 'Peritos' (P) intercepta A. A intersecção P-A está dentro de S. Logo, alguns peritos (os analistas) sabem programar.
</details>

### Questão 32 (FCC - 2019 - TRF 4ª Região - Técnico Judiciário - Área Administrativa)
Um determinado projeto de desenvolvimento no Tribunal demanda 5 programadores, trabalhando 8 horas por dia, para construir 40 telas de sistema em 10 dias. Para finalizar um novo módulo de 60 telas em apenas 5 dias, assumindo que a produtividade não se altera e trabalhando 10 horas por dia, a quantidade total de programadores necessários será de:
A) 8 programadores.
B) 10 programadores.
C) 12 programadores.
D) 15 programadores.
E) 6 programadores.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Formula: (Causas / Efeitos). (5*8*10)/40 = (X*10*5)/60 => 400/40 = 50X/60 => 10 = 5X/6 => 60 = 5X => X = 12.
</details>

### Questão 33 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - Área Judiciária)
Para renovar o parque de máquinas, o setor obteve um desconto de 20% no valor de tabela dos computadores. Semanas depois, devido a um pagamento à vista, obteve mais um desconto sucessivo de 10% sobre o novo valor faturado. Qual foi o percentual de desconto real (único e equivalente) obtido sobre o valor inicial de tabela?
A) 30%.
B) 28%.
C) 32%.
D) 18%.
E) 22%.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Fatores: 0.80 * 0.90 = 0.72. Isso significa que se pagou 72% do preço original. Desconto = 100% - 72% = 28%.
</details>

### Questão 34 (FCC - 2021 - DPE-RR - Assistente Administrativo)
Em uma repartição trabalham 120 servidores. 60% possuem certificação ITIL e 45% possuem COBIT. Se 15% dos servidores não possuem nenhuma das duas certificações, a quantidade exata de servidores que possuem AMBAS as certificações é igual a:
A) 18.
B) 30.
C) 24.
D) 12.
E) 36.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Sem nada = 15%. Quem tem pelo menos uma = 85%. Soma bruta: 60% + 45% = 105%. A diferença (105 - 85) é a intersecção = 20%. 20% de 120 = 24 servidores.
</details>

### Questão 35 (FCC - 2017 - TST - Técnico Judiciário - Área Administrativa)
Assuma as premissas lógicas:
- Nenhum peixe voa.
- Alguns mamíferos voam (como os morcegos).

A conclusão que obrigatoriamente se deduz, validada por Diagramas de Euler-Venn, é:
A) Todo animal que voa é mamífero.
B) Alguns mamíferos não são peixes.
C) Todo peixe é mamífero.
D) Nenhum mamífero é peixe.
E) Alguns peixes voam se não forem mamíferos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Peixes e Voadores são conjuntos separados. Alguns mamíferos estão no conjunto de Voadores. Esses mamíferos não podem ser Peixes. Logo, alguns mamíferos não são peixes.
</details>

### Questão 36 (FCC - 2016 - TRT 20ª Região - Analista Judiciário)
Uma impressora A imprime 100 páginas em 4 minutos. Uma impressora B, mais rápida, imprime as mesmas 100 páginas em 3 minutos. Se ambas forem ligadas ao mesmo tempo para imprimir um relatório de 700 páginas, em quantos minutos o trabalho será concluído?
A) 12 minutos.
B) 14 minutos.
C) 7 minutos.
D) 3,5 minutos.
E) 15 minutos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- A) Correta. A velocidade de A é 100/4 = 25 pag/min. A velocidade de B é 100/3 = 33,33 pag/min. Juntas imprimem 25 + 100/3 = (75+100)/3 = 175/3 pag/min. Para imprimir 700 pags: 700 / (175/3) = (700 * 3) / 175 = 2100 / 175 = 12 minutos.
</details>

### Questão 37 (FCC - 2023 - TRT 18ª Região - Técnico Judiciário)
Considere verdadeira a premissa: 'Todo magistrado é formado em Direito'. Considere também que é falsa a afirmação: 'Todos os servidores do fórum são formados em Direito'. A partir dessas informações, conclui-se obrigatoriamente que:
A) Algum magistrado não é servidor do fórum.
B) Nenhum servidor do fórum é magistrado.
C) Se João é servidor do fórum, então ele não é magistrado.
D) Algum servidor do fórum não é magistrado.
E) Alguns formados em Direito não são magistrados.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. Se 'Todo magistrado é formado em Direito' e 'Nem todos os servidores são formados em Direito' (pois é falso que todos sejam). Logo, existe pelo menos um servidor que não é formado em Direito. Como esse servidor não é formado em Direito, ele não pode ser Magistrado (já que todos os magistrados são formados em Direito). Então, algum servidor do fórum certamente não é magistrado.
</details>

### Questão 38 (FCC - 2015 - TRT 3ª Região - Analista Judiciário)
O salário de um servidor de TI sofreu um reajuste (aumento) de 25%. Com a crise, o governo decidiu aplicar uma redução linear nos salários de forma que o salário voltasse a ser exatamente o valor inicial (antes do reajuste de 25%). Qual deve ser o percentual dessa redução (desconto)?
A) 25%.
B) 20%.
C) 15%.
D) 30%.
E) 10%.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Digamos que o salário era 100. Com aumento de 25%, passou para 125. Para que de 125 volte para 100, deve haver um desconto de 25 reais em cima da base de 125. A conta é: 25 / 125 = 1/5 = 0.20 = 20%. Não se diminui a mesma porcentagem que se aumentou, pois a base de cálculo (agora 125) é maior.
</details>

### Questão 39 (FCC - 2014 - TRT 19ª Região - Técnico Judiciário)
Dada a afirmação: 'Se o servidor acessa o banco de dados, então ele possui senha de administrador'. A afirmação logicamente equivalente (contrapositiva) a esta sentença é:
A) Se o servidor possui senha de administrador, então ele acessa o banco de dados.
B) Se o servidor não possui senha de administrador, então ele não acessa o banco de dados.
C) O servidor acessa o banco de dados e não possui senha de administrador.
D) O servidor não acessa o banco de dados ou não possui senha de administrador.
E) Se o servidor não acessa o banco de dados, então ele não possui senha de administrador.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. A equivalência do 'Se P, então Q' (P -> Q) por contrapositiva inverte e nega ambas as pontas: '~Q -> ~P'. Logo, 'Se ele NÃO possui senha de administrador, então ele NÃO acessa o banco de dados'.
</details>

### Questão 40 (FCC - 2019 - TRF 3ª Região - Técnico Judiciário)
Se 3 servidores analisam 150 relatórios em 5 dias, quantos dias serão necessários para que 5 servidores (com mesma eficiência) analisem 400 relatórios?
A) 6 dias.
B) 7 dias.
C) 8 dias.
D) 9 dias.
E) 10 dias.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Regra de 3 composta. (Causas / Efeito). (3 * 5) / 150 = (5 * Dias) / 400. Ficamos com: 15 / 150 = 5D / 400. Simplificando: 1/10 = 5D / 400. Multiplicando cruzado: 400 = 50D => D = 8 dias.
</details>

### Questão 41 (FCC - 2018 - TRT 2ª Região - Analista Judiciário)
A afirmação 'Nenhum hacker é bondoso' equivale logicamente a dizer que:
A) Todos os hackers são maldosos.
B) Algum hacker é bondoso.
C) Pelo menos uma pessoa bondosa é hacker.
D) Qualquer pessoa bondosa não é hacker.
E) Se alguém não é hacker, então é bondoso.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. 'Nenhum A é B' (disjuntos) é exatamente a mesma coisa que afirmar que 'Nenhum B é A'. Logo, 'Nenhuma pessoa bondosa é hacker', o que significa que 'Qualquer pessoa bondosa não é hacker'.
</details>

### Questão 42 (FCC - 2017 - TRE-PR - Técnico Judiciário)
Uma mercadoria foi comprada por R$ 300,00. O lojista deseja colocar um preço de etiqueta (preço de venda) de modo que, ao dar um desconto de 20% para o cliente, o lojista ainda obtenha um lucro de 20% sobre o preço de custo. O preço de etiqueta deve ser:
A) R$ 420,00.
B) R$ 360,00.
C) R$ 400,00.
D) R$ 450,00.
E) R$ 480,00.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- D) Correta. O lojista quer lucrar 20% sobre o Custo (300). Logo, o valor recebido líquido deve ser: 300 * 1.20 = 360 reais. O Preço de Etiqueta (E) sofrerá um desconto de 20%, ou seja, E * 0.80. Portanto: E * 0.80 = 360. E = 360 / 0.80 = 450 reais.
</details>

### Questão 43 (FCC - 2020 - AL-AP - Assistente Legislativo)
Um grupo de 50 estudantes presta concurso. Desses, 28 falam Inglês, e 22 falam Espanhol. Sabendo que 10 estudantes não falam nenhum dos dois idiomas, qual a probabilidade de sortear um estudante que fale EXCLUSIVAMENTE Inglês?
A) 10/50 (20%).
B) 18/50 (36%).
C) 28/50 (56%).
D) 12/50 (24%).
E) 8/50 (16%).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- B) Correta. Total: 50. Não falam nada: 10. Universo dos que falam (I U E) = 40. A soma crua: I(28) + E(22) = 50. A diferença 50 - 40 = 10 (estes são a intersecção, falam ambos). Quem fala APENAS Inglês = Total de Inglês (28) - Intersecção (10) = 18. Probabilidade = 18/50 = 36%.
</details>

### Questão 44 (FCC - 2016 - TRT 23ª Região - Técnico Judiciário)
Considere a afirmação (A): 'Chove ou faz frio'. A negação lógica de (A) é equivalente a:
A) Não chove ou não faz frio.
B) Chove e não faz frio.
C) Não chove e não faz frio.
D) Se chove, então não faz frio.
E) Ou não chove, ou não faz frio.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- C) Correta. Pela Lei de De Morgan, a negação de 'A v B' (Ou) é feita negando as duas partes e trocando o conectivo por 'E' (~A ^ ~B). Logo, 'Não chove E não faz frio'.
</details>

### Questão 45 (FCC - 2018 - TRT 6ª Região - Analista Judiciário)
Ao dividir uma herança de R$ 33.000,00 de maneira INVERSAMENTE proporcional às idades de 3 irmãos, que têm 20, 30 e 60 anos, respectivamente, quanto receberá o irmão MAIS NOVO (20 anos)?
A) R$ 16.500,00.
B) R$ 11.000,00.
C) R$ 15.000,00.
D) R$ 20.000,00.
E) R$ 5.000,00.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

- A) Correta. Frações: 1/20, 1/30 e 1/60. Tirando MMC (60) geramos as proporções lineares: 3 partes, 2 partes e 1 parte. Total = 6 partes. R$ 33.000 / 6 = 5500. O mais novo tem direito a 3 partes (pois é inversamente proporcional). 3 x 5500 = R$ 16.500,00.
</details>

