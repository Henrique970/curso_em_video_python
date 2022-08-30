"""
EXERCÍCIO 082: Dividindo Valores em Várias Listas
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, cria duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.
"""
listaNumeros = []
listaPares = []
listaImpares = []
contador = 1
numeros = int(input(f'Informe o {contador}º número: '))
listaNumeros.append(numeros)
print('Números adcionado com sucesso!')

while True:
    pergunta = str(input('Deseja continuar[S/N]? ')).strip().upper()

    if pergunta == 'S':
        contador += 1
        numeros = int(input(f'Informe o {contador}º número: '))
        listaNumeros.append(numeros)
        print('Números adcionado com sucesso!')
    elif pergunta == 'N':
        print('Obrigado por usar nosso programa!')
        break
    else:
        print('Digite somente "s/S" par Sim ou "n/N" para Não.')

print('Você digitou os seguintes números: \n'
      f'{listaNumeros}')

for indece, numero in enumerate(listaNumeros):
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)

print(f'Numeros pares: {listaPares}')
print(f'Numeros impares: {listaImpares}')