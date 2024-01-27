# CARACTER DE ESCAPE

# Caracteres de escape são sequências especiais de caracteres que começam com uma barra invertida (\). Eles são utilizados dentro de strings para representar caracteres especiais ou codificados de forma especial, que de outra forma poderiam ser interpretados de maneira diferente pela linguagem. Alguns dos caracteres de escape mais comuns em Python incluem:

# \n: Representa uma quebra de linha (newline).
# \t: Representa um tabulação horizontal (tab).
# \\: Representa uma barra invertida literal.
# \' e \": Representam aspas simples e duplas, respectivamente, dentro de strings delimitadas por aspas do mesmo tipo.
# \xHH: Representa um caractere ASCII específico, onde HH são dígitos hexadecimais.

# Exemplo de uso de caracteres de escape em Python:

print('Olá, \nMundo!')          # quebra de linha
print('Python\té\tincrível!')   # tabulação horizontal
print('Eu disse \'Olá\'!')      # aspas simples dentro de aspas simples
print("Eu disse \"Olá\"!")      # aspas duplas dentro de aspas duplas
print(1, '"Primeiro Nome"')     # vários argumentos

# Barra invertida literalmente
print('Caminho do arquivo: C:\\users\\python\\arquivo.txt')

# Caracter Hexadecimal
print('O naipes do baralho são: \x03 \x04 \x05 \x06')

# Os caracteres de escape são úteis para representar caracteres especiais ou realizar formatação específica dentro de strings, tornando-as mais flexíveis e versáteis. Eles são amplamente utilizados em situações onde é necessário controlar a formatação ou a aparência do texto exibido.