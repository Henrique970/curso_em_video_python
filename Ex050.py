"""
EXERCÍCIO 050: Soma dos Pares
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0
quant = 0
for cont in range(1, 6+1):
    num = int(input('Informe um número: '))

    if num % 2 == 0:
        soma += num
        quant += 1

print(f'A soma de {quant} números pares digitados é de {soma}')