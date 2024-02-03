
# Flags

As flags, como ```None```, ```is``` e ```is not```, são utilizadas para operações de comparação e identidade entre objetos. 

## None
**None** é um objeto *singleton* que representa a ausência de valor ou a falta de qualquer valor significativo.
É comumente usado para inicializar variáveis quando ainda não têm um valor válido ou como um valor de retorno para indicar que uma função não produziu um resultado.

x = None
if x is None:
    print("x não tem valor")

## is
O operador **is** é usado para verificar se duas variáveis se referem ao mesmo objeto na memória. Ele retorna ```True``` se os operandos têm a mesma identidade (ou seja, o mesmo ID de objeto), e ```False``` caso contrário.

```
a = [1, 2, 3]
b = a
print(a is b)  # Saída: True
```

## is not
O operador **is not** é o oposto do **is** e é usado para verificar se dois objetos não têm a mesma identidade.
Retorna ```True``` se os operandos não têm a mesma identidade e ```False``` caso contrário.

```
x = 5
y = 10
print(x is not y)  # Saída: True
```

Essas flags são úteis em situações em que é necessário verificar a identidade ou a ausência de um valor específico em Python. O uso adequado delas pode ajudar a evitar erros de comparação e garantir o comportamento desejado em seu código.