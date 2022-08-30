"""
EXERCÍCIO 099: Função que descobri o maior
Faça um progama que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analizar todos os
valores e dizer qual deles é o maior.
"""
from time import sleep

def maiorValor(* numeros):
    contador = maior = 0
    print()
    print('-' * 40)
    print('Analizando o os valores passados!')
    sleep(1)
    for numero in numeros:
        print(f'{numero}', end=' ', flush=True)
        sleep(0.3)
        if contador == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero

        contador += 1
    print()
    sleep(1)
    print(f'Foram informados {contador} números ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {maior}')
    sleep(1.5)

maiorValor(2, 9, 4, 5, 7 ,1)
maiorValor(4, 7, 0)
maiorValor(1, 2)
maiorValor(6)
maiorValor()