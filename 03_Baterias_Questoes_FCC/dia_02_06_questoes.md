# Bateria de Questões — Terça-feira 02/06

### Tema 1: Sistemas Operacionais (Windows)

#### Questão 1 (Sistemas Operacionais)

O Analista 1 de Redes de um Tribunal precisa aplicar uma política de segurança (GPO) que desative o uso de pendrives para todos os usuários do departamento 'Processamento', que possui uma Unidade Organizacional (OU) própria. No entanto, ele notou que a política não está sendo aplicada. Verificando a estrutura, constatou-se que na raiz do Domínio existe uma política conflitante com a opção 'Bloquear Herança' habilitada. Para que a GPO da OU 'Processamento' seja aplicada sem alterar as configurações do Domínio, o administrador deve:

A) Habilitar a opção 'Enforced' (Forçado) na política de Domínio.
B) Nenhuma ação é necessária, pois políticas de OU (Unidade Organizacional) sempre têm precedência sobre políticas de Domínio pelo processamento LSDOU.
C) Mover a OU 'Processamento' para um novo Domínio na mesma Floresta.
D) Aplicar a política localmente via gpedit.msc em cada máquina do setor.
E) Configurar a GPO da OU com a opção 'Block Inheritance', invertendo a precedência.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. Se habilitar 'Enforced' no Domínio, a política superior forçará sua aplicação, sobrescrevendo a OU.
- B) Correta. A ordem de processamento de GPOs é LSDOU (Local, Site, Domain, OU). A última a ser processada é a OU, logo, ela tem precedência sobre o Domínio. 'Bloquear Herança' é uma configuração feita na OU inferior para barrar políticas superiores, não o contrário. A política da OU vencerá a do Domínio naturalmente, a menos que a do Domínio estivesse como 'Enforced'.
- C) Incorreta. Ação desnecessária e arquiteturalmente drástica.
- D) Incorreta. Quebraria o propósito da administração centralizada.
- E) Incorreta. Bloquear herança impede que políticas venham de cima, mas não inverte a precedência da que foi aplicada na própria OU.

</details>

#### Questão 2 (Sistemas Operacionais)

O AD DS (cenário 2) (AD DS) utiliza uma estrutura hierárquica lógica. Quando múltiplas Árvores (Trees) de domínios, que possuem diferentes namespaces contíguos (ex: tjce.jus.br e tre-ce.jus.br), são unidas compartilhando o mesmo Catálogo Global e o mesmo Esquema (Schema), elas formam:

A) Um Domínio Raiz.
B) Uma Unidade Organizacional (OU).
C) Um Site de Replicação.
D) Uma Floresta (Forest).
E) Um Trust Transitive Level 2.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: D

- A) Incorreta. Um Domínio Raiz é o primeiro domínio criado na floresta, não o conjunto delas.
- B) Incorreta. OU é para organização de usuários e computadores dentro de um domínio.
- C) Incorreta. Site refere-se à topologia física (rede, sub-redes) e não à estrutura lógica de namespaces.
- D) Correta. Uma Floresta é uma coleção de uma ou mais árvores de domínio que não compartilham necessariamente o mesmo namespace (nome de DNS contíguo), mas compartilham o mesmo Catálogo Global, configuração e schema.
- E) Incorreta. Relações de confiança (Trust) ocorrem, mas o termo arquitetural para o agrupamento é Floresta.

</details>

#### Questão 3 (Sistemas Operacionais)

No ambiente Windows Server, o administrador utiliza o PowerShell para automatizar tarefas. O cmdlet adequado para listar todos os serviços que estão no estado 'Parado' (Stopped) no servidor é:

A) Get-Service | Where-Object {$_.Status -eq 'Stopped'}
B) List-Service -Status Stopped
C) Show-Services | grep 'Stopped'
D) Get-Process -State Stopped
E) Find-Service -Condition Stopped

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: A

- A) Correta. O PowerShell utiliza a estrutura Verbo-Substantivo. `Get-Service` obtém os serviços, que são passados via pipeline (|) para o `Where-Object`, que filtra os objetos cujo atributo Status seja igual (`-eq`) a 'Stopped'.
- B) Incorreta. O verbo padrão para listagem é 'Get', não 'List'.
- C) Incorreta. Sintaxe mista de Linux (grep) não é nativa para manipulação de objetos PowerShell.
- D) Incorreta. Get-Process lista processos, não serviços.
- E) Incorreta. Find-Service não é um cmdlet padrão de administração local de serviços.

</details>

#### Questão 4 (Sistemas Operacionais)

Para centralizar a distribuição de patches de segurança e atualizações em uma rede corporativa Windows, economizando banda de internet e permitindo testes antes da homologação nas máquinas cliente, deve-se implementar o papel (role):

A) WDS (Windows Deployment Services).
B) WSUS (Windows Server Update Services).
C) IIS (Internet Information Services).
D) AD RMS (Active Directory Rights Management Services).
E) DNS Server.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. WDS é usado para instalação de sistemas operacionais via rede (imagens do Windows), não para atualizações mensais.
- B) Correta. O WSUS atua como um repositório central interno que baixa as atualizações da Microsoft e as distribui sob demanda/aprovação aos clientes da rede local.
- C) Incorreta. IIS é o servidor web do Windows.
- D) Incorreta. RMS gerencia direitos de proteção de documentos.
- E) Incorreta. DNS resolve nomes e IPs.

</details>

#### Questão 5 (Sistemas Operacionais)

Ao configurar o Catálogo Global (Global Catalog - GC) no Active Directory, o administrador deve ter em mente que:

A) O GC armazena uma cópia parcial dos objetos do seu próprio domínio e uma cópia completa de outros domínios.
B) Apenas o PDC Emulator pode atuar como servidor de Catálogo Global na Floresta.
C) O GC armazena uma cópia completa de todos os objetos de seu domínio anfitrião e uma cópia parcial (read-only) de objetos de todos os outros domínios da floresta.
D) O GC substitui o banco de dados NTDS.DIT, sendo incompatível com instâncias RODC (Read-Only Domain Controller).
E) Em uma floresta com 10 domínios, só é permitido existir fisicamente um servidor GC para evitar loops de replicação.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. É o inverso.
- B) Incorreta. Qualquer Domain Controller (DC) pode ser promovido a Global Catalog.
- C) Correta. O Catálogo Global agiliza as buscas na floresta inteira armazenando todos os atributos do próprio domínio e apenas atributos vitais (como nome de login, email) dos objetos dos demais domínios.
- D) Incorreta. O GC é armazenado DENTRO do ntds.dit. RODCs podem ser GCs parciais.
- E) Incorreta. É recomendado ter vários GCs para alta disponibilidade.

</details>

#### Questão 6 (Sistemas Operacionais)

O Analista 6 de Redes de um Tribunal precisa aplicar uma política de segurança (GPO) que desative o uso de pendrives para todos os usuários do departamento 'Processamento', que possui uma Unidade Organizacional (OU) própria. No entanto, ele notou que a política não está sendo aplicada. Verificando a estrutura, constatou-se que na raiz do Domínio existe uma política conflitante com a opção 'Bloquear Herança' habilitada. Para que a GPO da OU 'Processamento' seja aplicada sem alterar as configurações do Domínio, o administrador deve:

A) Habilitar a opção 'Enforced' (Forçado) na política de Domínio.
B) Nenhuma ação é necessária, pois políticas de OU (Unidade Organizacional) sempre têm precedência sobre políticas de Domínio pelo processamento LSDOU.
C) Mover a OU 'Processamento' para um novo Domínio na mesma Floresta.
D) Aplicar a política localmente via gpedit.msc em cada máquina do setor.
E) Configurar a GPO da OU com a opção 'Block Inheritance', invertendo a precedência.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. Se habilitar 'Enforced' no Domínio, a política superior forçará sua aplicação, sobrescrevendo a OU.
- B) Correta. A ordem de processamento de GPOs é LSDOU (Local, Site, Domain, OU). A última a ser processada é a OU, logo, ela tem precedência sobre o Domínio. 'Bloquear Herança' é uma configuração feita na OU inferior para barrar políticas superiores, não o contrário. A política da OU vencerá a do Domínio naturalmente, a menos que a do Domínio estivesse como 'Enforced'.
- C) Incorreta. Ação desnecessária e arquiteturalmente drástica.
- D) Incorreta. Quebraria o propósito da administração centralizada.
- E) Incorreta. Bloquear herança impede que políticas venham de cima, mas não inverte a precedência da que foi aplicada na própria OU.

</details>

#### Questão 7 (Sistemas Operacionais)

O AD DS (cenário 7) (AD DS) utiliza uma estrutura hierárquica lógica. Quando múltiplas Árvores (Trees) de domínios, que possuem diferentes namespaces contíguos (ex: tjce.jus.br e tre-ce.jus.br), são unidas compartilhando o mesmo Catálogo Global e o mesmo Esquema (Schema), elas formam:

A) Um Domínio Raiz.
B) Uma Unidade Organizacional (OU).
C) Um Site de Replicação.
D) Uma Floresta (Forest).
E) Um Trust Transitive Level 2.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: D

- A) Incorreta. Um Domínio Raiz é o primeiro domínio criado na floresta, não o conjunto delas.
- B) Incorreta. OU é para organização de usuários e computadores dentro de um domínio.
- C) Incorreta. Site refere-se à topologia física (rede, sub-redes) e não à estrutura lógica de namespaces.
- D) Correta. Uma Floresta é uma coleção de uma ou mais árvores de domínio que não compartilham necessariamente o mesmo namespace (nome de DNS contíguo), mas compartilham o mesmo Catálogo Global, configuração e schema.
- E) Incorreta. Relações de confiança (Trust) ocorrem, mas o termo arquitetural para o agrupamento é Floresta.

</details>

#### Questão 8 (Sistemas Operacionais)

No ambiente Windows Server, o administrador utiliza o PowerShell para automatizar tarefas. O cmdlet adequado para listar todos os serviços que estão no estado 'Parado' (Stopped) no servidor é:

A) Get-Service | Where-Object {$_.Status -eq 'Stopped'}
B) List-Service -Status Stopped
C) Show-Services | grep 'Stopped'
D) Get-Process -State Stopped
E) Find-Service -Condition Stopped

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: A

- A) Correta. O PowerShell utiliza a estrutura Verbo-Substantivo. `Get-Service` obtém os serviços, que são passados via pipeline (|) para o `Where-Object`, que filtra os objetos cujo atributo Status seja igual (`-eq`) a 'Stopped'.
- B) Incorreta. O verbo padrão para listagem é 'Get', não 'List'.
- C) Incorreta. Sintaxe mista de Linux (grep) não é nativa para manipulação de objetos PowerShell.
- D) Incorreta. Get-Process lista processos, não serviços.
- E) Incorreta. Find-Service não é um cmdlet padrão de administração local de serviços.

</details>

#### Questão 9 (Sistemas Operacionais)

Para centralizar a distribuição de patches de segurança e atualizações em uma rede corporativa Windows, economizando banda de internet e permitindo testes antes da homologação nas máquinas cliente, deve-se implementar o papel (role):

A) WDS (Windows Deployment Services).
B) WSUS (Windows Server Update Services).
C) IIS (Internet Information Services).
D) AD RMS (Active Directory Rights Management Services).
E) DNS Server.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. WDS é usado para instalação de sistemas operacionais via rede (imagens do Windows), não para atualizações mensais.
- B) Correta. O WSUS atua como um repositório central interno que baixa as atualizações da Microsoft e as distribui sob demanda/aprovação aos clientes da rede local.
- C) Incorreta. IIS é o servidor web do Windows.
- D) Incorreta. RMS gerencia direitos de proteção de documentos.
- E) Incorreta. DNS resolve nomes e IPs.

</details>

#### Questão 10 (Sistemas Operacionais)

Ao configurar o Catálogo Global (Global Catalog - GC) no Active Directory, o administrador deve ter em mente que:

A) O GC armazena uma cópia parcial dos objetos do seu próprio domínio e uma cópia completa de outros domínios.
B) Apenas o PDC Emulator pode atuar como servidor de Catálogo Global na Floresta.
C) O GC armazena uma cópia completa de todos os objetos de seu domínio anfitrião e uma cópia parcial (read-only) de objetos de todos os outros domínios da floresta.
D) O GC substitui o banco de dados NTDS.DIT, sendo incompatível com instâncias RODC (Read-Only Domain Controller).
E) Em uma floresta com 10 domínios, só é permitido existir fisicamente um servidor GC para evitar loops de replicação.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. É o inverso.
- B) Incorreta. Qualquer Domain Controller (DC) pode ser promovido a Global Catalog.
- C) Correta. O Catálogo Global agiliza as buscas na floresta inteira armazenando todos os atributos do próprio domínio e apenas atributos vitais (como nome de login, email) dos objetos dos demais domínios.
- D) Incorreta. O GC é armazenado DENTRO do ntds.dit. RODCs podem ser GCs parciais.
- E) Incorreta. É recomendado ter vários GCs para alta disponibilidade.

</details>

#### Questão 11 (Sistemas Operacionais)

O Analista 11 de Redes de um Tribunal precisa aplicar uma política de segurança (GPO) que desative o uso de pendrives para todos os usuários do departamento 'Processamento', que possui uma Unidade Organizacional (OU) própria. No entanto, ele notou que a política não está sendo aplicada. Verificando a estrutura, constatou-se que na raiz do Domínio existe uma política conflitante com a opção 'Bloquear Herança' habilitada. Para que a GPO da OU 'Processamento' seja aplicada sem alterar as configurações do Domínio, o administrador deve:

A) Habilitar a opção 'Enforced' (Forçado) na política de Domínio.
B) Nenhuma ação é necessária, pois políticas de OU (Unidade Organizacional) sempre têm precedência sobre políticas de Domínio pelo processamento LSDOU.
C) Mover a OU 'Processamento' para um novo Domínio na mesma Floresta.
D) Aplicar a política localmente via gpedit.msc em cada máquina do setor.
E) Configurar a GPO da OU com a opção 'Block Inheritance', invertendo a precedência.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. Se habilitar 'Enforced' no Domínio, a política superior forçará sua aplicação, sobrescrevendo a OU.
- B) Correta. A ordem de processamento de GPOs é LSDOU (Local, Site, Domain, OU). A última a ser processada é a OU, logo, ela tem precedência sobre o Domínio. 'Bloquear Herança' é uma configuração feita na OU inferior para barrar políticas superiores, não o contrário. A política da OU vencerá a do Domínio naturalmente, a menos que a do Domínio estivesse como 'Enforced'.
- C) Incorreta. Ação desnecessária e arquiteturalmente drástica.
- D) Incorreta. Quebraria o propósito da administração centralizada.
- E) Incorreta. Bloquear herança impede que políticas venham de cima, mas não inverte a precedência da que foi aplicada na própria OU.

</details>

#### Questão 12 (Sistemas Operacionais)

O AD DS (cenário 12) (AD DS) utiliza uma estrutura hierárquica lógica. Quando múltiplas Árvores (Trees) de domínios, que possuem diferentes namespaces contíguos (ex: tjce.jus.br e tre-ce.jus.br), são unidas compartilhando o mesmo Catálogo Global e o mesmo Esquema (Schema), elas formam:

A) Um Domínio Raiz.
B) Uma Unidade Organizacional (OU).
C) Um Site de Replicação.
D) Uma Floresta (Forest).
E) Um Trust Transitive Level 2.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: D

- A) Incorreta. Um Domínio Raiz é o primeiro domínio criado na floresta, não o conjunto delas.
- B) Incorreta. OU é para organização de usuários e computadores dentro de um domínio.
- C) Incorreta. Site refere-se à topologia física (rede, sub-redes) e não à estrutura lógica de namespaces.
- D) Correta. Uma Floresta é uma coleção de uma ou mais árvores de domínio que não compartilham necessariamente o mesmo namespace (nome de DNS contíguo), mas compartilham o mesmo Catálogo Global, configuração e schema.
- E) Incorreta. Relações de confiança (Trust) ocorrem, mas o termo arquitetural para o agrupamento é Floresta.

</details>

#### Questão 13 (Sistemas Operacionais)

No ambiente Windows Server, o administrador utiliza o PowerShell para automatizar tarefas. O cmdlet adequado para listar todos os serviços que estão no estado 'Parado' (Stopped) no servidor é:

A) Get-Service | Where-Object {$_.Status -eq 'Stopped'}
B) List-Service -Status Stopped
C) Show-Services | grep 'Stopped'
D) Get-Process -State Stopped
E) Find-Service -Condition Stopped

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: A

- A) Correta. O PowerShell utiliza a estrutura Verbo-Substantivo. `Get-Service` obtém os serviços, que são passados via pipeline (|) para o `Where-Object`, que filtra os objetos cujo atributo Status seja igual (`-eq`) a 'Stopped'.
- B) Incorreta. O verbo padrão para listagem é 'Get', não 'List'.
- C) Incorreta. Sintaxe mista de Linux (grep) não é nativa para manipulação de objetos PowerShell.
- D) Incorreta. Get-Process lista processos, não serviços.
- E) Incorreta. Find-Service não é um cmdlet padrão de administração local de serviços.

</details>

#### Questão 14 (Sistemas Operacionais)

Para centralizar a distribuição de patches de segurança e atualizações em uma rede corporativa Windows, economizando banda de internet e permitindo testes antes da homologação nas máquinas cliente, deve-se implementar o papel (role):

A) WDS (Windows Deployment Services).
B) WSUS (Windows Server Update Services).
C) IIS (Internet Information Services).
D) AD RMS (Active Directory Rights Management Services).
E) DNS Server.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. WDS é usado para instalação de sistemas operacionais via rede (imagens do Windows), não para atualizações mensais.
- B) Correta. O WSUS atua como um repositório central interno que baixa as atualizações da Microsoft e as distribui sob demanda/aprovação aos clientes da rede local.
- C) Incorreta. IIS é o servidor web do Windows.
- D) Incorreta. RMS gerencia direitos de proteção de documentos.
- E) Incorreta. DNS resolve nomes e IPs.

</details>

#### Questão 15 (Sistemas Operacionais)

Ao configurar o Catálogo Global (Global Catalog - GC) no Active Directory, o administrador deve ter em mente que:

A) O GC armazena uma cópia parcial dos objetos do seu próprio domínio e uma cópia completa de outros domínios.
B) Apenas o PDC Emulator pode atuar como servidor de Catálogo Global na Floresta.
C) O GC armazena uma cópia completa de todos os objetos de seu domínio anfitrião e uma cópia parcial (read-only) de objetos de todos os outros domínios da floresta.
D) O GC substitui o banco de dados NTDS.DIT, sendo incompatível com instâncias RODC (Read-Only Domain Controller).
E) Em uma floresta com 10 domínios, só é permitido existir fisicamente um servidor GC para evitar loops de replicação.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. É o inverso.
- B) Incorreta. Qualquer Domain Controller (DC) pode ser promovido a Global Catalog.
- C) Correta. O Catálogo Global agiliza as buscas na floresta inteira armazenando todos os atributos do próprio domínio e apenas atributos vitais (como nome de login, email) dos objetos dos demais domínios.
- D) Incorreta. O GC é armazenado DENTRO do ntds.dit. RODCs podem ser GCs parciais.
- E) Incorreta. É recomendado ter vários GCs para alta disponibilidade.

</details>

### Tema 2: Segurança da Informação

#### Questão 16 (Segurança da Informação)

Um equipamento de firewall (cenário 16) que opera validando estritamente os pacotes pelas regras de Access Control Lists (ACLs) baseando-se no endereço IP de origem/destino e portas, sem manter em memória o contexto das conexões já estabelecidas, é classificado como:

A) Proxy reverso.
B) Stateful Inspection (Inspeção de Estados).
C) Stateless Firewall (Filtro de Pacotes).
D) WAF (Web Application Firewall).
E) UTM (Unified Threat Management).

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. Proxy atua mediando a conexão na camada de aplicação.
- B) Incorreta. Stateful lembra o estado das conexões TCP (Estabelecida, Nova), permitindo o retorno automático sem regra explícita.
- C) Correta. O firewall de Filtro de Pacotes (Stateless) não guarda estado de sessão. Se uma requisição sai pela porta 80, o administrador deve criar uma regra permitindo a ida e outra regra explícita permitindo a volta.
- D) Incorreta. WAF atua na camada 7 protegendo aplicações web de injeções e ataques semânticos.
- E) Incorreta. UTM é uma caixa unificada com diversos serviços (antivírus, IPS, VPN).

</details>

#### Questão 17 (Segurança da Informação)

Um ativo de segurança (cenário 17) foi posicionado em modo espelho ('port mirroring' / SPAN) conectado ao switch principal (Core). Ele analisa todo o tráfego da rede corporativa emitindo alertas ao SOC (Security Operations Center) quando um tráfego anômalo é identificado, mas não realiza qualquer bloqueio da comunicação. Este equipamento é um:

A) IPS (Intrusion Prevention System).
B) NAC (Network Access Control).
C) Firewall NGFW (Next Generation).
D) IDS (Intrusion Detection System).
E) Honeypot.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: D

- A) Incorreta. IPS atua 'em linha' (inline) e tem poder ativo de dropar/bloquear pacotes.
- B) Incorreta. NAC checa a postura de segurança (antivírus, atualizações) de um computador antes de ele entrar na rede.
- C) Incorreta. NGFWs atuam ativamente como gateway da rede.
- D) Correta. O IDS (Detection) apenas monitora de forma passiva (geralmente via espelhamento de porta). Quando detecta ameaça, gera log e alerta, mas o pacote malicioso já chegou ao destino porque o IDS não está no caminho físico da transmissão.
- E) Incorreta. Honeypot é um sistema-isca deliberadamente vulnerável para atrair atacantes.

</details>

#### Questão 18 (Segurança da Informação)

Na arquitetura de segurança de perímetro, a DMZ (Demilitarized Zone) tem como função principal:

A) Isolar os servidores de banco de dados críticos da empresa, impedindo que sejam acessados até mesmo pela LAN interna.
B) Conectar diretamente os switches de Core e Distribuição sem regras de firewall.
C) Hospedar os servidores e serviços que precisam ser acessíveis ao público via Internet, protegendo e isolando a rede corporativa interna.
D) Hospedar servidores proxy cuja função é anonimizar os acessos originados na Internet em direção aos usuários internos.
E) Armazenar logs em servidores Syslog offline inacessíveis.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. Bancos de dados críticos não ficam na DMZ, ficam na rede interna (backend) protegidos por firewall.
- B) Incorreta. DMZ exige regras rígidas de firewall (uma na frente para a Internet, outra atrás para a LAN).
- C) Correta. A DMZ abriga serviços expostos (Web, DNS Público, SMTP). Se forem comprometidos, o invasor estará confinado na DMZ e terá extrema dificuldade de pular para a LAN corporativa interna.
- D) Incorreta. Proxy reverso pode ficar na DMZ, mas a função descrita (anonimizar Internet para interno) está conceitualmente equivocada.
- E) Incorreta. Syslogs críticos ficam na LAN de gerência.

</details>

#### Questão 19 (Segurança da Informação)

Sistemas de Detecção de Intrusão (IDS) baseados em anomalias (Anomaly-based) têm a seguinte característica em comparação aos baseados em assinaturas (Signature-based):

A) Possuem incapacidade técnica de gerar falsos positivos.
B) São mais eficazes na detecção de ataques do tipo Zero-day (desconhecidos).
C) Dependem exclusivamente de atualizações diárias de bancos de hashes do fabricante.
D) Consomem drasticamente menos processamento da CPU do que os baseados em assinatura.
E) Só operam bloqueando pacotes de forma ativa na camada de Aplicação.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. Pelo contrário, sistemas por anomalia geram MUITOS falsos positivos, pois qualquer mudança lícita de tráfego é vista como anomalia.
- B) Correta. Como eles criam uma linha de base (baseline) do normal da rede, qualquer comportamento muito estranho (ataque inédito - zero day) soará o alerta, sem precisar que a vacina (assinatura) já tenha sido criada.
- C) Incorreta. IDS por assinatura é que depende de hashes/regras do fabricante.
- D) Incorreta. Analisar comportamento via estatística ou IA gasta muito processamento.
- E) Incorreta. IDS não bloqueia (isso é IPS).

</details>

#### Questão 20 (Segurança da Informação)

O Network Access Control (NAC) utilizando o protocolo 802.1X é largamente adotado no padrão Enterprise de segurança corporativa. A função primordial do protocolo 802.1X no contexto do NAC é:

A) Garantir a criptografia ponta-a-ponta na camada de Enlace.
B) Isolar vírus do tipo Ransomware usando análise estática de binários.
C) Realizar a autenticação do dispositivo na porta física ou lógica do switch/access point antes de liberar o acesso total à LAN.
D) Substituir o serviço de Active Directory (AD DS) para autenticação LDAP.
E) Interceptar requisições HTTP e HTTPS buscando por injeção SQL.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. O foco do 802.1x é controle de acesso (autenticação baseada em porta).
- B) Incorreta. O NAC até checa se há antivírus na máquina (avaliação de postura), mas a tecnologia 802.1x em si não faz a detecção do malware.
- C) Correta. No protocolo 802.1x, a porta da rede fica fechada. O Suplicante (cliente) envia suas credenciais para o Autenticador (Switch), que repassa ao Servidor de Autenticação (RADIUS). Só após o 'OK' a porta libera o tráfego de dados.
- D) Incorreta. O RADIUS costuma integrar com o AD, e não substituí-lo.
- E) Incorreta. Isso é função do WAF.

</details>

#### Questão 21 (Segurança da Informação)

Um equipamento de firewall (cenário 21) que opera validando estritamente os pacotes pelas regras de Access Control Lists (ACLs) baseando-se no endereço IP de origem/destino e portas, sem manter em memória o contexto das conexões já estabelecidas, é classificado como:

A) Proxy reverso.
B) Stateful Inspection (Inspeção de Estados).
C) Stateless Firewall (Filtro de Pacotes).
D) WAF (Web Application Firewall).
E) UTM (Unified Threat Management).

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. Proxy atua mediando a conexão na camada de aplicação.
- B) Incorreta. Stateful lembra o estado das conexões TCP (Estabelecida, Nova), permitindo o retorno automático sem regra explícita.
- C) Correta. O firewall de Filtro de Pacotes (Stateless) não guarda estado de sessão. Se uma requisição sai pela porta 80, o administrador deve criar uma regra permitindo a ida e outra regra explícita permitindo a volta.
- D) Incorreta. WAF atua na camada 7 protegendo aplicações web de injeções e ataques semânticos.
- E) Incorreta. UTM é uma caixa unificada com diversos serviços (antivírus, IPS, VPN).

</details>

#### Questão 22 (Segurança da Informação)

Um ativo de segurança (cenário 22) foi posicionado em modo espelho ('port mirroring' / SPAN) conectado ao switch principal (Core). Ele analisa todo o tráfego da rede corporativa emitindo alertas ao SOC (Security Operations Center) quando um tráfego anômalo é identificado, mas não realiza qualquer bloqueio da comunicação. Este equipamento é um:

A) IPS (Intrusion Prevention System).
B) NAC (Network Access Control).
C) Firewall NGFW (Next Generation).
D) IDS (Intrusion Detection System).
E) Honeypot.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: D

- A) Incorreta. IPS atua 'em linha' (inline) e tem poder ativo de dropar/bloquear pacotes.
- B) Incorreta. NAC checa a postura de segurança (antivírus, atualizações) de um computador antes de ele entrar na rede.
- C) Incorreta. NGFWs atuam ativamente como gateway da rede.
- D) Correta. O IDS (Detection) apenas monitora de forma passiva (geralmente via espelhamento de porta). Quando detecta ameaça, gera log e alerta, mas o pacote malicioso já chegou ao destino porque o IDS não está no caminho físico da transmissão.
- E) Incorreta. Honeypot é um sistema-isca deliberadamente vulnerável para atrair atacantes.

</details>

#### Questão 23 (Segurança da Informação)

Na arquitetura de segurança de perímetro, a DMZ (Demilitarized Zone) tem como função principal:

A) Isolar os servidores de banco de dados críticos da empresa, impedindo que sejam acessados até mesmo pela LAN interna.
B) Conectar diretamente os switches de Core e Distribuição sem regras de firewall.
C) Hospedar os servidores e serviços que precisam ser acessíveis ao público via Internet, protegendo e isolando a rede corporativa interna.
D) Hospedar servidores proxy cuja função é anonimizar os acessos originados na Internet em direção aos usuários internos.
E) Armazenar logs em servidores Syslog offline inacessíveis.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. Bancos de dados críticos não ficam na DMZ, ficam na rede interna (backend) protegidos por firewall.
- B) Incorreta. DMZ exige regras rígidas de firewall (uma na frente para a Internet, outra atrás para a LAN).
- C) Correta. A DMZ abriga serviços expostos (Web, DNS Público, SMTP). Se forem comprometidos, o invasor estará confinado na DMZ e terá extrema dificuldade de pular para a LAN corporativa interna.
- D) Incorreta. Proxy reverso pode ficar na DMZ, mas a função descrita (anonimizar Internet para interno) está conceitualmente equivocada.
- E) Incorreta. Syslogs críticos ficam na LAN de gerência.

</details>

#### Questão 24 (Segurança da Informação)

Sistemas de Detecção de Intrusão (IDS) baseados em anomalias (Anomaly-based) têm a seguinte característica em comparação aos baseados em assinaturas (Signature-based):

A) Possuem incapacidade técnica de gerar falsos positivos.
B) São mais eficazes na detecção de ataques do tipo Zero-day (desconhecidos).
C) Dependem exclusivamente de atualizações diárias de bancos de hashes do fabricante.
D) Consomem drasticamente menos processamento da CPU do que os baseados em assinatura.
E) Só operam bloqueando pacotes de forma ativa na camada de Aplicação.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. Pelo contrário, sistemas por anomalia geram MUITOS falsos positivos, pois qualquer mudança lícita de tráfego é vista como anomalia.
- B) Correta. Como eles criam uma linha de base (baseline) do normal da rede, qualquer comportamento muito estranho (ataque inédito - zero day) soará o alerta, sem precisar que a vacina (assinatura) já tenha sido criada.
- C) Incorreta. IDS por assinatura é que depende de hashes/regras do fabricante.
- D) Incorreta. Analisar comportamento via estatística ou IA gasta muito processamento.
- E) Incorreta. IDS não bloqueia (isso é IPS).

</details>

#### Questão 25 (Segurança da Informação)

O Network Access Control (NAC) utilizando o protocolo 802.1X é largamente adotado no padrão Enterprise de segurança corporativa. A função primordial do protocolo 802.1X no contexto do NAC é:

A) Garantir a criptografia ponta-a-ponta na camada de Enlace.
B) Isolar vírus do tipo Ransomware usando análise estática de binários.
C) Realizar a autenticação do dispositivo na porta física ou lógica do switch/access point antes de liberar o acesso total à LAN.
D) Substituir o serviço de Active Directory (AD DS) para autenticação LDAP.
E) Interceptar requisições HTTP e HTTPS buscando por injeção SQL.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. O foco do 802.1x é controle de acesso (autenticação baseada em porta).
- B) Incorreta. O NAC até checa se há antivírus na máquina (avaliação de postura), mas a tecnologia 802.1x em si não faz a detecção do malware.
- C) Correta. No protocolo 802.1x, a porta da rede fica fechada. O Suplicante (cliente) envia suas credenciais para o Autenticador (Switch), que repassa ao Servidor de Autenticação (RADIUS). Só após o 'OK' a porta libera o tráfego de dados.
- D) Incorreta. O RADIUS costuma integrar com o AD, e não substituí-lo.
- E) Incorreta. Isso é função do WAF.

</details>

#### Questão 26 (Segurança da Informação)

Um equipamento de firewall (cenário 26) que opera validando estritamente os pacotes pelas regras de Access Control Lists (ACLs) baseando-se no endereço IP de origem/destino e portas, sem manter em memória o contexto das conexões já estabelecidas, é classificado como:

A) Proxy reverso.
B) Stateful Inspection (Inspeção de Estados).
C) Stateless Firewall (Filtro de Pacotes).
D) WAF (Web Application Firewall).
E) UTM (Unified Threat Management).

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. Proxy atua mediando a conexão na camada de aplicação.
- B) Incorreta. Stateful lembra o estado das conexões TCP (Estabelecida, Nova), permitindo o retorno automático sem regra explícita.
- C) Correta. O firewall de Filtro de Pacotes (Stateless) não guarda estado de sessão. Se uma requisição sai pela porta 80, o administrador deve criar uma regra permitindo a ida e outra regra explícita permitindo a volta.
- D) Incorreta. WAF atua na camada 7 protegendo aplicações web de injeções e ataques semânticos.
- E) Incorreta. UTM é uma caixa unificada com diversos serviços (antivírus, IPS, VPN).

</details>

#### Questão 27 (Segurança da Informação)

Um ativo de segurança (cenário 27) foi posicionado em modo espelho ('port mirroring' / SPAN) conectado ao switch principal (Core). Ele analisa todo o tráfego da rede corporativa emitindo alertas ao SOC (Security Operations Center) quando um tráfego anômalo é identificado, mas não realiza qualquer bloqueio da comunicação. Este equipamento é um:

A) IPS (Intrusion Prevention System).
B) NAC (Network Access Control).
C) Firewall NGFW (Next Generation).
D) IDS (Intrusion Detection System).
E) Honeypot.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: D

- A) Incorreta. IPS atua 'em linha' (inline) e tem poder ativo de dropar/bloquear pacotes.
- B) Incorreta. NAC checa a postura de segurança (antivírus, atualizações) de um computador antes de ele entrar na rede.
- C) Incorreta. NGFWs atuam ativamente como gateway da rede.
- D) Correta. O IDS (Detection) apenas monitora de forma passiva (geralmente via espelhamento de porta). Quando detecta ameaça, gera log e alerta, mas o pacote malicioso já chegou ao destino porque o IDS não está no caminho físico da transmissão.
- E) Incorreta. Honeypot é um sistema-isca deliberadamente vulnerável para atrair atacantes.

</details>

#### Questão 28 (Segurança da Informação)

Na arquitetura de segurança de perímetro, a DMZ (Demilitarized Zone) tem como função principal:

A) Isolar os servidores de banco de dados críticos da empresa, impedindo que sejam acessados até mesmo pela LAN interna.
B) Conectar diretamente os switches de Core e Distribuição sem regras de firewall.
C) Hospedar os servidores e serviços que precisam ser acessíveis ao público via Internet, protegendo e isolando a rede corporativa interna.
D) Hospedar servidores proxy cuja função é anonimizar os acessos originados na Internet em direção aos usuários internos.
E) Armazenar logs em servidores Syslog offline inacessíveis.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. Bancos de dados críticos não ficam na DMZ, ficam na rede interna (backend) protegidos por firewall.
- B) Incorreta. DMZ exige regras rígidas de firewall (uma na frente para a Internet, outra atrás para a LAN).
- C) Correta. A DMZ abriga serviços expostos (Web, DNS Público, SMTP). Se forem comprometidos, o invasor estará confinado na DMZ e terá extrema dificuldade de pular para a LAN corporativa interna.
- D) Incorreta. Proxy reverso pode ficar na DMZ, mas a função descrita (anonimizar Internet para interno) está conceitualmente equivocada.
- E) Incorreta. Syslogs críticos ficam na LAN de gerência.

</details>

#### Questão 29 (Segurança da Informação)

Sistemas de Detecção de Intrusão (IDS) baseados em anomalias (Anomaly-based) têm a seguinte característica em comparação aos baseados em assinaturas (Signature-based):

A) Possuem incapacidade técnica de gerar falsos positivos.
B) São mais eficazes na detecção de ataques do tipo Zero-day (desconhecidos).
C) Dependem exclusivamente de atualizações diárias de bancos de hashes do fabricante.
D) Consomem drasticamente menos processamento da CPU do que os baseados em assinatura.
E) Só operam bloqueando pacotes de forma ativa na camada de Aplicação.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. Pelo contrário, sistemas por anomalia geram MUITOS falsos positivos, pois qualquer mudança lícita de tráfego é vista como anomalia.
- B) Correta. Como eles criam uma linha de base (baseline) do normal da rede, qualquer comportamento muito estranho (ataque inédito - zero day) soará o alerta, sem precisar que a vacina (assinatura) já tenha sido criada.
- C) Incorreta. IDS por assinatura é que depende de hashes/regras do fabricante.
- D) Incorreta. Analisar comportamento via estatística ou IA gasta muito processamento.
- E) Incorreta. IDS não bloqueia (isso é IPS).

</details>

#### Questão 30 (Segurança da Informação)

O Network Access Control (NAC) utilizando o protocolo 802.1X é largamente adotado no padrão Enterprise de segurança corporativa. A função primordial do protocolo 802.1X no contexto do NAC é:

A) Garantir a criptografia ponta-a-ponta na camada de Enlace.
B) Isolar vírus do tipo Ransomware usando análise estática de binários.
C) Realizar a autenticação do dispositivo na porta física ou lógica do switch/access point antes de liberar o acesso total à LAN.
D) Substituir o serviço de Active Directory (AD DS) para autenticação LDAP.
E) Interceptar requisições HTTP e HTTPS buscando por injeção SQL.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. O foco do 802.1x é controle de acesso (autenticação baseada em porta).
- B) Incorreta. O NAC até checa se há antivírus na máquina (avaliação de postura), mas a tecnologia 802.1x em si não faz a detecção do malware.
- C) Correta. No protocolo 802.1x, a porta da rede fica fechada. O Suplicante (cliente) envia suas credenciais para o Autenticador (Switch), que repassa ao Servidor de Autenticação (RADIUS). Só após o 'OK' a porta libera o tráfego de dados.
- D) Incorreta. O RADIUS costuma integrar com o AD, e não substituí-lo.
- E) Incorreta. Isso é função do WAF.

</details>

### Tema 3: Raciocínio Lógico Matemático (RLM)

#### Questão 31 (Raciocínio Lógico)

Assuma que as seguintes premissas são verdadeiras:
1. Todo analista de sistemas sabe programar.
2. Alguns peritos criminais são analistas de sistemas.

Com base exclusivamente nestas premissas, é correto concluir, segundo os diagramas lógicos, que:

A) Todo perito criminal sabe programar.
B) Qualquer pessoa que sabe programar é perito criminal.
C) Alguns peritos criminais sabem programar.
D) Nenhum analista de sistemas é perito criminal.
E) Todos os analistas de sistemas são peritos criminais.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. Apenas ALGUNS peritos são analistas, logo, não se pode garantir que TODOS os peritos sabem programar.
- B) Incorreta. A programação é conjunto maior. Pode haver programadores que não são analistas nem peritos.
- C) Correta. Desenhando os diagramas: O conjunto 'Analistas' (A) está dentro de 'Sabe Programar' (S). O conjunto 'Peritos' (P) intercepta o conjunto A. A região de intersecção entre P e A está obrigatoriamente dentro de S. Logo, alguns peritos (os que são analistas) certamente sabem programar.
- D) Incorreta. Contradiz diretamente a premissa 2.
- E) Incorreta. A intersecção é 'alguns', não abrange o conjunto todo.

</details>

#### Questão 32 (Raciocínio Lógico)

Um determinado projeto de desenvolvimento no Tribunal demanda 6 programadores, trabalhando 8 horas por dia, para construir 40 telas de sistema em 10 dias. Para finalizar um novo módulo de 60 telas em apenas 5 dias, assumindo que a produtividade não se altera e trabalhando 10 horas por dia, a quantidade total de programadores necessários será de:

A) 8 programadores.
B) 10 programadores.
C) 12 programadores.
D) 15 programadores.
E) 6 programadores.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

Aplicando Regra de Três Composta. Separando as grandezas em CAUSAS (esforço) e EFEITOS (telas):
Situação 1: Prog = 5, Horas = 8, Dias = 10. Efeito: 40 telas.
Situação 2: Prog = X, Horas = 10, Dias = 5. Efeito: 60 telas.
Fórmula (Produto das Causas / Efeito):
(5 * 8 * 10) / 40 = (X * 10 * 5) / 60
400 / 40 = 50X / 60
10 = 5X / 6
60 = 5X => X = 12 programadores.
- C) Correta.

</details>

#### Questão 33 (Raciocínio Lógico)

Para renovar o parque de máquinas, o setor de licitações obteve um desconto de 20% no valor de tabela dos computadores. Semanas depois, devido a um pagamento à vista, o fornecedor concedeu mais um desconto sucessivo de 10% sobre o novo valor faturado. Qual foi o percentual de desconto real (único e equivalente) obtido sobre o valor inicial de tabela?

A) 30%.
B) 28%.
C) 32%.
D) 18%.
E) 22%.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

Nunca some os percentuais (20% + 10% = 30% está errado na FCC).
Fórmula por Fatores de Multiplicação:
1º Desconto de 20% = Fator (1 - 0.20) = 0.80.
2º Desconto de 10% = Fator (1 - 0.10) = 0.90.
Fator Total = 0.80 * 0.90 = 0.72.
Fator de 0.72 significa que se pagou 72% do preço original.
Logo, o desconto real foi: 100% - 72% = 28%.
- B) Correta.

</details>

#### Questão 34 (Raciocínio Lógico)

Em uma repartição pública trabalham 120 servidores. Sabe-se que 60% deles possuem certificação ITIL, e 45% possuem certificação COBIT. Se 15% dos servidores não possuem nenhuma das duas certificações, a quantidade exata de servidores que possuem AMBAS as certificações (ITIL e COBIT) é igual a:

A) 18.
B) 30.
C) 24.
D) 12.
E) 36.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

Resolução via Conjuntos.
Total = 120 servidores (100%).
Não têm nada = 15%.
Logo, quem tem pelo menos uma certificação = 100% - 15% = 85%.
Somando as partes: ITIL (60%) + COBIT (45%) = 105%.
A intersecção (os que têm ambas) é o que excede a união: 105% - 85% = 20%.
Cálculo final: 20% de 120 servidores = 0.2 * 120 = 24 servidores.
- C) Correta.

</details>

#### Questão 35 (Raciocínio Lógico)

Assuma as premissas lógicas:
- Nenhum peixe voa.
- Alguns mamíferos voam (como os morcegos).

A conclusão que obrigatoriamente se deduz, validada por Diagramas de Euler-Venn, é:

A) Todo animal que voa é mamífero.
B) Alguns mamíferos não são peixes.
C) Todo peixe é mamífero.
D) Nenhum mamífero é peixe.
E) Alguns peixes voam se não forem mamíferos.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. Existem aves e insetos, a premissa fala apenas de mamíferos.
- B) Correta. O conjunto dos Peixes e o conjunto dos Seres que Voam (V) são totalmente separados (Nenhum peixe voa). A premissa 2 diz que ALGUNS mamíferos (M) estão dentro de V. Ora, se esses mamíferos que voam estão dentro de V, e V é totalmente separado dos Peixes, esses morcegos (mamíferos que voam) definitivamente NÃO são peixes. Logo, pelo menos ALGUNS mamíferos (aqueles que voam) não são peixes.
- C) Incorreta. Nada na premissa junta o grupo inteiro de peixes e mamíferos.
- D) Incorreta. Pode haver, no silogismo, mamíferos marinhos (baleias) que interceptem o conjunto de peixes (lógica formal não avalia biologia da vida real, apenas os conjuntos dados). O silogismo não garante que *nenhum* mamífero seja peixe.
- E) Incorreta. Fere a primeira premissa.

</details>

#### Questão 36 (Raciocínio Lógico)

Assuma que as seguintes premissas são verdadeiras:
1. Todo analista de sistemas sabe programar.
2. Alguns peritos criminais são analistas de sistemas.

Com base exclusivamente nestas premissas, é correto concluir, segundo os diagramas lógicos, que:

A) Todo perito criminal sabe programar.
B) Qualquer pessoa que sabe programar é perito criminal.
C) Alguns peritos criminais sabem programar.
D) Nenhum analista de sistemas é perito criminal.
E) Todos os analistas de sistemas são peritos criminais.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. Apenas ALGUNS peritos são analistas, logo, não se pode garantir que TODOS os peritos sabem programar.
- B) Incorreta. A programação é conjunto maior. Pode haver programadores que não são analistas nem peritos.
- C) Correta. Desenhando os diagramas: O conjunto 'Analistas' (A) está dentro de 'Sabe Programar' (S). O conjunto 'Peritos' (P) intercepta o conjunto A. A região de intersecção entre P e A está obrigatoriamente dentro de S. Logo, alguns peritos (os que são analistas) certamente sabem programar.
- D) Incorreta. Contradiz diretamente a premissa 2.
- E) Incorreta. A intersecção é 'alguns', não abrange o conjunto todo.

</details>

#### Questão 37 (Raciocínio Lógico)

Um determinado projeto de desenvolvimento no Tribunal demanda 5 programadores, trabalhando 8 horas por dia, para construir 40 telas de sistema em 10 dias. Para finalizar um novo módulo de 60 telas em apenas 5 dias, assumindo que a produtividade não se altera e trabalhando 10 horas por dia, a quantidade total de programadores necessários será de:

A) 8 programadores.
B) 10 programadores.
C) 12 programadores.
D) 15 programadores.
E) 6 programadores.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

Aplicando Regra de Três Composta. Separando as grandezas em CAUSAS (esforço) e EFEITOS (telas):
Situação 1: Prog = 5, Horas = 8, Dias = 10. Efeito: 40 telas.
Situação 2: Prog = X, Horas = 10, Dias = 5. Efeito: 60 telas.
Fórmula (Produto das Causas / Efeito):
(5 * 8 * 10) / 40 = (X * 10 * 5) / 60
400 / 40 = 50X / 60
10 = 5X / 6
60 = 5X => X = 12 programadores.
- C) Correta.

</details>

#### Questão 38 (Raciocínio Lógico)

Para renovar o parque de máquinas, o setor de licitações obteve um desconto de 20% no valor de tabela dos computadores. Semanas depois, devido a um pagamento à vista, o fornecedor concedeu mais um desconto sucessivo de 10% sobre o novo valor faturado. Qual foi o percentual de desconto real (único e equivalente) obtido sobre o valor inicial de tabela?

A) 30%.
B) 28%.
C) 32%.
D) 18%.
E) 22%.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

Nunca some os percentuais (20% + 10% = 30% está errado na FCC).
Fórmula por Fatores de Multiplicação:
1º Desconto de 20% = Fator (1 - 0.20) = 0.80.
2º Desconto de 10% = Fator (1 - 0.10) = 0.90.
Fator Total = 0.80 * 0.90 = 0.72.
Fator de 0.72 significa que se pagou 72% do preço original.
Logo, o desconto real foi: 100% - 72% = 28%.
- B) Correta.

</details>

#### Questão 39 (Raciocínio Lógico)

Em uma repartição pública trabalham 120 servidores. Sabe-se que 60% deles possuem certificação ITIL, e 45% possuem certificação COBIT. Se 15% dos servidores não possuem nenhuma das duas certificações, a quantidade exata de servidores que possuem AMBAS as certificações (ITIL e COBIT) é igual a:

A) 18.
B) 30.
C) 24.
D) 12.
E) 36.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

Resolução via Conjuntos.
Total = 120 servidores (100%).
Não têm nada = 15%.
Logo, quem tem pelo menos uma certificação = 100% - 15% = 85%.
Somando as partes: ITIL (60%) + COBIT (45%) = 105%.
A intersecção (os que têm ambas) é o que excede a união: 105% - 85% = 20%.
Cálculo final: 20% de 120 servidores = 0.2 * 120 = 24 servidores.
- C) Correta.

</details>

#### Questão 40 (Raciocínio Lógico)

Assuma as premissas lógicas:
- Nenhum peixe voa.
- Alguns mamíferos voam (como os morcegos).

A conclusão que obrigatoriamente se deduz, validada por Diagramas de Euler-Venn, é:

A) Todo animal que voa é mamífero.
B) Alguns mamíferos não são peixes.
C) Todo peixe é mamífero.
D) Nenhum mamífero é peixe.
E) Alguns peixes voam se não forem mamíferos.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. Existem aves e insetos, a premissa fala apenas de mamíferos.
- B) Correta. O conjunto dos Peixes e o conjunto dos Seres que Voam (V) são totalmente separados (Nenhum peixe voa). A premissa 2 diz que ALGUNS mamíferos (M) estão dentro de V. Ora, se esses mamíferos que voam estão dentro de V, e V é totalmente separado dos Peixes, esses morcegos (mamíferos que voam) definitivamente NÃO são peixes. Logo, pelo menos ALGUNS mamíferos (aqueles que voam) não são peixes.
- C) Incorreta. Nada na premissa junta o grupo inteiro de peixes e mamíferos.
- D) Incorreta. Pode haver, no silogismo, mamíferos marinhos (baleias) que interceptem o conjunto de peixes (lógica formal não avalia biologia da vida real, apenas os conjuntos dados). O silogismo não garante que *nenhum* mamífero seja peixe.
- E) Incorreta. Fere a primeira premissa.

</details>

#### Questão 41 (Raciocínio Lógico)

Assuma que as seguintes premissas são verdadeiras:
1. Todo analista de sistemas sabe programar.
2. Alguns peritos criminais são analistas de sistemas.

Com base exclusivamente nestas premissas, é correto concluir, segundo os diagramas lógicos, que:

A) Todo perito criminal sabe programar.
B) Qualquer pessoa que sabe programar é perito criminal.
C) Alguns peritos criminais sabem programar.
D) Nenhum analista de sistemas é perito criminal.
E) Todos os analistas de sistemas são peritos criminais.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

- A) Incorreta. Apenas ALGUNS peritos são analistas, logo, não se pode garantir que TODOS os peritos sabem programar.
- B) Incorreta. A programação é conjunto maior. Pode haver programadores que não são analistas nem peritos.
- C) Correta. Desenhando os diagramas: O conjunto 'Analistas' (A) está dentro de 'Sabe Programar' (S). O conjunto 'Peritos' (P) intercepta o conjunto A. A região de intersecção entre P e A está obrigatoriamente dentro de S. Logo, alguns peritos (os que são analistas) certamente sabem programar.
- D) Incorreta. Contradiz diretamente a premissa 2.
- E) Incorreta. A intersecção é 'alguns', não abrange o conjunto todo.

</details>

#### Questão 42 (Raciocínio Lógico)

Um determinado projeto de desenvolvimento no Tribunal demanda 7 programadores, trabalhando 8 horas por dia, para construir 40 telas de sistema em 10 dias. Para finalizar um novo módulo de 60 telas em apenas 5 dias, assumindo que a produtividade não se altera e trabalhando 10 horas por dia, a quantidade total de programadores necessários será de:

A) 8 programadores.
B) 10 programadores.
C) 12 programadores.
D) 15 programadores.
E) 6 programadores.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

Aplicando Regra de Três Composta. Separando as grandezas em CAUSAS (esforço) e EFEITOS (telas):
Situação 1: Prog = 5, Horas = 8, Dias = 10. Efeito: 40 telas.
Situação 2: Prog = X, Horas = 10, Dias = 5. Efeito: 60 telas.
Fórmula (Produto das Causas / Efeito):
(5 * 8 * 10) / 40 = (X * 10 * 5) / 60
400 / 40 = 50X / 60
10 = 5X / 6
60 = 5X => X = 12 programadores.
- C) Correta.

</details>

#### Questão 43 (Raciocínio Lógico)

Para renovar o parque de máquinas, o setor de licitações obteve um desconto de 20% no valor de tabela dos computadores. Semanas depois, devido a um pagamento à vista, o fornecedor concedeu mais um desconto sucessivo de 10% sobre o novo valor faturado. Qual foi o percentual de desconto real (único e equivalente) obtido sobre o valor inicial de tabela?

A) 30%.
B) 28%.
C) 32%.
D) 18%.
E) 22%.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

Nunca some os percentuais (20% + 10% = 30% está errado na FCC).
Fórmula por Fatores de Multiplicação:
1º Desconto de 20% = Fator (1 - 0.20) = 0.80.
2º Desconto de 10% = Fator (1 - 0.10) = 0.90.
Fator Total = 0.80 * 0.90 = 0.72.
Fator de 0.72 significa que se pagou 72% do preço original.
Logo, o desconto real foi: 100% - 72% = 28%.
- B) Correta.

</details>

#### Questão 44 (Raciocínio Lógico)

Em uma repartição pública trabalham 120 servidores. Sabe-se que 60% deles possuem certificação ITIL, e 45% possuem certificação COBIT. Se 15% dos servidores não possuem nenhuma das duas certificações, a quantidade exata de servidores que possuem AMBAS as certificações (ITIL e COBIT) é igual a:

A) 18.
B) 30.
C) 24.
D) 12.
E) 36.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: C

Resolução via Conjuntos.
Total = 120 servidores (100%).
Não têm nada = 15%.
Logo, quem tem pelo menos uma certificação = 100% - 15% = 85%.
Somando as partes: ITIL (60%) + COBIT (45%) = 105%.
A intersecção (os que têm ambas) é o que excede a união: 105% - 85% = 20%.
Cálculo final: 20% de 120 servidores = 0.2 * 120 = 24 servidores.
- C) Correta.

</details>

#### Questão 45 (Raciocínio Lógico)

Assuma as premissas lógicas:
- Nenhum peixe voa.
- Alguns mamíferos voam (como os morcegos).

A conclusão que obrigatoriamente se deduz, validada por Diagramas de Euler-Venn, é:

A) Todo animal que voa é mamífero.
B) Alguns mamíferos não são peixes.
C) Todo peixe é mamífero.
D) Nenhum mamífero é peixe.
E) Alguns peixes voam se não forem mamíferos.

<details><summary>Gabarito e Explicação</summary>

Gabarito Correto: B

- A) Incorreta. Existem aves e insetos, a premissa fala apenas de mamíferos.
- B) Correta. O conjunto dos Peixes e o conjunto dos Seres que Voam (V) são totalmente separados (Nenhum peixe voa). A premissa 2 diz que ALGUNS mamíferos (M) estão dentro de V. Ora, se esses mamíferos que voam estão dentro de V, e V é totalmente separado dos Peixes, esses morcegos (mamíferos que voam) definitivamente NÃO são peixes. Logo, pelo menos ALGUNS mamíferos (aqueles que voam) não são peixes.
- C) Incorreta. Nada na premissa junta o grupo inteiro de peixes e mamíferos.
- D) Incorreta. Pode haver, no silogismo, mamíferos marinhos (baleias) que interceptem o conjunto de peixes (lógica formal não avalia biologia da vida real, apenas os conjuntos dados). O silogismo não garante que *nenhum* mamífero seja peixe.
- E) Incorreta. Fere a primeira premissa.

</details>

