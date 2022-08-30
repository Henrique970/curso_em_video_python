"""
EXERCÍCIO 058: Jogo da Adivinhação v2.0
Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""
from random import randint
from time import sleep
interronper = ''
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
sleep(2)
while interronper != 'Acertou':
    computador = randint(0, 10)
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    print('PERA AÍ...')
    sleep(1)
    if jogador == computador:
        print('PARABÉNS! Você conseguiu me vencer!')
        interronper = 'Acertou'
    else:
        print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
        print('Tente novamente!')