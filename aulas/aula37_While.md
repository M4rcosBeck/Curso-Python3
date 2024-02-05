# While
O `while` é uma estrutura de controle de fluxo que permite executar repetidamente um bloco de código enquanto uma condição específica permanecer verdadeira.

Sintaxe:
```
while condição:
    # Bloco de código a ser repetido enquanto a condição for verdadeira
```

## Execução Repetida
O bloco de código dentro do `while` é executado repetidamente enquanto a condição especificada for verdadeira.
A condição é verificada antes de cada iteração do loop. Se a condição for falsa, a execução do loop é interrompida e o controle passa para a próxima instrução após o bloco while.

## Controle de Loop
Dentro do bloco de código do `while`, é importante garantir que a condição eventualmente se torne falsa para evitar loops infinitos.
Você pode usar instruções como `break` para sair do loop prematuramente ou `continue` para pular a iteração atual e continuar com a próxima.

## Aplicações Comuns
O `while` é frequentemente usado quando o número de iterações não é conhecido antecipadamente e depende de alguma condição dinâmica.
É útil para implementar lógica de repetição baseada em eventos, validação de entrada do usuário, processamento de dados em tempo real, entre outros.

## Exemplo
```
# IMPRIME O CONTADOR ATÉ QUE ELE SEJA <= 5

contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

```
# SOLICITA UM NOME ATÉ QUE 'sair' SEJA DIGITADO

while True:
    nome = input("Digite um nome ou 'sair' para finalizar: ")
    if(nome == 'sair'):
        break
    print(nome)
```

```
# IMPRIME SOMENTE NÚMEROS PARES

contador = 0
while contador < 5:
    contador += 1
    # Verifica se o contador é par
    if contador % 2 == 0:
        continue  # Pula para a próxima iteração se o número for par
    print(contador)
```

O `while` é uma ferramenta poderosa para controlar o fluxo de execução, permitindo a repetição de um bloco de código enquanto uma condição específica for verdadeira. No entanto, é importante ter cuidado para evitar loops infinitos garantindo que a condição do `while` eventualmente se torne falsa.