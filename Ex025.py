"""
EXERCÍCIO 025: Procurando uma String Dentro de Outra
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome = str(input('informe o seu nome: '))

resposta = 'silva' in nome.lower()

if resposta == True:
    print('Sim')
else:
    print('Não')