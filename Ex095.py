"""
EXERCÍCIO 095: Aprimorando os Dicionários
Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
dictJogador = {}

ListaTime = []
ListaPartidas = []

while True:
    print('################################################################ \n'
          '# 1 - Cadastar informação de jogadores                         # \n'
          '# 2 - Mostrar uma tabela com as informações dos jogadores      # \n'
          '# 3 - Mostar o rendimento de um jogador expecifico             # \n'
          '# 4 - SAIR                                                     # \n'
          '################################################################')
    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        dictJogador.clear()

        dictJogador['Nome'] = str(input('Nome do Jogador: '))
        total_partidas = int(input(f'Quantas partidas {dictJogador["Nome"]} jogou? '))

        ListaPartidas.clear()

        for partida in range(1, total_partidas + 1):
            ListaPartidas.append(int(input(f'Quantos {dictJogador["Nome"]} gols na partidas {partida}? ')))

        dictJogador['Gols'] = ListaPartidas[:]
        # "sum" soma os elementos da lista
        dictJogador['Total'] = sum(ListaPartidas)

        ListaTime.append(dictJogador.copy())

        print(f'{dictJogador["Nome"]} cadastrado com sucesso!')

    elif opcao == 2:
        for keys in dictJogador.keys():
            print(f'{keys:<15}', end='')
        print()
        print('-' * 40)
        for partida, valores in enumerate(ListaTime):
            print(f'{partida + 1:>3} ', end='')
            for valor in valores.values():
                print(f'{str(valor):<15}', end='')
            print()
        print('-' * 40)

    elif opcao == 3:
        print('-=' * 30)
        print('ID ', end='')

        id = int(input('Mostrar dados de qual jogador (informe o ID)? '))

        if id > len(ListaTime):
            print(f'ERRO! Não existe jogador com código {id}!')
        else:
            print(f'Levantemento do jogador {ListaTime[id - 1]["Nome"]}:')

            for partida, gol in enumerate(ListaTime[id - 1]['Gols']):
                print(f'    No jogo {partida + 1} fez {gol} gols.')
        print('-' * 40)

    elif opcao == 4:
        print('Obrigado por usar o nosso programa!')
        break

    else:
        print('Opção Inválida')
