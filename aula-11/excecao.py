
try:
    numero = int(input('Digite um número: '))

    print(numero)

    numero/0

except ZeroDivisionError:
    print('Divisão por 0 não é possível')
except ValueError:
    print('Digite um valor válido.')
except:
    print('Erro inesperado.')
finally:
    print('Sempre Executa')