#todo: Inacabado
"""
EXERCÍCIO 019: Sorteando um Item na Lista
Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
import random
from random import choice

aluno1 = input('Informe o nome do aluno: ')
aluno2 = input('Informe o nome de outro aluno: ')
aluno3 = input('Informe o nome de outro aluno: ')
aluno4 = input('informe o nome de outros aluno: ')

lista_anlunos = [aluno1, aluno2, aluno3, aluno4]

# "random" é aleatorio "choice" é escolher
#print('O aluno escolhido para apagar o quadro é {}'.format(random.choice(lista_anlunos)))

escolhido = choice(lista_anlunos)

print('O aluno escolhido para apagar o quadro é {}'.format(escolhido))
