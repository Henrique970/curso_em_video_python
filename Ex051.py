"""
EXERCÍCIO 051: Progressão Aritmética
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

decimo =  primeiro + (10 - 1) * razao

for cont in range(primeiro, decimo + 1, razao):
    print('{}'.format(cont), end=' ')