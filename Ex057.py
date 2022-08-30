"""
EXERCÍCIO 057: Validação de Dados
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o seu sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Informção incorreta! Digite "M" ou "F".')
print('Obrigado pela informação')