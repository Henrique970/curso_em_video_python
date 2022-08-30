"""
EXERCÍCIO 012: Calculando Descontos
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
preco = float(input('Informe o preço do produto: '))

novo_preco = preco - (preco * 5 / 100)
0
print('O preço do produto é {:.2f}R$, mais com 5% de desconto fica {:.2f}'.format(preco, novo_preco))