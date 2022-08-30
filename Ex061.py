"""
EXERCÍCIO 061: Progressão Aritmética v2.0
Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
contador = 1

while contador <= 10:
    print(f'{primeiro}', end=' ')
    primeiro += razao
    contador += 1
