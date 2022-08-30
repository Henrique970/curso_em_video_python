"""
EXERCÍCIO 078: Maior e Menor Valores na Lista
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
listaNumeros = []

maior = 0
menor = 0

for contador in range(0, 5):
    listaNumeros.append(int(input(f'Digite um valor para a Posição {contador}: ')))

    if contador == 0:
        maior = menor = listaNumeros[contador]
    else:
        if listaNumeros[contador] > maior:
            maior = listaNumeros[contador]
        if listaNumeros[contador] < menor:
            menor = listaNumeros[contador]

print(f'Você digitou os valores {listaNumeros}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for posicao, valores in enumerate(listaNumeros):
    if valores == maior:
        print(f'{posicao}... ', end='')

print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for posicao, valores in enumerate(listaNumeros):
    if valores == menor:
        print(f'{posicao}... ', end='')

print()