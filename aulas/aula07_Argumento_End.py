# Em Python, o argumento 'end' na função 'print' é utilizado para especificar o que deve ser acrescentado ao final de cada chamada à função, além do padrão quebra de linha (\n). 
# Por padrão, 'print' adiciona uma quebra de linha ao final de cada chamada, movendo o cursor para a próxima linha.

# Sintaxe básica:
print('valor1', 'valor2', end='fim')
print('Alice tem 20 anos', end=' | ')

# Neste exemplo, o argumento end está configurado como ' | ', o que resulta em uma saída formatada onde o separador entre as chamadas à função 'print' é uma barra vertical (|). 
# Isso é útil para controlar a formatação da saída, evitando automaticamente a quebra de linha entre chamadas consecutivas.

# O uso do argumento 'end' permite personalizar a forma como o texto é exibido, sendo útil em situações em que se deseja uma formatação específica na saída padrão.

# Outros Exemplos:
print(12, 34, 56, end='\r\n') # mesmo que não apareça, este é o padrão.
print(12, 34, 56, end='\n') # mesmo que não apareça, este é o padrão.

# Adiciona a palavra 'fim' e quebra a linha.
print('valor1', 'valor2', end='fim\n')

#Quabra a linha e adiciona ## na próxima linha.
print('valor1', 'valor2', end='\n##') 
print('valor3', 'valor4', sep='-', end='\n')