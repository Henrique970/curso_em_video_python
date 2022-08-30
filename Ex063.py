"""
EXERCÍCIO 063: Sequência de Fibonacci v1.0
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""
elementos = int(input('informe quantos números da Sequência de Fibonacci você quer: '))
contador = 3
termo1 = 0
termo2 = 1

print(f'{termo1} - {termo2}', end=' - ')

while contador <= elementos + 1:
    termo3 = termo1 + termo2
    print(f'{termo3}', end=' - ')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print('FIM', end='')
