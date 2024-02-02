# Índices

Em Python, os índices são números que representam a posição de um elemento em uma sequência ordenada, como uma lista, tupla, string ou outra estrutura de dados semelhante.

## Posição de Elementos
Cada elemento em uma sequência tem um índice associado que indica sua posição na sequência.
O índice é usado para acessar ou manipular o elemento em uma determinada posição na sequência.

## Indexação Baseada em Zero
A indexação começa em 0. Isso significa que o primeiro elemento em uma sequência tem índice 0, o segundo tem índice 1, e assim por diante.
Por exemplo, em uma string (```texto = 'texto'```), ```texto[0]``` acessa o primeiro elemento (t), ```texto[1]``` acessa o segundo elemento (e), e assim por diante.

## Indexação Negativa
Além da indexação positiva (começando em 0), Python permite indexação negativa, onde -1 representa o último elemento, -2 representa o penúltimo, e assim por diante.
Por exemplo, em uma string (```texto = 'texto'```), ```texto[-1]``` acessa o último elemento (o), ```texto[-2]``` acessa o penúltimo elemento (t), e assim por diante.

## Acesso a Elementos
Os elementos em uma sequência são acessados utilizando colchetes [] com o índice do elemento desejado.
Por exemplo, ```texto[2]``` acessa o elemento na terceira posição da lista.

## Verificação de Limites
É importante verificar se um índice está dentro dos limites da sequência antes de acessá-lo para evitar erros de índice fora de alcance (IndexError).
Os índices são uma parte fundamental da manipulação de dados em Python, permitindo acesso eficiente a elementos individuais e a partes de sequências. Compreender como os índices funcionam é essencial para trabalhar com sucesso com estruturas de dados sequenciais em Python.