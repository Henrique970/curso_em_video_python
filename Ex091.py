"""
EXERCÍCIO 091: Jogo de Dados em Python
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

dictDados = {}
listRanking = []

for contador in range(1, 4 + 1):
    dictDados[(input(f'Informe o nome do jogador {contador}: '))] = randint(1, 6)

sleep(1)
for keys, values in dictDados.items():
    print(f'O jogador {keys} tirou {values}')
    sleep(0.5)

listRanking = sorted(dictDados.items(), key=itemgetter(1), reverse=True)

print('O RANKING FICA:')
sleep(1)
for posicao, jogador in enumerate(listRanking):
    print(f'{posicao + 1}ª {jogador[0]} - {jogador[1]}')
    sleep(0.5)