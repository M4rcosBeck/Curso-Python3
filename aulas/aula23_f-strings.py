# INTRODUÇÃO A FORMATAÇÃO F-STRINGS

# F-strings em Python são uma forma moderna e conveniente de formatar strings de maneira dinâmica, introduzidas na versão 3.6 da linguagem. 
# Com f-strings, é possível incorporar valores de variáveis e expressões diretamente em strings de forma mais legível e concisa.

# Para criar uma f-string, você adiciona um f ou F antes das aspas que delimitam a string e incorpora variáveis ou expressões entre chaves {} dentro da string. 
# Durante a execução, as expressões dentro das chaves são avaliadas e os resultados são inseridos na string.

nome = "João"
idade = 25

mensagem = f'Olá, meu nome é {nome} e tenho {idade} anos.'
print(mensagem) # Saída: Olá, meu nome é João e tenho 25 anos.

# ---

# É possível controlar o número de casas decimais exibidas em valores de ponto flutuante usando especificadores de formato. 
# Para formatar casas decimais em uma f-string, você pode adicionar um ponto seguido pelo número de casas decimais desejado após o nome da variável ou expressão dentro das chaves {}.

valor = 123.456789
mensagem = f'O valor é: {valor:.2f}'
print(mensagem) # Saída: O valor é: 123.46

# Neste exemplo, :.2f indica que queremos exibir valor com duas casas decimais.
# Você pode ajustar o número de casas decimais conforme necessário, alterando o número após o ponto. 
# Isso oferece flexibilidade para formatar valores de ponto flutuante de acordo com os requisitos específicos do seu programa.

# ---

# Também é possível formatar casas decimais com vírgulas, como por exemplo, para valores monetários.

valor = 1234.5678
mensagem = f"O total da compra é: R${valor:,.2f}"
print(mensagem) # Saída: O total da compra é: R$1,234.57

# Neste exemplo, :,.2f é usado para formatar o valor com duas casas decimais e adicionará uma vírgula conforme as casas decimais.
# Além disso, adicionamos o símbolo "R$" antes do valor para indicar que se trata de uma quantia em reais.

# ---

# As f-strings são uma maneira eficaz de formatar strings em Python, tornando o código mais legível e fácil de escrever. 
# Elas são especialmente úteis quando você precisa incorporar valores de variáveis ou expressões em strings de forma dinâmica.