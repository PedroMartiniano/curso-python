# big_mac() # erro, não pode chamar a função antes

def big_mac():
    print('Sanduiche Big Mac')

print('inicio')
big_mac()
print('fim')

def fazer_big_mac(nome):
    print(f'Sanduiche Big Mac do {nome}')

fazer_big_mac('Pedro')

def fazer_batata(tamanho):
    print(f'Batata tamanho {tamanho}')

fazer_batata('M')

def preparar_refrigerante(tipo, tamanho):
    print(f'Refrigerante {tipo} tamanho {tamanho}')

preparar_refrigerante('Coca Cola', 'Grande')

print('------------------')

def fazer_combo(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri, tamanho_refri)

fazer_combo('Pedro', 'M', 'Coca Cola', 'Grande')

print('------------------')

def soma_num(num1, num2):
    return num1 + num2

result = soma_num(5, 10)

print(result)

print('------------------')

def maior_num(arr):
    arr_test = arr.copy()

    arr_test.sort()

    return arr_test[len(arr_test) - 1]

maior = maior_num([1, 5, 2, 7, 3])

print(maior)