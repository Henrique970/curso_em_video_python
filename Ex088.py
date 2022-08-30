"""
EXERCÍCIO 088: Palpites Para a Mega Sena
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
# from random import randint
#
# listaJogos = []
# listaNumeros = []
#
# quantidades_jogos = int(input('Informe quantos palpites devem ser gerados: '))
#
# quantidade_numeros = 6
# numeros = 0
# contador = 0
#
# while quantidades_jogos > 0:
#     while quantidade_numeros > 0:
#         numeros = randint(1, 61)
#         if numeros not in listaNumeros:
#             listaNumeros.append(numeros)
#         quantidade_numeros -= 1
#
#     listaJogos.append(listaNumeros[:])
#     listaNumeros.clear()
#
#     contador += 1
#     quantidades_jogos -= 1
#
#     print(f'{contador}ª jogo: {listaJogos}')

from random import randint

listaPalpites = []
listaJogos = []

quantidades_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

while quantidades_jogos > 0:

    contador = 0

    while True:
        numeros = randint(1, 60)

        if numeros not in listaPalpites:
            listaPalpites.append(numeros)
            contador += 1

        if contador >= 6:
            break

    listaJogos.append(listaPalpites[:])
    listaPalpites.clear()

    quantidades_jogos -= 1

print('-=' * 3, f' SORTEANDO {quantidades_jogos} JOGOS ', '-=' * 3)
for indice, lista in enumerate(listaJogos):
    print(f'{indice + 1}ª jogo: {lista}')
