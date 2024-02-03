# IDs

Em Python, a função ```id()``` é usada para obter o identificador único de um objeto, que é um número inteiro que representa a identidade desse objeto durante sua vida útil. 

## Identificador Único
Cada objeto em Python tem um identificador único associado a ele. O identificador único é um número inteiro que identifica exclusivamente o objeto durante sua existência.

## Função id()
A função ```id()``` é usada para retornar o identificador único de um objeto.

**Sintaxe:** ```id(objeto)```.

```
x = 42
print(id(x))  # Saída: 140724070786736
```

## Identidade do Objeto
A identidade de um objeto é garantida ser única e imutável durante sua vida útil. Mesmo que o conteúdo ou valor de um objeto possa mudar, sua identidade permanece constante.

## Utilização
A função ```id()``` é frequentemente usada para comparar se dois objetos referenciam o mesmo objeto na memória. É comum em comparações de identidade de objetos ou no rastreamento de objetos em estruturas de dados complexas.

## Objetos Mutáveis e Imutáveis
Objetos mutáveis, como listas e dicionários, podem ter seu conteúdo alterado sem afetar sua identidade.

Objetos imutáveis, como strings e tuplas, têm sempre a mesma identidade, pois seu conteúdo não pode ser alterado.

O id em Python é uma ferramenta útil para rastrear a identidade dos objetos durante a execução do programa. Ele fornece um meio de verificar se dois nomes de variáveis se referem ao mesmo objeto na memória, o que pode ser útil em várias situações de programação.

Em Python, quando você define múltiplas variáveis com o mesmo valor literal, o interpretador é inteligente o suficiente para perceber que esses valores são imutáveis e podem ser compartilhados na memória. Isso significa que objetos imutáveis, como números inteiros pequenos, strings curtas e algumas tuplas, podem ser armazenados em um local único na memória e as variáveis que se referem a esses valores compartilham o mesmo identificador único (ID).

### Objetos Imutáveis
Objetos imutáveis, como inteiros pequenos (-5 a 256), strings curtas e algumas tuplas, têm valores fixos e não podem ser alterados após a criação. Devido à imutabilidade desses objetos, o interpretador Python pode otimizar o uso de memória compartilhando o mesmo objeto para valores iguais em diferentes variáveis.

### Literal Pooling
O Python usa uma técnica chamada **"literal pooling"** (ou "pooling de literais") para armazenar valores imutáveis em um pool de objetos, onde valores idênticos compartilham o mesmo espaço de memória. Isso significa que se você definir duas variáveis com o mesmo valor literal, elas podem se referir ao mesmo objeto na memória.

### Economia de Memória
Essa otimização ajuda a economizar memória, especialmente para valores comuns que são frequentemente usados em programas.

Por exemplo, se você definir x = 5 e y = 5, ambas as variáveis x e y se referirão ao mesmo objeto inteiro na memória, e seus IDs serão iguais.

### Limitações
Essa otimização é aplicável apenas a valores imutáveis e a uma faixa limitada de objetos comuns. Para objetos mutáveis, como listas e dicionários, cada variável terá seu próprio objeto na memória, mesmo que os valores sejam iguais.

Essa inteligência embutida no interpretador Python ajuda a otimizar o uso de memória, especialmente em situações em que valores imutáveis comuns são repetidamente utilizados em um programa. No entanto, é importante lembrar que essa otimização se aplica apenas a valores imutáveis e pode variar dependendo da implementação específica do interpretador Python.