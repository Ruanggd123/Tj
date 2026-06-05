# 📚 Guia de Estudos — Quinta-feira 04/06
## Foco: Banco de Dados, Cloud Computing (AWS/Containers) e APIs RESTful

Neste quarto dia de estudos da bateria, nosso objetivo principal é dominar conceitos clássicos e modernos muito cobrados pela banca FCC: Modelagem e Normalização Relacional, ferramentas e arquiteturas de Nuvem (AWS e Docker) e os princípios arquiteturais e contratuais de APIs RESTful.

---

## 🗄️ BLOCO 1: Banco de Dados (Modelagem ER e Normalização)

### 1. Modelagem Entidade-Relacionamento (ER)
* **Entidade Forte vs Fraca**: Entidade forte tem chave primária própria. Entidade fraca não possui chave suficiente para se identificar unicamente no banco de dados e depende de uma entidade forte (herda a chave da forte formando uma chave composta com seu discriminador).
* **Relacionamentos (Cardinalidade)**:
  - **1:N (Um para Muitos)**: A chave primária do lado "1" desce como chave estrangeira na tabela do lado "N". Ex: Um Autor tem vários Livros. A tabela Livro recebe o `id_autor`.
  - **N:M (Muitos para Muitos)**: É obrigatória a criação de uma **tabela associativa** (tabela de junção) contendo as chaves estrangeiras de ambas as tabelas originais, formando uma chave primária composta.
  - **1:N Recursivo (Auto-relacionamento)**: A tabela recebe uma chave estrangeira apontando para sua própria chave primária (ex: Funcionário recebendo `id_gerente`).

### 2. Normalização de Dados
Processo para organizar dados visando **evitar redundância e anomalias** (de inserção, atualização e exclusão).
* **1FN (Primeira Forma Normal)**: Exige que os valores sejam atômicos. Não permite grupos repetitivos, listas ou atributos multivalorados em uma mesma coluna.
* **2FN (Segunda Forma Normal)**: Deve estar na 1FN e **não possuir dependências parciais**. Toda coluna que não é chave deve depender da chave primária composta inteira, e não apenas de uma parte dela.
* **3FN (Terceira Forma Normal)**: Deve estar na 2FN e **não possuir dependências transitivas**. Um atributo não-chave não pode depender de outro atributo não-chave. (A regra é: Atributos dependem da chave, toda a chave, e *nada mais que a chave*).
* **FNBC (Forma Normal de Boyce-Codd)**: Uma versão mais forte da 3FN. Nela, para toda dependência funcional X -> Y, X deve ser necessariamente uma superchave candidata. Elimina sobreposições de chaves compostas que a 3FN ignora.
* **Desnormalização**: Ato deliberado de quebrar as regras de normalização (inserindo redundância) para otimizar o tempo de leitura de consultas pesadas (JOINs).

---

## ☁️ BLOCO 2: Cloud Computing (AWS e Containers)

### 1. Serviços Essenciais da AWS
* **Amazon EC2 (Elastic Compute Cloud)**: IaaS puro. Máquinas virtuais sob demanda. Principais formas de preço: On-demand (sob demanda normal), Reserved (instâncias reservadas com desconto para longo prazo) e Spot (usa capacidade ociosa com descontos enormes, mas podem ser desligadas a qualquer momento).
* **Amazon S3 (Simple Storage Service)**: Armazenamento de **Objetos** (e não blocos ou arquivos tradicionais). Usa *Buckets* contendo o arquivo e seus metadados. Ideal para backups e arquivos estáticos.
* **Amazon RDS (Relational Database Service)**: Banco de dados relacional gerenciado (PostgreSQL, MySQL, SQL Server). Permite escalabilidade vertical e uso de *Read Replicas* (réplicas de leitura para desafogar o banco principal de consultas analíticas).
* **AWS Lambda**: Serviço de computação *Serverless* (sem servidor). Executa código apenas em resposta a eventos (ex: um arquivo chegando no S3) sem necessidade de gerenciar o sistema operacional. Paga-se apenas pelo tempo de execução em milissegundos.

### 2. Virtualização e Containers (Docker)
* **VMs (Máquinas Virtuais)**: Usam um *Hypervisor* (Tipo 1 Bare-metal ou Tipo 2 Hosted) para emular hardware. Cada VM roda um Sistema Operacional convidado (Guest OS) completo. Mais pesado.
* **Containers (ex: Docker)**: Compartilham o Kernel do sistema operacional hospedeiro, mas rodam em espaços isolados de usuário. Não possuem Guest OS, o que os torna levíssimos (inicialização em segundos/milissegundos).
* **Namespaces e cgroups**: Tecnologias nativas do Kernel do Linux que permitem a magia dos containers. **Namespaces** cuidam do isolamento lógico (rede independente, IDs de processo independentes). **cgroups (Control Groups)** limitam o uso de hardware (CPU, RAM).

---

## 🔌 BLOCO 3: Engenharia de Software (APIs RESTful e Swagger)

### 1. Princípios de APIs REST
* **Statelessness (Sem Estado)**: Cada requisição do cliente para o servidor deve conter todas as informações necessárias para que o servidor entenda o pedido. O servidor não guarda sessão do cliente entre chamadas.
* **Idempotência**: Uma operação é idempotente se chamá-la 1 ou 100 vezes seguidas produz o mesmo resultado no estado do sistema. **GET, PUT, DELETE, HEAD e OPTIONS são idempotentes**. **POST e PATCH geralmente não são idempotentes**.
* **PUT vs PATCH**: 
  - `PUT`: Substituição **total** do recurso. Se não enviar um campo, ele é sobrescrito com nulo/vazio.
  - `PATCH`: Modificação **parcial** do recurso. Atualiza apenas os campos específicos enviados no JSON.
* **Paginação**: Técnica obrigatória para grandes volumes de dados. Retorna resultados em pedaços pequenos (chunks) utilizando variáveis na URL (ex: `?page=2&limit=50`), economizando banda e processamento.
* **HATEOAS**: A API se auto-descreve devolvendo hyperlinks de navegação para as ações seguintes que o cliente pode tomar a partir do estado atual daquele recurso.

### 2. Swagger / OpenAPI
* **O que é**: Uma linguagem de especificação padronizada para documentar APIs RESTful e seus contratos. 
* **Para que serve**: Permite visualizar claramente as rotas, os verbos HTTP, as respostas de sucesso/erro e os formatos (schemas) de JSON esperados. As especificações são comumente escritas em formato **YAML** ou JSON.

### 3. Códigos de Resposta HTTP Frequentes
* **200 OK**: Operação realizada com sucesso (mais comum em GET/PUT).
* **201 Created**: Recurso criado com sucesso (mais comum em POST).
* **400 Bad Request**: Erro do cliente (ex: JSON mal formatado ou faltando dados vitais).
* **404 Not Found**: A URL (o recurso) solicitado não foi encontrado no servidor.

---

## 📇 Flashcards de Memorização (Revisão Rápida)

1. **Qual a diferença entre a 2FN e a 3FN na normalização?**
   R: A 2FN proíbe dependência parcial (atributos dependendo de parte da chave composta). A 3FN proíbe dependência transitiva (atributo não-chave dependendo de outro atributo não-chave).
2. **O que é uma instância AWS Spot e quando usá-la?**
   R: É uma máquina virtual bem mais barata proveniente de capacidade ociosa do data center da Amazon, mas pode ser finalizada a qualquer momento. Ideal para processamentos em lote não-críticos.
3. **Quais são os verbos REST que realizam substituição total e parcial do recurso?**
   R: PUT (substituição total) e PATCH (atualização parcial).
4. **O que a tecnologia "cgroups" faz no contexto de containers Linux?**
   R: Ela restringe e mede a quantidade de recursos físicos de hardware (CPU, Memória, I/O) que um container pode utilizar.
5. **No modelo ER, como mapeamos um relacionamento N:M para o banco relacional lógico?**
   R: Criando obrigatoriamente uma terceira tabela (associativa/junção) contendo as chaves estrangeiras de ambas as tabelas originais.

---
*Fim do guia do dia 04/06. As questões de hoje já estão disponíveis no web app para você fixar tudo na prática!*
