# 🐍 30 Exercícios de Python para Praticar

Este arquivo contém 30 desafios de programação em Python, divididos por tópicos, para ajudar você a praticar e consolidar seus conhecimentos.

## 1. Fundamentos e Variáveis (Nível Júnior)

| # | Tópico | Enunciado |
|---|---|---|
| **1** | Variáveis e Tipos | Crie duas variáveis, `nome` (string) e `idade` (inteiro), e imprima uma frase que as utilize. |
| **2** | Entrada e Saída | Peça ao usuário para digitar um número e, em seguida, imprima o dobro desse número. |
| **3** | Operadores Aritméticos | Calcule a área de um círculo. Peça o raio ao usuário e use $\pi \approx 3.14159$. |
| **4** | Conversão de Tipo | Crie uma variável que armazena um valor de temperatura em Celsius. Converta-a para Fahrenheit: $F = C \times 1.8 + 32$. |
| **5** | Operadores Lógicos | Crie duas variáveis booleanas, `chove` e `sol`. Imprima o resultado de `chove AND NOT sol`. |

## 2. Estruturas de Controle (Nível Júnior/Pleno)

| # | Tópico | Enunciado |
|---|---|---|
| **6** | Condicional `if/elif/else` | Peça um número ao usuário. Classifique-o como "Positivo", "Negativo" ou "Zero". |
| **7** | Laço `for` (Intervalo) | Imprima todos os números pares de 1 a 20 usando um loop `for` e a função `range()`. |
| **8** | Laço `while` | Peça ao usuário para digitar números continuamente. O loop deve parar quando o usuário digitar o número 0. |
| **9** | Comparação de Strings | Peça ao usuário uma senha. Se a senha for "python123", imprima "Acesso concedido", caso contrário, "Senha incorreta". |
| **10** | Controle de Fluxo | Crie um loop que percorra números de 1 a 10. Se o número for 5, use `break` para sair do loop. |

## 3. Listas e Tuplas (Nível Pleno)

| # | Tópico | Enunciado |
|---|---|---|
| **11** | Criação e Acesso | Crie uma lista com 5 nomes de frutas. Imprima o primeiro e o último nome. |
| **12** | Modificação e Adição | Comece com uma lista vazia. Peça ao usuário 3 nomes de cidades e adicione-os à lista. Imprima a lista final. |
| **13** | Iteração em Lista | Dada a lista `numeros = [1, 5, 8, 12, 3]`, calcule e imprima a soma de todos os seus elementos. |
| **14** | Máximo e Mínimo | Dada uma lista de notas, encontre e imprima a nota mais alta. |
| **15** | Tuplas | Crie uma tupla chamada `ponto` com as coordenadas $(x, y)$. Desempacote a tupla em duas variáveis e imprima seus valores. |

## 4. Dicionários e Conjuntos (Nível Pleno)

| # | Tópico | Enunciado |
|---|---|---|
| **16** | Criação de Dicionário | Crie um dicionário para representar uma pessoa com chaves: `nome`, `idade` e `cidade`. Imprima a idade. |
| **17** | Iteração em Dicionário | Percorra o dicionário do exercício 16 e imprima todas as **chaves** e seus respectivos **valores**. |
| **18** | Adição e Remoção | Crie um dicionário vazio chamado `estoque`. Adicione 3 itens (chave: produto, valor: quantidade) e remova um deles. |
| **19** | Conjuntos (Sets) | Dadas duas listas: `a = [1, 2, 3, 4]` e `b = [3, 4, 5, 6]`. Use conjuntos para encontrar e imprimir os elementos em **comum** entre elas. |
| **20** | Contagem de Palavras | Dada a string: "banana maçã banana laranja", conte quantas vezes a palavra "banana" aparece. Use um dicionário para a contagem. |

## 5. Funções (Nível Pleno)

| # | Tópico | Enunciado |
|---|---|---|
| **21** | Função Simples | Escreva uma função chamada `saudacao` que receba um nome como argumento e imprima "Olá, [nome]!". |
| **22** | Função com Retorno | Escreva uma função chamada `calcular_media` que receba 3 números e retorne a média aritmética deles. |
| **23** | Argumentos Padrão | Crie uma função chamada `potencia` que receba dois números, `base` e `expoente`, e retorne o resultado. Defina `expoente` como 2 por padrão. |
| **24** | Docstrings | Crie uma função simples e adicione um `docstring` descrevendo o que ela faz, seus parâmetros e o que ela retorna. |
| **25** | Funções e Listas | Crie uma função que receba uma lista de números e retorne o maior número da lista. |

## 6. Lógica e Desafios (Nível Pleno/Sênior)

| # | Tópico | Enunciado |
|---|---|---|
| **26** | Fatorial | Escreva uma função que calcule e retorne o fatorial de um número inteiro positivo dado (ex: $4! = 4 \times 3 \times 2 \times 1$). |
| **27** | Palíndromo | Escreva uma função que receba uma string e retorne `True` se ela for um palíndromo (lida igual de trás para frente) e `False` caso contrário. Ignore maiúsculas/minúsculas. |
| **28** | Números Primos | Escreva uma função que determine se um número é primo (divisível apenas por 1 e por ele mesmo). |
| **29** | List Comprehensions | Dada a lista `numeros = [1, 2, 3, 4, 5, 6]`, use *List Comprehension* para criar uma nova lista contendo apenas o quadrado dos números pares. |
| **30** | Gerador de Senhas | Crie uma função que gere uma senha aleatória de 8 caracteres, contendo pelo menos letras minúsculas, maiúsculas e números. Você pode precisar da biblioteca `random`. |

---
---

## 🚀 Como usar

1. **Crie um novo arquivo:** Salve o código de cada exercício em um arquivo Python separado (ex: `ex1.py`, `ex2.py`).
2. **Implemente a solução:** Escreva o código Python necessário para resolver o enunciado.
3. **Execute e Teste:** Execute o arquivo para verificar se a saída está correta.
4. **Refatore:** Tente otimizar seu código ou encontrar uma maneira mais "pythônica" de resolver o problema.