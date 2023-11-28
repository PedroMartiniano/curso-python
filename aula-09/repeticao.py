i = 1

while i < 10:
    print(i)
    i += 1

print('terminou')

print('------------------')

frutas = ['banana', 'maçã', 'pera']

for item in frutas:
    print(item)

print('------------------')

canal = 'Refatorando'

for letra in canal:
    print(letra)

print('------------------')

# range aceita três parâmetros
# primeiro é qual indice irá começar
# segundo é até qual indice ele irá(não considera o indice, ex: 20, vai até o 19)
# terceiro é de quanto em quanto ele irá aumentar o indice, ex: 2

# começa no indice 0, vai até o indice 19, passando de 1 em 1
for i in range(0, 20, 1):
    print(i)

print('------------------')

# se passado só um parâmetro, será até qual indice ele irá
for i in range(len(frutas)): # não considera o ultimo valor, ex: 11, começa no 0 e vai até o 10
    print(frutas[i], i)

print('------------------')

for index in range(5):
    if index == 0:
        print(f'primeira linha {index}')
    else:
        print(f'outras linhas {index}')

print('------------------')

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0],
]

for linha in matriz:
    print(linha)
    for coluna in linha:
        print(coluna)