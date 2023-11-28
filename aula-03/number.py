import math as m

num1 = 5
num2 = 3.5


# tipos e conversão
print(type(num1))
print(type(num2))

a = float(num1)
print(a)
print(type(a))

b = int(num2)
print(b)
print(type(b))

x = float('5')
y = int(float('3.5'))

print(type(x))
print(type(y))

print('------------------------')

# operadores aritméticos
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(10 % 3)
print(num1 ** num2)
print(num1 // num2) # divisão com arredondamento pro inteiro mais próximo

print('------------------------')

# Funções númericas
print(abs(-15)) # número absoluto sem sinais
print(pow(3, 3)) # Potencia
print(max(1, 5, 3)) # retorna maior numero
print(min(1, 5, 3)) # retorna menor numero
print(round(8.3))
print(m.floor(8.3))
print(m.ceil(8.3))
print(m.sqrt(25))