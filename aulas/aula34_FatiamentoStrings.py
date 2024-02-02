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

# Fatiamento de Strings

# O fatiamento de strings em Python é uma técnica que permite extrair partes específicas de uma string, criando uma nova string a partir dessa extração. 

# Sintaxe:
# O fatiamento de strings é feito utilizando colchetes [] após a string, com a sintaxe [start:stop:step].
# start indica o índice de início da fatia (incluído na fatia).
# stop indica o índice de parada da fatia (excluído da fatia).
# step (opcional) indica o intervalo entre os elementos a serem incluídos na fatia.

# [i:f:p]
# [::]

# Exemplos Básicos:
# Para obter uma parte específica de uma string, basta especificar os índices de início e fim desejados.

frase = "Python é incrível"
parte = frase[7:9]  # Saída: "é"

# Índices negativos podem ser usados para contar a partir do final da string.

frase = "Python é incrível"
ultimas_letras = frase[-7:]  # Saída: "incrível"

# Intervalo Personalizado:
# O parâmetro step pode ser usado para especificar um intervalo personalizado entre os caracteres incluídos na fatia.

frase = "Python é incrível"
intervalo_personalizado = frase[::2]  # Saída: "Pto  nvl"

# String Original não é Modificada:
# É importante observar que o fatiamento de strings não modifica a string original, mas retorna uma nova string contendo a fatia desejada.
# O fatiamento de strings é uma técnica poderosa em Python, permitindo a extração eficiente de partes específicas de uma string com base em índices e intervalos especificados. 
# Essa funcionalidade é amplamente utilizada em tarefas de processamento de texto, manipulação de strings e análise de dados.

# Veja outros exeplos:

#        123456789
texto = 'Olá Mundo'
#        987654321-

print(texto[4:])        # Saída: "mundo"
print(texto[0:5])       # Saída: "Olá M"
print(texto[:5])        # Saída: "Olá M"
print(texto[-8:-2])     # Saída: "lá Mun"
print(texto[3])         # Saída: " "
print(texto[0:9:1])     # Saída: "Olá Mundo"
print(texto[0:9:2])     # Saída: "OáMuo"
print(texto[0:9:3])     # Saída: "O o"
print(texto[0:9:4])     # Saída: "OMo"
print(texto[::-1])      # Saída: "odnuM álO"
print(texto[0:9:-1])    # Saída: ""
print(texto[-1:-10:-1]) # Saída: "odnuM álO"
print(texto[-1:-10:-2]) # Saída: "onMáO"
