"""
EXERCÍCIO 060: Cálculo do Fatorial
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
#todo: Primeira forma de resolver usando o diretorio math.
"""
from math import factorial
numero = int(input('Informe um número para calcular o fatorial: '))
resultado = factorial(numero)
print('O fatorial de {} é {}.'.format(numero, resultado))
"""
#todo: Segunda forma de resolver usando estrutura for.
"""
numero = int(input('Informe um número para calcular o fatorial: '))
resultado = 1

print(f'Calculando {numero}!', end=' = ')

for contador in range(numero, 0, -1):
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    resultado *= contador
print(resultado)
"""
#todo: Terceira forma de resolver usando estrututa while.

numero = int(input('Informe um número para calcular o fatorial: '))
contador = numero
resultado = 1

print(f'Calculando {numero}!', end=' = ')

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    resultado *= contador
    contador -= 1
print(resultado)
