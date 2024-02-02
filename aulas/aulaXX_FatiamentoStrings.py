# Fatiamento de strings
#  012345678
#  Olá Mundo
# -987654321
# Fatiamento [i:f:p] [::]
# Fatiamento [inicio:fim:passo]
# Obs.: a função len retorna a quantidade de caracteres da string

# aula 46

variavel = 'Olá Mundo'
print(variavel[0:len(variavel[0:9:2])])
print(variavel[0:len(variavel[::2])])