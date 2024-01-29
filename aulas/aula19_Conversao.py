# CONVERSÃO DE TIPOS DE DADOS

# Em Python, existem três tipos de conversão de dados: type conversion, typecasting e coercion. 
# Todos são termos que se referem à conversão de um tipo de dado para outro. 
# Embora todos tenham o mesmo objetivo de alterar o tipo de dado de uma variável, existem algumas diferenças sutis entre eles:

# Type Conversion (Conversão de Tipo) 
# É o processo de converter um tipo de dado em outro explicitamente. 
# Isso pode ser feito usando funções ou construtores específicos para o tipo desejado.

# Exemplo:
numero_inteiro = 10
numero_decimal = float(numero_inteiro)  # Conversão de int para float

# Typecasting (Conversão de Tipo) 
# É semelhante à conversão de tipo, mas geralmente é usado para converter um tipo de dado em outro diretamente, sem a necessidade de chamar uma função específica. 
# Em Python, isso geralmente envolve a atribuição de um valor de um tipo a uma variável de outro tipo.

#Exemplo:
numero_inteiro = 10
numero_decimal = 10.5
numero_inteiro = int(numero_decimal)  # Typecasting de float para int

#Coercion (Coerção)
# Refere-se à conversão automática de tipos de dados em expressões ou operações. 
# Em Python, a coerção ocorre implicitamente em algumas situações, como em operações aritméticas ou comparações entre tipos diferentes.

#Exemplo:
numero_inteiro = 10
numero_decimal = 10.5
resultado = numero_inteiro + numero_decimal  # Coerção de int para float

# Em resumo, type conversion, typecasting e coercion são técnicas utilizadas em Python para modificar o tipo de dado de uma variável. 
# A escolha entre elas depende do contexto e das necessidades específicas do programa. 
# É importante entender esses conceitos para garantir o comportamento correto e esperado em suas operações de conversão de tipos de dados.

# ver a aula 22 do curso para completar essa aula.