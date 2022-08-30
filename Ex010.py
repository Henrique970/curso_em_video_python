"""
EXERCÍCIO 010: Conversor de Moedas
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
Considere U$ 1,00 = R$ 3,27
"""
real = float(input('Inform quanto dinheiro voçê possui em Reais(R$): '))

print('Voçê possui {:.2f}R$ isso da pra comprar {:.2f}U$'.format(real, real / 3,27))
