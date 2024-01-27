# Tipagem de Dados

<p style='text-align: justify;'>
A tipagem em linguagens de programação refere-se à forma como os tipos de dados são tratados, e há dois principais tipos de tipagem: tipagem estática e tipagem dinâmica.
</p>

## Tipagem Estática

<p style='text-align: justify;'>
Os tipos de dados são verificados em tempo de compilação, ou seja, durante a fase de desenvolvimento, antes da execução do programa. A característica da tipagem estática é que variáveis devem ser declaradas com um tipo específico e não podem mudar durante a execução do programa.
<p>

## Tipagem Dinâmica

<p style='text-align: justify;'>
A verificação dos tipos de dados ocorre em tempo de execução, ou seja, durante a execução do programa. A característica da tipagem dinâmica é que as variáveis podem ser declaradas sem a necessidade de especificar um tipo e podem ter seu tipo alterado durante a execução.
</p>
<br>

Em relação ao Python, é uma linguagem de programação de tipagem dinâmica. As principais características da tipagem em Python incluem:

* **Duck Typing:** Python utiliza o conceito de "duck typing", onde o tipo de uma variável é determinado pelo seu comportamento, e não pela sua classe ou tipo explicitamente declarado. Ou seja, se um objeto age como um determinado tipo, ele é tratado como sendo desse tipo.

* **Tipagem Forte:** Python é uma linguagem de tipagem forte, o que significa que a conversão entre tipos de dados não é realizada implicitamente. Operações entre tipos incompatíveis resultam em erros.

* **Tipagem Dinâmica:** Variáveis podem ter seu tipo alterado dinamicamente durante a execução do programa, facilitando a flexibilidade e a expressividade do código.

<br>

**Exemplo de tipagem dinâmica:**
```
x = 5       # x é do tipo int
x = "Olá"   # x é agora do tipo string(texto)
```

<p style='text-align: justify;'>
Essas características tornam Python uma linguagem versátil e facilitam o desenvolvimento rápido de código, ao mesmo tempo em que mantêm a integridade dos tipos de dados durante a execução.
</p>