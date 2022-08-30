"""
EXERCÍCIO 023: Separando Dígitos de um Número
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""
numero = int(input('Informe um número: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

if unidade == 0:
    pass
else:
    print(f'Unidade: {unidade}')
if dezena == 0:
    pass
else:
    print(f'Dezena: {dezena}')
if centena == 0:
    pass
else:
    print(f'Centena: {centena}')
if milhar == 0:
    pass
else:
    print(f'Milhar: {milhar}')

# print(f'A separação desses números fica: \n'
#       f'Unidade: {unidade} \n'
#       f'Dezena: {dezena} \n'
#       f'Centena: {centena} \n'
#       f'Milhar: {milhar} \n')