"""
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
# "O strip()" remove todos os espaços do comço e do fim
cidade = str(input('Informe o nome da cidade em que nasceu: ')).strip()

# "cidade[0:5]" seleciona as 4 primeiras letras e o "upper" trasnforma todas as letras em maiúscolas
print(cidade[0:5].upper() == 'SANTO')

