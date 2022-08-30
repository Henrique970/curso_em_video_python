"""
EXERCÍCIO 030: Par ou Ímpar?
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
numero = int(input('Informe um número: '))

if numero % 2 == 1:
    print(f'{numero} é impar!')
else:
    print(f'{numero} é par!')