sede = False

if sede:
    print('beber agua')

print('vida que segue')

print('------------------')

frio = True

if frio:
    print('Vestir casaco')
else:
    print('vestir camiseta')


print('------------------')

fome = False

if sede or fome:
    print('ir na cozinha')
else:
    print('ficar vendo netflix')

print('------------------')

if sede and fome:
    print('fazer lanche e pegar coca')
else:
    print('não tenho sede ou não tenho fome')

print('------------------')

dieta = True

if sede and fome:
    print('fazer lanche e pegar coca')
elif sede and not(fome):
    if dieta:
        print('tomar agua')
    else:
        print('tomar uma coca')
elif not(sede) and fome:
    print('Fazer um sanduiche')
else:
    print('Ver netflix')

print('------------------')

num1 = 5
num2 = 32

if num1 == num2:
    print('num1 igual a num2')
elif num1 != num2:
    print('num1 diferente de num2')
elif num1 > num2:
    print('num1 maior que num2')
elif num1 < num2:
    print('num1 menor que num2')

if num1 <= num2:
    print('num1 menor ou igual a num2')

if(num1 >= num2):
    print('num1 maior ou igual a num2')

print('------------------')

arr = [1, 4, 6, 3, 2]

num = 5

if num in arr:
    print('número está no arr')

if num not in arr:
    print('número não está no arr')