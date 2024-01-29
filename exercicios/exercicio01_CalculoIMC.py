# Exercício 01 de Python: Cálculo de IMC simples

# Escreva um programa em Python que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
# O IMC é uma medida que relaciona o peso e a altura de uma pessoa, e é comumente utilizado para avaliar se uma pessoa está dentro do peso considerado saudável.

# IMC = peso / altura²

# Depois de calcular o IMC, o programa deve exibir uma mensagem indicando o IMC calculado.

nome = 'Marcos'
altura = 1.74
peso = 75

imc = peso / altura ** 2
print(nome, 'tem', altura, 'de altura, pesa', peso, 'e seu IMC é de', imc)

# Também é possível realizar a conta diretamente através da função print.
print(nome, 'tem', altura, 'de altura, pesa', peso, 'e seu IMC é de', peso / (altura*altura))