# FUNÇÃO input()

A função ```input()``` em Python é usada para receber entrada do usuário via teclado. Quando chamada, ela exibe uma mensagem opcional para o usuário e aguarda que o usuário insira algum texto pelo teclado, seguido pela tecla "Enter". A função ```input()``` então retorna o texto digitado pelo usuário como uma **string**.

<br>

A sintaxe básica da função ```input()``` é:
```
resposta = input("Mensagem para o usuário: ")
```

Onde ``` "Mensagem para o usuário" ``` é uma mensagem opcional que será exibida para o usuário, e ```resposta``` é a variável que armazenará a entrada fornecida pelo usuário.

<br>

Exemplo:
```
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

Neste exemplo, o programa exibe a mensagem ```"Digite seu nome:"```, o usuário digita seu nome e pressiona "Enter", e o nome digitado é armazenado na variável ```nome```. 

Em seguida, o programa imprime uma mensagem de boas-vindas com o nome do usuário.

<br>

## CONVERSÃO DE INPUTS
É importante observar que a entrada fornecida pelo usuário é sempre tratada como uma **string**, independentemente do que seja digitado. Se você precisar converter a entrada para outro tipo de dado, como um número inteiro ou ponto flutuante, é necessário fazer a conversão manualmente usando as funções ```int()``` ou ```float()```.

A importância de não utilizar conversão de tipos diretamente nas variáveis do input, sem tratar os dados digitados pelo usuário anteriormente reside na garantia da integridade e validade dos dados inseridos.

### Validação de entrada
Antes de converter os dados do input, é crucial validar se o formato da entrada corresponde ao esperado. Por exemplo, se você espera um número inteiro, deve verificar se o input consiste apenas em dígitos.

### Tratamento de erros
A conversão direta sem validação pode levar a erros inesperados se o usuário fornecer uma entrada inválida. Por exemplo, tentar converter uma string que não representa um número para um tipo numérico resultará em um erro.

### Experiência do usuário
Tratar os dados do input não só previne erros, mas também melhora a experiência do usuário. Fornecer mensagens de erro claras e orientações sobre o formato esperado da entrada ajuda o usuário a entender como fornecer os dados corretamente.

### Segurança
A entrada de dados do usuário pode ser uma porta de entrada para vulnerabilidades de segurança, como injeção de código. Validar e sanitizar os dados de entrada é essencial para proteger contra essas ameaças.

Portanto, é importante sempre validar e tratar os dados do input antes de converter seus tipos, garantindo assim a integridade, segurança e usabilidade do seu programa.

Um exemplo muito comum de se encontrar, mas que não deve ser encorajado é a seguinte expressão:
```
numero_digitado = int(input('Digite um número: ' ))
print(f'O número digitado é {numero_digitado}')
```

Observe que, apesar dessa expressão funcionar, ela pode quebrar o programa antes mesmo do desenvolvedor tratar o ```input()```.

Uma das formas para isso acontecer é o usuário digitar um **caracter** ao invés de um **digito numérico** no entrada de dados.
Como vimos, **caracteres** não podem ser convertidos em **números**. 

Uma forma correta de agir nesse caso é:
```
numero_digitado = input('Digite um número: ' )

# Realizar a tratativa da entrada dos dados, caso ele for um digito inteiro, realize a conversão.

numero_inteiro = int(numero_digitado)
print(f'O número digitado é {numero_inteiro}')
```

Dessa forma o desenvolvedor garante a possibilidade de fazer tratativas e checagens no input antes de converter qualquer valor.