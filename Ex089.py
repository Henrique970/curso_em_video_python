"""
EXERCÍCIO 089: Boletim com Listas Compostas
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""
listaFicha = []

contador = 0
media = 0

while True:

    print('######################################################## \n'
          '# 1 - Cadastrar um aluno com suas notas                # \n'
          '# 2 - Mostrar Média dos alunos cadastrados             # \n'
          '# 3 - Mostrar nota de cada aluno individualmente       # \n'
          '# 4 - SAIR                                             # \n'
          '########################################################')

    opcao = int(input('Informe uma opção: '))

    if opcao == 1:
        nome = str(input('Informe o nome do aluno: '))

        nota1 = float(input('Informe a primeira nota: '))
        nota2 = float(input('Informe a segunda nota: '))
        media = (nota1 + nota2) / 2

        listaFicha.append([nome, [nota1, nota2], media])

        contador += 1

        print(f'Nª {contador} - {nome} foi cadastrado com sucesso!')

    elif opcao == 2:
        if len(listaFicha) == 0:
            print('Nenhum aluno cadastrado!')

        for indice, alunos in enumerate(listaFicha):
            print(f'{indice + 1} - {alunos[0]} {alunos[2]}')

    elif opcao == 3:
        if len(listaFicha) == 0:
            print('Nenhum aluno cadastrado!')

        aluno_desejado = int(input('Informe o índice do aluno desejado: '))

        if aluno_desejado > len(listaFicha) or aluno_desejado < 1:
            print('Índice inválido')
        else:
            print(f'{aluno_desejado} - {listaFicha[aluno_desejado - 1][0]} {listaFicha[aluno_desejado - 1][1]}')

    elif opcao == 4:
        print('Obrigado por usar nosso programa!')
        break

    else:
        print('Opção inválida.')
























# listaFicha = []
#
# while True:
#     nome = str(input('Informe o nome do aluno: '))
#     nota1 = float(input('Informe a primeira nota do aluno: '))
#     nota2 = float(input('Informe a segunda nota do aluno: '))
#     media = (nota1 + nota2) / 2
#
#     listaFicha.append([nome, [nota1, nota2], media])
#
#     resposta = str(input('Quer continuar [S/N]? '))
#
#     if resposta in 'Nn':
#         break
#
# for indice, aluno in enumerate(listaFicha):
#     print(f'{indice + 1} - {aluno[0]:<5} {aluno[2]:.1f}')
#
# while True:
#     print('-' * 35)
#     opcao = int(input('Informe o índice do aluno desejado (999 interrompe): '))
#
#     if opcao == 999:
#         print('Obrigado por usar o nosso programa!')
#         break
#
#     if opcao <= len(listaFicha) - 1:
#         print(f'Notas de {listaFicha[opcao - 1][0]} são {listaFicha[opcao - 1][1]}')
#     else:
#         print('Índice inválido.')

