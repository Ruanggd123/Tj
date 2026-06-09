# Manual Definitivo de Raciocínio Lógico (RLM) — Foco Total na FCC

A Fundação Carlos Chagas (FCC) aborda o raciocínio lógico muito mais como uma disciplina de "leitura atenta e regras estritas" do que como matemática avançada. O segredo é substituir a intuição por "Fórmulas de Linguagem".

---

### 1. A Regra de Identificação (O Teste da Proposição)
Para uma frase ser uma proposição lógica, ela deve ser uma oração declarativa com verbo que possa ser classificada como **VERDADEIRA** ou **FALSA**.
* **O Bloqueio Imediato (NÃO são proposições):**
  1. Frases Interrogativas (*Qual o seu nome?*)
  2. Frases Exclamativas (*Que dia lindo!*)
  3. Frases Imperativas/Ordens (*Feche a porta.*)
  4. Frases sem verbo (*A bela casa de campo.*)
  5. Sentenças Abertas (aquelas que dependem de uma variável para ter valor: *Ele é um bom juiz.* / *X + 5 = 10.* - Quem é "ele"? Quem é "x"? Como não sabemos, não dá para julgar como V ou F).

### 2. A Regra dos Conectivos (O Teste da Tabela Verdade)
Você não precisa decorar 5 tabelas inteiras, apenas o **"Calcanhar de Aquiles"** de cada conectivo (a regra de ouro que define o seu estado):
* **O "E" (Conjunção `^`):** É o chefe exigente. **Só é VERDADEIRO se TUDO for verdadeiro.** (Basta um Falso para derrubar a frase inteira).
* **O "OU" (Disjunção `v`):** É o chefe tolerante. **Só é FALSO se TUDO for falso.** (Basta um Verdadeiro para salvar a frase).
* **O "OU... OU" (Disjunção Exclusiva `v_`):** É o ciumento. **Só é VERDADEIRO se forem DIFERENTES** (V com F, ou F com V). Se os dois valores forem iguais (V com V / F com F), dá Falso.
* **O "SE... ENTÃO" (Condicional `->`):** É a regra suprema das bancas. **Só existe UMA forma de dar FALSO:** É a famosa regra da **Vera Fischer Falsa (V -> F = F)**. Ou seja, primeira verdadeira e segunda falsa. Qualquer outra combinação (F->V, F->F, V->V) é Verdadeira.
* **O "SE E SOMENTE SE" (Bicondicional `<->`):** É o espelho. **Só é VERDADEIRO se forem IGUAIS** (V com V, F com F).

### 3. A Regra da Negação do "E" e do "OU" (As Leis de De Morgan)
A banca pedirá para você "negar" uma frase composta. **NUNCA** negue um conectivo mantendo ele mesmo.
* **Como negar o E:** Troca o "E" por "OU" e nega as duas partes originais.
* **Como negar o OU:** Troca o "OU" por "E" e nega as duas partes originais.
  * *Frase:* O servidor trabalha muito **E** recebe pouco.
  * *Negação Correta:* O servidor NÃO trabalha muito **OU** NÃO recebe pouco.

### 4. A Regra da Negação do "SE... ENTÃO" (A Regra do MANÉ)
Quando a FCC mandar você **NEGAR** uma condicional (Se P, então Q), esqueça o "Se". A resposta correta **não terá o Se**.
* **A Fórmula (MA - NE):** **MA**ntém a primeira, troca o conectivo por **E**, e **NE**ga a segunda.
  * *Frase:* **Se** chove, **então** levo o guarda-chuva.
  * *Negação Correta:* Chove **E** NÃO levo o guarda-chuva.

### 5. A Regra das Equivalências do "SE... ENTÃO" (O Disfarce Lógico)
Equivalência é quando duas frases dizem a MESMA coisa matematicamente, mas com palavras diferentes. A FCC adora dar uma frase "Se... Então" e pedir outra equivalente. Só existem duas saídas válidas:
* **Saída 1 (A Contrapositiva):** Volta negando tudo (Inverte as duas de lugar e nega ambas, mantendo o "Se... Então").
  * *Original:* **Se** nasci no Ceará, **então** sou brasileiro.
  * *Equivalente:* **Se** NÃO sou brasileiro, **então** NÃO nasci no Ceará.
* **Saída 2 (A Regra do NEYMAR):** Troca o conectivo por OU, aplica **NE**ga a primeira, **Y** (ou), **MAR**ntém a segunda.
  * *Original:* **Se** chove, **então** o chão molha.
  * *Equivalente:* NÃO chove **OU** o chão molha.

### 6. A Regra da Negação de Quantificadores (Todo, Algum, Nenhum)
Pegadinha suprema: A negação de "TODO" **não é** "NENHUM", e vice-versa. Para quebrar uma regra totalitária, basta encontrar *uma única exceção*.
* **Para negar o "TODO":** Use o macete **PEA + NÃO** (Pelo menos um / Existe um / Algum + Ação Negada).
  * *Frase:* **Todo** programador é nerd.
  * *Negação Correta:* **Algum** programador **NÃO** é nerd. (Pelo menos um não é).
* **Para negar o "ALGUM" (Pelo menos um):** Use o **NENHUM** (ou Todo...Não).
  * *Frase:* **Algum** analista errou o código.
  * *Negação Correta:* **Nenhum** analista errou o código.
* **Para negar o "NENHUM":** Use o **ALGUM** (ou Existe um).
  * *Frase:* **Nenhum** juiz atrasou.
  * *Negação Correta:* **Algum** juiz atrasou.

### 7. A Regra dos Diagramas Lógicos (Desenhe as "Bolas")
Quando a questão der frases com "Todos", "Alguns" e "Nenhum" e pedir uma conclusão, NUNCA use a lógica do mundo real. Desenhe os conjuntos (Bolas).
* **TODO A é B:** Desenhe a bola do A totalmente dentro da bola do B. (Atenção: Se alguém está no B, não significa que está no A).
* **ALGUM A é B:** Desenhe duas bolas cruzadas (uma interseção no meio).
* **NENHUM A é B:** Desenhe duas bolas completamente separadas, sem se tocarem.
* **A Regra de Ouro do Desenho:** Se ao ler as premissas for possível fazer *mais de um desenho diferente* sem quebrar as regras dadas, então você **NÃO PODE** afirmar aquilo com certeza (a conclusão na prova será inválida). Conclusão lógica só é válida se ocorrer em 100% dos desenhos possíveis.

### 8. A Regra de Verdades e Mentiras (O Foco na Contradição)
Problemas clássicos de interrogatório (A, B e C estão em uma sala. Um mente, outro fala a verdade, quem quebrou o vaso?).
* **O Método do Conflito:** Procure imediatamente duas pessoas que **se contradizem** (Um acusa, o outro diz "o primeiro está mentindo" ou "fui eu não, foi ele").
* **A Dedução:** Se duas pessoas se contradizem diretamente de forma binária, obrigatoriamente **UMA disse a verdade e a OUTRA mentiu**. O erro não pode estar nos dois (nas regras de lógica de concursos). Sabendo onde está o conflito, sobra o terceiro personagem. A partir da afirmação do terceiro personagem, o problema se desmonta como dominó.

### 9. A Regra da Casa dos Pombos (A "Pior Sorte" Possível)
Questões do tipo: "Há 10 meias pretas e 10 brancas numa gaveta no escuro. Quantas preciso tirar para garantir que terei um par da mesma cor?"
* **A Regra do Azarado:** Para "garantir com certeza matemática", você deve simular que tem o pior azar do universo e tirar todas as opções erradas primeiro.
* **O Cálculo:** Você tira 1 meia preta. Em vez de sorte (tirar outra preta), o azar faz você tirar 1 branca. Agora você tem 1 preta e 1 branca. A terceira meia puxada, não importa a cor, fará par com uma das duas. Portanto, são necessárias **3 retiradas** para garantir o evento.
* **Fórmula Mestra:** Some tudo o que você NÃO quer + tudo o que esgota o grupo contrário + 1. O "+1" é sempre a garantia do evento esperado.

---

### 10. A Regra da Regra de Três (O Método de Causas e Efeitos)
A FCC ama textos imensos em Regra de Três Composta. Esqueça as setinhas confusas para cima e para baixo. Use a separação de Processos e Produtos.
* **O Processo (A Causa):** Tudo o que trabalha, o tempo ou os recursos usados para fazer algo (Pessoas, Máquinas, Dias, Horas/dia).
* **O Produto (O Efeito):** O objetivo final do trabalho (A parede construída, as peças produzidas, a distância percorrida).
* **Como Montar:** Coloque as Causas multiplicadas em uma linha e o Efeito no final. Na linha de baixo, coloque a segunda situação. Cruze multiplicando toda a linha de cima pelo Efeito de baixo, e iguale multiplicando toda a linha de baixo pelo Efeito de cima. Fim. Zero setas.

### 11. A Regra das Frações e Proporções (A Constante "K")
Quando o problema mandar dividir uma herança ou bônus "proporcionalmente" a 2, 3 e 5.
* **A Fórmula do "K":** Nunca tente chutar valores. Adicione a letra K (constante de proporcionalidade) a cada número dado e some tudo igualando ao total.
  * *Problema:* Dividir R$ 500 proporcionalmente a 2, 3 e 5.
  * *Solução:* 2K + 3K + 5K = 500 -> 10K = 500 -> K = 50.
  * *Resultado Final:* O primeiro ganha 2x50 = 100. O segundo 3x50 = 150. O terceiro 5x50 = 250.

### 12. A Regra da Porcentagem Sucessiva (O "100 Imaginário")
A FCC adora dar aumentos seguidos de descontos na mesma taxa para testar sua intuição (Ex: a bolsa subiu 20%, depois caiu 20%).
* **O 100 Imaginário:** Quando a questão trabalhar *apenas* com porcentagens e não der nenhum valor inicial em Reais, **finja sempre que o produto custa R$ 100,00**.
  * Aumentou 20% de 100 = Foi para R$ 120,00.
  * Caiu 20% de 120 = Tira R$ 24 = Foi para R$ 96,00.
  * Final: De 100 para 96 = Caiu 4%. (Atenção: Se você responder que "ficou na mesma" ou "empatou", a banca te elimina na hora).
* **O Fator Multiplicativo:** Se preferir cálculo direto, transforme porcentagem em decimal: (+20% vira 1,20) e (-20% vira 0,80). Multiplique um pelo outro: 1,20 x 0,80 = 0,96 (ou seja, sobraram 96% do valor original).

### 13. A Regra de Análise Combinatória (O Teste da Ordem)
Você tem 10 pessoas e precisa escolher 3. Qual fórmula usar (Arranjo ou Combinação)? Faça a "Pergunta da Ordem".
* **O Teste de Ouro:** "Se eu escolher o João, a Maria e o Pedro, o grupo formado é a mesma coisa que escolher o Pedro, o João e a Maria?"
* **Se a resposta for SIM (Não muda nada):** Trata-se de **Combinação** (Equipes, Comissões, Sorteios). A ordem dos fatores não altera o produto final. Você deve *dividir* o cálculo pelo fatorial das vagas para retirar as repetições (as contagens duplas).
* **Se a resposta for NÃO (A ordem altera tudo):** Trata-se de **Arranjo** (Senhas de banco, Pódio de corrida 1º/2º/3º, Cargos de Presidente/Vice). O cargo de presidente para o João é diferente de vice para o João. Você só multiplica as opções e NÃO divide por nada.

### 14. A Regra da Probabilidade (O Quero sobre o Tenho)
A probabilidade nada mais é do que a matemática misturada com a Lógica do "E" e do "OU".
* **A Fórmula Base:** Probabilidade = O que eu **QUERO** (Casos Favoráveis) dividido por Tudo o que eu **TENHO** (Total de Casos Possíveis da situação).
* **A Regra do "OU" (Soma):** Qual a chance de tirar um Ás **OU** um Rei puxando uma carta do baralho? Você **SOMA** as duas probabilidades isoladas.
* **A Regra do "E" (Multiplica):** Qual a chance de jogar duas moedas independentes e dar Cara na primeira **E** Cara na segunda? Você obrigatoriamente **MULTIPLICA** as probabilidades das frações (1/2 x 1/2 = 1/4).

### 15. A Regra dos Conjuntos (A Interseção é a Rainha)
Questões clássicas de pesquisas de grupos (Ex: 50 pessoas leem o jornal A, 30 leem o jornal B, 10 leem os dois...).
* **O Ponto de Partida Obrigatório:** Para não errar o diagrama, você deve **SEMPRE** começar preenchendo a Interseção (o grupo que faz "Tudo" ao mesmo tempo) de dentro para fora. Nunca comece pelas pontas.
* **A Regra do Desconto (A Palavra "Somente"):** O total do grupo A inclui a interseção. Logo, se 50 leem o jornal A, e 10 leem ambos, você deve fazer o desconto: 50 - 10 = 40. Ou seja, 40 leem **SOMENTE** o jornal A. Se você esquecer de descontar a interseção dos totais, a conta inteira dará errado.
* **A Fórmula Rápida da União:** Se não quiser desenhar bolas, use a equação direta: O Total de Pessoas (União) = Tudo de A + Tudo de B - A Interseção. O que você contou duas vezes (a interseção), você retira uma vez no final.

### 16. A Regra das Sequências Lógicas (A Divisão pelo Ciclo)
A FCC adora colocar um padrão de figuras ou uma palavra repetitiva (ex: TRIBUNALTRIBUNALTRIBUNAL...) e perguntar: "Qual será a 543ª letra?".
* **Encontre o Ciclo Base:** Conte quantos elementos existem antes de começar a repetir tudo de novo. Na palavra TRIBUNAL, o ciclo tem **8 letras**.
* **A Matemática do Resto:** Nunca tente desenhar 500 vezes. Pegue a posição que a banca quer (543) e divida pelo tamanho do ciclo (8).
  * O número inteiro da divisão não importa (significa apenas quantas vezes a palavra foi escrita inteira).
  * **Olhe SOMENTE para o RESTO da divisão.**
* **O Veredito:** Se o resto da divisão foi 3, a resposta é a 3ª letra da palavra/ciclo (Letra I). Se o resto for 5, é a 5ª letra. Se o resto der **ZERO** (divisão exata), a resposta é sempre a **ÚLTIMA** letra do ciclo (Letra L).
