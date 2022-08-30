"""
EXERCÍCIO 016: Quebrando um Número
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""
"""
#import math
from math import trunc
numero = float(input('Informe um número: '))

#print(f'O número {numero} tem parte inteira {math.trunc(numero)}')
print(f'O número {numero} tem parte inteira {trunc(numero)}')
"""
numero = float(input('Informe um número: '))

print(f'O número {numero} tem parte inteira {int(numero)}')