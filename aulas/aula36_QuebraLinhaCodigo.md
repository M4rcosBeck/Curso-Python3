# Quebra de Linha de Código

Em Python, uma linha de código pode ser quebrada em várias linhas físicas usando uma barra invertida (\\) no final da linha para indicar que a instrução continua na próxima linha. Isso é útil para melhorar a legibilidade do código, especialmente em instruções longas que podem se estender além da largura da tela. Por exemplo:

```
resultado = valor1 + valor2 + \
            valor3 + valor4
```

Neste exemplo, a adição dos valores está quebrada em duas linhas físicas para facilitar a leitura. O interpretador Python reconhece que a instrução continua na próxima linha por causa da barra invertida no final da primeira linha. Essa técnica é conhecida como "quebra de linha" ou "continuação de linha". É importante observar que o espaço em branco após a barra invertida é ignorado pelo interpretador Python, permitindo uma formatação mais limpa do código.