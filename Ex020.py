"""
EXERCÍCIO 020: Sorteando uma Ordem na Lista
O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
#import random
from random import shuffle

aluno1 = input('Informe o nome do aluno: ')
aluno2 = input('Informe o nome de outro aluno: ')
aluno3 = input('Informe o nome de outro aluno: ')
aluno4 = input('Informe o nome de outro aluno: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista_alunos)

print('A ordem de alunos que vai aprensentar é a senguinte')
print(lista_alunos)
