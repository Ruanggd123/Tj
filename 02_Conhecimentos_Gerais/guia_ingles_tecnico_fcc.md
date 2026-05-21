# Guia Definitivo de Inglês Técnico para a FCC
## TJ-CE 2026 (Analista Judiciário - TI - Sistemas)

Para o concurso do TJ-CE, a banca **FCC (Fundação Carlos Chagas)** adota um padrão muito claro e previsível na cobrança de **Inglês Técnico**. Você **não** precisa ser fluente em inglês, nem estudar gramática complexa (como voz passiva ou tempos verbais raros) para gabaritar essa matéria.

O foco da banca é a **Compreensão de Textos Técnicos** (extraídos de documentações oficiais como AWS, Docker, Kubernetes, Spring, Git, Scrum Guide, etc.). A FCC coloca um pequeno texto em inglês e faz perguntas de interpretação com enunciados e alternativas escritos em **português**.

Abaixo está o seu mapa de guerra para acertar qualquer questão desse tipo na prova.

---

## ⚡ Os 6 Macetes de Ouro para a Prova da FCC

### 1. A Técnica do *Scanning* e *Skimming* (Ler a Pergunta Primeiro)
**Nunca** comece lendo o texto em inglês do início ao fim tentando traduzir palavra por palavra. Isso gasta tempo e energia mental.
*   **O Macete:** Vá direto para o enunciado da questão e para as alternativas (em português).
*   **Como aplicar:** Identifique qual é a palavra-chave ou o conceito técnico que a questão está cobrando (ex: "escalabilidade", "segurança", "imagem de container"). Depois, volte ao texto em inglês procurando apenas por essa palavra-chave ou termos relacionados (**Scanning**). Leia com calma apenas o parágrafo ou frase onde ela se encontra.

### 2. O Superpoder do Contexto Técnico (A Vantagem do Dev)
Mais de **70%** dos termos em um texto de TI são palavras transparentes (cognatos) ou termos que você já usa diariamente em português como desenvolvedor ou analista.
*   **O Macete:** Use o seu conhecimento prévio de TI para prever o que o texto está dizendo. 
*   *Exemplo:* Se o texto fala sobre `containers`, `isolation`, `kernel` e `host OS`, você já sabe que o assunto é Docker/Virtualização. Mesmo que você não entenda um verbo ou outro, a lógica do funcionamento de containers (que você estudou em TI) vai te guiar para a alternativa correta.

### 3. Cuidado com os "Falsos Amigos" (Falsos Cognatos em TI)
Algumas palavras parecem uma coisa em português, mas significam outra completamente diferente. A FCC adora usá-las para criar pegadinhas. Memorize estas:

| Palavra em Inglês | O que PARECE | O que REALMENTE significa em TI |
| :--- | :--- | :--- |
| **Actually** | Atualmente | **Na verdade** / **Realmente** |
| **Pretend** | Pretender | **Fingir** / **Simular** (para pretender, usamos *intend*) |
| **Library** | Livraria | **Biblioteca** (de código/reaproveitamento) |
| **Eventually** | Eventualmente (às vezes) | **No final das contas** / **Com o tempo** (indica certeza futura) |
| **Resume** | Resumir | **Retomar** / **Reiniciar** (para resumir, usamos *summarize*) |
| **Comprehensive** | Compreensível | **Abrangente** / **Completo** (ex: *comprehensive test suite*) |
| **Realize** | Realizar (fazer) | **Perceber** / **Dar-se conta** (para realizar/fazer, usamos *perform* ou *carry out*) |
| **Novel** | Novela | **Romance** ou **Inovador** / **Novo** (*a novel approach*) |
| **Notice** | Notícia | **Perceber** / **Aviso** / **Notar** |
| **Exquisite** | Esquisito | **Refinado** / **Excelente** / **Belo** |
| **Application** | Apelação / Inscrição | **Aplicação** / **Sistema** / **Software** |
| **Policy** | Polícia | **Política** / **Diretriz** / **Regra de acesso** |

### 4. Os 15 Verbos de TI Mais Cobrados
Estes verbos aparecem em quase todas as documentações técnicas. Conhecê-los vai te dar velocidade de leitura:

1.  **Retrieve:** Recuperar / Buscar (dados de um banco, por exemplo).
2.  **Trigger:** Disparar / Acionar (um evento, um pipeline, uma função Lambda).
3.  **Deploy:** Implantar / Colocar em produção.
4.  **Troubleshoot:** Diagnosticar e resolver problemas / Solucionar falhas.
5.  **Fetch:** Buscar / Trazer (uma requisição de API, por exemplo).
6.  **Leverage:** Aproveitar / Potencializar / Tirar vantagem de (ex: *leverage cloud resources*).
7.  **Enhance:** Melhorar / Aprimorar / Otimizar.
8.  **Grant / Revoke:** Conceder / Revogar (direitos de acesso ou permissões).
9.  **Wrap:** Envolver / Empacotar (ex: *wrapper classes*).
10. **Scale:** Dimensionar / Escalar (aumentar ou diminuir recursos).
11. **Store:** Armazenar (dados, arquivos).
12. **Perform:** Realizar / Executar (ex: *perform queries*).
13. **Prevent:** Evitar / Prevenir.
14. **Ensure:** Garantir / Assegurar.
15. **Handle:** Tratar / Lidar com (ex: *handle exceptions* ou *handle requests*).

### 5. Os Conectivos Lógicos (Os Organizadores do Raciocínio)
A FCC costuma cobrar o sentido lógico de uma frase. Para não errar a lógica da frase, decore estes conectivos:

*   **Contraste (Ideias opostas):**
    *   *Although / Even though / Though:* Embora / Apesar de.
    *   *However / Nevertheless / Yet:* No entanto / Contudo / Entretanto.
    *   *Whereas:* Enquanto que / Ao passo que.
*   **Causa e Consequência:**
    *   *Since:* Já que / Visto que (também significa "desde" no sentido temporal).
    *   *Therefore / Thus / Hence:* Portanto / Sendo assim / Dessa forma.
    *   *Because of / Due to:* Devido a / Por causa de.
*   **Condição e Alternativa:**
    *   *Unless:* A menos que / A não ser que.
    *   *Instead of:* Em vez de / Ao invés de.
    *   *Whether:* Se (indica escolha entre alternativas, ex: *whether to use SQL or NoSQL*).
*   **Adição:**
    *   *Furthermore / Besides / Moreover:* Além disso / Adicionalmente.

### 6. Descarte de Alternativas com Termos Absolutos em Português
Na hora de traduzir a ideia do texto para as opções de resposta:
*   Se o texto em inglês diz: *"Typically, containers share the host OS kernel..."* (Tipicamente/Geralmente, os containers compartilham...)
*   E a alternativa em português diz: *"Os containers **obrigatoriamente** e **sempre** compartilham o kernel..."*
*   **Descarte!** Em tecnologia, quase nada é absoluto. Palavras extremas em português como **"sempre", "nunca", "exclusivamente", "única forma"** costumam invalidar alternativas, a menos que o texto original traga palavras equivalentes muito fortes (como *always, never, solely, exclusively*).

---

## 📝 Prática com Questões Simuladas no Estilo FCC

Vamos aplicar os macetes em dois simulados práticos baseados em documentações reais de TI.

### Simulado 1: Kubernetes & Deployments (Fonte: Kubernetes.io)

**Text:**
> "A Deployment provides declarative updates for Pods and ReplicaSets. You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments. Although Deployments simplify replica management, you should not manage ReplicaSets directly unless your application requires custom update orchestration or no updates at all."

**Questão 1:** 
De acordo com o texto sobre Deployments no Kubernetes, assinale a opção correta:

A) O Deployment Controller altera o estado desejado para o estado atual de forma instantânea e sem controle de taxa de transferência.
B) As atualizações declarativas de Pods e ReplicaSets são feitas manualmente pelos administradores de rede, sem interferência do Deployment.
C) Recomenda-se gerenciar os ReplicaSets de forma direta na maioria dos cenários, a menos que a aplicação precise de atualizações personalizadas.
D) Um Deployment permite que o estado atual seja modificado em direção ao estado desejado sob uma taxa controlada.
E) O uso de Deployments torna a gerência de réplicas complexa, forçando o administrador a interagir exclusivamente com os Pods de forma imperativa.

#### 💡 Resolução Comentada pelo Macete:
*   **Aplicando Scanning:** A pergunta é sobre o que o Deployment faz no Kubernetes. Buscamos termos como "actual state", "desired state", "rate", "ReplicaSets".
*   **Análise das Alternativas:**
    *   A: Incorreta. O texto diz *"at a controlled rate"* (taxa controlada), e não "instantânea e sem controle".
    *   B: Incorreta. O texto diz que o Deployment provê atualizações declarativas, automatizando o processo.
    *   C: Incorreta. Pegadinha do falso amigo/conectivo! O texto diz: *"you should **not** manage ReplicaSets directly **unless** your application requires..."* (você **não** deve gerenciar ReplicaSets diretamente **a menos que** sua aplicação exija...). A alternativa disse que "recomenda-se gerenciar diretamente na maioria dos cenários". O oposto!
    *   D: **Correta**. Tradução perfeita de: *"the Deployment Controller changes the actual state to the desired state at a controlled rate."*
    *   E: Incorreta. O texto diz *"Deployments simplify replica management"* (simplificam a gerência) e usa o termo "declarative updates" (declarativo), não "imperativa".
*   **Gabarito: D.**

---

### Simulado 2: AWS Shared Responsibility Model (Fonte: AWS Docs)

**Text:**
> "Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve the customer’s operational burden as AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. The customer assumes responsibility and management of the guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided firewall."

**Questão 2:**
Considerando o Modelo de Responsabilidade Compartilhada da AWS apresentado, conclui-se que:

A) A AWS assume de forma exclusiva a responsabilidade pela aplicação de patches de segurança e atualizações do sistema operacional convidado (*guest OS*).
B) O cliente é desonerado de qualquer atividade operacional ligada à segurança física e lógica de suas aplicações e firewalls.
C) A segurança física das instalações físicas onde o serviço é executado é uma atribuição gerenciada e controlada pela AWS.
D) A configuração do firewall fornecido pela AWS deve ser delegada aos técnicos da própria AWS para evitar brechas de segurança.
E) O cliente deve gerenciar o sistema operacional hospedeiro (*host OS*) e a camada de virtualização sempre que utilizar serviços de nuvem.

#### 💡 Resolução Comentada pelo Macete:
*   **Aplicando Scanning:** Procuramos quem faz o quê. AWS vs Customer.
*   *AWS cuida de:* "...from the host operating system and virtualization layer down to the physical security..." (sistema operacional hospedeiro, camada de virtualização e segurança física das instalações).
*   *Cliente (Customer) cuida de:* "...guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided firewall." (sistema operacional convidado, softwares de aplicação associados e configuração do firewall).
*   **Análise das Alternativas:**
    *   A: Incorreta. A aplicação de patches do *guest OS* é do cliente (*"The customer assumes responsibility... guest operating system (including updates and security patches)"*).
    *   B: Incorreta. Termo absoluto "desonerado de qualquer atividade". O cliente cuida do firewall e das aplicações.
    *   C: **Correta**. A segurança física das instalações é da AWS (*"...down to the physical security of the facilities in which the service operates"*).
    *   D: Incorreta. O cliente assume a configuração do firewall fornecido (*"...configuration of the AWS provided firewall"*).
    *   E: Incorreta. A AWS é quem gerencia o *host OS* e a camada de virtualização (*"...as AWS operates, manages and controls the components from the host operating system and virtualization layer..."*).
*   **Gabarito: C.**

---

## 🚀 Como Treinar no Seu Dia a Dia (Estudo Passivo)

Você não precisa reservar dias inteiros do seu calendário para estudar inglês. Use estas técnicas integradas:

1.  **Desative a Tradução Automática:** Sempre que estiver estudando tópicos de TI (como Kubernetes, Docker, Microsserviços, Banco de Dados) e pesquisando na internet, **não** use o tradutor automático do Google Chrome. Force a leitura da página em inglês.
2.  **Leia Docs Oficiais em Inglês:** Ao estudar qualquer ferramenta nova, abra a documentação oficial direto na versão em inglês.
3.  **Monte o seu deck no Anki:** Toda vez que encontrar uma palavra desconhecida nas suas leituras de TI que comprometa a interpretação, adicione-a ao Anki com a tradução e o contexto técnico dela.

Com esses macetes, o "Inglês Técnico" deixará de ser um obstáculo e passará a ser uma fonte de pontos fáceis e garantidos na sua prova da FCC!
