"""
EXERCÍCIO 070: Estatísticas em Produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
quantidade = total_gasto = mais_de_mil = mais_barato = 0
nome_mais_barato = ''

while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto: '))

    resposta = str(input('Deseja continuar[S/N]? ')).upper().strip()

    while resposta not in 'SN':
        print('Informe somente "sS" para sim ou "nN" para não.')
        resposta = str(input('Deseja continuar[S/N]? ')).upper().strip()

    quantidade += 1
    total_gasto += preco

    if preco > 1000:
        mais_de_mil += 1

    if quantidade == 1:
        mais_barato = preco
        nome_mais_barato = nome
    else:
        if preco < mais_barato:
            mais_barato = preco
            nome_mais_barato = nome

    if resposta == 'N':
        print('=-' * 31)
        print(f'Você informou {quantidade} produtos! \n'
              f'O total gasto {total_gasto} \n'
              f'São {mais_de_mil} pordutos com mais de R$ 1000 \n'
              f'O nome do produto mais barato é o {nome_mais_barato}.')
        print('=-' * 31)
        break