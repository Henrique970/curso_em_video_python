"""
EXERCÍCIO 103: Ficha do Jogador
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gols'


nome = str(input('Informe o nome do jogador: '))
gols = str(input(f'Informe quantos gols {nome} fez: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    print(ficha(gols=gols))
else:
    print(ficha(nome, gols))