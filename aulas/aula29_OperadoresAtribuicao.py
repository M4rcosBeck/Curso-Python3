# Operadores de Atribuição

# Os operadores de atribuição são utilizados para atribuir valores a variáveis. 
# Eles permitem que você atualize o valor de uma variável de forma rápida e conveniente. 

# Operador de Atribuição Simples (=)
# O operador de atribuição simples (=) é usado para atribuir um valor a uma variável.

a, b, c, d, e, f, g = 5, 5, 5, 5, 5, 5, 5

# Operadores de Atribuição Combinados
# Esses operadores combinam a operação de atribuição com uma operação aritmética. 
# Eles permitem atualizar o valor de uma variável em uma única linha.

# +=: Adição e atribuição
# -=: Subtração e atribuição
# *=: Multiplicação e atribuição
# /=: Divisão e atribuição
# %=: Módulo e atribuição
# //=: Divisão inteira e atribuição
# **=: Exponenciação e atribuição

a += 2   # Equivalente a x = x + 2  Saída: 7
print(a)
b -= 2   # Equivalente a x = x - 2  Saída: 3
print(b)
c *= 2   # Equivalente a x = x * 2  Saída: 10
print(c)
d /= 2   # Equivalente a x = x / 2  Saída: 2.5
print(d)
e %= 2   # Equivalente a x = x % 2  Saída: 1
print(e)
f //= 2  # Equivalente a x = x // 2 Saída: 2
print(f)
g **= 2  # Equivalente a x = x ** 2 Saída: 25
print(g)


# Operador de Atribuição Múltipla
# Python permite atribuir valores a múltiplas variáveis em uma única instrução de atribuição.

a, b, c = 1, 2, 3
print(a, b, c)

# CUIDADO
# É importante entender a diferença entre os operadores de atribuição combinados, como +=, e a combinação do operador de atribuição com o operador unário, como =+.

# Operadores de Atribuição Combinados
# Os operadores de atribuição combinados realizam uma operação aritmética e uma atribuição em uma única expressão, como vimos acima.
# Por exemplo, += realiza uma adição do valor à direita com o valor da variável à esquerda e atribui o resultado de volta à variável à esquerda.
# Exemplo: x += 5 é equivalente a x = x + 5.

# Operador de Atribuição com Operador Unário
# Quando o operador de atribuição é combinado com um operador unário, como =+, o operador unário é aplicado ao valor à direita e atribuído à variável à esquerda.
# Exemplo: x =+ 5 é equivalente a x = +5, onde +5 é simplesmente o número 5 com um sinal de mais, então o valor 5 é atribuído à variável x.

# Em resumo, a posição do operador faz uma diferença significativa no comportamento da expressão em Python. 
# Os operadores de atribuição combinados realizam operações aritméticas com a variável à esquerda, enquanto a combinação do operador de atribuição com um operador unário aplica o operador unário ao valor à direita e atribui o resultado à variável à esquerda.