minha_string = 'Qualquer Texto'

print(f'{minha_string} em string')

print(minha_string.upper())
print(minha_string.lower())

print(minha_string.capitalize()) # deixa a primeira letra maiuscula e o resto em minusculo

print(minha_string.isupper()) # retorna boolean se toda a string estiver em upper case
print(minha_string.islower()) # retorna boolean se toda a string estiver em lower case
print(minha_string.strip()) # remove espaços vazios no inicio e final da string
print(minha_string.replace('Qualquer', 'novo'))
print(minha_string.replace('u', 'U', 1))
print(len(minha_string)) # length
print(minha_string[0])
print(minha_string[13])
print(minha_string[0:5]) # recupera do indice 0 ao 5 (não inclui o indice 5)
print(minha_string[-4:-1])
print(minha_string.index('u')) # retorna o index do valor passado em parametro(primeira ocorrencia)

x = 'Texto' in minha_string # retorna boolean, se encontrar(true) ou não(false) o valor dentro da string
print(x)

a = """
Minha
String

Com espaço
"""

print(a)

# \ é caracteres de escape

a = 'Minha\nString\nCom\nEspaço'

print(a)

a = 'Minha "String" D\'agua'

print(a)
