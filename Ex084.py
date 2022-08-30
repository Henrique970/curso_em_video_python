"""
EXERCÍCIO 084: Lista Composta e Análise de Dados
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
listaTemporaria = []

listaPrincipal = []

maiorPeso = menorPeso = 0

while True:
    listaTemporaria.append(str(input('Nome: ')))
    listaTemporaria.append(float(input('Peso: ')))

    if len(listaPrincipal) == 0:
        maiorPeso = menorPeso = listaTemporaria[1]

    else:
        if listaTemporaria[1] > maiorPeso:
            maiorPeso = listaTemporaria[1]
        if listaTemporaria[1] < menorPeso:
            menorPeso = listaTemporaria[1]

    listaPrincipal.append(listaTemporaria[:])
    listaTemporaria.clear()

    resposta = str(input('Quer continuar [S/N]? ')).strip()

    if resposta in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(listaPrincipal)} pessoas.')
print(f'O maior peso foi de {maiorPeso} kg. Peso de ', end='')
for pessoas in listaPrincipal:
    if pessoas[1] == maiorPeso:
        print(f'{pessoas[0]} ', end='')
print()
print(f'O menor peso foi de {menorPeso} kg. Peso de ', end='')
for pessoas in listaPrincipal:
    if pessoas[1] == menorPeso:
        print(f'{pessoas[0]} ', end='')
print()