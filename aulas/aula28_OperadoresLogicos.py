# OPERADORES LÓGICOS and/or/not
# e/ou/não

# Operadores lógicos são utilizados para combinar múltiplas expressões lógicas e produzir um resultado lógico. 

# AND
# O operador and retorna True se todas as expressões lógicas forem True.
x = 5
resultado = (x > 0) and (x < 10)  # Resultado é True
print(f'{x} é menor que 0 e menor que 10? {resultado}')

# OR
# O operador or retorna True se pelo menos uma das expressões lógicas for True.
x = 15
resultado = (x < 0) or (x > 10)  # Resultado é True
print(f'{x} é menor que 0 ou maior que 10? {resultado}')

# NOT
# O operador not inverte o valor de uma expressão lógica.
x = 5
resultado = not (x > 10)  # Resultado é True
print(f'{x} é maior que 10? {resultado}')

# Esses operadores lógicos são frequentemente usados em combinação com as estruturas condicionais if/elif/else para controlar o fluxo do programa com base em múltiplas condições.
# Eles ajudam a criar expressões lógicas complexas e permitem que os programadores criem lógica condicional sofisticada em seus programas Python.