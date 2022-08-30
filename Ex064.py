"""
EXERCÍCIO 064: Tratando Vários Valores v1.0
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""

numero = 1
quantidade = 0
total = 0

while numero != 999:
    if quantidade == 0:
        numero = int(input('Informe um número: '))
    elif quantidade == 1:
        numero = int(input('informe mais um número: '))
    else:
        numero = int(input('Deseja informar mais algum número? Se não digite 999: '))
    total += numero
    quantidade += 1

print(f'Você digitou {quantidade - 1} números e soma de todos ele é de {total - 999}')