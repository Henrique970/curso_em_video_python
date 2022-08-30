"""
EXERCÍCIO 106: Sistema interativo de ajuda em Python
Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar
o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa
se encerrará.
OBS: use cores.
"""
c = [
    '\033[n',        # 0 - Sem cor
    '\033[0;30;41m', # 1 - Vermelho
    '\033[0;30;42m', # 2 - Verde
    '\033[0;30;43m', # 3 - Amarelo
    '\033[0;30;44m', # 4 - Azul
    '\033[0;30;45m', # 5 - Roxo
    '\033[7;30m'     # 6 = Branco
    ]

def titulo(mensagem, cor=0):
    tamanho = len(mensagem) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'    {mensagem}')
    print('~' * tamanho)
    print(c[0], end='')


def ajuda(comando):
    titulo(f'Acessoando o  comando {comando}', 0)
    print(c[6], end='')
    print(help(comando))
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    com = str(input('Função ou Biblioteca >'))
    if com.upper() == 'FIM':
        break
    else:
        ajuda(com)
titulo('ATÉ LOGO!')