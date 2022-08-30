"""
EXERCÍCIO 052: Números Primos
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
numero = int(input('Informe um número para ver se ele número primo ou não: '))

for cont in range(1, numero + 1):
    if numero % cont == 0:
        print('\033[34m', end=' ')
    else:
        print('\033[33m', end=' ')
    print(cont, end=' ')