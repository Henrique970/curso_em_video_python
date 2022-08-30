"""
EXERCÍCIO 074: Maior e Menor Valores em Tupla
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
"""
from random import randint

computador = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

for numeros in computador:
    print(f'{numeros}', end=' ')
print()
print(f'O maior número é {max(computador)}')
print(f'O menor número é {min(computador)}')
