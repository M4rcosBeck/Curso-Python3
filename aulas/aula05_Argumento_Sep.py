# O argumento nomeado 'sep' dentro da função 'print' em Python é utilizado para especificar o separador entre os diferentes argumentos passados para a função. O valor padrão do 'sep' é um espaço em branco. Ao fornecer um valor diferente para o 'sep', você pode controlar como os diferentes itens devem ser separados ao serem exibidos.

print('valor1', 'valor2', 'valor3', sep=' | ')

# Neste exemplo, o argumento 'sep' é configurado como ' | ', o que resulta em uma saída formatada com barras verticais como separadores entre os diferentes elementos. Isso pode ser útil para melhorar a legibilidade ou formatar a saída de acordo com as necessidades específicas do programa.

# O uso do argumento 'sep' oferece flexibilidade na formatação da saída da função 'print' e é especialmente útil ao combinar diferentes tipos de dados em uma única chamada à função.

print(12, 34, 56, sep='-')
print(78, 90, 0, sep=', ')