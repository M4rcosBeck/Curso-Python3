# Interpolação Básica de Strings

# A interpolação de strings refere-se ao processo de incorporar valores de variáveis ou expressões dentro de uma string, permitindo a criação de strings formatadas de maneira dinâmica. 
# Existem várias maneiras de realizar interpolação de strings em Python, algumas das quais incluem:

# Uso do operador %
# Esse método utiliza o operador % seguido de uma letra representativa do tipo de variável para inserir valores em uma string formatada.
# %s - string
# %d - int
# %i - int
# %f - float
# %x - hexadecimal (0123456789abcdef)
# %X - hexadecimal (0123456789ABCDEF)
# Os valores a serem inseridos são passados como uma tupla após a string formatada.

nome = 'João'
idade = 30
print('Olá, %s! Você tem %d anos.' % (nome, idade))

# Também é possível controlar o número de casas decimais adicionando um ponto seguido pelo número de casas decimais desejado, após o operador %.

produto = 'arroz'
preco = 19.9
print('O %s está na promoção custando apenas R$%.2f' % (produto, preco))

# Também é possível converter valores inteiros em valores haxadecimais.

digito = 150
print('O valor hexadecimal correspondente ao valor %d é %x' % (digito, digito))

# Por convenção, valores hexadecimais possuem 4 casas decimais, então podemos controlar as casas decimais adicionando um 0 (zero) seguido pelo número de casas desejadas após o operador %.

digito = 150
print('O valor hexadecimal correspondente ao valor %d é %04x' % (digito, digito))

# F-strings (strings formatadas)
# Introduzido a partir do Python 3.6, f-strings oferecem uma maneira mais simples e legível de realizar interpolação de strings. 
# Elas permitem a inserção direta de expressões Python dentro de strings prefixadas com f ou F como vimos na aula 23.

nome = 'Ana'
idade = 35
print(f'Olá, {nome}! Você tem {idade} anos.')

# Essas são apenas algumas das maneiras de realizar interpolação de strings em Python. 
# Cada método tem suas próprias vantagens e é importante escolher o método mais adequado para a situação específica em que está trabalhando. 
# Interpolação de strings é uma técnica poderosa que torna a formatação de strings dinâmicas e personalizadas muito mais conveniente e legível.