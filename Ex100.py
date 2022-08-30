"""
EXERCÍCIO 100: Funções para sortear e somar
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
somaPar(). A primeira função vai sortear 5 números e vai coloca-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores PARES sorteados
pela função anterior.
"""
from random import randint


numeros = []

def sorteia():
    for quantidade in range(1, 6):
        numeros.append(randint(1, 10))
    print(f'Os 5 números sortiados foram: {numeros}')


def somaPar():
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'A soma dos números pares é: {soma}')

print('-' * 60)
sorteia()
print('-' * 60)
somaPar()
print('-' * 60)