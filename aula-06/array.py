familia = ['Pedro', 'Karla', 'Julia', 'Ismael']

print(familia)
print(familia[1])
print(familia[2:]) # irá pegar do indice 2 para frente
print(familia[1:3]) # irá pegar do indice 1 ao indice 3 (não inclui o indice 3)

familia[2] = 'Julia Paulino'

print(familia)

familia.extend(['Kiron', 'Mariah']) # "concatenar" os arrays
familia.append('Plinio') # adiciona um valor
familia.insert(0, 'Inicio') # dizer em qual indice eu quero adicionar o valor no arr
familia.pop() # remove o ultimo indice
familia.remove('Inicio') # remove o valor passado em parametro

print(familia)

# familia.clear() # remove todos os valores do arr

print(familia)

print(familia.index('Pedro')) # retorna o index do valor passado
print(familia.count('Pedro')) # retorna a quantidade de valor do parametros encontrados

print('------------------------------')

idade_familia = [19, 48, 25, 67, 3, 16]

print(idade_familia)

idade_familia.sort() # ordena em ordem crescente o arr, modifica o arr atual, pode ser feito com arr de string também

print(idade_familia)

idade_familia.reverse() # reverte o arr, de tras pra frente

print(idade_familia)

print('------------------------------')

familia = ['Pedro', 'Karla', 'Julia', 'Ismael']

familia2 = familia # cria outro arr com a mesma referencia na memória, cópia de referencia

print(familia2)

familia.pop() # irá alterar nos dois arr

print(familia2)

familia3 = familia.copy() # cria outro arr com outro espaço de memória, cópia de valores apenas

print(familia3)

familia.pop() # irá alterar apenas no arr familia

print(familia3)

coordenadas = (-49, -36) # Tuple, valores não podem ser alterados, lista imutável
# coordenadas.pop() # irá gerar um erro
# coordenadas[1] = 1 # irá gerar um erro
print(type(coordenadas))
print(coordenadas)