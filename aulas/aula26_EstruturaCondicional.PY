# Estrutura Condicional if/ elif / else 
# (se / se não se / se não)

# A estrutura condicional if/elif/else em Python é usada para tomar decisões com base em condições. 
# Ela permite que um programa execute diferentes blocos de código dependendo se uma ou mais condições são verdadeiras ou falsas.

# A estrutura básica da declaração if/elif/else é a seguinte:

"""

if condição1:
    bloco de código a ser executado se condição1 for verdadeira
elif condição2:
    bloco de código a ser executado se condição1 for falsa e condição2 for verdadeira
else:
    bloco de código a ser executado se todas as condições anteriores forem falsas
    
"""

# A estrutura sempre começa com um bloco if, seguido opcionalmente por zero ou mais blocos elif e um bloco else opcional. 
# Aqui está um resumo completo:

# if
# A estrutura sempre começa com um bloco if e é seguida por uma condição a ser avaliada. 
# Ele verifica uma condição e executa um bloco de código se a condição for verdadeira. 
# Se a condição for falsa, o programa passa para a próxima condição na estrutura ou sai dela se não houver mais elif ou else.

# elif (opcional)
# elif é a abreviação de "else if".
# O bloco elif é usado para verificar condições adicionais se a condição do bloco if for falsa.
# Pode haver zero ou mais blocos elif na estrutura. 
# Cada bloco elif verifica uma nova condição e executa um bloco de código correspondente se a condição for verdadeira.

# else (opcional)
# O bloco else é executado se nenhuma das condições anteriores for verdadeira. 
# Ele serve como um bloco de "último recurso" e não possui uma condição associada.
# Pode haver no máximo um bloco else na estrutura.


# Exemplo:
idade = 18

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Acabou de fazer 18 anos")
else:
    print("Maior de idade")

# Neste exemplo, o programa verifica a idade e imprime uma mensagem dependendo da faixa etária. 
# Se a idade for menor que 18, imprime "Menor de idade". 
# Se a idade for igual a 18, imprime "Acabou de fazer 18 anos". 
# Caso contrário, imprime "Maior de idade".
