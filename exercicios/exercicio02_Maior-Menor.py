
# Exercício: Comparação de Valores

# Escreva um programa que solicite ao usuário que digite dois valores numéricos. 
# Em seguida, compare os valores digitados e informe se o primeiro valor é maior, menor ou igual ao segundo valor.
# Considere todos os tipos de números (inteiros, decimais, positivos e negativos).

# Dica: Use a estrutura condicional if/elif/else para comparar os valores e imprimir a mensagem apropriada.

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

valor1 = float(primeiro_valor)
valor2 = float(segundo_valor)

if(valor1 > valor2):
    print(f'O primeiro {valor1=:.2f} é maior que o segundo {valor2=:.2f}.')
elif(valor2 > valor1):
    print(f'O segundo {valor2=:.2f} é maior que o primeiro {valor1=:.2f}.')
elif(valor1 == valor2):
    print(f'Os dois valores são iguais.')
else:
    print('Não foi possível saber a diferença entre os valores')