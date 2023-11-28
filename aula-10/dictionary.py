# Não aceita valores duplicados
meses = {
    "Jan": "Janeiro",
    "Fev": "Fevereiro",
    "Mar": "Março",
    "Mar2": "Março",
    "Mar": "Março2" # atributo duplicado, irá trazer apenas o ultimo que foi definino
}

print(meses)
print(len(meses))

print(meses['Jan']) # se não existir retornará um erro
print(meses.get('Jan')) # se não exister retornará "None"
print(meses.get('Ters', 'Padrão')) # segundo parâmetro é um valor padrão que ele irá retornar caso não exista a chave do primeiro parâmetro

if not(meses.get('Jane')):
    print('cuzinho')

