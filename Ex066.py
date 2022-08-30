"""
EXERCÍCIO 066: Vários Números com Flag
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
numero = quantidade = soma = 0

while True:
    if quantidade == 0:
        numero = int(input('Informe um número: '))
    elif quantidade > 0:
        numero = int(input('Informe mais um número(caso queira encerrar digite 999): '))
    if numero == 999:
        break
    else:
        quantidade += 1
        soma += numero

print(f'Você digitou {quantidade} de números e a somade todos eles é {soma}')