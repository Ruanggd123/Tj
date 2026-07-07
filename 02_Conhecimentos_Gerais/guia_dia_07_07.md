# Guia de Estudos Definitivo — Terça-feira, 07/07/2026

**Semana 8: Fechamento de Edital e Decorebas Pesadas**
O foco desta semana é a memória de curto prazo (Decoreba) para a banca FCC. Hoje o dia é intenso, cheio de normativos e arquitetura.

---

## 🎯 Bloco 1: Banco de Dados — Formas Normais, JOINs e Sintaxes

### 1. Formas Normais (Decoreba Express)
*   **1FN:** Todos os atributos devem ser **atômicos** (indivisíveis) e monovalorados. (Fim das listas e vírgulas na mesma célula).
*   **2FN:** Estar na 1FN + **NÃO haver dependência parcial**. (Todos os atributos não-chave devem depender da *chave primária inteira*, não só de um pedaço dela). *Dica: Se a tabela tem chave simples, e está na 1FN, já está automaticamente na 2FN.*
*   **3FN:** Estar na 2FN + **NÃO haver dependência transitiva**. (Um atributo não-chave não pode depender de outro atributo não-chave. Todos dependem *apenas* da chave).
*   **FNBC (Boyce-Codd):** Versão mais rígida da 3FN. Regra de ouro: *Para toda dependência funcional X → Y, X deve ser uma superchave.*

### 2. Tipos de JOIN
*   **INNER JOIN:** Retorna apenas as linhas com correspondência nas duas tabelas (intersecção).
*   **LEFT (OUTER) JOIN:** Retorna TODAS as linhas da tabela da esquerda e as correspondências da direita (ou NULL).
*   **RIGHT (OUTER) JOIN:** Retorna TODAS as linhas da tabela da direita e as correspondências da esquerda (ou NULL).
*   **FULL (OUTER) JOIN:** Retorna TODAS as linhas de ambas (LEFT + RIGHT juntas).
*   **CROSS JOIN:** Produto cartesiano. Combina cada linha da esquerda com todas da direita.

### 3. Diferenças Críticas de Sintaxe (PostgreSQL x Oracle)
*   **Data/Hora Atual:**
    *   *PostgreSQL:* `CURRENT_DATE`, `CURRENT_TIMESTAMP`, `NOW()`
    *   *Oracle:* `SYSDATE`, `SYSTIMESTAMP`
*   **Concatenação:**
    *   *PostgreSQL/Oracle:* Usa `||` (ex: `nome || ' ' || sobrenome`)
*   **Limitar linhas (Top N):**
    *   *PostgreSQL:* `LIMIT 10`
    *   *Oracle 12c+:* `FETCH FIRST 10 ROWS ONLY` (Oracle mais antigo usava `ROWNUM <= 10`)

---

## 🔒 Bloco 2: Segurança da Informação e Normas

### 1. Portas Seguras vs Inseguras
*   **HTTP (80) / HTTPS (443)** — Web
*   **Telnet (23) / SSH (22)** — Terminal
*   **FTP (20,21) / SFTP (22) / FTPS (990)** — Transferência
*   **SMTP (25/587) / SMTPS (465)** — Envio de E-mail
*   **IMAP (143) / IMAPS (993)** — Leitura (Sincronização)
*   **POP3 (110) / POP3S (995)** — Leitura (Baixa e apaga)

### 2. Família ISO 27000 (O que cai na FCC)
*   **27001:** Define os **Requisitos** do SGSI. É a única que é *certificável*. Utiliza o ciclo PDCA.
*   **27002:** Código de prática (Boas práticas). Descreve os **Controles**. *Não é certificável*.
*   **27005:** Gestão de **Riscos** de SI. (Identificação, Análise, Avaliação, Tratamento).
*   **27017:** Controles de segurança em **Computação em Nuvem** (Cloud).
*   **27035:** Gestão de **Incidentes** de Segurança. (Abordagem em 5 fases).

### 3. NIST SP 800-61 (Tratamento de Incidentes)
*Fases do ciclo de vida da resposta a incidentes segundo o NIST:*
1.  **Preparação:** Criação de times (CSIRT), ferramentas, políticas.
2.  **Detecção e Análise:** Identificação do incidente (falsos positivos, precursores vs indicadores).
3.  **Contenção, Erradicação e Recuperação:** Conter o dano (isolar), remover a ameaça (apagar malware) e voltar à operação normal.
4.  **Atividade Pós-Incidente:** Lições aprendidas (Reunião), retenção de evidências.

---

## 🏛️ Bloco 3: Arquitetura — SSO, OAuth2 e Keycloak

### 1. SSO (Single Sign-On)
Permite que o usuário faça login uma única vez e tenha acesso a múltiplos sistemas (ex: o usuário loga na intranet do TJ-CE e já está logado no PJe e no SEI). Reduz a fadiga de senhas.

### 2. OAuth 2.0 (RFC 6749)
**Não é protocolo de Autenticação**, é protocolo de **AUTORIZAÇÃO** (Delegação de acesso).
*   **Resource Owner:** O dono dos dados (Você).
*   **Client:** A aplicação que quer acessar os dados.
*   **Authorization Server:** Quem emite o token.
*   **Resource Server:** Onde estão as APIs/Dados.
*   *Fluxo mais seguro e cobrado:* **Authorization Code Grant** (Usa um código intermediário trocado no backend pelo Access Token).

### 3. OpenID Connect (OIDC)
É uma camada de **AUTENTICAÇÃO** (Identidade) construída *por cima* do OAuth 2.0.
*   Usa o **ID Token** (formato JWT - JSON Web Token).
*   Possui endpoint `/userinfo` para pegar os dados do perfil do usuário.

### 4. Keycloak
Produto open-source da RedHat para **Identity and Access Management (IAM)**.
*   Suporta nativamente OIDC, OAuth 2.0 e SAML 2.0.
*   Conceito de **Realm:** Um espaço isolado que gerencia usuários, credenciais, papéis (roles) e clientes. Um realm não vê os dados do outro (Multitenancy).
