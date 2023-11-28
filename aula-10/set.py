# Set
# não é ordenado
# não aceita itens duplicados
# pode adicionar e remover itens, mas não pode modificar itens existentes
frutas = {'maçã', 'laranja', 'abacaxi', 'maçã'} # irá ter apenas 1 maçã

print(frutas)
print(len(frutas))

frutas.add('pera')

print(frutas)

frutas.remove('maçã')

print(frutas)

frutas.pop() # pop remove o ultimo valor, porém como não é ordenado irá remover um valor aleatório

print(frutas)

set1 = {'maçã', 'laranja', 'abacaxi'}
set2 = {1, 4, 6, 2}
set3 = {True, 'teste', 1, False}