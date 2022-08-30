"""
EXERCÍCIO 033: Maior e Menor Valores
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe outro número: '))
numero3 = int(input('Informe o ultimo número: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'O maior número é {numero1}')
elif numero2 > numero1 and numero2 > numero3:
    print(f'O maior número é {numero2}')
else:
    print(f'O maior número é {numero3}')