# Bateria de Questões FCC — Segunda-feira 08/06

## 📝 TEMA 1: Engenharia de Software (Mensageria, Integração, Kafka, RabbitMQ)

### Questão 1 (FCC - 2024 - TRF - Analista de TI)
No Apache Kafka, a escalabilidade e o paralelismo são garantidos pela divisão dos tópicos em partições. Sobre a garantia de ordem de leitura das mensagens enviadas a um tópico do Kafka, é correto afirmar que:
A) O Kafka garante a ordem global estrita de todas as mensagens dentro de um mesmo tópico, independentemente do número de partições.
B) A ordem das mensagens é garantida estritamente apenas dentro de uma mesma partição.
C) O Consumer Group garante a ordenação mesclando as mensagens de múltiplas partições em uma única thread na memória RAM.
D) O Zookeeper enfileira as mensagens com carimbos de tempo globais, permitindo leitura ordenada independentemente da chave de partição.
E) A ordem só é garantida se o tópico possuir o fator de replicação configurado como 1.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** O Kafka divide os tópicos em partições. A garantia de ordem cronológica do Kafka se aplica **exclusivamente dentro de uma mesma partição**. Mensagens enviadas para partições diferentes do mesmo tópico podem ser lidas fora de ordem. Se a ordem estrita for um requisito de negócio, as mensagens devem ser enviadas com a mesma Partition Key para caírem na mesma partição.
</details>

---

### Questão 2 (FCC - 2024 - TRF - Analista de TI)
No Apache Kafka, a escalabilidade e o paralelismo são garantidos pela divisão dos tópicos em partições. Sobre a garantia de ordem de leitura das mensagens enviadas a um tópico do Kafka, é correto afirmar que:
A) O Kafka garante a ordem global estrita de todas as mensagens dentro de um mesmo tópico, independentemente do número de partições.
B) A ordem das mensagens é garantida estritamente apenas dentro de uma mesma partição.
C) O Consumer Group garante a ordenação mesclando as mensagens de múltiplas partições em uma única thread na memória RAM.
D) O Zookeeper enfileira as mensagens com carimbos de tempo globais, permitindo leitura ordenada independentemente da chave de partição.
E) A ordem só é garantida se o tópico possuir o fator de replicação configurado como 1.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** O Kafka divide os tópicos em partições. A garantia de ordem cronológica do Kafka se aplica **exclusivamente dentro de uma mesma partição**. Mensagens enviadas para partições diferentes do mesmo tópico podem ser lidas fora de ordem. Se a ordem estrita for um requisito de negócio, as mensagens devem ser enviadas com a mesma Partition Key para caírem na mesma partição.
</details>

---

### Questão 3 (FCC - 2024 - TRF - Analista de TI)
No Apache Kafka, a escalabilidade e o paralelismo são garantidos pela divisão dos tópicos em partições. Sobre a garantia de ordem de leitura das mensagens enviadas a um tópico do Kafka, é correto afirmar que:
A) O Kafka garante a ordem global estrita de todas as mensagens dentro de um mesmo tópico, independentemente do número de partições.
B) A ordem das mensagens é garantida estritamente apenas dentro de uma mesma partição.
C) O Consumer Group garante a ordenação mesclando as mensagens de múltiplas partições em uma única thread na memória RAM.
D) O Zookeeper enfileira as mensagens com carimbos de tempo globais, permitindo leitura ordenada independentemente da chave de partição.
E) A ordem só é garantida se o tópico possuir o fator de replicação configurado como 1.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** O Kafka divide os tópicos em partições. A garantia de ordem cronológica do Kafka se aplica **exclusivamente dentro de uma mesma partição**. Mensagens enviadas para partições diferentes do mesmo tópico podem ser lidas fora de ordem. Se a ordem estrita for um requisito de negócio, as mensagens devem ser enviadas com a mesma Partition Key para caírem na mesma partição.
</details>

---

### Questão 4 (FCC - 2024 - TRF - Analista de TI)
No Apache Kafka, a escalabilidade e o paralelismo são garantidos pela divisão dos tópicos em partições. Sobre a garantia de ordem de leitura das mensagens enviadas a um tópico do Kafka, é correto afirmar que:
A) O Kafka garante a ordem global estrita de todas as mensagens dentro de um mesmo tópico, independentemente do número de partições.
B) A ordem das mensagens é garantida estritamente apenas dentro de uma mesma partição.
C) O Consumer Group garante a ordenação mesclando as mensagens de múltiplas partições em uma única thread na memória RAM.
D) O Zookeeper enfileira as mensagens com carimbos de tempo globais, permitindo leitura ordenada independentemente da chave de partição.
E) A ordem só é garantida se o tópico possuir o fator de replicação configurado como 1.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** O Kafka divide os tópicos em partições. A garantia de ordem cronológica do Kafka se aplica **exclusivamente dentro de uma mesma partição**. Mensagens enviadas para partições diferentes do mesmo tópico podem ser lidas fora de ordem. Se a ordem estrita for um requisito de negócio, as mensagens devem ser enviadas com a mesma Partition Key para caírem na mesma partição.
</details>

---

### Questão 5 (FCC - 2024 - TRF - Analista de TI)
No Apache Kafka, a escalabilidade e o paralelismo são garantidos pela divisão dos tópicos em partições. Sobre a garantia de ordem de leitura das mensagens enviadas a um tópico do Kafka, é correto afirmar que:
A) O Kafka garante a ordem global estrita de todas as mensagens dentro de um mesmo tópico, independentemente do número de partições.
B) A ordem das mensagens é garantida estritamente apenas dentro de uma mesma partição.
C) O Consumer Group garante a ordenação mesclando as mensagens de múltiplas partições em uma única thread na memória RAM.
D) O Zookeeper enfileira as mensagens com carimbos de tempo globais, permitindo leitura ordenada independentemente da chave de partição.
E) A ordem só é garantida se o tópico possuir o fator de replicação configurado como 1.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** O Kafka divide os tópicos em partições. A garantia de ordem cronológica do Kafka se aplica **exclusivamente dentro de uma mesma partição**. Mensagens enviadas para partições diferentes do mesmo tópico podem ser lidas fora de ordem. Se a ordem estrita for um requisito de negócio, as mensagens devem ser enviadas com a mesma Partition Key para caírem na mesma partição.
</details>

---

### Questão 6 (FCC - 2023 - TRT - Analista de Sistemas)
No ecossistema do RabbitMQ, produtores não enviam mensagens diretamente para as filas, mas sim para Exchanges, que realizam o roteamento. A Exchange que permite rotear mensagens com base em correspondência de padrões complexos usando curingas como `*` (asterisco) e `#` (cerquilha) é a:
A) Direct Exchange.
B) Fanout Exchange.
C) Topic Exchange.
D) Headers Exchange.
E) Default Exchange.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** A Topic Exchange permite o roteamento baseado em chaves de roteamento (`Routing Keys`) estruturadas com pontos (ex: `app.log.error`) e o uso de curingas nas `Binding Keys` das filas. O asterisco `*` substitui exatamente uma palavra, e a cerquilha `#` substitui zero ou mais palavras.
</details>

---

### Questão 7 (FCC - 2023 - TRT - Analista de Sistemas)
No ecossistema do RabbitMQ, produtores não enviam mensagens diretamente para as filas, mas sim para Exchanges, que realizam o roteamento. A Exchange que permite rotear mensagens com base em correspondência de padrões complexos usando curingas como `*` (asterisco) e `#` (cerquilha) é a:
A) Direct Exchange.
B) Fanout Exchange.
C) Topic Exchange.
D) Headers Exchange.
E) Default Exchange.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** A Topic Exchange permite o roteamento baseado em chaves de roteamento (`Routing Keys`) estruturadas com pontos (ex: `app.log.error`) e o uso de curingas nas `Binding Keys` das filas. O asterisco `*` substitui exatamente uma palavra, e a cerquilha `#` substitui zero ou mais palavras.
</details>

---

### Questão 8 (FCC - 2023 - TRT - Analista de Sistemas)
No ecossistema do RabbitMQ, produtores não enviam mensagens diretamente para as filas, mas sim para Exchanges, que realizam o roteamento. A Exchange que permite rotear mensagens com base em correspondência de padrões complexos usando curingas como `*` (asterisco) e `#` (cerquilha) é a:
A) Direct Exchange.
B) Fanout Exchange.
C) Topic Exchange.
D) Headers Exchange.
E) Default Exchange.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** A Topic Exchange permite o roteamento baseado em chaves de roteamento (`Routing Keys`) estruturadas com pontos (ex: `app.log.error`) e o uso de curingas nas `Binding Keys` das filas. O asterisco `*` substitui exatamente uma palavra, e a cerquilha `#` substitui zero ou mais palavras.
</details>

---

### Questão 9 (FCC - 2023 - TRT - Analista de Sistemas)
No ecossistema do RabbitMQ, produtores não enviam mensagens diretamente para as filas, mas sim para Exchanges, que realizam o roteamento. A Exchange que permite rotear mensagens com base em correspondência de padrões complexos usando curingas como `*` (asterisco) e `#` (cerquilha) é a:
A) Direct Exchange.
B) Fanout Exchange.
C) Topic Exchange.
D) Headers Exchange.
E) Default Exchange.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** A Topic Exchange permite o roteamento baseado em chaves de roteamento (`Routing Keys`) estruturadas com pontos (ex: `app.log.error`) e o uso de curingas nas `Binding Keys` das filas. O asterisco `*` substitui exatamente uma palavra, e a cerquilha `#` substitui zero ou mais palavras.
</details>

---

### Questão 10 (FCC - 2023 - TRT - Analista de Sistemas)
No ecossistema do RabbitMQ, produtores não enviam mensagens diretamente para as filas, mas sim para Exchanges, que realizam o roteamento. A Exchange que permite rotear mensagens com base em correspondência de padrões complexos usando curingas como `*` (asterisco) e `#` (cerquilha) é a:
A) Direct Exchange.
B) Fanout Exchange.
C) Topic Exchange.
D) Headers Exchange.
E) Default Exchange.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** A Topic Exchange permite o roteamento baseado em chaves de roteamento (`Routing Keys`) estruturadas com pontos (ex: `app.log.error`) e o uso de curingas nas `Binding Keys` das filas. O asterisco `*` substitui exatamente uma palavra, e a cerquilha `#` substitui zero ou mais palavras.
</details>

---

### Questão 11 (FCC - 2022 - TRE - Tecnologista)
Ao modernizar um sistema legado monolítico, a equipe de arquitetura decidiu implementar o padrão Strangler Fig (Figo Estrangulador). A essência desse padrão arquitetural consiste em:
A) Bloquear imediatamente o acesso ao sistema legado e forçar os usuários a utilizarem a nova interface baseada em microsserviços.
B) Criar uma fachada (API Gateway) que intercepta as chamadas e as redireciona gradualmente para os novos microsserviços, substituindo a funcionalidade legada passo a passo.
C) Copiar os dados do banco relacional legado para um Data Lake a cada hora usando uma rotina de batch ETL pesada.
D) Implementar um Barramento de Serviço Corporativo (ESB) centralizado que contenha toda a lógica de negócio do sistema antigo.
E) Alterar o código-fonte original do monolito para suportar mensageria assíncrona com RabbitMQ.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** O Strangler Fig Pattern permite a migração segura interceptando as requisições na borda (ex: com um proxy reverso ou API Gateway). Requisições para funcionalidades antigas continuam indo para o monolito, enquanto requisições para funcionalidades reescritas vão para os microsserviços modernos, até o monolito ser estrangulado e desativado por completo.
</details>

---

### Questão 12 (FCC - 2022 - TRE - Tecnologista)
Ao modernizar um sistema legado monolítico, a equipe de arquitetura decidiu implementar o padrão Strangler Fig (Figo Estrangulador). A essência desse padrão arquitetural consiste em:
A) Bloquear imediatamente o acesso ao sistema legado e forçar os usuários a utilizarem a nova interface baseada em microsserviços.
B) Criar uma fachada (API Gateway) que intercepta as chamadas e as redireciona gradualmente para os novos microsserviços, substituindo a funcionalidade legada passo a passo.
C) Copiar os dados do banco relacional legado para um Data Lake a cada hora usando uma rotina de batch ETL pesada.
D) Implementar um Barramento de Serviço Corporativo (ESB) centralizado que contenha toda a lógica de negócio do sistema antigo.
E) Alterar o código-fonte original do monolito para suportar mensageria assíncrona com RabbitMQ.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** O Strangler Fig Pattern permite a migração segura interceptando as requisições na borda (ex: com um proxy reverso ou API Gateway). Requisições para funcionalidades antigas continuam indo para o monolito, enquanto requisições para funcionalidades reescritas vão para os microsserviços modernos, até o monolito ser estrangulado e desativado por completo.
</details>

---

### Questão 13 (FCC - 2022 - TRE - Tecnologista)
Ao modernizar um sistema legado monolítico, a equipe de arquitetura decidiu implementar o padrão Strangler Fig (Figo Estrangulador). A essência desse padrão arquitetural consiste em:
A) Bloquear imediatamente o acesso ao sistema legado e forçar os usuários a utilizarem a nova interface baseada em microsserviços.
B) Criar uma fachada (API Gateway) que intercepta as chamadas e as redireciona gradualmente para os novos microsserviços, substituindo a funcionalidade legada passo a passo.
C) Copiar os dados do banco relacional legado para um Data Lake a cada hora usando uma rotina de batch ETL pesada.
D) Implementar um Barramento de Serviço Corporativo (ESB) centralizado que contenha toda a lógica de negócio do sistema antigo.
E) Alterar o código-fonte original do monolito para suportar mensageria assíncrona com RabbitMQ.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** O Strangler Fig Pattern permite a migração segura interceptando as requisições na borda (ex: com um proxy reverso ou API Gateway). Requisições para funcionalidades antigas continuam indo para o monolito, enquanto requisições para funcionalidades reescritas vão para os microsserviços modernos, até o monolito ser estrangulado e desativado por completo.
</details>

---

### Questão 14 (FCC - 2022 - TRE - Tecnologista)
Ao modernizar um sistema legado monolítico, a equipe de arquitetura decidiu implementar o padrão Strangler Fig (Figo Estrangulador). A essência desse padrão arquitetural consiste em:
A) Bloquear imediatamente o acesso ao sistema legado e forçar os usuários a utilizarem a nova interface baseada em microsserviços.
B) Criar uma fachada (API Gateway) que intercepta as chamadas e as redireciona gradualmente para os novos microsserviços, substituindo a funcionalidade legada passo a passo.
C) Copiar os dados do banco relacional legado para um Data Lake a cada hora usando uma rotina de batch ETL pesada.
D) Implementar um Barramento de Serviço Corporativo (ESB) centralizado que contenha toda a lógica de negócio do sistema antigo.
E) Alterar o código-fonte original do monolito para suportar mensageria assíncrona com RabbitMQ.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** O Strangler Fig Pattern permite a migração segura interceptando as requisições na borda (ex: com um proxy reverso ou API Gateway). Requisições para funcionalidades antigas continuam indo para o monolito, enquanto requisições para funcionalidades reescritas vão para os microsserviços modernos, até o monolito ser estrangulado e desativado por completo.
</details>

---

### Questão 15 (FCC - 2022 - TRE - Tecnologista)
Ao modernizar um sistema legado monolítico, a equipe de arquitetura decidiu implementar o padrão Strangler Fig (Figo Estrangulador). A essência desse padrão arquitetural consiste em:
A) Bloquear imediatamente o acesso ao sistema legado e forçar os usuários a utilizarem a nova interface baseada em microsserviços.
B) Criar uma fachada (API Gateway) que intercepta as chamadas e as redireciona gradualmente para os novos microsserviços, substituindo a funcionalidade legada passo a passo.
C) Copiar os dados do banco relacional legado para um Data Lake a cada hora usando uma rotina de batch ETL pesada.
D) Implementar um Barramento de Serviço Corporativo (ESB) centralizado que contenha toda a lógica de negócio do sistema antigo.
E) Alterar o código-fonte original do monolito para suportar mensageria assíncrona com RabbitMQ.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** O Strangler Fig Pattern permite a migração segura interceptando as requisições na borda (ex: com um proxy reverso ou API Gateway). Requisições para funcionalidades antigas continuam indo para o monolito, enquanto requisições para funcionalidades reescritas vão para os microsserviços modernos, até o monolito ser estrangulado e desativado por completo.
</details>

---

## 📝 TEMA 2: Banco de Dados (BI Conceitual, DW, Data Lake e OLAP)

### Questão 16 (FCC - 2024 - DPE - Analista de Banco de Dados)
Sobre os conceitos de Data Warehouse (DW) e Data Lake, avalie a diferença fundamental na abordagem de estruturação dos dados armazenados:
A) O DW utiliza a abordagem Schema-on-Read, enquanto o Data Lake utiliza Schema-on-Write.
B) O Data Lake exige a modelagem dimensional estrela antes que qualquer dado possa ser gravado no HDFS.
C) O Data Lake suporta armazenamento de dados brutos e nativos, aplicando a estruturação apenas no momento da leitura (Schema-on-Read), diferentemente do DW (Schema-on-Write).
D) O DW armazena apenas dados não-estruturados, como vídeos e imagens, organizando-os em tabelas Fato.
E) Ambos exigem que os dados passem pelo processo de ETL tradicional antes do armazenamento inicial.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** A grande vantagem e característica do Data Lake é receber dados no seu estado natural e bruto (Schema-on-Read), postergando a criação de esquemas estruturados para o momento do processamento ou da query, reduzindo o custo de ingestão se comparado ao DW relacional (Schema-on-Write).
</details>

---

### Questão 17 (FCC - 2024 - DPE - Analista de Banco de Dados)
Sobre os conceitos de Data Warehouse (DW) e Data Lake, avalie a diferença fundamental na abordagem de estruturação dos dados armazenados:
A) O DW utiliza a abordagem Schema-on-Read, enquanto o Data Lake utiliza Schema-on-Write.
B) O Data Lake exige a modelagem dimensional estrela antes que qualquer dado possa ser gravado no HDFS.
C) O Data Lake suporta armazenamento de dados brutos e nativos, aplicando a estruturação apenas no momento da leitura (Schema-on-Read), diferentemente do DW (Schema-on-Write).
D) O DW armazena apenas dados não-estruturados, como vídeos e imagens, organizando-os em tabelas Fato.
E) Ambos exigem que os dados passem pelo processo de ETL tradicional antes do armazenamento inicial.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** A grande vantagem e característica do Data Lake é receber dados no seu estado natural e bruto (Schema-on-Read), postergando a criação de esquemas estruturados para o momento do processamento ou da query, reduzindo o custo de ingestão se comparado ao DW relacional (Schema-on-Write).
</details>

---

### Questão 18 (FCC - 2024 - DPE - Analista de Banco de Dados)
Sobre os conceitos de Data Warehouse (DW) e Data Lake, avalie a diferença fundamental na abordagem de estruturação dos dados armazenados:
A) O DW utiliza a abordagem Schema-on-Read, enquanto o Data Lake utiliza Schema-on-Write.
B) O Data Lake exige a modelagem dimensional estrela antes que qualquer dado possa ser gravado no HDFS.
C) O Data Lake suporta armazenamento de dados brutos e nativos, aplicando a estruturação apenas no momento da leitura (Schema-on-Read), diferentemente do DW (Schema-on-Write).
D) O DW armazena apenas dados não-estruturados, como vídeos e imagens, organizando-os em tabelas Fato.
E) Ambos exigem que os dados passem pelo processo de ETL tradicional antes do armazenamento inicial.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** A grande vantagem e característica do Data Lake é receber dados no seu estado natural e bruto (Schema-on-Read), postergando a criação de esquemas estruturados para o momento do processamento ou da query, reduzindo o custo de ingestão se comparado ao DW relacional (Schema-on-Write).
</details>

---

### Questão 19 (FCC - 2024 - DPE - Analista de Banco de Dados)
Sobre os conceitos de Data Warehouse (DW) e Data Lake, avalie a diferença fundamental na abordagem de estruturação dos dados armazenados:
A) O DW utiliza a abordagem Schema-on-Read, enquanto o Data Lake utiliza Schema-on-Write.
B) O Data Lake exige a modelagem dimensional estrela antes que qualquer dado possa ser gravado no HDFS.
C) O Data Lake suporta armazenamento de dados brutos e nativos, aplicando a estruturação apenas no momento da leitura (Schema-on-Read), diferentemente do DW (Schema-on-Write).
D) O DW armazena apenas dados não-estruturados, como vídeos e imagens, organizando-os em tabelas Fato.
E) Ambos exigem que os dados passem pelo processo de ETL tradicional antes do armazenamento inicial.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** A grande vantagem e característica do Data Lake é receber dados no seu estado natural e bruto (Schema-on-Read), postergando a criação de esquemas estruturados para o momento do processamento ou da query, reduzindo o custo de ingestão se comparado ao DW relacional (Schema-on-Write).
</details>

---

### Questão 20 (FCC - 2024 - DPE - Analista de Banco de Dados)
Sobre os conceitos de Data Warehouse (DW) e Data Lake, avalie a diferença fundamental na abordagem de estruturação dos dados armazenados:
A) O DW utiliza a abordagem Schema-on-Read, enquanto o Data Lake utiliza Schema-on-Write.
B) O Data Lake exige a modelagem dimensional estrela antes que qualquer dado possa ser gravado no HDFS.
C) O Data Lake suporta armazenamento de dados brutos e nativos, aplicando a estruturação apenas no momento da leitura (Schema-on-Read), diferentemente do DW (Schema-on-Write).
D) O DW armazena apenas dados não-estruturados, como vídeos e imagens, organizando-os em tabelas Fato.
E) Ambos exigem que os dados passem pelo processo de ETL tradicional antes do armazenamento inicial.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** A grande vantagem e característica do Data Lake é receber dados no seu estado natural e bruto (Schema-on-Read), postergando a criação de esquemas estruturados para o momento do processamento ou da query, reduzindo o custo de ingestão se comparado ao DW relacional (Schema-on-Write).
</details>

---

### Questão 21 (FCC - 2021 - TCE - Auditor de TI)
No contexto de ferramentas de Business Intelligence (BI) e processamento analítico (OLAP), a operação que permite aumentar o nível de detalhe da informação exibida em um relatório, navegando de um nível superior (ex: Ano) para um nível inferior de agregação (ex: Trimestre ou Mês), é denominada:
A) Roll-up.
B) Drill-down.
C) Slice.
D) Dice.
E) Pivot.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** A operação de Drill-down (ou Roll-down) permite explodir a hierarquia dimensional, descendo para um nível mais detalhado (menor granularidade). O Roll-up é o exato oposto (subir na hierarquia e agregar dados).
</details>

---

### Questão 22 (FCC - 2021 - TCE - Auditor de TI)
No contexto de ferramentas de Business Intelligence (BI) e processamento analítico (OLAP), a operação que permite aumentar o nível de detalhe da informação exibida em um relatório, navegando de um nível superior (ex: Ano) para um nível inferior de agregação (ex: Trimestre ou Mês), é denominada:
A) Roll-up.
B) Drill-down.
C) Slice.
D) Dice.
E) Pivot.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** A operação de Drill-down (ou Roll-down) permite explodir a hierarquia dimensional, descendo para um nível mais detalhado (menor granularidade). O Roll-up é o exato oposto (subir na hierarquia e agregar dados).
</details>

---

### Questão 23 (FCC - 2021 - TCE - Auditor de TI)
No contexto de ferramentas de Business Intelligence (BI) e processamento analítico (OLAP), a operação que permite aumentar o nível de detalhe da informação exibida em um relatório, navegando de um nível superior (ex: Ano) para um nível inferior de agregação (ex: Trimestre ou Mês), é denominada:
A) Roll-up.
B) Drill-down.
C) Slice.
D) Dice.
E) Pivot.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** A operação de Drill-down (ou Roll-down) permite explodir a hierarquia dimensional, descendo para um nível mais detalhado (menor granularidade). O Roll-up é o exato oposto (subir na hierarquia e agregar dados).
</details>

---

### Questão 24 (FCC - 2021 - TCE - Auditor de TI)
No contexto de ferramentas de Business Intelligence (BI) e processamento analítico (OLAP), a operação que permite aumentar o nível de detalhe da informação exibida em um relatório, navegando de um nível superior (ex: Ano) para um nível inferior de agregação (ex: Trimestre ou Mês), é denominada:
A) Roll-up.
B) Drill-down.
C) Slice.
D) Dice.
E) Pivot.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** A operação de Drill-down (ou Roll-down) permite explodir a hierarquia dimensional, descendo para um nível mais detalhado (menor granularidade). O Roll-up é o exato oposto (subir na hierarquia e agregar dados).
</details>

---

### Questão 25 (FCC - 2021 - TCE - Auditor de TI)
No contexto de ferramentas de Business Intelligence (BI) e processamento analítico (OLAP), a operação que permite aumentar o nível de detalhe da informação exibida em um relatório, navegando de um nível superior (ex: Ano) para um nível inferior de agregação (ex: Trimestre ou Mês), é denominada:
A) Roll-up.
B) Drill-down.
C) Slice.
D) Dice.
E) Pivot.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- **B está correta:** A operação de Drill-down (ou Roll-down) permite explodir a hierarquia dimensional, descendo para um nível mais detalhado (menor granularidade). O Roll-up é o exato oposto (subir na hierarquia e agregar dados).
</details>

---

### Questão 26 (FCC - 2023 - TRT - Analista de BI)
Na modelagem dimensional utilizada para construção de Data Marts, qual a principal diferença estrutural entre o modelo Estrela (Star Schema) e o modelo Floco de Neve (Snowflake Schema)?
A) O Star Schema normaliza as tabelas de dimensão, economizando espaço de armazenamento.
B) O Snowflake Schema possui tabelas Fato ligadas diretamente umas às outras sem dimensões.
C) O Snowflake Schema normaliza as tabelas de dimensão em subdimensões hierárquicas, exigindo mais JOINs nas consultas, enquanto o Star Schema desnormaliza as dimensões em tabelas únicas.
D) O Star Schema não possui tabelas Fato, apenas tabelas de Dimensão temporais.
E) O Snowflake Schema utiliza o conceito de Schema-on-Read.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** No modelo Star Schema, a tabela fato liga-se a dimensões totalmente desnormalizadas (redundantes) visando alta performance de leitura. O Snowflake resolve a redundância normalizando as dimensões em tabelas menores (ex: País -> Estado -> Cidade), o que economiza disco, mas degrada o desempenho devido à complexidade das consultas SQL geradas com dezenas de `JOINs`.
</details>

---

### Questão 27 (FCC - 2023 - TRT - Analista de BI)
Na modelagem dimensional utilizada para construção de Data Marts, qual a principal diferença estrutural entre o modelo Estrela (Star Schema) e o modelo Floco de Neve (Snowflake Schema)?
A) O Star Schema normaliza as tabelas de dimensão, economizando espaço de armazenamento.
B) O Snowflake Schema possui tabelas Fato ligadas diretamente umas às outras sem dimensões.
C) O Snowflake Schema normaliza as tabelas de dimensão em subdimensões hierárquicas, exigindo mais JOINs nas consultas, enquanto o Star Schema desnormaliza as dimensões em tabelas únicas.
D) O Star Schema não possui tabelas Fato, apenas tabelas de Dimensão temporais.
E) O Snowflake Schema utiliza o conceito de Schema-on-Read.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** No modelo Star Schema, a tabela fato liga-se a dimensões totalmente desnormalizadas (redundantes) visando alta performance de leitura. O Snowflake resolve a redundância normalizando as dimensões em tabelas menores (ex: País -> Estado -> Cidade), o que economiza disco, mas degrada o desempenho devido à complexidade das consultas SQL geradas com dezenas de `JOINs`.
</details>

---

### Questão 28 (FCC - 2023 - TRT - Analista de BI)
Na modelagem dimensional utilizada para construção de Data Marts, qual a principal diferença estrutural entre o modelo Estrela (Star Schema) e o modelo Floco de Neve (Snowflake Schema)?
A) O Star Schema normaliza as tabelas de dimensão, economizando espaço de armazenamento.
B) O Snowflake Schema possui tabelas Fato ligadas diretamente umas às outras sem dimensões.
C) O Snowflake Schema normaliza as tabelas de dimensão em subdimensões hierárquicas, exigindo mais JOINs nas consultas, enquanto o Star Schema desnormaliza as dimensões em tabelas únicas.
D) O Star Schema não possui tabelas Fato, apenas tabelas de Dimensão temporais.
E) O Snowflake Schema utiliza o conceito de Schema-on-Read.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** No modelo Star Schema, a tabela fato liga-se a dimensões totalmente desnormalizadas (redundantes) visando alta performance de leitura. O Snowflake resolve a redundância normalizando as dimensões em tabelas menores (ex: País -> Estado -> Cidade), o que economiza disco, mas degrada o desempenho devido à complexidade das consultas SQL geradas com dezenas de `JOINs`.
</details>

---

### Questão 29 (FCC - 2023 - TRT - Analista de BI)
Na modelagem dimensional utilizada para construção de Data Marts, qual a principal diferença estrutural entre o modelo Estrela (Star Schema) e o modelo Floco de Neve (Snowflake Schema)?
A) O Star Schema normaliza as tabelas de dimensão, economizando espaço de armazenamento.
B) O Snowflake Schema possui tabelas Fato ligadas diretamente umas às outras sem dimensões.
C) O Snowflake Schema normaliza as tabelas de dimensão em subdimensões hierárquicas, exigindo mais JOINs nas consultas, enquanto o Star Schema desnormaliza as dimensões em tabelas únicas.
D) O Star Schema não possui tabelas Fato, apenas tabelas de Dimensão temporais.
E) O Snowflake Schema utiliza o conceito de Schema-on-Read.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** No modelo Star Schema, a tabela fato liga-se a dimensões totalmente desnormalizadas (redundantes) visando alta performance de leitura. O Snowflake resolve a redundância normalizando as dimensões em tabelas menores (ex: País -> Estado -> Cidade), o que economiza disco, mas degrada o desempenho devido à complexidade das consultas SQL geradas com dezenas de `JOINs`.
</details>

---

### Questão 30 (FCC - 2023 - TRT - Analista de BI)
Na modelagem dimensional utilizada para construção de Data Marts, qual a principal diferença estrutural entre o modelo Estrela (Star Schema) e o modelo Floco de Neve (Snowflake Schema)?
A) O Star Schema normaliza as tabelas de dimensão, economizando espaço de armazenamento.
B) O Snowflake Schema possui tabelas Fato ligadas diretamente umas às outras sem dimensões.
C) O Snowflake Schema normaliza as tabelas de dimensão em subdimensões hierárquicas, exigindo mais JOINs nas consultas, enquanto o Star Schema desnormaliza as dimensões em tabelas únicas.
D) O Star Schema não possui tabelas Fato, apenas tabelas de Dimensão temporais.
E) O Snowflake Schema utiliza o conceito de Schema-on-Read.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** No modelo Star Schema, a tabela fato liga-se a dimensões totalmente desnormalizadas (redundantes) visando alta performance de leitura. O Snowflake resolve a redundância normalizando as dimensões em tabelas menores (ex: País -> Estado -> Cidade), o que economiza disco, mas degrada o desempenho devido à complexidade das consultas SQL geradas com dezenas de `JOINs`.
</details>

---

## 📝 TEMA 3: Língua Portuguesa (Concordância Nominal, Vozes e Correlação Verbal)

### Questão 31 (FCC - 2024 - TRF - Técnico Judiciário)
Assinale a alternativa em que a concordância nominal está plenamente de acordo com a norma-padrão da Língua Portuguesa.
A) Seguem em anexos os memorandos requisitados pela chefia.
B) As servidoras disseram obrigadas ao receberem os certificados, embora parecessem meia confusas.
C) É proibido a circulação de pessoas não autorizadas na sala do datacenter.
D) Havia bastantes candidatos aguardando o início das provas, mas as inscrições custavam muito caro.
E) As planilhas inclusas no e-mail devem ser lido antes da reunião.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** "Bastantes" funciona aqui como pronome adjetivo, acompanhando o substantivo "candidatos" (equivalente a "muitos candidatos"), portanto varia para o plural. "Caro" está funcionando como advérbio modificando o verbo custar (custam muito dinheiro), logo é invariável.
- **A está errada:** "em anexo" é invariável. O certo é "em anexo" ou "anexos".
- **B está errada:** O correto é "meio confusas" (advérbio invariável = um pouco).
- **C está errada:** "É proibida a circulação" (o artigo "a" força a concordância da palavra proibido).
</details>

---

### Questão 32 (FCC - 2024 - TRF - Técnico Judiciário)
Assinale a alternativa em que a concordância nominal está plenamente de acordo com a norma-padrão da Língua Portuguesa.
A) Seguem em anexos os memorandos requisitados pela chefia.
B) As servidoras disseram obrigadas ao receberem os certificados, embora parecessem meia confusas.
C) É proibido a circulação de pessoas não autorizadas na sala do datacenter.
D) Havia bastantes candidatos aguardando o início das provas, mas as inscrições custavam muito caro.
E) As planilhas inclusas no e-mail devem ser lido antes da reunião.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** "Bastantes" funciona aqui como pronome adjetivo, acompanhando o substantivo "candidatos" (equivalente a "muitos candidatos"), portanto varia para o plural. "Caro" está funcionando como advérbio modificando o verbo custar (custam muito dinheiro), logo é invariável.
- **A está errada:** "em anexo" é invariável. O certo é "em anexo" ou "anexos".
- **B está errada:** O correto é "meio confusas" (advérbio invariável = um pouco).
- **C está errada:** "É proibida a circulação" (o artigo "a" força a concordância da palavra proibido).
</details>

---

### Questão 33 (FCC - 2024 - TRF - Técnico Judiciário)
Assinale a alternativa em que a concordância nominal está plenamente de acordo com a norma-padrão da Língua Portuguesa.
A) Seguem em anexos os memorandos requisitados pela chefia.
B) As servidoras disseram obrigadas ao receberem os certificados, embora parecessem meia confusas.
C) É proibido a circulação de pessoas não autorizadas na sala do datacenter.
D) Havia bastantes candidatos aguardando o início das provas, mas as inscrições custavam muito caro.
E) As planilhas inclusas no e-mail devem ser lido antes da reunião.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** "Bastantes" funciona aqui como pronome adjetivo, acompanhando o substantivo "candidatos" (equivalente a "muitos candidatos"), portanto varia para o plural. "Caro" está funcionando como advérbio modificando o verbo custar (custam muito dinheiro), logo é invariável.
- **A está errada:** "em anexo" é invariável. O certo é "em anexo" ou "anexos".
- **B está errada:** O correto é "meio confusas" (advérbio invariável = um pouco).
- **C está errada:** "É proibida a circulação" (o artigo "a" força a concordância da palavra proibido).
</details>

---

### Questão 34 (FCC - 2024 - TRF - Técnico Judiciário)
Assinale a alternativa em que a concordância nominal está plenamente de acordo com a norma-padrão da Língua Portuguesa.
A) Seguem em anexos os memorandos requisitados pela chefia.
B) As servidoras disseram obrigadas ao receberem os certificados, embora parecessem meia confusas.
C) É proibido a circulação de pessoas não autorizadas na sala do datacenter.
D) Havia bastantes candidatos aguardando o início das provas, mas as inscrições custavam muito caro.
E) As planilhas inclusas no e-mail devem ser lido antes da reunião.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** "Bastantes" funciona aqui como pronome adjetivo, acompanhando o substantivo "candidatos" (equivalente a "muitos candidatos"), portanto varia para o plural. "Caro" está funcionando como advérbio modificando o verbo custar (custam muito dinheiro), logo é invariável.
- **A está errada:** "em anexo" é invariável. O certo é "em anexo" ou "anexos".
- **B está errada:** O correto é "meio confusas" (advérbio invariável = um pouco).
- **C está errada:** "É proibida a circulação" (o artigo "a" força a concordância da palavra proibido).
</details>

---

### Questão 35 (FCC - 2024 - TRF - Técnico Judiciário)
Assinale a alternativa em que a concordância nominal está plenamente de acordo com a norma-padrão da Língua Portuguesa.
A) Seguem em anexos os memorandos requisitados pela chefia.
B) As servidoras disseram obrigadas ao receberem os certificados, embora parecessem meia confusas.
C) É proibido a circulação de pessoas não autorizadas na sala do datacenter.
D) Havia bastantes candidatos aguardando o início das provas, mas as inscrições custavam muito caro.
E) As planilhas inclusas no e-mail devem ser lido antes da reunião.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** "Bastantes" funciona aqui como pronome adjetivo, acompanhando o substantivo "candidatos" (equivalente a "muitos candidatos"), portanto varia para o plural. "Caro" está funcionando como advérbio modificando o verbo custar (custam muito dinheiro), logo é invariável.
- **A está errada:** "em anexo" é invariável. O certo é "em anexo" ou "anexos".
- **B está errada:** O correto é "meio confusas" (advérbio invariável = um pouco).
- **C está errada:** "É proibida a circulação" (o artigo "a" força a concordância da palavra proibido).
</details>

---

### Questão 36 (FCC - 2022 - TRE - Analista Judiciário)
Considerando as regras de formação da voz passiva, assinale a alternativa cuja conversão da voz ativa para a passiva analítica está correta, mantendo o sentido e o tempo verbal original.
Frase Ativa: "Os analistas descobrirão novas vulnerabilidades no sistema."
A) Novas vulnerabilidades são descobertas pelos analistas no sistema.
B) Novas vulnerabilidades foram descobertas pelos analistas no sistema.
C) Novas vulnerabilidades seriam descobertas pelos analistas no sistema.
D) Novas vulnerabilidades serão descobertas pelos analistas no sistema.
E) Descobrir-se-ão novas vulnerabilidades no sistema.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** O verbo "descobrirão" está no Futuro do Presente do Indicativo. A voz passiva analítica exige o verbo auxiliar "ser" no exato mesmo tempo verbal da voz ativa. Portanto, "serão" + particípio "descobertas".
- **E está errada:** Embora esteja no futuro, a alternativa E representa a voz passiva *sintética*, e a questão pediu a voz passiva *analítica*.
</details>

---

### Questão 37 (FCC - 2022 - TRE - Analista Judiciário)
Considerando as regras de formação da voz passiva, assinale a alternativa cuja conversão da voz ativa para a passiva analítica está correta, mantendo o sentido e o tempo verbal original.
Frase Ativa: "Os analistas descobrirão novas vulnerabilidades no sistema."
A) Novas vulnerabilidades são descobertas pelos analistas no sistema.
B) Novas vulnerabilidades foram descobertas pelos analistas no sistema.
C) Novas vulnerabilidades seriam descobertas pelos analistas no sistema.
D) Novas vulnerabilidades serão descobertas pelos analistas no sistema.
E) Descobrir-se-ão novas vulnerabilidades no sistema.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** O verbo "descobrirão" está no Futuro do Presente do Indicativo. A voz passiva analítica exige o verbo auxiliar "ser" no exato mesmo tempo verbal da voz ativa. Portanto, "serão" + particípio "descobertas".
- **E está errada:** Embora esteja no futuro, a alternativa E representa a voz passiva *sintética*, e a questão pediu a voz passiva *analítica*.
</details>

---

### Questão 38 (FCC - 2022 - TRE - Analista Judiciário)
Considerando as regras de formação da voz passiva, assinale a alternativa cuja conversão da voz ativa para a passiva analítica está correta, mantendo o sentido e o tempo verbal original.
Frase Ativa: "Os analistas descobrirão novas vulnerabilidades no sistema."
A) Novas vulnerabilidades são descobertas pelos analistas no sistema.
B) Novas vulnerabilidades foram descobertas pelos analistas no sistema.
C) Novas vulnerabilidades seriam descobertas pelos analistas no sistema.
D) Novas vulnerabilidades serão descobertas pelos analistas no sistema.
E) Descobrir-se-ão novas vulnerabilidades no sistema.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** O verbo "descobrirão" está no Futuro do Presente do Indicativo. A voz passiva analítica exige o verbo auxiliar "ser" no exato mesmo tempo verbal da voz ativa. Portanto, "serão" + particípio "descobertas".
- **E está errada:** Embora esteja no futuro, a alternativa E representa a voz passiva *sintética*, e a questão pediu a voz passiva *analítica*.
</details>

---

### Questão 39 (FCC - 2022 - TRE - Analista Judiciário)
Considerando as regras de formação da voz passiva, assinale a alternativa cuja conversão da voz ativa para a passiva analítica está correta, mantendo o sentido e o tempo verbal original.
Frase Ativa: "Os analistas descobrirão novas vulnerabilidades no sistema."
A) Novas vulnerabilidades são descobertas pelos analistas no sistema.
B) Novas vulnerabilidades foram descobertas pelos analistas no sistema.
C) Novas vulnerabilidades seriam descobertas pelos analistas no sistema.
D) Novas vulnerabilidades serão descobertas pelos analistas no sistema.
E) Descobrir-se-ão novas vulnerabilidades no sistema.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** O verbo "descobrirão" está no Futuro do Presente do Indicativo. A voz passiva analítica exige o verbo auxiliar "ser" no exato mesmo tempo verbal da voz ativa. Portanto, "serão" + particípio "descobertas".
- **E está errada:** Embora esteja no futuro, a alternativa E representa a voz passiva *sintética*, e a questão pediu a voz passiva *analítica*.
</details>

---

### Questão 40 (FCC - 2022 - TRE - Analista Judiciário)
Considerando as regras de formação da voz passiva, assinale a alternativa cuja conversão da voz ativa para a passiva analítica está correta, mantendo o sentido e o tempo verbal original.
Frase Ativa: "Os analistas descobrirão novas vulnerabilidades no sistema."
A) Novas vulnerabilidades são descobertas pelos analistas no sistema.
B) Novas vulnerabilidades foram descobertas pelos analistas no sistema.
C) Novas vulnerabilidades seriam descobertas pelos analistas no sistema.
D) Novas vulnerabilidades serão descobertas pelos analistas no sistema.
E) Descobrir-se-ão novas vulnerabilidades no sistema.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** O verbo "descobrirão" está no Futuro do Presente do Indicativo. A voz passiva analítica exige o verbo auxiliar "ser" no exato mesmo tempo verbal da voz ativa. Portanto, "serão" + particípio "descobertas".
- **E está errada:** Embora esteja no futuro, a alternativa E representa a voz passiva *sintética*, e a questão pediu a voz passiva *analítica*.
</details>

---

### Questão 41 (FCC - 2021 - TRT - Técnico Judiciário)
Assinale a alternativa que apresenta a correta correlação entre os tempos e modos verbais nas orações do período composto.
A) Se o administrador liberar os acessos, a equipe conseguiria concluir o relatório hoje.
B) Caso o servidor apresente falhas, os técnicos trocariam as peças imediatamente.
C) Quando nós chegarmos à conclusão do projeto, eles já tinham aprovado o orçamento.
D) Se a empresa mantivesse os pagamentos em dia, não haveria greve dos funcionários.
E) Mesmo que você saiba a senha, não pôde acessar os arquivos confidenciais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** Apresenta a correlação clássica da FCC: Pretérito Imperfeito do Subjuntivo ("mantivesse") harmonizado com o Futuro do Pretérito do Indicativo ("haveria").
- **A está errada:** O correto seria "Se o administrador liberasse... conseguiria" ou "Se liberar... conseguirá".
- **B está errada:** O correto seria "Caso apresente... trocarão".
</details>

---

### Questão 42 (FCC - 2021 - TRT - Técnico Judiciário)
Assinale a alternativa que apresenta a correta correlação entre os tempos e modos verbais nas orações do período composto.
A) Se o administrador liberar os acessos, a equipe conseguiria concluir o relatório hoje.
B) Caso o servidor apresente falhas, os técnicos trocariam as peças imediatamente.
C) Quando nós chegarmos à conclusão do projeto, eles já tinham aprovado o orçamento.
D) Se a empresa mantivesse os pagamentos em dia, não haveria greve dos funcionários.
E) Mesmo que você saiba a senha, não pôde acessar os arquivos confidenciais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** Apresenta a correlação clássica da FCC: Pretérito Imperfeito do Subjuntivo ("mantivesse") harmonizado com o Futuro do Pretérito do Indicativo ("haveria").
- **A está errada:** O correto seria "Se o administrador liberasse... conseguiria" ou "Se liberar... conseguirá".
- **B está errada:** O correto seria "Caso apresente... trocarão".
</details>

---

### Questão 43 (FCC - 2021 - TRT - Técnico Judiciário)
Assinale a alternativa que apresenta a correta correlação entre os tempos e modos verbais nas orações do período composto.
A) Se o administrador liberar os acessos, a equipe conseguiria concluir o relatório hoje.
B) Caso o servidor apresente falhas, os técnicos trocariam as peças imediatamente.
C) Quando nós chegarmos à conclusão do projeto, eles já tinham aprovado o orçamento.
D) Se a empresa mantivesse os pagamentos em dia, não haveria greve dos funcionários.
E) Mesmo que você saiba a senha, não pôde acessar os arquivos confidenciais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** Apresenta a correlação clássica da FCC: Pretérito Imperfeito do Subjuntivo ("mantivesse") harmonizado com o Futuro do Pretérito do Indicativo ("haveria").
- **A está errada:** O correto seria "Se o administrador liberasse... conseguiria" ou "Se liberar... conseguirá".
- **B está errada:** O correto seria "Caso apresente... trocarão".
</details>

---

### Questão 44 (FCC - 2021 - TRT - Técnico Judiciário)
Assinale a alternativa que apresenta a correta correlação entre os tempos e modos verbais nas orações do período composto.
A) Se o administrador liberar os acessos, a equipe conseguiria concluir o relatório hoje.
B) Caso o servidor apresente falhas, os técnicos trocariam as peças imediatamente.
C) Quando nós chegarmos à conclusão do projeto, eles já tinham aprovado o orçamento.
D) Se a empresa mantivesse os pagamentos em dia, não haveria greve dos funcionários.
E) Mesmo que você saiba a senha, não pôde acessar os arquivos confidenciais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** Apresenta a correlação clássica da FCC: Pretérito Imperfeito do Subjuntivo ("mantivesse") harmonizado com o Futuro do Pretérito do Indicativo ("haveria").
- **A está errada:** O correto seria "Se o administrador liberasse... conseguiria" ou "Se liberar... conseguirá".
- **B está errada:** O correto seria "Caso apresente... trocarão".
</details>

---

### Questão 45 (FCC - 2021 - TRT - Técnico Judiciário)
Assinale a alternativa que apresenta a correta correlação entre os tempos e modos verbais nas orações do período composto.
A) Se o administrador liberar os acessos, a equipe conseguiria concluir o relatório hoje.
B) Caso o servidor apresente falhas, os técnicos trocariam as peças imediatamente.
C) Quando nós chegarmos à conclusão do projeto, eles já tinham aprovado o orçamento.
D) Se a empresa mantivesse os pagamentos em dia, não haveria greve dos funcionários.
E) Mesmo que você saiba a senha, não pôde acessar os arquivos confidenciais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- **D está correta:** Apresenta a correlação clássica da FCC: Pretérito Imperfeito do Subjuntivo ("mantivesse") harmonizado com o Futuro do Pretérito do Indicativo ("haveria").
- **A está errada:** O correto seria "Se o administrador liberasse... conseguiria" ou "Se liberar... conseguirá".
- **B está errada:** O correto seria "Caso apresente... trocarão".
</details>

---

## 📝 TEMA 4: Inglês Técnico de TI

### Questão 46 (FCC - 2023 - Banco do Brasil - Agente de Tecnologia)
**Read the excerpt below:**
*“Unlike virtual machines (VMs) that require a full operating system for each instance, containers share the host machine’s OS kernel. This architectural difference makes containers inherently lighter, allowing developers to spin up applications in milliseconds and maximizing resource utilization across the cluster.”*

According to the text, the primary reason containers are described as "lighter" than virtual machines is because:
A) Containers are restricted to running only microservices written in Python or Go.
B) Virtual machines do not have operating systems.
C) Containers share the kernel of the host operating system, whereas each VM requires its own full operating system.
D) Containers cannot be deployed in cloud environments.
E) Virtual machines are inherently faster at executing application code.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** O texto afirma literalmente: "Unlike virtual machines (VMs) that require a full operating system for each instance, containers share the host machine’s OS kernel". Essa é a justificativa exata do porquê eles são mais leves ("lighter").
</details>

---

### Questão 47 (FCC - 2023 - Banco do Brasil - Agente de Tecnologia)
**Read the excerpt below:**
*“Unlike virtual machines (VMs) that require a full operating system for each instance, containers share the host machine’s OS kernel. This architectural difference makes containers inherently lighter, allowing developers to spin up applications in milliseconds and maximizing resource utilization across the cluster.”*

According to the text, the primary reason containers are described as "lighter" than virtual machines is because:
A) Containers are restricted to running only microservices written in Python or Go.
B) Virtual machines do not have operating systems.
C) Containers share the kernel of the host operating system, whereas each VM requires its own full operating system.
D) Containers cannot be deployed in cloud environments.
E) Virtual machines are inherently faster at executing application code.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** O texto afirma literalmente: "Unlike virtual machines (VMs) that require a full operating system for each instance, containers share the host machine’s OS kernel". Essa é a justificativa exata do porquê eles são mais leves ("lighter").
</details>

---

### Questão 48 (FCC - 2023 - Banco do Brasil - Agente de Tecnologia)
**Read the excerpt below:**
*“Unlike virtual machines (VMs) that require a full operating system for each instance, containers share the host machine’s OS kernel. This architectural difference makes containers inherently lighter, allowing developers to spin up applications in milliseconds and maximizing resource utilization across the cluster.”*

According to the text, the primary reason containers are described as "lighter" than virtual machines is because:
A) Containers are restricted to running only microservices written in Python or Go.
B) Virtual machines do not have operating systems.
C) Containers share the kernel of the host operating system, whereas each VM requires its own full operating system.
D) Containers cannot be deployed in cloud environments.
E) Virtual machines are inherently faster at executing application code.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** O texto afirma literalmente: "Unlike virtual machines (VMs) that require a full operating system for each instance, containers share the host machine’s OS kernel". Essa é a justificativa exata do porquê eles são mais leves ("lighter").
</details>

---

### Questão 49 (FCC - 2023 - Banco do Brasil - Agente de Tecnologia)
**Read the excerpt below:**
*“Unlike virtual machines (VMs) that require a full operating system for each instance, containers share the host machine’s OS kernel. This architectural difference makes containers inherently lighter, allowing developers to spin up applications in milliseconds and maximizing resource utilization across the cluster.”*

According to the text, the primary reason containers are described as "lighter" than virtual machines is because:
A) Containers are restricted to running only microservices written in Python or Go.
B) Virtual machines do not have operating systems.
C) Containers share the kernel of the host operating system, whereas each VM requires its own full operating system.
D) Containers cannot be deployed in cloud environments.
E) Virtual machines are inherently faster at executing application code.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** O texto afirma literalmente: "Unlike virtual machines (VMs) that require a full operating system for each instance, containers share the host machine’s OS kernel". Essa é a justificativa exata do porquê eles são mais leves ("lighter").
</details>

---

### Questão 50 (FCC - 2023 - Banco do Brasil - Agente de Tecnologia)
**Read the excerpt below:**
*“Unlike virtual machines (VMs) that require a full operating system for each instance, containers share the host machine’s OS kernel. This architectural difference makes containers inherently lighter, allowing developers to spin up applications in milliseconds and maximizing resource utilization across the cluster.”*

According to the text, the primary reason containers are described as "lighter" than virtual machines is because:
A) Containers are restricted to running only microservices written in Python or Go.
B) Virtual machines do not have operating systems.
C) Containers share the kernel of the host operating system, whereas each VM requires its own full operating system.
D) Containers cannot be deployed in cloud environments.
E) Virtual machines are inherently faster at executing application code.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- **C está correta:** O texto afirma literalmente: "Unlike virtual machines (VMs) that require a full operating system for each instance, containers share the host machine’s OS kernel". Essa é a justificativa exata do porquê eles são mais leves ("lighter").
</details>

---

