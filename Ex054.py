"""
EXERCÍCIO 054: Grupo de Maioridade
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

maior = 0
menor = 0

hoje = date.today().year

for quant in range(1, 8):
    nascimento = int(input('Informe seu ano de nascimento: '))

    idade = hoje - nascimento

    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'A quantidade de pessoas maiores de idade é de {maior}\n'
      f'A quantidade de pessoas menores de idade é de {menor}')