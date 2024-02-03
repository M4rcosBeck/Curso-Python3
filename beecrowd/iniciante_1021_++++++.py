# Notas e Moedas

'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Exemplo:
Entrada: 576.73

Saída:
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01

DICA: o segredo desse exercício é converter a valor de ponto flutuante para inteiro. Como se trata de um valor monetário, basta multiplicado o valor inserido por 100 (centavos). Divisão de ponto flutuante pode causar imprecisões devido à forma como os números de ponto flutuante são apresentados em computadores. Devido à imprecisão de números de ponto flutuante, em algumas divisões, o resultado pode ser arredondado para baixo, causando na final do programa alguns resultados de 0 onde deveriam ser 1.

DESMISTIFICANDO: Executar esse exerício sem a conversão para centavos daria um erro quando um valor que resultasse em uma quantidade de centavos menor do que 1 fosse inserido. Isso aconteceria em casos em que o valor após a conversão para centavos não seria um número inteiro. Por exemplo, se você inserisse o valor 0.01, que representa 1 centavo, após a conversão para centavos (multiplicando por 100), o resultado seria 1.0, que é um número de ponto flutuante. Quando você tenta calcular a quantidade de moedas de 1 centavo usando valor // 1, o resultado seria 1.0, mas você espera um número inteiro.

valor1 = 1.0
valor2 = 1


print(f'{valor1 // 1}')
print(f'{valor1 // 1}')

print(f'{valor2 // 1}')
print(f'{valor2 // 1.0}')
'''

# SOULUÇÃO:
valor = float(input()) * 100

print('NOTAS:')
print(f'{valor // 10000:.0f} nota(s) de R$ 100.00')
valor = valor % 10000

print(f'{valor // 5000:.0f} nota(s) de R$ 50.00')
valor = valor % 5000

print(f'{valor // 2000:.0f} nota(s) de R$ 20.00')
valor = valor % 2000

print(f'{valor // 1000:.0f} nota(s) de R$ 10.00')
valor = valor % 1000

print(f'{valor // 500:.0f} nota(s) de R$ 5.00')
valor = valor % 500

print(f'{valor // 200:.0f} nota(s) de R$ 2.00')
valor = valor % 200

print('MOEDAS:')
print(f'{valor // 100:.0f} moeda(s) de R$ 1.00')
valor = valor % 100

print(f'{valor // 50:.0f} moeda(s) de R$ 0.50')
valor = valor % 50

print(f'{valor // 25:.0f} moeda(s) de R$ 0.25')
valor = valor % 25

print(f'{valor // 10:.0f} moeda(s) de R$ 0.10')
valor = valor % 10

print(f'{valor // 5:.0f} moeda(s) de R$ 0.05')
valor = valor % 5

print(f'{valor:.0f} moeda(s) de R$ 0.01')