# Exercício xx de Python: Calculadora de IMC

# Escreva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
# O IMC é uma medida que relaciona o peso e a altura de uma pessoa, e é comumente utilizado para avaliar se uma pessoa está dentro do peso considerado saudável.
# O programa deve solicitar ao usuário que insira seu peso em quilogramas e sua altura em metros. 

# IMC = peso / altura²

# Depois de calcular o IMC, o programa deve exibir uma mensagem indicando o IMC calculado e a faixa de classificação de acordo com a tabela a seguir:

# Abaixo de 18.5: Abaixo do peso
# 18.5 a 24.9: Peso normal
# 25.0 a 29.9: Sobrepeso
# 30.0 ou mais: Obesidade

nome = input('Digite seu nome: ')
altura = input('Digite sua altura em metros: ')
peso = input('Digite o seu peso em kg: ')

altura = float(altura)
peso = float(peso)

imc = peso / altura ** 2
print(f'{nome} tem {altura}m de altura, pesa {peso} e seu IMC é de {imc:.2f}')
      
if(imc < 18.5):
    print('Você está abaixo do peso!')
elif(imc > 18.5 and imc < 24.9):
    print('Você está dentro do peso normal!')
elif(imc > 25.0 and imc < 29.9):
    print('Você está com sobrepeso!')
elif(imc > 30.0):
    print('Você está com obesidade!')
else:
    print('Não foi possível calcular a faixa do seu IMC!')