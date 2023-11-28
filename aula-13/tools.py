# pela convenção, toda variavel que estiver em maiuscula deve ser tratada como uma constante e o valor não deve ser alterado
PI = 3.14
GRAVITY = 9.8

def get_extension(file: str):
    return file[file.index('.') + 1:]

def highest_number(numbers):
    return max(numbers)