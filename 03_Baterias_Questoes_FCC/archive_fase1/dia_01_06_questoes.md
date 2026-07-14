# Bateria de Questões FCC — Segunda-feira 01/06

## 📝 TEMA 1: Programação Python (Django, Flask, manipulação de arquivos, orientação a objetos e sintaxe)

### Questão 1 (FCC - 2022 - TRT 22ª Região - Analista Judiciário - Tecnologia da Informação)
Considere o seguinte trecho de código escrito em Python 3:
```python
x = 10
def funcao_externa():
    x = 20
    def funcao_interna():
        nonlocal x
        x = 30
        global y
        y = 40
    funcao_interna()
    print(x)

funcao_externa()
print(x)
print(y)
```
Ao executar este código, as saídas impressas no console serão, respectivamente:
A) 20, 10 e 40.
B) 30, 10 e 40.
C) 30, 30 e 40.
D) 20, 30 e NameError (pois y não foi definido no escopo global antes).
E) 30, 10 e NameError (pois y só é acessível dentro de funcao_interna).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão cobra a compreensão das regras de escopo de variáveis em Python 3, especificamente o uso das palavras-chave `nonlocal` e `global`.

- **A está incorreta:** A saída da primeira impressão (`print(x)` dentro de `funcao_externa`) é `30`, e não `20`, porque a instrução `nonlocal x` faz com que o nome `x` dentro de `funcao_interna` se refira à variável `x` no escopo local imediatamente superior (o de `funcao_externa`).
- **B está correta:** 
  1. A variável `x` global é inicializada com `10`.
  2. `funcao_externa()` é chamada e cria um `x` local com valor `20`.
  3. Dentro de `funcao_externa`, define-se `funcao_interna`, que utiliza `nonlocal x`. Isso vincula o `x` de `funcao_interna` ao `x` de `funcao_externa` (que era `20`). A atribuição `x = 30` altera esse `x` externo para `30`.
  4. A instrução `global y` declara que `y` deve ser inserido no escopo global do módulo. A atribuição `y = 40` cria essa variável no escopo global.
  5. Ao terminar a execução de `funcao_interna()`, a execução volta para `funcao_externa`, que executa `print(x)`. Como `x` local de `funcao_externa` foi modificado para `30` pelo `nonlocal`, imprime `30`.
  6. Em seguida, após `funcao_externa()` retornar, executa-se `print(x)` no escopo global. O `x` global nunca foi modificado, mantendo-se `10`.
  7. Finalmente, `print(y)` imprime `40`, pois a variável `y` foi criada no escopo global através da diretiva `global y` executada em tempo de execução.
- **C está incorreta:** O `print(x)` final imprime o `x` global, que permaneceu `10`. Ele não foi modificado, pois `nonlocal` só altera variáveis em escopos intermediários (locais envolventes), e não o escopo global.
- **D está incorreta:** Não ocorre `NameError`. A diretiva `global y` instrui o interpretador de que `y` pertence ao escopo global. Quando a atribuição `y = 40` é executada dentro da função, a variável global `y` é criada em tempo de execução e torna-se acessível fora da função após ela ser invocada.
- **E está incorreta:** Não ocorre `NameError` para `y` e a primeira saída é `30`.
</details>

---

### Questão 2 (FCC - 2021 - DPE RR - Analista de Sistemas)
Analise o trecho de código em Python 3 a seguir:
```python
dados = [1, 2, 3, 4, 5]
gen = (x * 2 for x in dados if x % 2 != 0)
lista = [x * 2 for x in dados if x % 2 != 0]

print(type(gen))
print(next(gen))
print(next(gen))
print(lista)
```
Assinale a opção que descreve corretamente o retorno e o tipo dos elementos obtidos nas linhas impressas:
A) `<class 'generator'>`, `2`, `6` e `[2, 6, 10]`.
B) `<class 'tuple'>`, `2`, `4` e `[2, 6, 10]`.
C) `<class 'generator'>`, `2`, `4` e `[2, 4, 6, 8, 10]`.
D) `<class 'list'>`, `2`, `6` e `(2, 6, 10)`.
E) `<class 'generator'>`, `1`, `3` e `[2, 6, 10]`.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A questão avalia a diferença entre List Comprehension e Generator Expression em Python.

- **A está correta:** 
  1. A sintaxe de parênteses `(x * 2 for x in dados if x % 2 != 0)` cria um *generator object*, cuja classe é `<class 'generator'>`.
  2. A condição `if x % 2 != 0` filtra apenas os números ímpares da lista `dados` (`1`, `3` e `5`).
  3. A expressão calcula `x * 2`. Portanto, a sequência gerada sob demanda será `1*2 = 2`, `3*2 = 6`, e `5*2 = 10`.
  4. A primeira chamada a `next(gen)` retorna o primeiro elemento calculado, que é `2`.
  5. A segunda chamada a `next(gen)` avança o gerador para o segundo elemento, retornando `6`.
  6. A variável `lista` é gerada por uma *List Comprehension* (uso de colchetes `[...]`), que computa imediatamente todos os valores baseados nos ímpares: `[2, 6, 10]`.
- **B está incorreta:** A expressão com parênteses `(...)` não cria uma tupla se contiver um loop `for`. Para criar uma tupla via compressão, deve-se usar explicitamente `tuple(...)`.
- **C está incorreta:** Os valores intermediários pares de `dados` (`2` e `4`) não entram na saída devido ao filtro `if x % 2 != 0` (apenas ímpares passam pelo filtro). Logo, `4` não é gerado.
- **D está incorreta:** O gerador é do tipo `generator`, e a lista é impressa como `[2, 6, 10]`, e não como tupla.
- **E está incorreta:** Os valores do gerador e da lista sofrem a multiplicação por 2 (`x * 2`). Logo, as saídas são `2` e `6`, e não `1` e `3`.
</details>

---

### Questão 3 (FCC - 2018 - TRT 2ª Região - Analista Judiciário - Tecnologia da Informação)
Em Python 3, a herança múltipla é resolvida utilizando o algoritmo MRO (Method Resolution Order). Considere o código abaixo:
```python
class A:
    def falar(self):
        return "A"

class B(A):
    def falar(self):
        return "B" + super().falar()

class C(A):
    def falar(self):
        return "C" + super().falar()

class D(B, C):
    def falar(self):
        return "D" + super().falar()

print(D().falar())
```
Qual será a saída gerada ao executar o código acima?
A) DBCA
B) DBA
C) DBCA
D) DB A
E) D B C A (com espaços)

Wait, deixa eu verificar a lógica de super() com MRO nessa hierarquia em diamante clássica.
O MRO de D é D -> B -> C -> A -> object.
Quando D chama `super().falar()`, ele chama o próximo na cadeia MRO, que é `B.falar()`.
`B.falar()` retorna "B" + `super().falar()`. Como a chamada `super()` em B ocorre no contexto de um objeto do tipo D, ela busca o próximo elemento na cadeia MRO de D após B. O próximo após B é C.
Então, `super().falar()` em B chama `C.falar()`.
`C.falar()` retorna "C" + `super().falar()`. O próximo após C no MRO de D é A.
Então, `super().falar()` em C chama `A.falar()`.
`A.falar()` retorna "A".
Assim, a cadeia retorna "D" + "B" + "C" + "A" = "DBCA".
Vamos colocar as alternativas corretas e explicar muito bem.

A) DBCA
B) DBA
C) DBC
D) DACB
E) NameError por herança circular.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A questão cobra a compreensão profunda da Ordem de Resolução de Métodos (Method Resolution Order - MRO) e do comportamento cooperativo da função `super()` em Python.

- **A está correta:** 
  1. A estrutura apresentada é um diamante clássico, onde a classe `D` herda de `B` e `C`, que por suas vezes herdam de `A`.
  2. Em Python, o MRO é calculado usando o algoritmo C3 Linearization. Para a classe `D`, a ordem de busca de métodos é resolvida como: `D -> B -> C -> A -> object`. Podemos verificar isso chamando `D.__mro__`.
  3. Quando instanciamos `D()` e invocamos `.falar()`, o método `D.falar()` é executado. Ele inicia com `"D" + super().falar()`.
  4. O `super()` não se refere simplesmente ao "pai direto no código-fonte", mas sim ao *próximo elemento na cadeia MRO do objeto atual* (que é do tipo `D`). O próximo após `D` é `B`.
  5. `B.falar()` executa e faz `"B" + super().falar()`. No MRO de `D`, o elemento que vem logo após `B` é `C`. Portanto, o `super()` dentro de `B` chama `C.falar()`, e NÃO `A.falar()`.
  6. `C.falar()` executa e faz `"C" + super().falar()`. O próximo elemento na cadeia MRO após `C` é `A`. Portanto, chama `A.falar()`.
  7. `A.falar()` retorna `"A"`.
  8. Desempilhando as execuções, temos: `"C" + "A"` = `"CA"`; depois `"B" + "CA"` = `"BCA"`; e por fim `"D" + "BCA"` = `"DBCA"`.
- **B está incorreta:** Assume-se incorretamente que `B` chamará diretamente o método de seu pai direto `A`. Em Python, o `super()` apoia a herança múltipla de forma cooperativa avançando no MRO global da instância, que coloca `C` antes de `A`.
- **C está incorreta:** O método do topo da hierarquia (`A.falar()`) é executado e retorna `"A"`. Ele não é ignorado.
- **D está incorreta:** A ordem das classes na definição `class D(B, C)` define que a busca prioriza `B` antes de `C`. Se a definição fosse `class D(C, B)`, a saída seria `DCBA`.
- **E está incorreta:** Python aceita perfeitamente herança múltipla e resolve colisões de forma nativa e determinística sem gerar erros em diamante.
</details>

---

### Questão 4 (FCC - 2017 - TST - Analista Judiciário - Tecnologia da Informação)
Em Python 3, classes podem implementar métodos especiais (dunder methods) para responder a operadores ou funções internas do sistema. Considere a implementação abaixo:
```python
class ColecaoDeItens:
    def __init__(self, itens):
        self._itens = list(itens)
        
    def __len__(self):
        return len(self._itens)
        
    def __getitem__(self, index):
        return self._itens[index]

colecao = ColecaoDeItens(['A', 'B', 'C'])
```
A execução de instruções externas sobre o objeto `colecao` irá se comportar da seguinte forma:
A) A função `len(colecao)` causará um AttributeError, pois `__len__` é de uso exclusivo interno da classe.
B) A expressão `colecao[1]` retornará `'B'`, pois `__getitem__` mapeia o operador de indexação.
C) O laço `for item in colecao:` gerará um TypeError, uma vez que a classe não implementa `__iter__`.
D) A expressão `colecao[0:2]` gerará um TypeError, pois `__getitem__` só aceita inteiros como índice, não fatiamentos (slices).
E) A classe não é considerada um iterável e qualquer tentativa de usá-la em funções como `list(colecao)` falhará em tempo de compilação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Esta questão avalia o conhecimento sobre o protocolo de sequência em Python e os dunder methods (`__len__` e `__getitem__`).

- **A está incorreta:** O método `__len__` é o método especial que a função embutida `len()` do Python chama implicitamente. Assim, `len(colecao)` funcionará perfeitamente, retornando `3`.
- **B está correta:** O método `__getitem__` é responsável por interceptar o operador de indexação `[]`. Quando o código executa `colecao[1]`, o Python traduz internamente para `colecao.__getitem__(1)`, retornando o segundo item da lista interna (`'B'`).
- **C está incorreta:** Em Python, para que um objeto seja iterável, o interpretador busca primeiro pelo método `__iter__`. Se ele não estiver presente, o Python busca pelo método `__getitem__` como mecanismo de fallback, tentando acessar itens do índice `0` em diante até capturar uma exceção do tipo `IndexError`. Portanto, o laço `for` funciona normalmente no objeto `colecao`.
- **D está incorreta:** O operador de fatiamento (`colecao[0:2]`) passa um objeto do tipo `slice` para o método `__getitem__`. Como o método delega a operação para `self._itens[index]`, e a lista interna do Python suporta fatiamentos de forma nativa, a chamada `colecao[0:2]` retornará com sucesso a sublista `['A', 'B']`.
- **E está incorreta:** Python é uma linguagem interpretada e dinâmica (não há "tempo de compilação" com checagem estática que previna isso) e, devido ao fallback de `__getitem__` explicado acima, a chamada `list(colecao)` funcionará retornando uma nova lista com os elementos.
</details>

---

### Questão 5 (FCC - 2019 - TRF 3ª Região - Técnico Judiciário - Informática)
Considere a seguinte classe implementada em Python 3:
```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    def obter_saldo(self):
        return self.__saldo

conta = ContaBancaria("Carlos", 1500)
```
Sobre a manipulação dos atributos do objeto `conta`, assinale a alternativa correta:
A) O atributo `__saldo` pode ser livremente acessado e modificado fora do escopo da classe usando a instrução `conta.__saldo`.
B) O encapsulamento com duplo sublinhado (`__saldo`) impede fisicamente qualquer forma de alteração externa ao saldo depois de instanciado.
C) A instrução `conta._ContaBancaria__saldo = 2000` executada fora da classe modificará o saldo interno do objeto para `2000` devido ao Name Mangling.
D) Ao tentar rodar `conta.__saldo = 2000`, o interpretador lançará um AttributeError informando que o atributo é somente leitura.
E) Atributos criados com duplo sublinhado são armazenados em um dicionário criptografado do Python para fins de segurança cibernética.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Esta questão foca na mecânica de Name Mangling (desfiguração de nomes) que o Python utiliza para simular atributos privados.

- **A está incorreta:** A tentativa de ler ou escrever diretamente em `conta.__saldo` fora da classe irá falhar ou criar uma nova variável paralela dinâmica de nome `__saldo` no objeto, mas não alterará nem lerá o saldo original interno do construtor, pois o nome foi desfigurado internamente.
- **B está incorreta:** O encapsulamento em Python é baseado em convenções e modificações de nomes em tempo de tradução do código. Não há um bloqueio físico de hardware ou memória que impeça o acesso ou modificação se o desenvolvedor usar o nome desfigurado correto.
- **C está correta:** Para evitar colisões de nomes em subclasses, qualquer identificador dentro de uma classe que comece com pelo menos dois sublinhados e termine com no máximo um sublinhado (como `__saldo`) é reescrito silenciosamente pelo interpretador no formato `_NomeDaClasse__nome_do_atributo` (Name Mangling). Sendo assim, o atributo real no objeto passa a se chamar `_ContaBancaria__saldo`. Alterar esse atributo diretamente afeta o valor retornado pelo método `obter_saldo()`.
- **D está incorreta:** Rodar `conta.__saldo = 2000` não gera exceção. O Python apenas criará um novo atributo público no objeto chamado `__saldo` de forma dinâmica. A variável desfigurada original `_ContaBancaria__saldo` permanecerá intocada com o valor `1500`.
- **E está incorreta:** O armazenamento utiliza o dicionário padrão do objeto (`__dict__`) como texto puro, sem qualquer mecanismo de criptografia.
</details>

---

### Questão 6 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - Tecnologia da Informação)
Ao manipular arquivos texto em Python 3, a escolha do modo de abertura determina o comportamento do ponteiro de escrita e leitura. Considere que o arquivo `relatorio.txt` existe previamente e possui o conteúdo "Linha 1\nLinha 2". Analise os dois blocos de execução independentes a seguir:

Bloco 1:
```python
with open("relatorio.txt", "r+") as f:
    f.write("Nova")
```

Bloco 2:
```python
with open("relatorio.txt", "w+") as f:
    f.write("Nova")
```

Após a execução isolada de cada bloco, o conteúdo final do arquivo `relatorio.txt` em cada caso será, respectivamente:
A) "Nova\nLinha 2" e "Nova".
B) "Nova" e "Nova".
C) "NovaLinha 1\nLinha 2" e "Nova".
D) "Novaa 1\nLinha 2" e "Nova".
E) "Nova" e "Linha 1\nLinha 2Nova".

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão cobra a diferença entre os modos de abertura de arquivos `r+` (leitura e escrita, sem truncamento) e `w+` (leitura e escrita, com truncamento imediato).

- **A está incorreta:** A palavra "Nova" possui 4 caracteres. Ao escrever no início do arquivo em modo `r+`, os primeiros 4 caracteres do arquivo original ("Linh") são sobrescritos, resultando em "Novaa 1\nLinha 2". A letra "a" e o espaço " " de "Linha 1" são preservados.
- **B está incorreta:** No Bloco 1, o conteúdo original do arquivo não é totalmente apagado, pois o modo `r+` não trunca o arquivo na abertura. Ele apenas sobrescreve a partir do início (posição zero do cursor).
- **C está incorreta:** O modo `r+` não funciona como o modo append (`a`). Ele não insere texto empurrando o conteúdo anterior, e sim sobrescreve caractere por caractere a partir de onde o cursor do arquivo está posicionado.
- **D está correta:** 
  1. No Bloco 1 (`r+`): O arquivo é aberto preservando o conteúdo original ("Linha 1\nLinha 2"). O cursor começa na posição `0`. Ao escrever `"Nova"`, os caracteres nas posições `0, 1, 2, 3` (que eram `'L', 'i', 'n', 'h'`) são substituídos por `'N', 'o', 'v', 'a'`. O restante do arquivo fica inalterado. Assim, `"Linha 1\nLinha 2"` vira `"Novaa 1\nLinha 2"`.
  2. No Bloco 2 (`w+`): O arquivo é aberto em modo de escrita. A especificação do modo `w` (ou `w+`) trunca imediatamente o arquivo, ou seja, apaga todo o seu conteúdo existente, reduzindo seu tamanho a zero. Em seguida, grava-se `"Nova"`. Logo, o conteúdo final é apenas `"Nova"`.
- **E está incorreta:** Inverte a ordem lógica dos modos de abertura.
</details>

---

### Questão 7 (FCC - 2016 - TRT 20ª Região - Analista Judiciário - Tecnologia da Informação)
No desenvolvimento de aplicações com Python 3, a instrução `with` é amplamente utilizada para garantir a liberação segura de recursos. Do ponto de vista técnico, a fim de que um objeto de uma classe personalizada possa ser utilizado diretamente com a instrução `with`, a classe correspondente é obrigada a implementar os métodos:
A) `__init__` e `__del__`
B) `__open__` e `__close__`
C) `__start__` e `__stop__`
D) `__enter__` e `__exit__`
E) `__connect__` and `__disconnect__`

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão cobra a especificação do protocolo do gerenciador de contexto (Context Manager) do Python.

- **A está incorreta:** `__init__` é o construtor do objeto e `__del__` é o destrutor (chamado pelo garbage collector quando não há mais referências ao objeto, o que não é determinístico no tempo). O `with` garante a liberação de recursos em tempo de execução imediato ao sair do bloco, independentemente de quando o garbage collector atuar.
- **B está incorreta:** Os métodos `__open__` e `__close__` não fazem parte de nenhuma especificação interna da linguagem Python para este protocolo.
- **C está incorreta:** Nomes incorretos.
- **D está correta:** Para aderir ao protocolo de Context Manager (utilizável via `with`), o objeto precisa implementar:
  1. `__enter__(self)`: executado antes de entrar no escopo do bloco `with`. O valor retornado por este método é atribuído à variável que segue a cláusula `as` (se presente).
  2. `__exit__(self, exc_type, exc_val, exc_tb)`: executado obrigatoriamente após a saída do bloco do `with`, mesmo se uma exceção tiver ocorrido dentro dele. Esse método recebe parâmetros detalhando possíveis exceções ocorridas para que possam ser tratadas ou suprimidas.
- **E está incorreta:** Nomes falsos e inexistentes no protocolo padrão do Python.
</details>

---

### Questão 8 (FCC - 2017 - TRE-PR - Analista Judiciário - Análise de Sistemas)
O framework Django adota uma arquitetura inspirada no padrão MVC (Model-View-Controller). No entanto, o próprio Django se descreve como um framework MVT (Model-View-Template). A correspondência de responsabilidades no Django funciona da seguinte forma:
A) O Controller do MVC tradicional é substituído no Django pelo Template, que renderiza os dados em HTML.
B) A View no Django desempenha o papel que o Controller possui no MVC tradicional, processando as requisições HTTP e decidindo quais dados ler e qual template carregar.
C) O Model do Django é responsável apenas por guardar os arquivos de configuração do banco de dados (ex: `settings.py`), enquanto a lógica de persistência de dados fica inteiramente nas views.
D) O próprio framework Django atua unicamente como Model, dependendo de outras bibliotecas de terceiros para estruturar as Views e Controllers.
E) A View no Django atua renderizando o layout da página web (HTML/CSS), enquanto o Template atua processando as chamadas ao banco de dados ORM.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão foca no entendimento da arquitetura interna do framework web Django.

- **A está incorreta:** O Template no Django equivale à View do MVC clássico (exibição gráfica ao usuário final). O Controller tradicional (que recebe os dados, trata a requisição e interage com o modelo) é implementado internamente pelo core do Django (por meio do despachante de URLs e middleware) e pelas Views desenvolvidas pelo programador.
- **B está correta:** No Django, a terminologia é ligeiramente deslocada:
  - **Model:** A camada de acesso aos dados, representada pelas classes ORM em Python. (Mesmo papel do Model no MVC).
  - **View:** A função ou classe que recebe a requisição HTTP, interage com o Model para buscar as informações necessárias, executa a lógica de negócios e chama o template adequado. Ou seja, a View do Django executa a lógica de controle correspondente ao Controller do MVC tradicional.
  - **Template:** A camada de apresentação (geralmente arquivos HTML com a sintaxe do template engine do Django). Corresponde à View do MVC clássico.
- **C está incorreta:** O `settings.py` é um arquivo global de configurações do projeto. O Model no Django é uma classe Python herdada de `django.db.models.Model` que define a tabela do banco de dados e expõe a API do ORM para consultas e persistência.
- **D está incorreta:** Django é um framework full-stack e traz nativamente todas as três camadas do MVT.
- **E está incorreta:** Inverte completamente as atribuições de View e Template.
</details>

---

### Questão 9 (FCC - 2018 - TRT 2ª Região - Analista Judiciário - Tecnologia da Informação)
No desenvolvimento de consultas com o ORM do Django, a eficiência de acesso ao banco de dados é um fator crítico. Suponha que existam as tabelas `Livro` e `Autor`, em que cada `Livro` tem uma chave estrangeira (`ForeignKey`) apontando para um `Autor`. Ao buscar uma lista de livros e exibir o nome de seus respectivos autores, o desenvolvedor deseja mitigar o problema de performance conhecido como "N+1 queries". O comando ORM ideal para este cenário é:
A) `Livro.objects.all().prefetch_related('autor')`
B) `Livro.objects.all().select_related('autor')`
C) `Livro.objects.filter(autor__isnull=False)`
D) `Livro.objects.all().join('autor')`
E) `Livro.objects.raw("SELECT * FROM Livro JOIN Autor ON ...")` que é a única forma de realizar junções no Django.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão cobra técnicas de otimização de consultas no ORM do Django, focando na diferença entre `select_related` e `prefetch_related`.

- **A está incorreta:** Embora `prefetch_related` resolva o problema de N+1 consultas realizando uma busca adicional com uma cláusula `IN` no SQL (ideal para relacionamentos muitos-para-muitos ou chaves estrangeiras reversas), o método `select_related` é mais adequado e eficiente para relacionamentos de chave estrangeira simples (`ForeignKey` ou `OneToOneField`), pois executa um único comando SQL contendo uma cláusula `INNER JOIN` diretamente no banco de dados.
- **B está correta:** O método `select_related` cria um ganho de performance gerando um único comando SQL mais robusto com um `JOIN` no banco de dados, recuperando os campos do objeto relacionado na mesma consulta original. Quando você itera sobre os livros chamando `livro.autor.nome`, o Django não precisará fazer uma nova consulta ao banco para cada livro individual, pois os dados do autor já foram carregados previamente na memória.
- **C está incorreta:** O `filter(autor__isnull=False)` apenas restringe o resultado para livros que possuam autores vinculados. Ele não altera o comportamento do carregamento das relações, que continuará sendo do tipo lazy (preguiçoso), disparando N consultas adicionais na iteração da lista.
- **D está incorreta:** Não existe um método `.join()` exposto diretamente na API de QuerySet do Django.
- **E está incorreta:** O Django ORM permite realizar junções complexas de forma nativa e limpa usando sua própria linguagem de consulta sem precisar recorrer a SQL cru (`raw`), preservando a portabilidade do banco de dados.
</details>

---

### Questão 10 (FCC - 2022 - TRT 22ª Região - Analista Judiciário - Tecnologia da Informação)
As migrações (`migrations`) no Django são um recurso essencial para gerenciar a evolução do esquema do banco de dados ao longo do tempo. Sobre o ciclo de migrações e comandos do Django CLI, assinale a alternativa correta:
A) O comando `python manage.py makemigrations` é responsável por ler os arquivos de migração existentes e aplicá-los de fato ao banco de dados físico.
B) As migrações devem ser executadas diretamente via comandos SQL no console do banco de dados de produção para que o Django possa ler as alterações dinamicamente de forma reversa.
C) O comando `python manage.py migrate` inspeciona os modelos do código-fonte e gera novos arquivos de script python de migração dentro do diretório `migrations/` de cada app.
D) O histórico de quais migrações já foram executadas com sucesso no banco de dados é monitorado pelo Django através de uma tabela interna chamada `django_migrations` criada no próprio banco de dados de destino.
E) Uma migração que já tenha sido aplicada ao banco de dados em produção nunca pode ser desfeita, necessitando a exclusão manual de tabelas pelo administrador.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão cobra o funcionamento interno e CLI do sistema de migrations do Django.

- **A está incorreta:** O comando `makemigrations` apenas gera os arquivos de migração em Python baseando-se nas mudanças detectadas nas classes do seu código em `models.py`. Ele não executa alterações no banco de dados físico.
- **B está incorreta:** O fluxo correto é atualizar as classes nos arquivos `models.py`, gerar as migrations e aplicá-las com a CLI do Django. Alterações diretas no banco de dados de produção causam dessincronização com o estado dos modelos do Django.
- **C está incorreta:** A descrição fornecida refere-se ao comando `makemigrations`. O comando `migrate` lê os scripts de migração já criados e os traduz para comandos SQL específicos do banco de dados conectado, aplicando-os na base de dados.
- **D está correta:** O Django gerencia o controle de versão do banco de dados por meio da tabela `django_migrations` gravada no próprio banco. Sempre que o comando `migrate` é executado, o Django checa essa tabela para descobrir quais arquivos de migração já foram consolidados, aplicando apenas as migrações que ainda não constam na tabela.
- **E está incorreta:** Migrações podem ser desfeitas (rolled back) utilizando o comando `python manage.py migrate [nome_do_app] [numero_da_migracao_anterior]`, desde que os arquivos correspondentes possuam a lógica reversa no método `reverse_code` (o Django gera isso automaticamente na maioria dos casos).
</details>

---

### Questão 11 (FCC - 2016 - TRT 23ª Região - Analista Judiciário - Tecnologia da Informação)
Em uma aplicação desenvolvida com o microframework Flask (Python), as rotas definem como os endpoints respondem às requisições do cliente. Considere o código a seguir:
```python
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/calcular/<int:valor>', methods=['POST'])
def calcular(valor):
    dados = request.get_json()
    multiplicador = dados.get('mult', 1)
    resultado = valor * multiplicador
    return jsonify(res=resultado)
```
Se uma requisição HTTP do tipo POST for feita para a URL `/calcular/5` contendo o corpo JSON `{"mult": 3}`, a resposta retornada pela aplicação Flask conterá:
A) O JSON `{"res": 15}` com código de status HTTP 200.
B) O JSON `{"res": 5}` com código de status HTTP 200.
C) Um erro HTTP 405 (Method Not Allowed), pois a variável na rota impede requisições POST.
D) Um erro HTTP 400 (Bad Request), pois o parâmetro da rota `<int:valor>` só aceita valores decimais fracionados.
E) Uma string `"res=15"`, já que a função `jsonify` converte a saída em texto plano (URL-encoded).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A questão visa avaliar a manipulação de parâmetros de rotas, requisições com dados JSON e respostas JSON no Flask.

- **A está correta:** 
  1. A rota `/calcular/<int:valor>` possui um conversor de tipo `<int:valor>`, o que significa que o Flask capturará a parte final da URL como um número inteiro e a passará como argumento da função `calcular(valor)`. Para a chamada `/calcular/5`, a variável `valor` recebe o valor inteiro `5`.
  2. O argumento `methods=['POST']` permite requisições POST para este endpoint.
  3. `request.get_json()` analisa o corpo da requisição e o carrega como um dicionário Python. Para o JSON `{"mult": 3}`, o dicionário `dados` terá a chave `'mult'` associada ao valor `3`.
  4. O cálculo é `resultado = 5 * 3 = 15`.
  5. `jsonify(res=resultado)` gera um objeto de resposta HTTP contendo o corpo `{"res": 15}` serializado em JSON com o cabeçalho `Content-Type: application/json` e retorna o código padrão de sucesso HTTP 200 OK.
- **B está incorreta:** O multiplicador `3` é obtido com sucesso do corpo do JSON e usado na multiplicação. Logo, o resultado é 15, e não 5 (que ocorreria se o valor padrão `1` fosse usado).
- **C está incorreta:** A rota suporta requisições POST conforme definido explicitamente no parâmetro `methods`.
- **D está incorreta:** O conversor `int` aceita inteiros. Para floats, o conversor correto seria `float`. Não ocorre erro 400.
- **E está incorreta:** A função `jsonify` cria uma instância de objeto Response com o tipo MIME `application/json`, não gerando texto plano formatado como URL-encoded.
</details>

---

### Questão 12 (FCC - 2019 - TRF 4ª Região - Analista Judiciário - Sistemas da Informação)
No desenvolvimento de aplicações de médio a grande porte com Flask, a modularização é obtida através do conceito de Blueprints. Um Blueprint no Flask atua principalmente:
A) Substituindo o uso do servidor web de desenvolvimento (WSGI) do Flask por um servidor de produção embarcado.
B) Como uma coleção de rotas, views, templates e arquivos estáticos que podem ser registrados de forma modular em um ou mais locais da aplicação principal.
C) Como uma ferramenta de ORM integrada para fazer interface direta com bancos de dados relacionais e criar migrações automaticamente.
D) Forçando a aplicação Flask a seguir obrigatoriamente a estrutura rígida de pastas de modelos e templates do Django.
E) Permitindo criar conexões seguras de soquetes (WebSockets) de forma automatizada sem configurar bibliotecas externas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão cobra o entendimento do mecanismo de Blueprints no ecossistema do Flask.

- **A está incorreta:** Blueprints são conceitos de arquitetura e organização de código, sem relação direta com servidores WSGI de desenvolvimento ou de produção (como Gunicorn ou uWSGI).
- **B está correta:** No Flask, à medida que a aplicação cresce, centralizar todas as rotas em uma única instância `app` torna o código ilegível e difícil de manter. Os Blueprints resolvem isso permitindo agrupar rotas, manipuladores de erros e middlewares correlatos em um objeto "planta". Esse objeto é posteriormente "registrado" na aplicação central (`app.register_blueprint()`), podendo conter prefixos de URL específicos e diretórios de templates próprios.
- **C está incorreta:** O Flask não acompanha uma ferramenta de ORM embutida (diferente do Django). A biblioteca comumente utilizada para persistência em Flask é o Flask-SQLAlchemy (extensão de terceiros).
- **D está incorreta:** O Flask é conhecido por sua flexibilidade e não impõe nenhuma estrutura rígida de diretórios. O uso de Blueprints dá autonomia para organizar o código conforme a preferência do desenvolvedor.
- **E está incorreta:** Blueprints não tratam de conexões de rede em tempo real como WebSockets.
</details>

---

### Questão 13 (FCC - 2018 - TRT 15ª Região - Analista Judiciário - Tecnologia da Informação)
Durante o ciclo de vida de uma requisição HTTP, o Flask gerencia diferentes contextos. Dentre as variáveis globais locais de thread (`thread-local variables`) expostas pelo Flask, aquela que é ligada ao Contexto da Aplicação (Application Context) e serve como um armazenamento temporário de dados compartilhados durante a requisição (como conexões de banco de dados compartilhadas) é:
A) `request`
B) `session`
C) `g`
D) `current_app`
E) `config`

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Esta questão avalia o conhecimento sobre o funcionamento e o gerenciamento de contextos (Application Context e Request Context) no Flask.

- **A está incorreta:** A variável `request` pertence ao Contexto da Requisição (`Request Context`) e armazena os dados da solicitação HTTP recebida do cliente (como cabeçalhos, formulário, argumentos da URL).
- **B está incorreta:** A variável `session` pertence ao Contexto da Requisição e é um dicionário para persistir dados entre múltiplas requisições usando cookies criptografados.
- **C está correta:** A variável `g` (sigla para global) é um objeto de armazenamento especial associado ao Contexto da Aplicação (`Application Context`). Ela é criada de forma limpa a cada nova requisição que chega e serve para que desenvolvedores compartilhem dados (por exemplo, guardar uma conexão aberta de banco de dados ou o usuário atualmente logado que foi validado por um middleware/before_request) entre diferentes funções e rotas durante o ciclo de processamento daquela requisição específica.
- **D está incorreta:** `current_app` é um proxy que aponta para a instância da aplicação Flask ativa que está processando a requisição atual, servindo para ler configurações gerais e rotas, e não para armazenar estados mutáveis do ciclo de vida da requisição.
- **E está incorreta:** `config` é o dicionário de configurações gerais de ambiente do Flask (`app.config`), mantido estático após a inicialização.
</details>

---

### Questão 14 (FCC - 2015 - TRT 3ª Região - Analista Judiciário - Tecnologia da Informação)
No desenvolvimento de formulários usando o framework Django, a validação de campos individuais e de dependências entre campos é tratada de forma declarativa e imperativa. Para realizar uma validação customizada em um campo de nome `email` de um formulário herdado de `forms.Form`, o desenvolvedor deve implementar na classe o método com o nome:
A) `validate_email(self)`
B) `check_email(self)`
C) `clean_email(self)`
D) `email_clean(self)`
E) `email_validation(self)`

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A questão cobra a convenção de nomenclatura de métodos utilizada pelo ciclo de limpeza e validação de formulários do Django.

- **A está incorreta:** Embora o nome "validate" faça sentido semântico, o Django não busca por este prefixo durante o ciclo de validação.
- **B está incorreta:** Nome falso.
- **C está correta:** No ciclo de validação do Django Forms, quando o método `is_valid()` ou `full_clean()` é invocado, o formulário processa individualmente cada campo declarado. Para cada campo com nome `[nome_do_campo]`, o Django busca e executa um método chamado `clean_[nome_do_campo]()` na classe do formulário (ex: `clean_email(self)`). Esse método é responsável por ler o dado pré-processado em `self.cleaned_data.get('email')`, validar seu formato sob regras específicas e retornar o valor limpo ou disparar uma exceção `ValidationError`.
- **D está incorreta:** A ordem do sufixo está invertida.
- **E está incorreta:** Nome falso.
</details>

---

### Questão 15 (FCC - 2017 - TRE-SP - Analista Judiciário - Programação de Sistemas)
Os decoradores (decorators) são amplamente utilizados em Python para modificar o comportamento de funções ou métodos de forma declarativa. Considere a implementação abaixo de um decorador customizado:
```python
from functools import wraps

def limitar_acesso(funcao):
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        # código de verificação
        return funcao(*args, **kwargs)
    return wrapper
```
O uso do decorador `@wraps(funcao)` importado da biblioteca `functools` sobre a função interna `wrapper` tem a finalidade técnica de:
A) Transformar a função decorada em um processo paralelo em segundo plano (background thread).
B) Impedir que a função original receba argumentos posicionais inválidos.
C) Preservar os metadados originais da função decorada (como nome `__name__` e docstring `__doc__`), evitando que eles sejam substituídos pelos metadados da função interna `wrapper`.
D) Compilar a função em código nativo C (C-extension) para acelerar o desempenho de execução da chamada.
E) Forçar a tipagem estática dos argumentos passados para a função decorada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A questão aborda as melhores práticas na criação de decoradores em Python usando o módulo padrão `functools`.

- **A está incorreta:** `@wraps` não lida com concorrência, threads ou processamento paralelo.
- **B está incorreta:** O tratamento e validação de argumentos continuam sendo de responsabilidade da assinatura do código interno da função decorada ou do próprio wrapper, não sendo controlados pelo `@wraps`.
- **C está correta:** Quando aplicamos um decorador clássico a uma função, a função original acaba sendo substituída pela função interna definida no decorador (no caso, a função `wrapper`). Sem o uso do `@wraps`, se chamarmos `print(funcao_decorada.__name__)` no console, a saída seria `"wrapper"` em vez do nome original da função, quebrando introspecções de código, geradores de documentação e frameworks que dependem do nome real. O decorador `@wraps(funcao)` copia os metadados essenciais da função original (`__name__`, `__doc__`, `__module__`, `__annotations__`) para a função `wrapper`.
- **D está incorreta:** `@wraps` é um utilitário escrito em Python puro e não envolve compilação para linguagem C ou geração de extensões de máquina.
- **E está incorreta:** Python mantém sua natureza de tipagem dinâmica. O decorador não impõe nem valida tipos estáticos em tempo de execução.
</details>

---

## 📝 TEMA 2: NoSQL — Redis (cache, pub/sub) + Modelagem Dimensional (star e snowflake - fatos, dimensões, métricas)

### Questão 1 (FCC - 2022 - TRT 22ª Região - Analista Judiciário)
O Redis é um banco de dados NoSQL do tipo chave-valor extremamente rápido, pois mantém os dados em memória RAM. Ao projetar o armazenamento de dados de perfil de um usuário contendo nome, e-mail e idade, duas abordagens são comumente discutidas na documentação oficial:

Abordagem I: Serializar o perfil em formato JSON e salvá-lo como uma String comum usando o comando `SET usuario:1001 '{"nome": "Maria", "email": "maria@mail.com", "idade": 30}'`.

Abordagem II: Armazenar as propriedades como campos de uma estrutura nativa do Redis usando o comando `HSET usuario:1001 nome "Maria" email "maria@mail.com" idade 30`.

Comparando as duas abordagens, é correto afirmar:
A) A Abordagem I é mais eficiente para atualizar pontualmente apenas o campo "idade" do usuário, pois exige menor consumo de rede para ler e gravar dados.
B) A Abordagem II (Hashes) permite ler ou atualizar atributos individuais do usuário (como `HINCRBY usuario:1001 idade 1`) sem a necessidade de transferir e desserializar todo o objeto na aplicação.
C) A Abordagem II consome consideravelmente mais memória RAM global no Redis do que a Abordagem I para pequenos conjuntos de campos devido ao custo fixo de indexação interna.
D) O comando `HGETusuario:1001` retornará todo o JSON gerado na Abordagem II, enquanto na Abordagem I deve-se usar `HGETALL`.
E) A Abordagem I inviabiliza o uso de expiração de chaves (TTL), pois o Redis não suporta comandos de expiração (`EXPIRE`) sobre valores do tipo String.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Esta questão avalia a capacidade de modelagem de dados no Redis comparando chaves do tipo String convencional e Hashes.

- **A está incorreta:** Para atualizar um único campo na Abordagem I (String/JSON), a aplicação cliente é obrigada a buscar a string completa no Redis via rede, desserializá-la no backend, alterar o valor do campo em memória, serializar novamente para JSON e transmitir toda a string de volta usando o comando `SET`. Isso gera um consumo de rede e processamento ineficientes se comparado ao Hash.
- **B está correta:** A Abordagem II mapeia os dados em um `Hash` (equivalente a um dicionário/objeto chave-valor dentro do Redis). Isso permite o acesso granular. Com comandos específicos como `HSET usuario:1001 idade 31` ou `HINCRBY usuario:1001 idade 1`, o Redis realiza a alteração in-place em memória na chave indicada sem precisar trafegar os campos `nome` e `email` pela rede.
- **C está incorreta:** A documentação oficial do Redis destaca que chaves estruturadas como Hashes pequenos são otimizadas na memória interna utilizando uma estrutura chamada `ziplist` (ou `listpack` nas versões recentes), que compacta os dados de forma extremamente eficiente, consumindo inclusive MENOS memória RAM do que salvar várias chaves simples ou uma string longa com a sintaxe do JSON redundante.
- **D está incorreta:** O comando `HGET` precisa de dois argumentos: o nome da chave e o nome do campo desejado (ex: `HGET usuario:1001 nome`). Para retornar todos os campos e valores na Abordagem II, utiliza-se `HGETALL usuario:1001`.
- **E está incorreta:** O Redis suporta expiração (`EXPIRE` e `TTL`) para qualquer tipo de chave, incluindo Strings simples, Hashes, Lists, Sets e Sorted Sets.
</details>

---

### Questão 2 (FCC - 2023 - TRT 18ª Região - Técnico Judiciário)
Uma equipe de TI necessita criar um barramento de mensagens assíncronas utilizando a estrutura de Listas (`Lists`) do Redis. Para implementar o padrão produtor-consumidor de forma eficiente, mitigando o desperdício de CPU com requisições repetitivas do tipo polling (busy wait) pelo cliente consumidor, a combinação de comandos adequada no Redis é:
A) `LPUSH` pelo produtor para inserir itens e `RPOP` em um laço infinito pelo consumidor.
B) `PUBLISH` pelo produtor para enviar mensagens e `SUBSCRIBE` pelo consumidor para escutar o canal.
C) `RPUSH` pelo produtor para enfileirar itens e `BRPOP` pelo consumidor para retirar itens da fila de forma bloqueante.
D) `SADD` pelo produtor para adicionar as mensagens e `SPOP` pelo consumidor para removê-las de forma ordenada.
E) `SET` pelo produtor para definir a mensagem e `GET` pelo consumidor para ler a fila.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A questão cobra a implementação prática de filas de mensagens (message queues) no Redis, utilizando comandos bloqueantes em listas para otimização de recursos.

- **A está incorreta:** Usar `LPUSH` (inserir na esquerda) e `RPOP` (remover da direita) estabelece uma fila FIFO correta. Contudo, se a fila estiver vazia, o comando `RPOP` retornará imediatamente `nil`. Para obter novas mensagens, o consumidor teria que executar o comando em um loop constante na rede, caracterizando o padrão de *polling* (desperdício de CPU e banda), o que contraria o requisito de eficiência do enunciado.
- **B está incorreta:** O comando `PUBLISH`/`SUBSCRIBE` implementa o padrão Pub/Sub de difusão de mensagens em tempo real (estilo rádio). Ele não utiliza a estrutura de Listas (`Lists`) do Redis solicitada no enunciado. No Pub/Sub, se o consumidor estiver offline no momento do envio, a mensagem é perdida (fire-and-forget), o que não serve para o comportamento clássico de persistência de filas.
- **C está correta:** Para trabalhar com listas de forma eficiente como filas, o produtor insere itens na lista com `RPUSH` (ou `LPUSH`). O consumidor utiliza o comando bloqueante `BRPOP` (ou `BLPOP` se o produtor usou o oposto). A letra "B" em `BRPOP` significa *Blocking*. Quando o consumidor chama `BRPOP fila_nome 30`, a conexão do cliente é colocada em espera pelo Redis. Se a lista estiver vazia, o Redis mantém a conexão aberta bloqueada por até 30 segundos (ou tempo indefinido se passado 0) aguardando um novo item. Assim que um produtor rodar `RPUSH fila_nome "mensagem"`, o Redis empurra o dado imediatamente para o consumidor pendente e encerra o bloqueio. Isso elimina completamente o overhead de polling.
- **D está incorreta:** O comando `SADD` manipula conjuntos (`Sets`). Conjuntos no Redis não são ordenados e não aceitam duplicados, o que viola o comportamento esperado de uma fila que exige ordem de chegada (FIFO).
- **E está incorreta:** O comando `SET`/`GET` trabalha com strings de chave-valor simples, incapazes de estruturar uma fila compartilhada ordenada com múltiplos produtores/consumidores nativamente.
</details>

---

### Questão 3 (FCC - 2021 - TRT 15ª Região - Analista Judiciário)
O Redis disponibiliza uma estrutura avançada de dados chamada Sorted Sets (Conjuntos Ordenados), manipulada pelo grupo de comandos iniciado com a letra 'Z'. Um Sorted Set é conceitualmente:
A) Uma lista encadeada ordenada de strings que aceita valores duplicados e é ideal para pilhas LIFO.
B) Um conjunto de elementos únicos do tipo string onde cada elemento é associado a um valor numérico de pontuação (score) flutuante usado para ordenação.
C) Uma tabela hash interna que armazena pares chave-valor criptografados com base no hash SHA-256.
D) Um array ordenado de tamanho fixo inicializado obrigatoriamente com o tamanho de alocação de memória reservado.
E) Um canal de pub/sub ordenado que garante que os consumidores leiam mensagens em ordem de prioridade definida na rede.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão cobra a definição estrutural e o comportamento dos Sorted Sets (conjuntos ordenados) no Redis.

- **A está incorreta:** Sorted Sets não admitem strings duplicadas. Além disso, listas encadeadas normais sofrem com tempo de busca linear $O(N)$ em posições intermediárias, enquanto Sorted Sets possuem buscas rápidas de complexidade logarítmica $O(\log N)$ para intervalos devido ao uso combinado de tabelas Hash e Skip Lists.
- **B está correta:** O Sorted Set (`zset`) no Redis é uma coleção onde cada membro é uma string única. A ordenação é feita através de um valor numérico decimal associado a cada membro chamado de `score`. Se múltiplos elementos possuírem o mesmo score, eles são ordenados de forma lexicográfica (alfabética). Comandos como `ZADD`, `ZRANGEBYSCORE` e `ZREVRANK` tornam essa estrutura excelente para implementar painéis de pontuação (leaderboards), índices secundários e limitadores de requisições por segundo (rate limiters).
- **C está incorreta:** Não há criptografia SHA-256 intrínseca nos tipos de ordenação do Redis.
- **D está incorreta:** Sorted Sets são dinâmicos e seu tamanho cresce/diminui sob demanda, sem tamanho estático pré-alocado.
- **E está incorreta:** Sorted Sets e o subsistema de Pub/Sub são estruturas e conceitos totalmente distintos no Redis.
</details>

---

### Questão 4 (FCC - 2022 - TRT 14ª Região - Técnico Judiciário)
Quando a memória máxima configurada no arquivo `redis.conf` é atingida, o Redis aplica políticas de despejo (eviction policies) para decidir quais chaves serão removidas e liberar espaço. O administrador configurou a propriedade `maxmemory-policy` com o valor `volatile-lru`. Esse comportamento define que o Redis irá:
A) Remover qualquer chave de forma aleatória (random) para liberar memória, ignorando se há tempo de expiração definido.
B) Lançar imediatamente um erro para todas as operações de escrita, impedindo novas gravações até que a memória seja liberada manualmente.
C) Remover as chaves menos recentemente utilizadas (LRU) dentre aquelas que possuem um tempo de expiração configurado (TTL).
D) Remover primeiro as chaves que possuem maior tempo de expiração restante (maior TTL), de forma a manter os dados mais persistentes.
E) Apagar todas as chaves persistentes (sem TTL) para assegurar que apenas dados voláteis temporários permaneçam no banco.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A questão avalia as estratégias de limpeza de chaves (eviction policies) no Redis.

- **A está incorreta:** A remoção de chaves de forma aleatória em todas as chaves é feita pela política `allkeys-random`. E a política aleatória em chaves com expiração é `volatile-random`.
- **B está incorreta:** Lançar erro de escrita é o comportamento padrão da política `noeviction`.
- **C está correta:** A política `volatile-lru` remove primeiro as chaves que estão menos propensas a uso recente (LRU - Least Recently Used) restringindo a busca exclusivamente àquelas chaves que possuem um prazo de validade (TTL) configurado via `EXPIRE`. Desta forma, chaves criadas como persistentes (sem TTL definido) são protegidas e nunca serão apagadas por essa política.
- **D está incorreta:** A remoção de chaves com base no tempo de expiração restante (removendo chaves com menor TTL) é chamada de `volatile-ttl`.
- **E está incorreta:** Políticas iniciadas com `volatile-` preservam os dados persistentes (sem TTL), focando a remoção apenas nos dados que já foram criados para expirar.
</details>

---

### Questão 5 (FCC - 2019 - TRF 3ª Região - Analista Judiciário)
O padrão de comunicação Publish/Subscribe (Pub/Sub) no Redis possibilita a troca de mensagens em tempo real entre diferentes clientes. Sobre a arquitetura Pub/Sub do Redis, é correto afirmar:
A) O Redis garante nativamente a persistência em disco de todas as mensagens publicadas em canais Pub/Sub para que leitores atrasados possam consumi-las posteriormente.
B) Clientes que realizam a assinatura de canais via comando `SUBSCRIBE` entram em um modo especial de conexão onde o Redis envia automaticamente as novas mensagens publicadas de forma assíncrona.
C) O remetente que publica uma mensagem em um canal precisa saber previamente quantos clientes estão inscritos para enviar cópias individuais das mensagens.
D) A assinatura de múltiplos canais com base em padrões com caracteres curinga (wildcards), como `canal:*`, deve ser feita através do comando `SUBSCRIBE`.
E) O Pub/Sub do Redis foi projetado para substituir completamente o uso de filas persistentes de banco de dados, oferecendo garantia de entrega com confirmação (ACK).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão foca no funcionamento e nos comandos do sistema de Pub/Sub do Redis.

- **A está incorreta:** Diferente de brokers de mensageria tradicionais (como RabbitMQ ou Apache Kafka), o Pub/Sub do Redis é puramente em memória e não persistente (*fire and forget*). Se uma mensagem é publicada e não há ouvintes ativos naquele milissegundo, a mensagem é descartada.
- **B está correta:** Quando um cliente executa `SUBSCRIBE canal_nome`, o Redis altera o estado daquela conexão. O socket do cliente fica aberto apenas para escuta das mensagens empurradas pelo Redis de forma assíncrona. Nesse estado, o cliente só pode enviar comandos de controle de canais (como `SUBSCRIBE`, `UNSUBSCRIBE`, `PSUBSCRIBE`, etc.).
- **C está incorreta:** O remetente apenas chama o comando `PUBLISH canal_nome "mensagem"`. O Redis gerencia o roteamento interno de forma transparente para todos os assinantes daquele canal. O remetente não conhece os destinatários.
- **D está incorreta:** O comando correto para realizar assinaturas por casamento de padrões com wildcards (curingas) é o `PSUBSCRIBE` (Pattern Subscribe), e não o `SUBSCRIBE` comum, que busca o nome exato do canal.
- **E está incorreta:** Como dito na alternativa A, o Pub/Sub do Redis é volátil. Para ter garantia de entrega com ACK e persistência de mensagens, deve-se usar as estruturas nativas de *Streams* (introduzidas no Redis 5.0) ou filas construídas sobre listas.
</details>

---

### Questão 6 (FCC - 2023 - TRT 11ª Região - Analista Judiciário)
Para garantir a durabilidade dos dados sem comprometer severamente o desempenho, o Redis implementa dois mecanismos de persistência: RDB (Redis Database Backup) e AOF (Append Only File). Sobre essas tecnologias, assinale a opção correta:
A) O RDB gera logs em formato de texto contendo todas as operações de escrita recebidas, adicionando-os linha por linha ao final do arquivo para remontagem de transações.
B) O AOF gera uma captura do estado do banco (snapshot) em um arquivo binário extremamente compacto e otimizado em intervalos definidos de tempo.
C) O principal risco ao utilizar somente a persistência RDB é a perda de dados ocorridos entre o último snapshot salvo com sucesso e uma interrupção abrupta do servidor.
D) O uso exclusivo do AOF garante alta performance em processos de escrita, pois realizar escritas contínuas em disco é computacionalmente mais leve do que armazenar dados na memória RAM.
E) Quando o arquivo AOF cresce excessivamente, o Redis entra em modo de falha e exige uma limpeza manual do disco, pois ele não possui mecanismos de compactação em tempo de execução.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A questão cobra as características, diferenças e trade-offs dos modelos de persistência RDB e AOF do Redis.

- **A está incorreta:** A descrição oferecida refere-se ao mecanismo AOF, e não RDB. O AOF registra de forma incremental todas as operações que alteram o banco em um log de comandos.
- **B está incorreta:** A descrição oferecida refere-se ao mecanismo RDB. O RDB gera instantâneos binários em disco.
- **C está correta:** O RDB faz snapshots pontuais (por exemplo, a cada 15 minutos se houver pelo menos 1 alteração, ou conforme configurado). Se o servidor do Redis sofrer uma queda de energia ou travamento aos 14 minutos do intervalo, todos os dados modificados após o último snapshot serão perdidos permanentemente.
- **D está incorreta:** A memória RAM é infinitamente mais rápida do que operações de gravação física em disco. Habilitar o AOF com sincronização frequente reduz a performance do Redis devido à latência de gravação de arquivos (I/O).
- **E está incorreta:** O Redis possui o comando `BGREWRITEAOF` que roda em segundo plano. Ele lê o banco de dados em memória e gera um novo arquivo AOF menor, contendo apenas a menor sequência de instruções necessárias para reconstruir o estado atual do banco (compactando múltiplos incrementos em chaves iguais).
</details>

---

### Questão 7 (FCC - 2018 - TRT 2ª Região - Técnico Judiciário)
O Redis Sentinel e o Redis Cluster são duas arquiteturas distintas para escalar o banco de dados e garantir alta disponibilidade. A diferença conceitual fundamental entre eles é:
A) O Redis Cluster serve apenas para cópias de leitura simples (Read Replicas), enquanto o Sentinel gerencia a partição física de dados fragmentados (sharding).
B) O Redis Sentinel foca na alta disponibilidade e failover automático de arquiteturas Master-Slave (Mestre-Escravo), sem distribuir os dados em múltiplos nós (sharding), enquanto o Redis Cluster distribui os dados horizontalmente entre múltiplos nós primários de forma nativa.
C) O Sentinel exige o desligamento manual do servidor master em caso de falha, enquanto o Cluster realiza failover por hardware.
D) O Redis Cluster armazena todos os dados de forma idêntica e completa em todos os nós participantes do anel, não existindo conceito de divisão de chaves.
E) A arquitetura Sentinel divide as chaves do banco de dados em exatos 16.384 slots lógicos distribuídos entre servidores escravos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão avalia a capacidade do candidato em distinguir as arquiteturas oficiais de Alta Disponibilidade (Sentinel) e Escalabilidade Horizontal (Cluster) do Redis.

- **A está incorreta:** Inverte a função do Cluster, que é focado em particionamento de chaves (sharding).
- **B está correta:** 
  - **Redis Sentinel:** É um sistema externo de monitoramento. Ele não divide os dados. Sua função é vigiar o nó Master e os Slaves. Se o Master cair, os Sentinels fazem uma votação eletrônica e promovem um dos Slaves a novo Master automaticamente, direcionando as conexões dos clientes.
  - **Redis Cluster:** É uma solução de escalabilidade horizontal. Os dados são particionados de forma transparente entre múltiplos nós Master ativos usando o conceito de hash slots (16.384 slots). Cada nó primário fica encarregado de uma faixa de slots.
- **C está incorreta:** O Sentinel automatiza completamente a detecção e promoção do novo Master (failover), não exigindo intervenção manual do administrador.
- **D está incorreta:** O Redis Cluster particiona os dados. Cada chave é mapeada a um slot e cada slot reside em um nó Master específico. Não há replicação completa de todo o banco em todos os nós Masters (apenas de Master para seu respectivo Slave).
- **E está incorreta:** Quem divide o banco em 16.384 slots lógicos é o Redis Cluster, distribuindo-os entre seus nós Master primários, e não o Sentinel.
</details>

---

### Questão 8 (FCC - 2021 - TRT 15ª Região - Técnico Judiciário)
Na modelagem de dados para sistemas analíticos e de Business Intelligence (BI), a abordagem de Modelagem Dimensional de Ralph Kimball contrasta fortemente com o modelo corporativo normalizado proposto por Bill Inmon. A filosofia de Kimball defende que o Data Warehouse empresarial deve ser construído:
A) De maneira centralizada em um modelo relacional puramente normalizado na Terceira Forma Normal (3FN), criando os subconjuntos de dados posteriormente.
B) Através da união incremental de múltiplos Data Marts dimensionais orientados a processos de negócios específicos, utilizando dimensões conformadas para garantir a integração.
C) Usando estruturas de banco de dados NoSQL do tipo chave-valor para evitar por completo a criação de esquemas lógicos estruturados.
D) Mantendo todas as tabelas em um único nível relacional gigante totalmente desprovido de chaves primárias e estrangeiras.
E) De cima para baixo (top-down), iniciando por uma base de dados replicada em tempo real diretamente dos servidores transacionais OLTP de produção.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Esta questão avalia o conhecimento sobre as metodologias de design de Data Warehouses (Kimball vs Inmon).

- **A está incorreta:** A construção centralizada e normalizada na 3FN (Corporate Information Factory - CIF) é a base conceitual da metodologia de Bill Inmon, e não de Kimball.
- **B está correta:** Ralph Kimball propôs a abordagem "Bottom-Up" (de baixo para cima). Ele sugere que a empresa crie Data Marts dimensionais progressivamente para processos específicos (vendas, estoque, RH) usando modelos estrela/floco de neve. A integração e coerência global de todo o Data Warehouse é obtida pelo uso de "Dimensões Conformadas" (dimensões padronizadas e compartilhadas por vários fatos, ex: dimensão Cliente, dimensão Tempo).
- **C está incorreta:** A modelagem dimensional tradicional de Kimball foi desenhada e é amplamente utilizada sobre bancos de dados relacionais e bancos colunares analíticos usando SQL tradicional.
- **D está incorreta:** Tabelas de fatos e dimensões possuem chaves primárias e relacionamentos lógicos complexos bem estruturados.
- **E está incorreta:** OLTP e data warehouses (OLAP) são mantidos isolados para evitar impacto operacional de consultas analíticas pesadas sobre os servidores de produção. A proposta de Kimball não é uma replicação OLTP direta.
</details>

---

### Questão 9 (FCC - 2022 - TRT 14ª Região - Analista Judiciário)
No design de esquemas para Data Warehouses, a estrutura em Estrela (Star Schema) é um dos modelos mais adotados. Dentre as características estruturais desse esquema, destaca-se:
A) O fato de que todas as tabelas dimensão são totalmente normalizadas na terceira forma normal, gerando cadeias complexas de junções (joins).
B) A presença de uma tabela fato central altamente desnormalizada rodeada por dimensões normalizadas em níveis hierárquicos ramificados.
C) O relacionamento direto de cada tabela dimensão com a tabela fato central através de chaves, onde as dimensões são desnormalizadas e contêm dados redundantes para acelerar consultas analíticas.
D) A inexistência de chaves estrangeiras na tabela fato, que confia unicamente em nomes de colunas idênticos para realizar cruzamentos automáticos.
E) O isolamento completo das tabelas dimensão, que não possuem qualquer relacionamento físico ou lógico com a tabela fato principal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A questão cobra as características físicas e lógicas do esquema em Estrela (Star Schema).

- **A está incorreta:** A normalização das dimensões é a característica principal do esquema Floco de Neve (Snowflake), e não do esquema em Estrela.
- **B está incorreta:** No esquema estrela, a tabela fato é centralizada e as tabelas dimensão ao redor são desnormalizadas (unificadas sem subdivisões de níveis hierárquicos). Se as dimensões fossem normalizadas de forma ramificada, o modelo seria Floco de Neve.
- **C está correta:** No modelo Star Schema, a tabela fato fica no centro e se conecta diretamente a todas as tabelas dimensão. As tabelas dimensão são intencionalmente mantidas desnormalizadas, o que significa que hierarquias inteiras (ex: Cidade -> Estado -> País) são salvas em colunas da mesma tabela de dimensão. Isso simplifica a escrita de consultas SQL e reduz drasticamente o número de junções (`JOINs`) necessárias, aumentando a velocidade de agregação dos dados analíticos.
- **D está incorreta:** A tabela fato é composta majoritariamente por chaves estrangeiras que apontam para as chaves primárias correspondentes em cada tabela de dimensão envolvida no grão do negócio.
- **E está incorreta:** A tabela fato é intrinsicamente relacionada com suas tabelas dimensão através de chaves estrangeiras.
</details>

---

### Questão 10 (FCC - 2018 - TRT 6ª Região - Analista Judiciário)
O esquema Floco de Neve (Snowflake Schema) é uma variação do modelo dimensional. A principal vantagem técnica que justifica a escolha do esquema Floco de Neve em detrimento do esquema Estrela (Star Schema) é:
A) A simplificação das consultas SQL, diminuindo a quantidade de comandos JOIN necessários nas queries.
B) A minimização da redundância de dados nas tabelas dimensão por meio da normalização, o que reduz o espaço em disco ocupado pelas dimensões e facilita a manutenção da consistência dos atributos hierárquicos.
C) A velocidade superior na execução de consultas OLAP, visto que navegar em múltiplas tabelas indexadas é sempre mais rápido do que varrer uma única tabela larga.
D) A total eliminação da necessidade de definir granularidades e chaves artificiais (surrogate keys) nas tabelas fato.
E) A compatibilidade exclusiva do Snowflake com servidores NoSQL que não aceitam bancos relacionais.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão aborda os prós e contras da modelagem em Floco de Neve (Snowflake Schema).

- **A está incorreta:** O Snowflake *dificulta* e *complexifica* as consultas SQL porque fragmenta as dimensões em múltiplas tabelas normalizadas, exigindo que o motor analítico processe mais comandos `JOIN` para remontar a dimensão e seus atributos hierárquicos.
- **B está correta:** O esquema Floco de Neve normaliza as tabelas de dimensão que possuem hierarquias. Por exemplo, em vez de guardar Cidade, Estado e País na tabela `Dim_Geografia` como colunas simples com repetições (como no Star Schema), o Snowflake separa em tabelas distintas `Dim_Cidade -> Dim_Estado -> Dim_Pais` com relacionamentos um-para-muitos. A principal vantagem é a redução de redundância de strings repetidas de texto nas dimensões, gerando economia de espaço de armazenamento e melhor integridade de dados na atualização dessas categorias.
- **C está incorreta:** Em geral, o Snowflake é *mais lento* na execução de consultas de leitura de dados por causa do overhead computacional necessário para resolver múltiplas junções físicas de tabelas.
- **D está incorreta:** Granularidade e chaves substitutas (surrogate keys) continuam sendo requisitos fundamentais em ambos os modelos dimensionais.
- **E está incorreta:** O Snowflake é implementado e suportado em bancos relacionais tradicionais e em data warehouses analíticos padrão.
</details>

---

### Questão 11 (FCC - 2023 - TRE SP - Técnico Judiciário)
Na modelagem dimensional, a tabela Fato desempenha o papel de repositório central de métricas quantificáveis de um processo de negócio. Do ponto de vista de sua estrutura, a tabela fato é composta essencialmente por:
A) Dados textuais detalhados que descrevem o comportamento e nome dos clientes, sem referências numéricas.
B) Códigos de controle de segurança do banco de dados e arquivos de logs do sistema operacional.
C) Apenas chaves primárias compostas por strings textuais dinâmicas inseridas pelos sistemas transacionais nativos.
D) Uma chave primária composta (ou chaves estrangeiras) que faz a ligação para as tabelas de dimensões e colunas com medidas numéricas correspondentes aos fatos.
E) Descrições redundantes dos produtos da empresa e o fluxo completo de histórico do cliente (SCD).

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão foca no conteúdo estrutural das tabelas fato dentro de modelos relacionais analíticos.

- **A está incorreta:** Textos longos descritivos (nomes, e-mails, descrições de produtos, categorias) pertencem exclusivamente às tabelas Dimensão, e não à tabela Fato.
- **B está incorreta:** Logs de sistemas não entram no modelo analítico de tabelas fato diretamente.
- **C está incorreta:** As chaves de ligação do modelo de Kimball costumam ser chaves artificiais numéricas do tipo inteiro denominadas Surrogate Keys (chaves substitutas), e não strings geradas dinamicamente.
- **D está correta:** A tabela Fato possui uma chave primária que normalmente é composta pela combinação de todas as chaves estrangeiras (`Foreign Keys`) que apontam para as tabelas dimensão participantes (ex: data_key, cliente_key, produto_key). Além destas chaves de vinculação contextual, ela contém as colunas de dados numéricos mensuráveis do negócio (como valor_venda, quantidade_itens, percentual_desconto) conhecidas como métricas ou medidas.
- **E está incorreta:** O histórico de alteração de atributos descritivos do cliente (Slowly Changing Dimensions) é tratado e gravado na própria tabela Dimensão, mantendo a tabela fato focada apenas nos eventos numéricos e suas respectivas chaves.
</details>

---

### Questão 12 (FCC - 2019 - TRF 4ª Região - Técnico Judiciário)
As métricas (ou medidas) inseridas em tabelas fato podem ser classificadas conforme seu comportamento de agregação ao longo das dimensões do modelo. Considere os três exemplos clássicos de medidas a seguir:

I. O valor total faturado em uma venda.
II. O saldo diário de uma conta bancária.
III. A margem percentual de lucro de um produto.

Essas medidas são classificadas, respectivamente, como:
A) Aditiva, Não aditiva e Semi-aditiva.
B) Semi-aditiva, Aditiva e Não aditiva.
C) Aditiva, Semi-aditiva e Não aditiva.
D) Não aditiva, Semi-aditiva e Aditiva.
E) Aditiva, Aditiva e Não aditiva.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Esta questão avalia a capacidade de diferenciar os três comportamentos de soma de métricas em tabelas fato: Aditivas, Semi-aditivas e Não aditivas.

- **A está incorreta:** Inverte a classificação das duas últimas métricas.
- **B está incorreta:** Inverte a classificação das duas primeiras.
- **C está correta:** 
  - **Métrica Aditiva (Exemplo I - Valor faturado):** Pode ser somada de forma significativa ao longo de todas as dimensões do modelo (você pode somar o faturamento por tempo, por produto, por região, etc.).
  - **Métrica Semi-aditiva (Exemplo II - Saldo da conta):** Pode ser somada apenas ao longo de algumas dimensões, mas não de todas. Você pode somar os saldos de diferentes clientes em um dia para obter o saldo total do banco (soma por cliente). Contudo, você NÃO pode somar o saldo de segunda-feira com o de terça-feira para obter o "saldo acumulado" da conta (soma pelo tempo), pois essa soma geraria um valor financeiro falso. Para a dimensão tempo, calcula-se geralmente a média ou o saldo final do período.
  - **Métrica Não aditiva (Exemplo III - Margem percentual):** Não pode ser somada em nenhuma dimensão. Se o produto A tem margem de 10% e o B de 15%, a margem total deles não é a soma simples de 25%. Métricas não aditivas (como taxas, razões e índices percentuais) devem ser calculadas no momento de exibição dividindo os valores aditivos agregados subjacentes (ex: somar lucro total e dividir por somatório de receita total).
- **D está incorreta:** Classificação invertida de ponta a ponta.
- **E está incorreta:** O saldo diário bancário não pode ser somado na dimensão tempo, logo não é aditiva pura.
</details>

---

### Questão 13 (FCC - 2018 - TRT 15ª Região - Técnico Judiciário)
No projeto de tabelas Dimensão, os projetistas preferem utilizar chaves artificiais do tipo inteiro geradas sequencialmente pelo próprio Data Warehouse (Surrogate Keys) no lugar das chaves primárias dos sistemas de origem (Natural Keys/Operational Keys). A razão técnica primordial para essa prática é:
A) Ocultar a identidade e dados reais dos clientes para cumprir a Lei Geral de Proteção de Dados (LGPD).
B) Garantir a compatibilidade do sistema com consultas que não usem a linguagem SQL.
C) Permitir que o Data Warehouse registre de forma independente o histórico de alterações dos atributos das dimensões ao longo do tempo (como na técnica de SCD Tipo 2), isolando a chave de BI de mudanças de IDs nos bancos transacionais.
D) Forçar o banco OLAP a rodar em servidores distribuídos baseados em sistemas de arquivos NoSQL HDFS.
E) Reduzir o número de registros na tabela fato, mantendo apenas 1 linha por cliente independente do número de compras dele.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A questão cobra a justificativa técnica para o uso de Surrogate Keys (chaves substitutas) nas tabelas de dimensão de um Data Warehouse.

- **A está incorreta:** Embora Surrogate Keys protejam o design interno de chaves de negócio expostas, a LGPD exige técnicas de anonimização e criptografia para segurança pessoal de dados. Surrogate Keys são geradas por razões de arquitetura e integridade do modelo dimensional analítico, e não para criptografia de conformidade de privacidade.
- **B está incorreta:** Consultas SQL funcionam perfeitamente com qualquer tipo de chave primária, natural ou surrogate.
- **C está correta:** A chave natural (ex: ID da tabela transacional do cliente) identifica univocamente um cliente no banco de origem. No entanto, se o cliente mudar de endereço e o DW usar a técnica de Slowly Changing Dimension (SCD) Tipo 2 para registrar o histórico (criando uma nova linha para representar o endereço novo mantendo o registro do endereço antigo para estatísticas passadas), haverá múltiplos registros para a mesma chave natural. O uso de uma Surrogate Key (ex: `cliente_sk`) gerada de forma incremental e numérica no DW permite associar diferentes versões históricas do mesmo cliente a chaves primárias físicas diferentes na dimensão, permitindo que a tabela Fato aponte para a versão exata do cliente no momento em que a compra ocorreu. Além disso, protege o DW contra reuso de IDs ou mudanças estruturais nos sistemas OLTP de origem.
- **D está incorreta:** O uso de Surrogate Keys é um conceito independente do tipo de sistema de arquivos ou infraestrutura operacional.
- **E está incorreta:** Surrogate Keys não limitam o número de registros na tabela fato.
</details>

---

### Questão 14 (FCC - 2021 - TRT 11ª Região - Analista Judiciário)
Em modelagem dimensional, o conceito de Dimensão Conformada (Conformed Dimension) é essencial para o sucesso de uma arquitetura empresarial integrada. Uma dimensão é dita conformada quando ela:
A) Possui o formato físico de uma estrela perfeita e é construída na terceira forma normal.
B) É criada especificamente para ser usada por um único Data Mart departamental, impedindo o cruzamento de dados com outros setores da empresa.
C) Apresenta o mesmo significado exato, conteúdo idêntico e estrutura de dados padronizada ao ser compartilhada por diferentes tabelas Fato de múltiplos Data Marts.
D) É armazenada de forma criptografada para proteger informações de faturamento confidencial.
E) Contém apenas atributos numéricos mutáveis gerados por sistemas transacionais operacionais OLTP.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

Esta questão avalia a compreensão do conceito de Dimensão Conformada proposto na metodologia de Ralph Kimball.

- **A está incorreta:** A conformação não tem relação direta com formas normais físicas ou o desenho estético em estrela.
- **B está incorreta:** O objetivo de uma dimensão conformada é justamente o oposto: ela é compartilhada por *múltiplos* Data Marts para integrar a visão dos dados em toda a organização.
- **C está correta:** Dimensões Conformadas são a espinha dorsal da integração do Data Warehouse corporativo no modelo de Kimball. Trata-se de uma dimensão (ex: tempo, cliente ou produto) que foi unificada e padronizada. Dessa forma, ela pode ser usada simultaneamente por diferentes tabelas fato (como Vendas e Logística). Isso viabiliza a execução de consultas consolidadas cruzadas (drill-across) com a garantia de que as chaves e terminologias são idênticas.
- **D está incorreta:** A conformação aborda integridade lógica e semântica, sem relação direta com métodos de encriptação ou segurança de chaves.
- **E está incorreta:** Dimensões contêm atributos de texto descritivos (dados qualitativos), não apenas métricas numéricas operacionais mutáveis.
</details>

---

### Questão 15 (FCC - 2022 - TRT 4ª Região - Analista Judiciário)
Considere dois conceitos especiais em modelagem dimensional:

I. Uma tabela fato que registra a ocorrência de um evento (ex: presença de aluno em sala de aula) contendo apenas chaves estrangeiras para as dimensões, sem apresentar colunas de métricas/medidas numéricas de valor.
II. Uma dimensão cujo atributo identificador (ex: número da nota fiscal ou número do pedido) é armazenado diretamente dentro da tabela fato devido ao grão do negócio, sem a necessidade de criar uma tabela de dimensão física separada na base de dados.

Esses conceitos referem-se, respectivamente, a:
A) Tabela Fato Semi-aditiva e Dimensão Conformada.
B) Tabela Fato sem Fatos (Factless Fact Table) e Dimensão Degenerada (Degenerate Dimension).
C) Tabela Fato Aditiva e Dimensão Floco de Neve.
D) Tabela Fato Rápida e Dimensão Lixo (Junk Dimension).
E) Tabela Fato sem Fatos (Factless Fact Table) e Dimensão Conformada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão avalia a capacidade de identificar e diferenciar o conceito de Factless Fact Table (Tabela Fato Sem Fatos) e Degenerate Dimension (Dimensão Degenerada).

- **A está incorreta:** O saldo diário bancário é semi-aditivo, não tem relação com tabelas sem métricas numéricas.
- **B está correta:** 
  - **Item I - Tabela Fato sem Fatos (Factless Fact Table):** É uma tabela fato que não possui medidas numéricas próprias além das chaves estrangeiras. Ela serve para registrar a associação de eventos ou relacionamentos (ex: a presença de um aluno no dia de aula, onde temos apenas chaves de ligação para aluno, sala, data, sem métricas quantitativas. Para contar os eventos, usa-se a função de agregação `COUNT`).
  - **Item II - Dimensão Degenerada (Degenerate Dimension):** Ocorre quando um atributo identificador único (como número do cupom fiscal, número do ticket de suporte ou número de rastreamento) é de extrema importância para rastrear o grão de cada linha na tabela fato, mas não possui nenhum outro atributo qualitativo que justifique a criação de uma tabela dimensão própria em separado no disco. Logo, esse atributo de controle é salvo diretamente como coluna física da própria tabela Fato.
- **C está incorreta:** Inadequado.
- **D está incorreta:** Dimensões de lixo (Junk Dimensions) agrupam múltiplos indicadores low-cardinality (sinalizadores de status, flags de sim/não) em uma única tabela física para economizar colunas na tabela fato, o que difere de colocar um atributo identificador como nota fiscal diretamente na fato.
- **E está incorreta:** A dimensão conformada é uma dimensão compartilhada padronizada, diferente do conceito de dimensão degenerada exposto no Item II.
</details>

---

## 📝 TEMA 3: Português: Sintaxe da Oração e do Período + Elementos estruturais e processos de formação de palavras (derivação/composição)

### Questão 1 (FCC - 2022 - TRT 22ª Região - Analista Judiciário)
Observe a oração em destaque no período abaixo:
"Constatou-se **que os servidores do Tribunal necessitam de novos equipamentos de informática**."
Do ponto de vista da sintaxe do período composto, a oração destacada é classificada como oração subordinada substantiva:
A) Objetiva direta, pois funciona como objeto direto do verbo "constatar".
B) Completiva nominal, tendo em vista que completa o sentido do substantivo abstrato "Tribunal".
C) Subjetiva, uma vez que desempenha a função sintática de sujeito do verbo da oração principal "constatar-se".
D) Apositiva, pois serve para explicar um termo anteriormente mencionado no texto.
E) Predicativa, exercendo a função de predicativo do sujeito na oração principal.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A questão cobra a identificação sintática de orações subordinadas substantivas, especificamente o caso da oração subjetiva em oração principal com voz passiva sintética.

- **A está incorreta:** O aluno desatento pode pensar que a oração é objetiva direta devido à transitividade direta do verbo "constatar" (quem constata, constata algo). Porém, a presença da partícula apassivadora "se" muda a voz do verbo para a passiva sintética. Equivale semanticamente a: "Que os servidores necessitam de novos equipamentos **foi constatado**". O que é constatado torna-se o sujeito paciente da oração.
- **B está incorreta:** A oração subordinada substantiva completiva nominal integra o sentido de um nome (substantivo, adjetivo ou advérbio) pertencente à oração principal. O termo anterior é "constatou-se", que é um verbo.
- **C está correta:** A estrutura "VTD + se" (Constatou-se) configura voz passiva sintética. A oração introduzida pela conjunção integrante "que" ("que os servidores do Tribunal necessitam de novos equipamentos de informática") funciona como o sujeito paciente dessa forma verbal. Logo, trata-se de uma Oração Subordinada Substantiva Subjetiva.
- **D está incorreta:** Orações apositivas funcionam como aposto de um termo da oração principal, normalmente antecedidas por dois-pontos ou travessões.
- **E está incorreta:** A oração predicativa exige a presença de um verbo de ligação expresso na oração principal exercendo o papel de conectar o sujeito ao predicativo (ex: "A verdade é que eles virão").
</details>

---

### Questão 2 (FCC - 2023 - TRT 18ª Região - Técnico Judiciário)
Assinale a alternativa em que a classificação do termo destacado está INCORRETA:
A) O julgamento **do réu** foi rápido. (Complemento Nominal, pois o substantivo abstrato "julgamento" tem sentido passivo: o réu foi julgado).
B) O amor **de mãe** é incondicional. (Adjunto Adnominal, pois a preposição + substantivo possui valor ativo: a mãe ama).
C) Os assessores tinham necessidade **de auxílio**. (Complemento Nominal, pois completa o sentido do substantivo abstrato transitivo "necessidade").
D) O envio **de relatórios** ao Diretor ocorreu pela manhã. (Complemento Nominal, porquanto "relatórios" recebe a ação expressa pelo substantivo transitivo "envio").
E) A leitura **do analista** sobre o caso foi brilhante. (Complemento Nominal, visto que completa o sentido do nome "leitura").

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: E**

A questão cobra a distinção sintática clássica entre Complemento Nominal (CN) e Adjunto Adnominal (AA) preposicionados ligados a substantivos abstratos.

- **A está correta (classificação correta):** O substantivo "julgamento" é abstrato (derivado de ação). O termo "do réu" recebe a ação de ser julgado (sentido passivo). Logo, sintaticamente, é um **Complemento Nominal**.
- **B está correta (classificação correta):** O termo "de mãe" indica o agente do amor (a mãe que ama/sentido ativo). Quando o termo preposicionado possui valor ativo sobre o substantivo abstrato, classifica-se como **Adjunto Adnominal**.
- **C está correta (classificação correta):** O substantivo "necessidade" exige complemento para ter sentido completo (quem tem necessidade, tem necessidade *de algo*). O termo "de auxílio" atua como paciente dessa necessidade. Sendo assim, é um **Complemento Nominal**.
- **D está correta (classificação correta):** O substantivo "envio" provém do verbo enviar (ação). Os "relatórios" sofrem a ação de serem enviados (paciente). Termos preposicionados com valor paciente ligados a substantivos abstratos de ação são **Complementos Nominais**.
- **E está incorreta (gabarito da questão):** No trecho "A leitura do analista", o termo "do analista" refere-se ao agente da ação de ler (o analista leu/sentido ativo). Como o termo preposicionado tem valor ativo sobre o substantivo abstrato "leitura", ele desempenha a função de **Adjunto Adnominal**, e não de Complemento Nominal. Por possuir classificação incorreta na afirmativa, esta é a alternativa a ser assinalada.
</details>

---

### Questão 3 (FCC - 2021 - TRT 15ª Região - Analista Judiciário)
No trecho: "O juiz, **que agiu com extrema cautela durante a audiência**, preferiu adiar a sentença."
A oração em destaque e o pronome relativo que a introduz exercem, respectivamente, as funções sintáticas de:
A) Oração subordinada adjetiva restritiva; sujeito da oração subordinada.
B) Oração subordinada adjetiva explicativa; sujeito da oração subordinada.
C) Oração subordinada adjetiva explicativa; objeto direto da oração subordinada.
D) Oração subordinada substantiva apositiva; adjunto adnominal da oração principal.
E) Oração subordinada adjetiva restritiva; objeto indireto da oração subordinada.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão aborda a identificação e classificação das Orações Subordinadas Adjetivas e a função sintática exercida pelo pronome relativo dentro da oração que ele encabeça.

- **A está incorreta:** A oração está isolada por vírgulas. Gramaticalmente, as orações adjetivas isoladas por vírgulas são explicativas, enquanto as restritivas não admitem o uso de vírgulas.
- **B está correta:** 
  1. A oração "**que agiu com extrema cautela durante a audiência**" refere-se ao substantivo "O juiz" explicando um detalhe sobre ele. Como está isolada por vírgulas, classifica-se como **Oração Subordinada Adjetiva Explicativa**.
  2. O conectivo "que" é um pronome relativo que retoma o termo antecedente "O juiz". Para identificar a função sintática do pronome relativo, substituímos o "que" pelo seu antecedente na oração subordinada: "[O juiz] agiu com extrema cautela durante a audiência". Nessa oração isolada, "O juiz" pratica a ação de agir, exercendo a função de **sujeito**. Logo, o pronome relativo "que" funciona como sujeito.
- **C está incorreta:** O pronome "que" funciona como sujeito do verbo "agiu", e não como objeto direto.
- **D está incorreta:** A oração é introduzida por pronome relativo (equivalendo a "o qual agiu..."), o que a caracteriza como adjetiva, e não substantiva apositiva.
- **E está incorreta:** A oração é explicativa (contém vírgulas) e a função sintática do pronome relativo é de sujeito.
</details>

---

### Questão 4 (FCC - 2022 - TRT 14ª Região - Técnico Judiciário)
Considere o período abaixo:
"**Embora o sistema de peticionamento eletrônico apresentasse instabilidade**, os advogados conseguiram protocolar as peças processuais dentro do prazo legal."
A oração destacada no período estabelece uma relação semântica de:
A) Condição, equivalendo a: "Caso o sistema de peticionamento eletrônico apresentasse...".
B) Causa, indicando o motivo direto pelo qual os advogados protocolaram as peças.
C) Consequência, expressando o resultado gerado pelo protocolo das peças.
D) Concessão, expressando uma quebra de expectativa ou obstáculo que não impede a realização da oração principal.
E) Proporção, sinalizando que a instabilidade aumentava na mesma medida do protocolo.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão cobra a classificação semântica das Orações Subordinadas Adverbiais, focando no conectivo concessivo "Embora".

- **A está incorreta:** As orações condicionais exprimem uma hipótese necessária para que o fato principal ocorra, introduzidas por conjunções como "se", "caso". A instabilidade do sistema não foi uma condição para que eles protocolassem as peças.
- **B está incorreta:** A causa explica o motivo. A instabilidade do sistema não causou o sucesso do protocolo.
- **C está incorreta:** O fato de protocolar não é consequência direta da instabilidade.
- **D está correta:** A conjunção "Embora" introduz uma **Oração Subordinada Adverbial Concessiva**. A concessão representa uma oposição atenuada, ou seja, apresenta um fato contrário (instabilidade no sistema) que, teoricamente, dificultaria a realização da ação principal (protocolar as peças), mas que é insuficiente para impedir o seu cumprimento.
- **E está incorreta:** As proporcionais indicam simultaneidade de variação de intensidade, marcadas por conectivos como "à medida que", "à proporção que".
</details>

---

### Questão 5 (FCC - 2019 - TRF 3ª Região - Analista Judiciário)
"Ao analisar os processos, o assessor identificou erros de digitação."
A oração reduzida destacada no período acima, quando desenvolvida para uma oração correspondente com conjunção explícita, assume o formato correto e a classificação semântica de:
A) "Visto que analisou os processos..." — Oração subordinada adverbial causal.
B) "Se analisar os processos..." — Oração subordinada adverbial condicional.
C) "Assim que analisou os processos..." — Oração subordinada adverbial temporal.
D) "Conforme analisava os processos..." — Oração subordinada adverbial conformativa.
E) "Para analisar os processos..." — Oração subordinada adverbial final.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: C**

A questão avalia a capacidade de identificar o valor semântico de orações reduzidas e convertê-las adequadamente em orações desenvolvidas (introduzidas por conjunção + verbo conjugado).

- **A está incorreta:** O ato de analisar não foi a causa/motivo de encontrar os erros, mas sim o momento em que isso ocorreu.
- **B está incorreta:** A oração original expressa um fato consumado no passado ("identificou"), e não uma condição futura.
- **C está correta:** A oração "Ao analisar os processos..." é uma **Oração Reduzida de Infinitivo** (composta pela preposição "a" contraída com o artigo "o" + verbo "analisar" no infinitivo). Ela possui nítido valor temporal, indicando o momento em que a ação de identificar os erros ocorreu (tempo). Desenvolvendo-a com uma conjunção temporal subordinativa equivalente e mantendo a concordância de tempo verbal no passado, obtemos: "Assim que analisou os processos...", "Quando analisava os processos..." ou "Logo que analisou os processos...".
- **D está incorreta:** A conformação indica acordo/conformidade (como "de acordo com o que analisava"), o que destoa da ideia de tempo do trecho original.
- **E está incorreta:** A preposição "para" indicaria finalidade (objetivo), alterando o sentido temporal do texto.
</details>

---

### Questão 6 (FCC - 2023 - TRT 11ª Região - Analista Judiciário)
Assinale a alternativa que apresenta oração sem sujeito:
A) Havia muitos candidatos inscritos no concurso para o Tribunal.
B) Alugaram-se várias salas no bloco administrativo do fórum.
C) Devem existir soluções melhores para este problema de rede.
D) Bateram à porta da assessoria jurídica logo cedo.
E) Nós fomos ao gabinete do magistrado ontem à tarde.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A questão cobra o reconhecimento dos casos de impessoalidade verbal que resultam em Oração Sem Sujeito (sujeito inexistente).

- **A está correta:** O verbo **haver** é impessoal quando empregado com o sentido de "existir", "acontecer" ou indicando tempo transcorrido. Como verbo impessoal, ele não possui sujeito e deve obrigatoriamente permanecer na 3ª pessoa do singular ("Havia muitos candidatos...", e não "Haviam"). Sendo assim, a frase é uma **Oração Sem Sujeito**.
- **B está incorreta:** O verbo "alugar" é transitivo direto (VTD). Na presença da partícula "se", esta funciona como partícula apassivadora (PA). A frase equivale a: "Várias salas foram alugadas". Portanto, "várias salas" é o **sujeito paciente** da oração (sujeito simples).
- **C está incorreta:** O verbo **existir** NÃO é impessoal (diferente de "haver"). Ele possui sujeito expresso no período. Na locução "Devem existir soluções", o substantivo "soluções" é o **sujeito** da oração, o que inclusive obriga o verbo auxiliar "dever" a flexionar-se no plural ("Devem").
- **D está incorreta:** O verbo "bater" na 3ª pessoa do plural ("Bateram") sem referência prévia de contexto configura caso clássico de **Sujeito Indeterminado**, e não sujeito inexistente.
- **E está incorreta:** O sujeito é simples e explícito: "Nós" (sujeito determinado simples).
</details>

---

### Questão 7 (FCC - 2018 - TRT 2ª Região - Técnico Judiciário)
Na frase: "O diretor considerou a proposta **inaceitável**."
O termo destacado exerce a função sintática de:
A) Adjunto Adnominal, pois modifica diretamente o substantivo "proposta" de forma permanente.
B) Objeto Direto, uma vez que completa o sentido do verbo transitivo direto "considerar".
C) Predicativo do Sujeito, caracterizando o estado do termo "O diretor".
D) Predicativo do Objeto, pois atribui uma característica temporária/opinião ao objeto direto "a proposta" por meio da ação verbal.
E) Adjunto Adverbial de modo, pois explica a maneira como o diretor considerou a proposta.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão exige a diferenciação entre Adjunto Adnominal e Predicativo do Objeto no âmbito da análise sintática.

- **A está incorreta:** O termo "inaceitável" não é um adjunto adnominal aqui. O adjunto adnominal fica junto do nome, caracterizando-o de forma inerente. Se fosse adjunto, a frase "O diretor considerou a proposta inaceitável" indicaria que a proposta já era conhecida como inaceitável antes do ato de considerar. Aqui, o termo é um atributo resultante do julgamento do verbo.
- **B está incorreta:** O objeto direto é "a proposta".
- **C está incorreta:** O adjetivo "inaceitável" não qualifica o sujeito "O diretor", e sim a "proposta".
- **D está correta:** O verbo "considerar" é um verbo transitivo predicativo. O termo "a proposta" é o Objeto Direto. O adjetivo "inaceitável" qualifica o objeto direto "a proposta" por intermédio do verbo (julgamento/opinião do sujeito sobre o objeto). Trata-se, portanto, de um **Predicativo do Objeto**. O predicado dessa oração é classificado como verbo-nominal.
- **E está incorreta:** "Inaceitável" é um adjetivo (atribui qualidade a um substantivo) e não um advérbio (que modificaria o verbo). A função é de predicativo.
</details>

---

### Questão 8 (FCC - 2021 - TRT 15ª Região - Técnico Judiciário)
Em relação aos elementos estruturais das palavras, assinale a opção em que a análise morfológica do termo sublinhado está INCORRETA:
A) Na palavra "canta**va**mos", o elemento em destaque é a desinência número-pessoal.
B) Na palavra "livr**o**s", a letra destacada é a desinência nominal de gênero.
C) Na palavra "estud**a**r", a letra destacada é a vogal temática verbal.
D) Na palavra "gato**s**", a letra destacada é a desinência nominal de número.
E) Na palavra "in**feliz**", a parte destacada é o radical da palavra.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão cobra a identificação correta dos morfemas (elementos estruturais das palavras) da língua portuguesa.

- **A está correta (análise correta):** Na forma verbal "cantávamos", a terminação "-mos" indica a 1ª pessoa do plural (nós). Trata-se da **desinência número-pessoal** (DNP). O elemento "-va-" é a desinência modo-temporal (DMT) que indica o pretérito imperfeito do indicativo.
- **B está incorreta (gabarito da questão):** Na palavra "livros", a vogal "o" não funciona como desinência de gênero, pois a palavra "livro" não sofre variação de gênero (não existe o feminino "livra"). A vogal "o", nesses casos de substantivos masculinos ou femininos fixos que não possuem oposição de sexo, é classificada como **vogal temática nominal** (VT). Sendo uma classificação incorreta, esta é a alternativa a ser assinalada.
- **C está correta (análise correta):** A vogal "a" em "estudar" caracteriza o verbo como pertencente à 1ª conjugação. É a **vogal temática verbal**.
- **D está correta (análise correta):** O morfema "s" indica a flexão de plural na palavra "gatos", sendo a **desinência nominal de número** (DNP).
- **E está correta (análise correta):** O vocábulo "infeliz" é formado pelo acréscimo do prefixo de negação "in-" ao termo principal "feliz", que carrega o significado lexical básico da palavra, ou seja, o **radical**.
</details>

---

### Questão 9 (FCC - 2022 - TRT 14ª Região - Analista Judiciário)
A palavra **empobrecer** é formada pelo seguinte processo de formação de palavras:
A) Derivação prefixal, devido à inclusão do prefixo "em-".
B) Derivação sufixal, devido à inclusão do sufixo "-ecer".
C) Derivação prefixal e sufixal, pois os afixos foram adicionados de maneira independente.
D) Derivação parassintética, visto que o prefixo "em-" e o sufixo "-ecer" foram anexados simultaneamente ao radical "pobre", sendo mutuamente dependentes.
E) Derivação regressiva, por ser uma redução do substantivo abstrato correspondente "pobreza".

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão aborda a diferença sutil entre Derivação Prefixal e Sufixal concomitante e a Derivação Parassintética.

- **A está incorreta:** A palavra não possui apenas o prefixo. O termo "pobrece" ou "pobrecer" não existe de forma isolada na língua portuguesa como verbo sem o prefixo.
- **B está incorreta:** A inclusão não é apenas de sufixo. Não existe a palavra "pobrecer" de forma independente.
- **C está incorreta:** Na derivação prefixal e sufixal, os afixos são independentes. Se você retirar um deles, a palavra restante continua existindo (ex: "infelizmente" -> se tirar "in-", sobra "felizmente", que existe; se tirar "-mente", sobra "infeliz", que também existe). Em "empobrecer", se tirarmos o prefixo "em-", a palavra "pobrecer" não existe. Se tirarmos o sufixo "-ecer", a palavra "empobre" também não existe.
- **D está correta:** A **parassíntese** (ou derivação parassintética) ocorre quando um prefixo e um sufixo são agregados *simultaneamente* ao radical de modo que a remoção de qualquer um deles gera uma palavra inexistente. É o caso de "em + pobre + ecer" = **empobrecer**.
- **E está incorreta:** A derivação regressiva gera substantivos a partir de verbos (ex: combater -> combate) e ocorre com redução da palavra, o oposto do que ocorre na criação do verbo "empobrecer".
</details>

---

### Questão 10 (FCC - 2018 - TRT 6ª Região - Analista Judiciário)
Os substantivos **choro** (do verbo chorar), **pesca** (do verbo pescar) e **portuga** (de português) são formados, respectivamente, pelos processos de derivação:
A) Parassintética, sufixal e imprópria.
B) Regressiva, regressiva e regressiva.
C) Regressiva, regressiva e imprópria.
D) Imprópria, imprópria e regressiva.
E) Regressiva, imprópria e imprópria.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

Esta questão cobra a identificação e os conceitos da Derivação Regressiva.

- **A está incorreta:** Nenhuma das palavras é parassintética.
- **B está correta:** 
  1. A **derivação regressiva** (ou deverbamento) ocorre quando uma palavra nova é criada por redução de outra já existente. É comum na formação de substantivos abstratos indicadores de ação (substantivos deverbais) a partir de verbos:
     - De "chorar" (verbo) retira-se a terminação verbal e acrescenta-se uma vogal temática nominal, gerando "**choro**".
     - De "pescar" (verbo) obtém-se "**pesca**".
  2. O substantivo "**portuga**" também é formado por redução da palavra "português", o que caracteriza o processo de derivação regressiva por corte silábico/abreviação informal popular.
- **C está incorreta:** "Portuga" não é derivação imprópria. Derivação imprópria é quando a classe gramatical muda sem alteração física na grafia da palavra original (ex: "O *jantar* estava ótimo" - onde o verbo jantar virou substantivo). "Portuga" sofreu alteração física (redução).
- **D está incorreta:** "Choro" e "pesca" sofreram alteração física (redução de morfemas verbais), logo são regressivos.
- **E está incorreta:** "Pesca" provém de "pescar", configurando derivação regressiva, e não imprópria.
</details>

---

### Questão 11 (FCC - 2023 - TRE SP - Técnico Judiciário)
Assinale a alternativa que apresenta duas palavras formadas por processos de **Composição**:
A) Girassol e Planalto.
B) Desalmado e Anoitecer.
C) Burocracia e Crueldade.
D) Desigualdade e Hidrelétrica.
E) Guarda-chuva e Lealdade.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A questão cobra a classificação dos processos de formação de palavras por Composição (Justaposição e Aglutinação).

- **A está correta:** 
  1. "**Girassol**" é uma palavra composta por **Justaposição** (Gira + Sol). Os dois radicais originais foram unidos sem sofrerem qualquer alteração fonética (o acréscimo da letra 's' é uma regra ortográfica meramente de pronúncia/fonética para manter o som sibilante, mas não há perda de fonemas das palavras originais).
  2. "**Planalto**" é uma palavra composta por **Aglutinação** (Plano + Alto). Na fusão dos radicais, houve alteração fonética com a perda da vogal 'o' de plano.
- **B está incorreta:** "Desalmado" (des + alma + ado) e "Anoitecer" (a + noite + ecer) são palavras formadas pelo processo de derivação parassintética, e não composição.
- **C está incorreta:** "Crueldade" é derivação sufixal (cruel + dade).
- **D está incorreta:** "Desigualdade" é derivação prefixal e sufixal (des + igual + dade).
- **E está incorreta:** "Lealdade" é derivação sufixal (leal + dade).
</details>

---

### Questão 12 (FCC - 2019 - TRF 4ª Região - Técnico Judiciário)
No caso da palavra **planalto**, ocorreu composição por aglutinação. O mesmo processo de formação (Composição por Aglutinação) é verificado em:
A) Passatempo.
B) Embora.
C) Pé-de-moleque.
D) Pontapé.
E) Saca-rolhas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: B**

A questão exige a identificação específica da Composição por Aglutinação, distinguindo-a da Composição por Justaposição.

- **A está incorreta:** "Passatempo" é formado por Justaposição (Passa + Tempo), pois ambos os radicais mantêm sua integridade fonética e ortográfica original.
- **B está correta:** A palavra "**embora**" é um exemplo clássico de composição por **Aglutinação**. Ela se origina da fusão histórica da expressão "em + boa + hora". Nesse processo, houve perda de fonemas e sílabas, alterando a grafia e a fonética dos termos originais que a compõem.
- **C está incorreta:** "Pé-de-moleque" é formado por Justaposição de três termos conectados por preposição, sem perda fonética de nenhuma das partes.
- **D está incorreta:** "Pontapé" é composto por Justaposição (Ponta + Pé), sem qualquer alteração fonética.
- **E está incorreta:** "Saca-rolhas" é composto por Justaposição (Saca + Rolhas).
</details>

---

### Questão 13 (FCC - 2018 - TRT 15ª Região - Técnico Judiciário)
Considere a frase abaixo:
"O **andar** dos servidores pelo fórum denotava preocupação com os prazos."
O processo de formação de palavras que justifica a classificação do termo destacado como substantivo é a:
A) Derivação sufixal.
B) Derivação parassintética.
C) Derivação regressiva.
D) Derivação imprópria.
E) Composição por aglutinação.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão cobra a identificação do processo de Derivação Imprópria (conversão de classe gramatical).

- **A está incorreta:** Não houve adição de sufixo no termo. O verbo "andar" foi mantido idêntico à sua forma original de infinitivo.
- **B está incorreta:** Não houve acréscimo de afixos parassintéticos.
- **C está incorreta:** Não houve redução da palavra (como em "cantar" -> "canto").
- **D está correta:** A **derivação imprópria** (ou conversão) ocorre quando uma palavra muda de classe gramatical devido ao contexto da frase, sem sofrer nenhuma alteração em sua estrutura de letras e fonemas. No caso de "O andar", o verbo "andar" foi substantivado pela presença antecedente do artigo definido "O", passando a atuar sintaticamente como o núcleo do sujeito da oração.
- **E está incorreta:** O processo não envolve junção de radicais, logo não é composição.
</details>

---

### Questão 14 (FCC - 2021 - TRT 11ª Região - Analista Judiciário)
As palavras **sociologia** e **televisão** são formadas, respectivamente, por:
A) Hibridismo e Hibridismo.
B) Composição por justaposição e derivação sufixal pura.
C) Derivação prefixal e composição por aglutinação.
D) Derivação sufixal e hibridismo.
E) Estruturas puras do latim arcaico sem afixos.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: A**

A questão cobra o entendimento de processos atípicos ou secundários de formação de palavras, com destaque para o Hibridismo.

- **A está correta:** 
  - O **Hibridismo** é o processo de formação de palavras em que se unem elementos de idiomas diferentes:
    1. "**Sociologia**" mescla o termo do latim *socio* (sociedade) com o termo grego *logia* (estudo).
    2. "**Televisão**" mescla o elemento grego *tele* (longe) com o termo latino *visão* (do verbo *videre*).
- **B está incorreta:** Ambos os termos contêm mesclas de diferentes idiomas clássicos na composição de seus radicais (Hibridismo).
- **C está incorreta:** A classificação não condiz com as origens de prefixos e processos de aglutinação fonética.
- **D está incorreta:** "Sociologia" é hibridismo e não derivação sufixal pura de radical português.
- **E está incorreta:** Os termos são compostos e formados por hibridismo com radicais gregos e latinos acoplados, não são palavras latinas arcaicas primitivas puras.
</details>

---

### Questão 15 (FCC - 2022 - TRT 4ª Região - Analista Judiciário)
Considere o período abaixo e a análise sintática de seus termos:
"Aprovado o projeto de lei de autoria do Tribunal, **enviaram-se as diretrizes aos assessores para análise**."
Em relação à oração destacada, assinale a afirmativa correta:
A) O termo "as diretrizes" atua como objeto direto da forma verbal "enviaram-se".
B) O termo "aos assessores" classifica-se como complemento nominal do adjetivo "enviaram".
C) A partícula "se" atua como índice de indeterminação do sujeito, tornando o sujeito da oração indeterminado.
D) O termo "as diretrizes" exerce a função de sujeito paciente, e o termo "aos assessores" funciona como objeto indireto.
E) O termo "para análise" é um adjunto adnominal que qualifica as diretrizes enviadas.

<details><summary>🔑 Ver Gabarito e Explicação</summary>

**Gabarito: D**

A questão avalia a capacidade de identificar funções sintáticas complexas em orações na voz passiva sintética contendo objeto indireto.

- **A está incorreta:** Na voz passiva sintética ("enviaram-se"), o termo que seria objeto direto na voz ativa assume o papel de **sujeito paciente**. Equivale a: "As diretrizes foram enviadas".
- **B está incorreta:** "Enviaram" é verbo (do verbo enviar), e não adjetivo. E "aos assessores" é complemento verbal (objeto indireto) de "enviaram", visto que quem envia, envia algo *a alguém*.
- **C está incorreta:** Como o verbo "enviar" é transitivo direto e indireto (VTDI), a partícula "se" associada a ele funciona como **partícula apassivadora** (PA), e não como índice de indeterminação. O sujeito é determinado ("as diretrizes").
- **D está correta:** 
  1. A oração está na voz passiva sintética introduzida pela partícula apassivadora "se". O termo "as diretrizes" (coisa enviada) é o **sujeito paciente** da oração (concordando em número com o verbo: "enviaram-se").
  2. O verbo enviar exige dois complementos: o que se envia (as diretrizes - que virou sujeito) e a quem se envia (aos assessores). O termo "aos assessores" é regido pela preposição "a", exercendo a função de **objeto indireto**.
- **E está incorreta:** O termo "para análise" indica a finalidade do envio (para que foram enviadas). Trata-se, portanto, de um **adjunto adverbial de finalidade** (ou oração reduzida de infinitivo se subentendido "para serem analisadas").
</details>
