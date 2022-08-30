"""
EXERCÍCIO 055: Maior e Menor da Sequência
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = 0
menor = 0

for quant in range(1,6):
    peso = float(input(f'Informe o peso da {quant}º pessoa: '))
    if quant == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso é {maior}\n'
      f'O menos peso é {menor}')
