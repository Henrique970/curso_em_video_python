"""
EXERCÍCIO 076: Lista de Preços com Tupla
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
produtos = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, \
           'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, \
           'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90

print(f'{"LISTAGEM DE PREÇOS" :^40}')

print('-' * 40)
for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao] :.<30}', end='')
    else:
        print(f'R${produtos[posicao] :>8}')
print('-' * 40)