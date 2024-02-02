# Avaliação de Curto-cIRCUITO

A avaliação de curto-circuito refere-se ao comportamento dos operadores lógicos ```and``` e ```or``` de interromper a avaliação de expressões assim que o resultado final for determinado, sem avaliar todas as partes da expressão.

## Avaliação de curto-circuito com o operador ```and```

Se a primeira expressão em uma operação ```and``` for avaliada como ```False```, o resultado geral da expressão será ```False```, e a avaliação é interrompida, pois não importa o que ocorra nas outras expressões - o resultado já está determinado como ```False```.

```
# A divisão por zero não é avaliada devido ao curto-circuito
resultado = (5 > 10) and (10 / 0)   
```

Neste exemplo, como a primeira expressão (5 > 10) é ```False```, a segunda expressão (10 / 0) não é avaliada devido ao curto-circuito, pois não afetará o resultado final da operação ```and```.

## Avaliação de curto-circuito com o operador ```or```

Se a primeira expressão em uma operação ```or``` for avaliada como ```True```, o resultado geral da expressão será ```True```, e a avaliação é interrompida, pois não importa o que ocorra nas outras expressões - o resultado já está determinado como ```True```.

```
# A divisão por zero não é avaliada devido ao curto-circuito
resultado = (5 < 10) or (10 / 0)  
```

Neste exemplo, como a primeira expressão (5 < 10) é ```True```, a segunda expressão (10 / 0) não é avaliada devido ao curto-circuito, pois não afetará o resultado final da operação ```or```.

A avaliação de curto-circuito é uma técnica eficaz para melhorar a eficiência e o desempenho de expressões lógicas, evitando avaliar partes desnecessárias da expressão quando o resultado final já está determinado. Isso pode ser especialmente útil em situações onde a segunda parte da expressão pode gerar um erro, como divisão por zero.





