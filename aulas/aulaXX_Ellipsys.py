# ELLIPSYS

# Em Python, ellipsis (...) é um objeto especial que pode ser usado em várias situações para representar uma operação ou estrutura de dados incompleta. 

# Ellipsis (...)
# O objeto ellipsis é representado por três pontos (...) e é usado principalmente em fatias de arrays multidimensionais para indicar que todas as dimensões devem ser incluídas.
# Também pode ser utilizado para indicar uma operação ou estrutura de dados incompleta em várias situações.
# Exemplo de uso em fatias de arrays multidimensionais:

np = ...
matriz = np.array([[1, 2, 3], [4, 5, 6]])
primeira_coluna = matriz[..., 0]  # Retorna a primeira coluna da matriz