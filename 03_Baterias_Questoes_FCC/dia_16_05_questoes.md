# Bateria de Questões FCC — Sábado 16/05

Este arquivo contém 45 questões da banca FCC (15 por tema estudado) com gabarito comentado ocultável. Tente resolver cada questão antes de expandir o gabarito.

---

## 📝 TEMA 1: Engenharia de Software — Ciclo de Vida e Modelo Cascata

### Questão 1 (FCC - TRT 11ª Região - Analista Judiciário - Tecnologia da Informação)
No contexto do ciclo de vida de desenvolvimento de software, a atividade que se preocupa em avaliar se o sistema correto foi construído, garantindo que atende às necessidades de negócio reais do usuário final, é denominada:
A) Verificação.
B) Validação.
C) Depuração (Debugging).
D) Análise de Requisitos.
E) Projeto de Arquitetura.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** 
- **Validação:** Responde à pergunta "Estamos construindo o produto correto?" (garante que atende ao negócio/cliente).
- **Verificação:** Responde à pergunta "Estamos construindo o produto corretamente?" (garante que está de acordo com as especificações técnicas). A FCC adora cobrar essa diferença clássica de Barry Boehm.
</details>

---

### Questão 2 (FCC - TRT 24ª Região - Analista - Sistemas)
Considere o Modelo de Ciclo de Vida Cascata (Waterfall). Uma de suas características fundamentais é:
A) A possibilidade de refinar requisitos e alterar o escopo dinamicamente em qualquer fase do projeto sem custos adicionais.
B) A execução concorrente e sobreposta de todas as fases, permitindo que a codificação comece no dia 1 do projeto.
C) O caráter linear e sequencial, no qual a fase seguinte só se inicia após a conclusão e documentação da anterior.
D) A entrega frequente de protótipos incrementais e funcionais ao cliente ao final de cada iteração de duas semanas.
E) O foco principal na gestão de riscos operacionais em cada uma das fases do ciclo de desenvolvimento.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O modelo Cascata (linear/sequencial) divide o desenvolvimento em fases sucessivas que ocorrem em uma ordem rígida (Requisitos -> Projeto -> Codificação -> Teste -> Implantação -> Manutenção), com cada fase gerando documentos de saída formalizados antes da próxima começar.
</details>

---

### Questão 3 (FCC - TRT 15ª Região - Analista Judiciário - TI)
No Modelo em V de desenvolvimento de software, a fase de testes que se correlaciona diretamente com a fase de Análise de Requisitos de Negócio (Requisitos do Sistema) é o teste de:
A) Unidade (Unitário).
B) Integração.
C) Sistema.
D) Aceitação.
E) Regressão.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** No Modelo em V:
- Requisitos de Negócio / Aceitação ↔ Testes de Aceitação.
- Requisitos do Sistema / Arquitetura ↔ Testes de Sistema.
- Projeto Detalhado / Componentes ↔ Testes de Integração.
- Codificação ↔ Testes Unitários.
</details>

---

### Questão 4 (FCC - TRT 4ª Região - Analista de Sistemas)
Em um projeto de software gerenciado sob o modelo Cascata, a descoberta tardia de inconsistências nos requisitos durante a fase de testes de aceitação resulta em:
A) Baixo custo de correção, pois o sistema já está codificado e empacotado.
B) Facilidade de correção imediata, devido à flexibilidade típica do modelo linear.
C) Retorno imediato à fase de projeto de banco de dados sem a necessidade de reescrever códigos.
D) Alto custo de correção, uma vez que as fases de requisitos, projeto e codificação já foram finalizadas e precisam ser retrabalhadas.
E) Nenhuma alteração no cronograma, pois a fase de implantação já absorveu os prazos.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** Um dos maiores pontos fracos do Modelo Cascata é o alto custo do retrabalho caso erros de fases iniciais (Requisitos) só sejam detectados nas fases finais (Testes). Como o modelo é rígido, redefinir requisitos significa refazer o projeto e a implementação correspondente.
</details>

---

### Questão 5 (FCC - Assembleia Legislativa da Paraíba - Analista - Sistemas)
Considere as fases do Ciclo de Vida clássico de um software. A fase que tem por objetivo traduzir os requisitos de software em uma estrutura lógica, detalhando arquitetura de componentes, interfaces de comunicação e diagramas de banco de dados, é denominada:
A) Análise de Requisitos.
B) Implementação.
C) Projeto (Design).
D) Engenharia de Negócios.
E) Verificação.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O **Projeto (Design)** é a fase de engenharia em que se planeja *como* o sistema será estruturado para atender aos requisitos levantados na fase de Análise. É nela que são desenhados diagramas UML, arquitetura física, interfaces e o modelo de banco de dados.
</details>

---

### Questão 6 (FCC - PGE-CE - Analista de Sistemas)
Sobre a atividade de Manutenção de Software no ciclo de vida, a manutenção que é motivada pela necessidade de ajustar o software a mudanças no ambiente operacional externo (como atualização do sistema operacional ou do SGBD) sem alterar a funcionalidade do software é classificada como:
A) Corretiva.
B) Adaptativa.
C) Perfectiva (ou Evolutiva).
D) Preventiva.
E) Preditiva.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** 
- **Adaptativa:** Ajustes para rodar em novos ambientes (hardware, OS, SGBD, etc.).
- **Corretiva:** Conserto de erros reais do software.
- **Perfectiva:** Inserção de novos recursos/melhorias.
- **Preventiva:** Refatoração para evitar erros futuros.
</details>

---

### Questão 7 (FCC - Sabesp - Analista de Sistemas)
O modelo de desenvolvimento que combina aspectos do ciclo de vida clássico com a prototipação sistemática, organizando o projeto em ciclos iterativos que dão ênfase primordial à análise e mitigação de riscos, é o modelo:
A) Incremental.
B) Cascata.
C) Espiral (de Boehm).
D) RAD (Rapid Application Development).
E) RUP (Rational Unified Process).

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O modelo **Espiral** (proposto por Barry Boehm) é caracterizado por ciclos repetitivos que integram protótipos e focam intensamente em **análise de riscos** antes de dar o próximo passo do projeto.
</details>

---

### Questão 8 (FCC - TRF 3ª Região - Analista Judiciário)
O modelo Cascata de ciclo de vida de desenvolvimento de software é mais adequado para projetos que possuam:
A) Requisitos altamente dinâmicos, com constantes alterações solicitadas pelos stakeholders.
B) Requisitos conhecidos, estáveis e bem documentados desde o início do projeto.
C) Alta incerteza tecnológica, exigindo protótipos funcionais recorrentes.
D) Prazos extremamente curtos que exijam codificação imediata sem planejamento prévio.
E) Equipes que utilizem metodologias ágeis e auto-gerenciáveis como Scrum.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O modelo Cascata funciona perfeitamente quando os requisitos do projeto são perfeitamente estáveis, claros e conhecidos pela equipe desde o início, reduzindo o risco de alterações de escopo ao longo do ciclo.
</details>

---

### Questão 9 (FCC - TRT 6ª Região - Tecnologia da Informação)
No ciclo de vida de desenvolvimento, a verificação estatística de que o código escrito atende às especificações de design construídas na fase anterior é realizada primariamente na fase de:
A) Projeto Físico.
B) Testes Unitários e de Integração.
C) Análise de Requisitos.
D) Levantamento de Dados.
E) Implantação do Sistema.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Os testes unitários e de integração servem para verificar se o código escrito reflete e respeita as especificações detalhadas do projeto, validando se os componentes se integram conforme a arquitetura planejada.
</details>

---

### Questão 10 (FCC - MPE-RS - Analista - Banco de Dados)
A engenharia de requisitos possui uma atividade que busca assegurar que a especificação de requisitos definida de fato descreve o comportamento pretendido do sistema e é aceitável pelos stakeholders. Essa atividade é denominada:
A) Elicitação de requisitos.
B) Análise e negociação.
C) Validação de requisitos.
D) Gerenciamento de requisitos.
E) Projeto de dados.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A **Validação de Requisitos** é a fase onde se revisam os requisitos junto ao cliente e especialistas para certificar que eles estão corretos, consistentes, completos e condizentes com a realidade de negócio.
</details>

---

### Questão 11 (FCC - TRT 11ª Região - Analista)
Em um projeto desenvolvido sob o modelo Cascata, a fase de testes sistemáticos de todo o sistema integrado, simulando o ambiente de produção antes do aceite final do cliente, é:
A) Teste de Unidade.
B) Teste de Sistema.
C) Teste de Caixa-Preta Individual.
D) Depuração de Compilação.
E) Validação Unitária.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O **Teste de Sistema** valida o comportamento global do software integrado rodando em condições similares às de produção, focando nas especificações do sistema de ponta a ponta.
</details>

---

### Questão 12 (FCC - ARTESP - Analista de Sistemas)
No contexto do ciclo de vida de software, as atividades de engenharia destinadas a determinar as restrições operacionais e os limites físicos de desempenho do sistema que não estão diretamente ligados às funções de negócio são classificados na fase de requisitos como:
A) Requisitos Funcionais.
B) Requisitos Não Funcionais.
C) Requisitos de Domínio.
D) Casos de Uso Físicos.
E) Regras de Negócio Primárias.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Os **Requisitos Não Funcionais (RNFs)** determinam aspectos qualitativos do sistema (desempenho, segurança, portabilidade, usabilidade, disponibilidade) e restrições de tecnologia.
</details>

---

### Questão 13 (FCC - TRT 20ª Região - Tecnologia da Informação)
Uma das desvantagens mais apontadas do modelo linear clássico (Cascata) no desenvolvimento moderno de aplicações de software corporativas é:
A) A falta de estruturação e documentação nas entregas de cada etapa.
B) A exigência de constante interação do cliente ao longo de todas as semanas do ciclo.
C) A indisponibilidade de um produto funcional (software executável) até que as fases finais do ciclo estejam concluídas.
D) A dependência excessiva de ferramentas CASE de modelagem visual.
E) A natureza caótica de codificação e correção contínua sem regras de transição.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** No modelo Cascata, como o software só é construído de fato nas etapas tardias (implementação/teste), o cliente passa a maior parte do tempo vendo apenas papéis e especificações, tendo acesso à primeira versão executável apenas no final do projeto.
</details>

---

### Questão 14 (FCC - Sabesp - Analista)
O modelo de ciclo de vida que se baseia na filosofia de reuso sistemático e no desenvolvimento de múltiplos ciclos curtos e rápidos, focando no desenvolvimento e na avaliação conjunta com o usuário por meio de ferramentas visuais e geradores de código, é o modelo:
A) RUP.
B) Cascata puro.
C) RAD (Rapid Application Development).
D) Espiral de 4 quadrantes.
E) Ciclo de Vida Clássico com Revisões.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O modelo **RAD** (Desenvolvimento Rápido de Aplicações) busca acelerar o ciclo de desenvolvimento usando ferramentas de alta produtividade (como geradores automáticos de código e interfaces visuais) e foca fortemente no reuso de componentes de software.
</details>

---

### Questão 15 (FCC - TRF 3ª Região - Analista)
A primeira fase formal do Ciclo de Vida de Software que tem como principal entregável o Estudo de Viabilidade Econômica, Técnica e Organizacional, respondendo se o desenvolvimento do sistema proposto faz sentido para a instituição, é denominada:
A) Análise de Requisitos.
B) Planejamento / Investigação Preliminar.
C) Projeto Lógico.
D) Codificação e Provas.
E) Implantação e Transição.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O **Planejamento** (ou Estudo de Viabilidade / Análise Preliminar) avalia se o projeto deve prosseguir ou não, gerando relatórios de viabilidade financeira e técnica antes de alocar recursos para o levantamento de requisitos.
</details>

---

## 📝 TEMA 2: Banco de Dados — Modelo Relacional e Conceitos de Chave

### Questão 16 (FCC - TRT 11ª Região - Analista Judiciário - TI)
No modelo de dados relacional, uma restrição de integridade que determina que nenhum valor pertencente à chave primária de uma tabela (relação) pode receber um valor nulo (NULL) é denominada:
A) Integridade Referencial.
B) Integridade de Domínio.
C) Integridade de Entidade.
D) Integridade de Chave Estrangeira.
E) Restrição de Nulidade Comum.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A **Integridade de Entidade** é a regra formal que garante que nenhuma tupla de uma tabela possua valores nulos na coluna (ou conjunto de colunas) da Chave Primária (PK). Afinal, o nulo impede a identificação única do registro.
</details>

---

### Questão 17 (FCC - TRT 24ª Região - Analista - Tecnologia da Informação)
Considere duas tabelas no modelo relacional: `CLIENTES` (com chave primária `id_cliente`) e `VENDAS` (com chave primária `id_venda` e uma chave estrangeira `id_cliente` que referencia a tabela `CLIENTES`). Se tentarmos excluir um cliente da tabela `CLIENTES` que possui registros de vendas vinculados na tabela `VENDAS`, e o banco de dados disparar um erro bloqueando a transação, a política de integridade referencial configurada para esta exclusão é:
A) ON DELETE CASCADE.
B) ON DELETE SET NULL.
C) ON DELETE NO ACTION (ou RESTRICT).
D) ON DELETE DEFAULT.
E) ON DELETE BLOCK.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A política **RESTRICT** ou **NO ACTION** impede/bloqueia a exclusão da tupla pai caso existam tuplas filhas vinculadas pela chave estrangeira.
- `CASCADE` excluiria as vendas filhas automaticamente.
- `SET NULL` colocaria `NULL` no campo `id_cliente` das vendas.
</details>

---

### Questão 18 (FCC - TRT 3ª Região - Analista - Banco de Dados)
Em termos formais de bancos de dados relacionais, o número de colunas (atributos) que constituem uma relação (tabela) e o número de linhas (tuplas) nela armazenadas em um determinado momento são denominados, respectivamente:
A) Grau e Cardinalidade.
B) Cardinalidade e Grau.
C) Domínio e Instância.
D) Esquema e Extensão.
E) Grau e Domínio.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** 
- **Grau:** Quantidade de colunas (atributos).
- **Cardinalidade:** Quantidade de linhas (tuplas). 
Isso cai com muita frequência nas provas de TI da FCC.
</details>

---

### Questão 19 (FCC - PGE-CE - Analista de Sistemas)
No modelo relacional de bancos de dados, qualquer conjunto de um ou mais atributos cujos valores identificam unicamente cada tupla de uma relação é classificado conceitualmente como:
A) Superchave.
B) Chave Alternativa.
C) Chave Estrangeira.
D) Domínio Unívoco.
E) Chave Surrogada.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** Uma **Superchave** é um conjunto de atributos que identifica unicamente uma tupla de uma relação. Se uma superchave não possuir nenhum subconjunto próprio que também seja uma superchave, ela é uma **Chave Candidata** (superchave minimal).
</details>

---

### Questão 20 (FCC - TRF 3ª Região - Analista TI)
Ao projetar uma tabela `FUNCIONARIOS` em um banco de dados relacional, constatou-se que as colunas `CPF` e `EMAIL` possuem valores únicos e não nulos para todos os registros. O analista de banco de dados escolheu a coluna `CPF` como a Chave Primária (PK) da tabela. Conceitualmente, a coluna `EMAIL` será classificada como uma:
A) Chave Primária Secundária.
B) Chave Estrangeira.
C) Chave Candidata que se tornou Chave Alternativa.
D) Chave Alternativa que se tornou Chave Candidata.
E) Superchave Não Candidata.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** CPF e EMAIL são **Chaves Candidatas** (podem identificar unicamente a tupla). Ao selecionar o CPF como Chave Primária, as chaves candidatas restantes (neste caso, o EMAIL) tornam-se **Chaves Alternativas**.
</details>

---

### Questão 21 (FCC - Sabesp - Analista)
Em uma modelagem de banco de dados relacional, a restrição que define o conjunto de valores admissíveis para uma determinada coluna da tabela, determinando seu tipo (ex: inteiro, data, texto de 20 caracteres) e limites adicionais, é a restrição de:
A) Chave Primária.
B) Integridade de Domínio.
C) Integridade Referencial.
D) Chave Estrangeira.
E) Autenticidade de Atributo.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A **Integridade de Domínio** define o conjunto de valores válidos para um atributo. Inclui tipo de dados, formato e restrições de verificação (CHECK constraints).
</details>

---

### Questão 22 (FCC - MPE-RS - Engenheiro de Dados)
Considere a seguinte regra sobre chaves no modelo relacional: "Uma chave estrangeira em uma relação R1 refere-se aos valores da chave primária em outra relação R2." O que acontece se uma tupla em R1 contiver um valor na chave estrangeira que não existe na chave primária de R2?
A) O modelo relacional aceita a inclusão normalmente se a tabela R1 possuir mais de 100 registros.
B) A restrição de integridade de entidade é violada e o banco de dados altera os valores de R2 automaticamente.
C) A restrição de integridade referencial é violada e o SGBD impede a transação.
D) O SGBD cria automaticamente uma linha correspondente em R2 para restabelecer a integridade.
E) A tabela R1 é destruída (DROP) pelo banco de dados por motivos de segurança estrutural.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A **Integridade Referencial** impede que existam "ponteiros órfãos", ou seja, valores de chave estrangeira (FK) que não possuam correspondente exato na tabela referenciada (PK). O SGBD impedirá a transação de inserção ou atualização que viole essa regra.
</details>

---

### Questão 23 (FCC - TRT 6ª Região - Tecnologia da Informação)
Uma chave artificial (ou sintética), gerada de forma automatizada pelo próprio SGBD (por exemplo, usando auto-incremento, sequências ou UUID) com a única finalidade de servir como chave primária simplificada de uma relação, sem possuir qualquer significado para o negócio, é denominada:
A) Chave Estrangeira Redundante.
B) Chave Alternativa.
C) Chave Composta.
D) Chave Surrogada (Surrogate Key).
E) Chave de Domínio Interno.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** A **Chave Surrogada (Surrogate Key)** é um identificador único artificial gerado pelo sistema (ex: ID numérico incremental) que serve de PK para contornar problemas de chaves naturais complexas ou instáveis.
</details>

---

### Questão 24 (FCC - TRT 20ª Região - Analista Judiciário)
Em bancos de dados relacionais, o valor especial `NULL` representa:
A) O valor numérico zero.
B) Uma string de texto vazia `""`.
C) A ausência de valor ou um valor desconhecido.
D) Um erro crítico de corrupção física do disco.
E) O ponteiro de endereço do início da tabela.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O `NULL` no modelo relacional e em SQL não significa zero ou string vazia, mas sim que o valor é **ausente, omitido ou desconhecido**.
</details>

---

### Questão 25 (FCC - DPE-SP - Analista de Tecnologia da Informação)
Considere as propriedades do Modelo Relacional de Dados. Qual das seguintes afirmações está correta?
A) Uma relação pode conter linhas duplicadas em sua totalidade (idênticas em todas as colunas).
B) A ordem física de armazenamento das linhas em uma tabela altera o resultado lógico das consultas SQL relacionais.
C) A ordem de exibição das colunas no esquema lógico de uma tabela interfere na integridade física do banco de dados.
D) Cada célula (interseção de linha e coluna) em uma relação clássica deve conter um valor atômico (único e indivisível).
E) O número de tuplas em uma relação deve ser sempre um múltiplo do grau da relação.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** No modelo relacional clássico (baseado na Primeira Forma Normal - 1FN), as relações não admitem atributos multivalorados ou compostos. Toda interseção de linha e coluna deve armazenar valores **atômicos**.
</details>

---

### Questão 26 (FCC - TRF 3ª Região - Analista de Sistemas)
Se uma chave primária é composta por mais de uma coluna, o mecanismo de banco de dados garante que:
A) Apenas a primeira coluna selecionada na PK não pode conter valores nulos.
B) A combinação de valores de todas as colunas que compõem a PK deve ser única e nenhuma das colunas pode ser NULL.
C) O SGBD cria automaticamente tabelas virtuais para cada coluna da chave composta.
D) O grau da tabela é multiplicado pela quantidade de colunas da chave composta.
E) A tabela passa a aceitar chaves estrangeiras sem verificação referencial.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Em uma **Chave Primária Composta**, a restrição de unicidade e a restrição de não-nulidade aplicam-se ao conjunto e a cada um dos atributos individuais envolvidos.
</details>

---

### Questão 27 (FCC - ARTESP - Especialista)
Qual das seguintes operações pode vir a violar a integridade de entidade em um banco de dados relacional?
A) Inserir uma linha na tabela filha cuja FK aponte para um pai existente.
B) Atualizar a PK de um registro para um valor já existente ou para NULL.
C) Deletar uma linha de uma tabela que não é referenciada por nenhuma outra.
D) Alterar a coluna de descrição (texto) de um registro para NULL.
E) Consultar registros de uma tabela ordenando por uma coluna indexada.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A integridade de entidade proíbe que a PK seja nula ou duplicada. Ao tentar atualizar a PK de um registro existente para `NULL` ou para um valor idêntico ao de outra linha, violamos essa integridade.
</details>

---

### Questão 28 (FCC - TRT 15ª Região - Analista)
Em uma tabela chamada `PRODUTOS`, deseja-se criar uma coluna `preco` que não permita valores negativos. A restrição que garante essa regra a nível de banco de dados é classificada como:
A) Restrição de Integridade Referencial.
B) Restrição de Integridade de Entidade.
C) Restrição de Verificação (CHECK constraint), que é um tipo de integridade de domínio.
D) Restrição de Chave Alternativa.
E) Gatilho de Sistema (System Trigger).

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A restrição do tipo `CHECK (preco >= 0)` limita os valores válidos para uma coluna no seu domínio, sendo uma restrição de integridade de domínio.
</details>

---

### Questão 29 (FCC - Sabesp - TI)
No modelo relacional, quando dizemos que as tabelas são "relações", estamos nos baseando no conceito matemático de:
A) Matrizes bidimensionais indexadas.
B) Relação matemática, que é um subconjunto do produto cartesiano de domínios.
C) Teoria dos Grafos direcionados acíclicos.
D) Árvores binárias de busca balanceada.
E) Cálculo diferencial multivariável.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Edgar F. Codd baseou o modelo relacional na matemática de conjuntos, definindo uma "relação" como um subconjunto do produto cartesiano dos domínios dos seus atributos.
</details>

---

### Questão 30 (FCC - TRT 9ª Região - Tecnologia da Informação)
Uma tabela `CONTRATOS` possui os atributos `numero_contrato`, `ano_contrato`, `id_cliente` e `valor`. Sabendo que a identificação unívoca de cada contrato exige a combinação de `numero_contrato` e `ano_contrato`, qual será o grau mínimo de integridade de entidade exigido para essa tabela?
A) Que apenas o `numero_contrato` não seja nulo.
B) Que nem `numero_contrato` nem `ano_contrato` contenham valores nulos e a sua combinação nunca se repita.
C) Que `id_cliente` seja cadastrado na tabela de clientes.
D) Que o `valor` seja um decimal positivo maior que zero.
E) Que a tabela possua no máximo duas chaves estrangeiras.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** Sendo a chave primária composta por `(numero_contrato, ano_contrato)`, ambos os campos são obrigatórios (não nulos) e a combinação deve ser unívoca em toda a tabela.
</details>

---

## 📝 TEMA 3: Língua Portuguesa — Compreensão e Interpretação de Textos

*Instruções: Leia os textos sugeridos para responder às questões correspondentes, seguindo o perfil rigoroso de leitura lógica e análise semântica da FCC.*

---

### Texto I
> *"O avanço tecnológico, longe de simplesmente extinguir o labor humano, desloca-o para zonas de maior abstração. O artesão que outrora moldava o ferro à força do braço vê-se hoje obrigado a programar o algoritmo da prensa automatizada. Não houve alívio da exigência de rigor ou de dedicação intelectual; houve, isto sim, uma alteração de sintaxe produtiva. Aqueles que advogam o fim do trabalho ignoram a persistente necessidade de mediação interpretativa que as máquinas exigem."*

### Questão 31 (FCC - Adaptada)
Segundo o autor do Texto I, o advento da tecnologia no processo de produção industrial:
A) Reduziu a carga de dedicação intelectual exigida do trabalhador fabril.
B) Eliminou completamente a presença humana na sintaxe produtiva.
C) Transferiu o esforço humano para atividades que demandam maior capacidade de abstração.
D) Confirmou a tese de que o trabalho humano será extinto em curto prazo pelas máquinas.
E) Restabeleceu o trabalho puramente braçal como a base de valor da economia de mercado.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O texto afirma expressamente no primeiro período: *"O avanço tecnológico, longe de simplesmente extinguir o labor humano, desloca-o para zonas de maior abstração."* As outras alternativas distorcem ou contradizem as ideias do autor.
</details>

---

### Questão 32 (FCC - Adaptada)
Infere-se do Texto I que o autor:
A) Vê a automação como um retrocesso civilizatório que precariza a capacitação do trabalhador.
B) Acredita que as máquinas dependem da inteligência humana para operar e contextualizar as tarefas.
C) Considera que a programação de algoritmos exige menor esforço que a atividade do antigo artesão.
D) Defende a abolição imediata da tecnologia para preservar os postos de trabalho tradicionais.
E) Considera as máquinas autossuficientes na interpretação e execução de seus próprios processos.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A inferência é sustentada pela última frase do texto: *"Aqueles que advogam o fim do trabalho ignoram a persistente necessidade de mediação interpretativa que as máquinas exigem."* Isso demonstra que as máquinas ainda demandam a mediação da capacidade humana de interpretar dados.
</details>

---

### Questão 33 (FCC - Adaptada)
No trecho *"O artesão que outrora moldava o ferro à força do braço vê-se hoje obrigado a programar o algoritmo..."*, o termo sublinhado **outrora** estabelece uma relação lógica de:
A) Oposição às condições atuais de trabalho.
B) Concessão a fatos históricos irrelevantes.
C) Causa do desenvolvimento de prensa automatizada.
D) Tempo, situando a atividade do artesão em um período passado.
E) Consequência imediata da inserção de computadores na indústria.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** O advérbio **outrora** significa "em outro tempo", "antigamente", possuindo valor puramente temporal que contrasta o passado do artesão com o seu presente (*"vê-se hoje..."*).
</details>

---

### Questão 34 (FCC - Adaptada)
Sem prejuízo para o sentido original e mantendo a correção gramatical do texto, a expressão *"longe de simplesmente extinguir"* poderia ser substituída por:
A) Apesar de extinguir de modo sumário.
B) Sem que isso implique a mera extinção.
C) Contanto que se elimine de forma simples.
D) À medida que se extingue sumariamente.
E) Conquanto extinga de forma definitiva.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A expressão *"longe de simplesmente extinguir"* indica que a extinção não é o resultado real da tecnologia, apenas um deslocamento. A opção B preserva esse sentido de forma gramaticalmente correta.
</details>

---

### Texto II
> *"A pressa contemporânea por respostas prontas tem esvaziado o debate público de sua necessária espessura reflexiva. O cidadão, saturado por fluxos ininterruptos de dados digitais, confunde a posse da informação com a aquisição do conhecimento. A primeira é externa, instantânea e acumulável; o segundo exige tempo de maturação, confronto de hipóteses e silêncio cognitivo."*

### Questão 35 (FCC - Adaptada)
Com base no Texto II, é correto afirmar que:
A) O debate público atual está mais profundo devido à abundância de informações na internet.
B) A posse de informações garante automaticamente a evolução cultural do indivíduo.
C) Informação e conhecimento são apresentados pelo autor como conceitos distintos e com dinâmicas próprias.
D) O fluxo incessante de dados impede que o cidadão tenha acesso à informação de qualidade.
E) O silêncio cognitivo é prejudicial para o debate político.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O autor descreve a informação como *"externa, instantânea e acumulável"* e o conhecimento como algo que *"exige tempo de maturação, confronto de hipóteses e silêncio cognitivo"*, explicitando que a posse de dados não equivale à inteligência ou sabedoria.
</details>

---

### Questão 36 (FCC - Adaptada)
No Texto II, a oração *"confunde a posse da informação com a aquisição do conhecimento"* revela:
A) Uma atitude crítica do autor diante do comportamento cognitivo gerado pela velocidade das redes digitais.
B) O endosso do autor à fusão definitiva desses dois conceitos na era moderna.
C) A incapacidade biológica do cérebro humano em processar dados computacionais.
D) Um elogio do autor à inteligência do cidadão contemporâneo na triagem de dados.
E) Uma justificativa de ordem econômica para o esvaziamento das bibliotecas físicas.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

**Justificativa:** O autor critica a "pressa contemporânea" e a confusão mental gerada pelo excesso de dados, que empobrece a qualidade do debate público e da reflexão pessoal.
</details>

---

### Questão 37 (FCC - Adaptada)
De acordo com o Texto II, o conhecimento, diferentemente da informação, pressupõe:
A) Velocidade de replicação digital.
B) Acúmulo de dados desestruturados.
C) Processos internos de análise e reflexão no decorrer do tempo.
D) Acesso imediato a respostas curtas nas redes sociais.
E) Esvaziamento completo da memória individual de longo prazo.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O texto diz expressamente que o conhecimento *"exige tempo de maturação, confronto de hipóteses e silêncio cognitivo"*, o que nos direciona para processos reflexivos internos.
</details>

---

### Questão 38 (FCC - Adaptada)
*"A primeira é externa, instantânea e acumulável; o segundo exige tempo..."*
Nesse trecho do Texto II, os pronomes sublinhados referem-se, respectivamente, a:
A) Pressa e resposta.
B) Espessura e informação.
C) Posse e aquisição.
D) Informação e conhecimento.
E) Informação e cidadão.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** Pela regra gramatical de coesão referencial por anáfora:
- "A primeira" retoma a última palavra feminina listada na comparação anterior: **informação**.
- "O segundo" retoma o último termo masculino correspondente: **conhecimento**.
</details>

---

### Texto III
> *"Não há dúvida de que o cumprimento estrito das formalidades processuais constitui garantia inalienável do cidadão contra os arbítrios do poder estatal. Entretanto, a hipertrofia de ritos burocráticos, quando apartada da razoabilidade e do anseio de pacificação social, degenera em mero formalismo vazio. O direito que se perde em labirintos procedimentais nega-se a si mesmo, convertendo-se em instrumento de protelação e injustiça."*

### Questão 39 (FCC - Adaptada)
A ideia central defendida pelo autor no Texto III é:
A) O formalismo processual deve ser completamente abandonado para acelerar os julgamentos.
B) A burocracia é o único mecanismo capaz de impedir a corrupção institucional do judiciário.
C) O excesso de formalidades processuais, quando desprovido de sentido prático e de justiça, prejudica a própria finalidade do direito.
D) O cidadão comum prefere a protelação do processo à obtenção de sentenças rápidas.
E) O poder estatal deve intervir nos processos para garantir que os ritos sejam executados de forma rápida.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** O texto argumenta que embora as formalidades sejam garantias contra o arbítrio, o excesso sem nexo e sem razoabilidade (hipertrofia) transforma o direito em um labirinto protelatório inútil.
</details>

---

### Questão 40 (FCC - Adaptada)
No Texto III, a palavra **Entretanto** inicia o período introduzindo uma relação lógica de:
A) Explicação do período anterior.
B) Conclusão sobre as garantias inalienáveis.
C) Concessão às decisões da justiça estatal.
D) Oposição e limitação às ideias já apresentadas.
E) Comparação entre burocracia e formalismo.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

**Justificativa:** A palavra **Entretanto** é uma conjunção adversativa, introduzindo uma ideia de contraposição ou limitação em relação à afirmação de que as formalidades são garantias inalienáveis.
</details>

---

### Questão 41 (FCC - Adaptada)
Considere a frase do Texto III: *"Entretanto, a hipertrofia de ritos burocráticos, quando apartada da razoabilidade..."*
A palavra **apartada** pode ser substituída, sem alteração de sentido no contexto, por:
A) Unida.
B) Separada.
C) Protegida.
D) Identificada.
E) Conduzida.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** "Apartado" significa isolado, separado, afastado de algo. No contexto, significa que a burocracia foi separada/desconectada da razoabilidade.
</details>

---

### Questão 42 (FCC - Adaptada)
A última oração do Texto III (*"...convertendo-se em instrumento de protelação..."*) indica que o direito degenerado atua como causa de:
A) Julgamentos eficientes.
B) Atrasos desnecessários na solução de conflitos.
C) Transparência absoluta do poder do Estado.
D) Inclusão das minorias no sistema legal.
E) Redução imediata das custas processuais.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** A palavra **protelação** significa adiar, atrasar, postergar. Logo, converter-se em instrumento de protelação significa atuar gerando atrasos na justiça.
</details>

---

### Questão 43 (FCC - Adaptada)
O autor do Texto III qualifica as formalidades processuais como *"garantia inalienável"*. Com essa expressão, infere-se que tais formalidades:
A) Podem ser vendidas ou trocadas pelos advogados no decorrer do processo.
B) São dispensáveis sempre que o réu for considerado culpado de antemão.
C) São direitos fundamentais de defesa que não podem ser retirados do cidadão.
D) Devem ser ditadas unicamente pela força policial.
E) Foram revogadas pelas leis processuais modernas.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A palavra **inalienável** qualifica algo de que não se pode abrir mão, transferir ou renunciar. Logo, as formalidades são retratadas como direitos fundamentais insubstituíveis e irrenunciáveis.
</details>

---

### Questão 44 (FCC - Adaptada)
*"O direito que se perde em labirintos procedimentais nega-se a si mesmo..."*
A metáfora **labirintos procedimentais** sugere:
A) O caminho reto e simples traçado pelas leis modernas.
B) A transparência do atendimento judiciário em balcões digitais.
C) A complexidade confusa e inútil que dificulta a resolução dos processos.
D) O mapeamento lógico do fluxo de dados em computadores de alto desempenho.
E) A arquitetura física moderna das varas dos tribunais de justiça.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

**Justificativa:** A figura de linguagem do "labirinto" evoca caminhos confusos, perdas de rumo e dificuldades de saída, aplicando-se à burocracia processual exagerada que impede o cidadão de obter uma resposta rápida da justiça.
</details>

---

### Questão 45 (FCC - Adaptada)
Qual das seguintes atitudes é incompatível com o posicionamento geral do autor do Texto III?
A) Simplificar etapas do rito processual respeitando o contraditório e a ampla defesa.
B) Exigir que todas as petições passem por múltiplos cartórios redundantes apenas para recolher assinaturas burocráticas sem valor prático.
C) Promover a conciliação judicial para acelerar a pacificação social.
D) Ponderar a aplicação de regras processuais rígidas com base no bom senso e na razoabilidade.
E) Garantir que o réu tenha amplo acesso aos recursos legais previstos em lei contra o abuso de autoridade.

<details>
<summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

**Justificativa:** O autor critica a "hipertrofia de ritos burocráticos" e o "formalismo vazio", logo, a atitude descrita em B (burocracia redundante inútil) vai diretamente contra a tese defendida no texto.
</details>
