"""
EXERCÍCIO 059: Criando um Menu de Opções
Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
opcao = 0
numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))

while opcao != 5:

    print(''
          '[ 1 ] Somar \n'
          '[ 2 ] Multiplicar \n'
          '[ 3 ] Maior \n'
          '[ 4 ] Novos Números \n'
          '[ 5 ] Sair do programa \n')

    opcao = int(input('Informe uma das opção informadas acima: '))

    if opcao == 1:
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    elif opcao == 2:
        print(f'{numero1} x {numero2} = {numero1 * numero2}')
    elif opcao == 3:
        if numero1 > numero2:
            print(f'O maior número é o {numero1}')
        elif numero1 == numero2:
            print('Os números são os mesmos valores!')
        else:
            print(f'O maior número é o {numero2}')
    elif opcao == 4:
        print('Informe os novos números')
        numero1 = float(input('Informe o primeiro número: '))
        numero2 = float(input('Informe o segundo número: '))

print('Obrigado por usar nossos serviços! Volte em breve, Tchau.')