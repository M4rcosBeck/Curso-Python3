# PRECEDÊNCIA DE OPERADORES

# A precedência dos operadores determina a ordem em que as operações são realizadas em uma expressão. 
# Isso significa que certos operadores têm prioridade sobre outros e são avaliados primeiro.

# Aqui está um resumo da precedência dos operadores, da mais alta para a mais baixa:

# Parênteses (): São utilizados para agrupar partes de uma expressão e têm a maior precedência. As expressões dentro dos parênteses são avaliadas primeiro.
# Exponenciação **: O operador de exponenciação tem a segunda maior precedência e é usado para calcular uma base elevada a uma potência.
# Multiplicação *, Divisão /, Divisão Inteira //, Módulo %: Esses operadores têm a terceira maior precedência e são avaliados antes da adição e subtração.
# Adição +, Subtração -: São operadores de menor precedência e são avaliados por último, após a multiplicação, divisão e outros operadores de maior precedência.

# É importante lembrar que, quando há operadores com a mesma precedência em uma expressão, a avaliação é feita da esquerda para a direita. 
# No entanto, você pode alterar a ordem de avaliação usando parênteses para garantir que as operações sejam realizadas na ordem desejada.

resultado = 5 + 2 * 3  # Multiplicação é avaliada primeiro: 5 + 6 = 11
print(resultado)

# Mas:
resultado = (5 + 2) * 3  # Adição é avaliada primeiro: 7 * 3 = 21
print(resultado)

# Compreender a precedência dos operadores é fundamental para escrever expressões matemáticas e lógicas corretas em Python e garantir que seu código produza os resultados esperados.