"""
EXERCÍCIO 045: Pedra, Papel e Tesoura
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep
print('##################\n'
    '# 1 para PEDRA   #\n'
    '# 2 para  PAPEL  #\n'
    '# 3 para TESOURA #\n'
    '##################')

usuario = int(input('Informe uma opção: '))

computador = randint(1, 4)

if usuario == 1:
    print('Você escolheu PEDRA!')
elif usuario == 2:
    print('Você escolheu PAPEL!')
elif usuario == 3:
    print('Você escolheu TESOURA!')
else:
    print('opção inválida!')

if computador == 1:
    print('O computador escolheu PEDRA!')
elif computador == 2:
    print('O computador escolheu PAPEL!')
elif computador == 3:
    print('O computador escolheu TESOURA!')
sleep(2)
if usuario == computador:
    print('\033[1;30mDeu empate! \033[m')
elif usuario == 1 and computador == 2 or usuario == 2 and computador == 3 or usuario == 3 and computador == 1:
    print('\033[1;31mO computador venceu! \033[m')
else:
    print('\033[1;34mVocê venceu, PARABÉNS! \033[m')