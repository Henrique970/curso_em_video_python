"""
EXERCÍCIO 068: Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from time import sleep
from random import randint

vitorias = 0

while True:
    print('######################## \n'
          '#                      # \n'
          '# JOGO DO PAR OU IMPAR # \n'
          '#                      # \n'
          '########################')
    sleep(1)
    print('Aguarde...')
    sleep(3)
    print('=-' * 15)
    escolha = str(input('Escolha Par ou Impar[P/I]: ')).upper().strip()
    print('=-' * 15)
    sleep(1)
    if escolha == 'P':
        usuario = int(input('Informe um número de 1 a 10: '))
        computador = randint(1, 10 + 1)
        soma = usuario + computador

        print(f'Vocês escolheu {usuario} \n'
              f'O computador escolheu {computador}')

        if soma % 2 == 0:
            vitorias += 1
            print('\033[4;34mVocê venceu!\033[m')
        else:
            print('\033[4;31mVocê perdeu!\033[m')
            break
    elif escolha == 'I':
        usuario = int(input('Informe um número de 1 a 10: '))
        computador = randint(1, 10 + 1)
        soma = usuario + computador

        print(f'Vocês escolheu {usuario} \n'
              f'O computador escolheu {computador}')

        if soma % 2 != 0:
            vitorias += 1
            print('\033[4;34mVocê venceu!\033[m')
        else:
            print('\033[4;31mVocê perdeu!\033[m')
            break
    else:
        print('Opção Inválida!')
print(f'Você conseguiu um total de {vitorias} vitorias consecutivas!')