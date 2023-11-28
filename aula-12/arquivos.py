# Open() para abrir arquivos
# 1º parâmetro é o caminho
# 2º parâmetro é a maneira como irá abrir o arquivo, existem 5 maneira:
## "r" = read / leitura
## "a" = append / incrementar (irá incrementar o arquivo, mantendo as infos anteriores dele)
## "w" = write / escrita (irá sobreescrever todo o arquivo, também pode criar arquivos)
## "x" = create / criar arquivo
## "r+" = leitura + escrita

# arquivo = open('./aula-12/test3.txt', 'x')

# --------------------------
# LEITURA "r"

# retorna boolean para se o arquivo pode ser lido ou não
# print(arquivo.readable())

# lê todo o arquivo em si
# print(arquivo.read())

# lê a primeira linha do arquivo, e assim por diante para cada print(irá iterar as linhas lidas e ler a próxima)
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# cria um arr com todas as linhas do arquivo, cada posição do arr é uma linha
# lists = arquivo.readlines()

# print(lists)

# print(lists[3])

# --------------------------
# Incremetar "a" | Escrever "w" / Criar "x"

# retorna boolean para se o arquivo pode ser escrito / incrementado / criado ou não
# print(arquivo.writable())

# escrever no arquivo
# arquivo.write('Python\n')
# arquivo.write('Terraform\n')

# --------------------------
# Excluir arquivo através da biblioteca os
# se o arquivo não estiver fechado ele não será removido
import os

# if os.path.exists('./aula-12/test2.txt'):
#     os.remove('./aula-12/test2.txt')
#     print('arquivo excluido')
# else:
#     print('arquivo não existe')

# excluir pasta
# só irá excluir uma pasta se ela estiver vazia
os.rmdir('./aula-12/nova-pasta')

# fechar o arquivo após concluir a leitura ou o que tiver que ser feito
# sempre fechar o arquivo após utiliza-lo
# arquivo.close()