# Falsy
Valores "falsy" (falsos) são aqueles que são considerados como False quando avaliados em um contexto booleano. Esses valores, embora não sejam o booleano False em si, são tratados como False quando utilizados em expressões booleanas ou em estruturas de controle de fluxo condicionais, como os operadores lógicos and, or e not, e a estrutura if.

Os valores considerados "falsy" em Python são:

* **False:** O valor booleano False.
* **None:** O valor nulo.
* **0:** O inteiro zero.
* **0.0:** O ponto flutuante zero.
* **'':** A string vazia.
* **[]:** A lista vazia.
* **():** A tupla vazia.
* **{}:** O dicionário vazio.
* **set():** O conjunto vazio.

Quando qualquer um desses valores é usado em uma expressão booleana, ele é tratado como False. Todos os outros valores são considerados como "truthy" (verdadeiros) em Python, o que significa que são avaliados como True em um contexto booleano.

Essa distinção é útil ao escrever código que depende da avaliação de expressões booleanas ou da verificação de condições em estruturas de controle de fluxo condicionais, permitindo que os programadores escrevam código conciso e legível.