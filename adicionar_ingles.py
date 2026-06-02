import os

def append_english_questions():
    filepath = r'c:\Users\Ruan Gomes\Downloads\TJC\03_Baterias_Questoes_FCC\dia_02_06_questoes.md'
    
    content = """
## 📝 TEMA 4: Inglês Técnico

### Texto para as questões 46 a 50
**Zero Trust Architecture in Modern IT**

Historically, IT departments relied on a perimeter security model. This traditional approach assumes that everything on the inside of an organization's network can be trusted. However, this model is fundamentally flawed because once an attacker breaches the perimeter, they have free rein to move laterally throughout the internal network. 

Zero Trust is a security framework requiring all users, whether in or outside the organization's network, to be authenticated, authorized, and continuously validated for security configuration and posture before being granted or keeping access to applications and data. **It** operates on the principle of "never trust, always verify." 

By implementing Zero Trust, organizations can prevent unauthorized access, contain breaches, and reduce the risk of an attacker's lateral movement.

---

### Questão 46 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - Tecnologia da Informação)
According to the text, what is the main flaw of the traditional perimeter security model?
A) It requires users to be authenticated constantly, which slows down productivity.
B) It allows attackers to move freely within the network once the outer defenses are compromised.
C) It prevents lateral movement, making it hard for employees to share files.
D) It relies entirely on cloud computing infrastructures that are inherently insecure.
E) It assumes that users outside the organization's network can be trusted without validation.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

- A) Incorreta. Isso é uma característica (mal interpretada) do Zero Trust, não do modelo de perímetro.
- B) Correta. O texto afirma: "...this model is fundamentally flawed because once an attacker breaches the perimeter, they have free rein to move laterally throughout the internal network." (uma vez que o atacante rompe o perímetro, ele tem passe livre para se mover lateralmente na rede interna).
- C) Incorreta. O modelo falha justamente por NÃO prevenir o movimento lateral.
- D) Incorreta. O texto não menciona cloud computing como a causa da falha.
- E) Incorreta. O modelo tradicional confia no que está DENTRO ("inside") da rede, não fora ("outside").
</details>

### Questão 47 (FCC - 2021 - DPE-RR - Analista de Sistemas)
In the second paragraph, the bolded pronoun "**It**" in the sentence "*It operates on the principle of 'never trust, always verify.'*" refers to:
A) An attacker.
B) The organization's network.
C) Security configuration.
D) Zero Trust.
E) The traditional approach.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- A FCC frequentemente cobra referência pronominal. Para encontrar a resposta, lemos a frase anterior: "Zero Trust is a security framework requiring all users...". O pronome "It" atua como sujeito da frase seguinte, substituindo o sujeito principal do contexto recém-apresentado, que é o modelo "Zero Trust".
- A, B, C e E estão incorretas pois não se alinham semanticamente e gramaticalmente ao conceito que "opera sob o princípio de nunca confiar, sempre verificar".
</details>

### Questão 48 (FCC - 2019 - TRF 3ª Região - Analista Judiciário - Informática)
Based on the principles described in the text, which of the following is an action aligned with the Zero Trust framework?
A) Granting lifetime network access to an employee after their first login.
B) Removing password requirements for users physically present in the main office.
C) Continuously validating a user's security posture even after they have already logged in.
D) Focusing all security investments exclusively on the outer firewall defenses.
E) Trusting any device that is connected to the company's internal Wi-Fi.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

- A) Incorreta. O acesso vitalício após um login quebra a regra de "validação contínua".
- B) Incorreta. A presença física dentro do escritório (perímetro interno) não concede confiança no modelo Zero Trust.
- C) Correta. O texto diz: "...continuously validated for security configuration and posture before being granted or keeping access...".
- D) Incorreta. Focar só na borda (firewall) é a definição do modelo tradicional.
- E) Incorreta. Conectar-se no Wi-Fi interno não garante confiança no Zero Trust.
</details>

### Questão 49 (FCC - 2023 - TRT 18ª Região - Técnico Judiciário)
The word "**breaches**" in the sentence "...contain breaches, and reduce the risk..." (last paragraph) is closest in meaning to:
A) Agreements.
B) Upgrades.
C) Connections.
D) Violations or intrusions.
E) Investments.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- No vocabulário técnico de TI e segurança, a palavra *breach* (ou *data breach*) significa brecha, violação, intrusão ou vazamento de dados. 
- A) Agreements = Acordos.
- B) Upgrades = Atualizações.
- C) Connections = Conexões.
- D) Violations or intrusions = Violações ou intrusões (Correta).
- E) Investments = Investimentos.
</details>

### Questão 50 (FCC - 2017 - TRE-SP - Analista Judiciário - Programação de Sistemas)
Which of the following sentences correctly expresses the meaning of the phrase "*have free rein*" found in the first paragraph?
A) Be completely restricted and monitored.
B) Have to pay a fee to access data.
C) Experience frequent network disconnections.
D) Have the freedom to act or move without limitations.
E) Be caught immediately by the security systems.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

- A expressão idiomática "free rein" tem origem no controle das rédeas (reins) de um cavalo. Dar "rédea solta" (free rein) significa dar liberdade total para agir ou se mover sem restrições. No contexto do texto, se o invasor passa o firewall (perímetro), ele tem liberdade total ("free rein") para acessar as máquinas internas. 
- Logo, a alternativa D ("ter liberdade para agir ou se mover sem limitações") é a única que reflete o sentido correto.
</details>

"""
    
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(content)

    print("Ingles adicionado!")

append_english_questions()
