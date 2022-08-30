"""
EXERCÍCIO 067: Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    numero = int(input('Informe um número: '))

    if numero < 0:
        print('Obrigado por utilizar o nosso programa, Tchau!')
        break
    else:
        operacao = str(input('Informe qual operação matematica você deseja[+, -, * , /]: ')).upper()
        for contador in range(1,11):
            if operacao == '+':
                print(f'{numero} + {contador} = {numero + contador}')
            elif operacao == '-':
                print(f'{numero} - {contador} = {numero - contador}')
            elif operacao == '*':
                print(f'{numero} * {contador} = {numero * contador}')
            elif operacao == '/':
                print('{} / {} = {:.2f}'.format(numero, contador, numero / contador))
            else:
                print('Opção inválida')
