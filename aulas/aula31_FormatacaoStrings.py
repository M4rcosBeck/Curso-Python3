# Formatação de Strings Básica

# A formatação de strings em Python permite controlar a aparência dos valores inseridos em uma string formatada. 
# Além de especificar o número de casas decimais, é possível alinhar o texto, definir largura mínima e preencher com caracteres específicos. 

# Alinhamento: 
# Utilizando <, >, ^ para alinhar o texto.

# <: Alinha o texto à esquerda.
# >: Alinha o texto à direita.
# ^: Alinha o texto ao centro.

# Largura mínima
# Define a largura mínima do campo em que o valor será inserido.

# Preenchimento
# Define o caractere de preenchimento para alcançar a largura mínima.

# Número de casas decimais
# Especifica o número de casas decimais para valores de ponto flutuante.

# Sinal de + ou -
# Controla a exibição do sinal de mais ou menos para números.

# Exemplo de formatação: {:<largura>.<casas_decimais>f}

valor = -100.1234
largura = 10
casas_decimais = 2

# Alinha à direita, largura mínima de 10 caracteres, 2 casas decimais
formatado = f"{valor:>{largura}.{casas_decimais}f}"
print(formatado)  # Saída: "   -100.12"

# Neste exemplo, o valor é alinhado à direita em um campo de 10 caracteres, com duas casas decimais exibidas. O sinal de menos é preservado e a largura mínima é preenchida com espaços.

# Outros exemplo:
print(50 * '-')

texto = 'TEXTO'
numero = 9999.000457265
hexadecimal = 225
print(f'->{texto: >10}<-')
print(f'->{texto: <10}<-')
print(f'->{texto: ^10}<-')
print(f'{numero:.2f}')
print(f'{numero:+.2f}')
print(f'{numero:-.2f}') # o - é o valor padrão
print(f'{numero*(-1):+.2f}') # adiciona o + caso o número for positivo
print(f'{numero*(-1):-.2f}')

print(f'{numero:0>+10.0f}') 
# O exemplo acima possui algumas características:
# Preenche de zeros até completar 10 casas. 
# O sinal conta como uma casa. 
# Na expressão, o sinal deve vir antes do número. 
# Na saída, o sinal sai depois dos zeros.

print(f'{numero:0>+15,.5f}') # adiciona uma vírgula para separar a milhar. 
print(f'{numero:0=+10.0f}') # Podemos fazer o sinal sair antes dos zeros trocando o sinal > por um sinal de =

print(f'O hexadecimal do número {hexadecimal} é correspondente à {hexadecimal:04x}')