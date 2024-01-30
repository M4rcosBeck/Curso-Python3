# VARIÁVEIS

# Variáveis em Python são utilizadas para armazenar e manipular dados. 
# Cada variável possui um nome único que serve como uma referência para o valor que ela contém. 
# O operador de atribuição (=) é utilizado para associar um valor a uma variável. 


# A sintaxe básica para definir uma variável em Python é:
# nome_da_variavel = valor

# Onde 'nome_da_variavel' é o identificador da variável e 'valor' é o dado que será armazenado nela. 

# Por exemplo:
idade = 25
nome = "Maria"

# Para imprimir os valores armazenados em variáveis, basta passá-las como argumentos para a função print(). 
# Por exemplo:

print(idade)                            # Saída: 25
print(nome)                             # Saída: Maria

# Você pode imprimir múltiplas variáveis separadas por vírgula. 
# Lembre que, por padrão, o print() possui o 'sep' como 'espaço', então não é preciso criar espaço entre os valores.

print("A idade é:", idade)              # Saída: A idade é: 25
print("O nome é:", nome)                # Saída: O nome é: Maria
print(nome, "tem", idade, "anos")       # Saída: Maria tem 25 anos.

# Outros exemplos com expressões:
soma = 2 + 2
print("A soma é:", soma)               # A soma é 4    

# As variáveis desempenham um papel fundamental na minimização da repetição de código.
# Ao armazenar valores em variáveis, você pode reutilizá-los em diferentes partes do seu código sem precisar digitá-los novamente. 
# Isso reduz a duplicação de código e torna o código mais conciso e fácil de manter.
# Se um valor precisa ser alterado em várias partes do seu código, você só precisa atualizá-lo uma vez, atribuindo o novo valor à variável. 
# Isso evita erros decorrentes de atualizações inconsistentes e simplifica o processo de manutenção do código.

# ---
# A PEP8 é um guia de estilo para código Python, que define recomendações sobre a formatação e organização do código-fonte. 
# Embora não seja estritamente necessário seguir a PEP8, aderir a suas diretrizes pode tornar seu código mais legível e consistente. 
# Isso inclui recomendações sobre o uso de espaços em branco, indentação, nomes de variáveis, comentários e outras práticas de codificação.
# ---