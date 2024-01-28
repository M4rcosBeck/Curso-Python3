# STRING BRUTA (RAW)

# Quando uma string é prefixada com r, ela é tratada como uma "string bruta" ou "raw", na qual os caracteres de escape (como \n, \t, etc.) não são interpretados.

# Isso significa que os caracteres precedidos por uma barra invertida (\) dentro da string bruta são tratados literalmente, em vez de serem interpretados como sequências de escape.
# Portanto, os caracteres de escape são considerados parte do texto da string, e não como instruções para a linguagem Python.

print(r"C:\users\python\arquivo.txt")

# Neste exemplo, a string bruta r"C:\users\python\arquivo.txt" será impressa como está, incluindo as barras invertidas (\), que normalmente seriam interpretadas como caracteres de escape se não fosse pela formatação bruta. 
# Isso é útil quando se está lidando com caminhos de arquivos em sistemas Windows, por exemplo, onde as barras invertidas são comuns e não devem ser interpretadas como caracteres de escape.