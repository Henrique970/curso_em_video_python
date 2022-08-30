"""
EXERCÍCIO 046: Contagem Regressiva
Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep

for contagem in range(10,0,-1):
    sleep(1)
    print(contagem)
print('\033[1;31mBuuuuummmmmmm \033[m')