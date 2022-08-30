"""
EXERCÍCIO 031: Custo da Viagem
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""
distancia = float(input('Qual é a distância da sua viagem(km)? '))

if distancia <= 200:
    preco = distancia * 0.50
    print(f'O preço da fica {preco}R$')
else:
    preco = distancia * 0.45
    print(f'O preço da fica {preco}R$')