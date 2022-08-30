"""
EXERCÍCIO 015: Aluguel de Carros
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""
dias = int(input('Informe quantos dias voçê ficou com a posse do veículo: '))
km = float(input('Informe a kilometragem percorrido por voçê com esse veículo: '))

preco_dias = dias * 60
preco_km = km * 0.15
preco_pagar = preco_dias + preco_km

print('O preço do aluguel com {:.2f} dias fica {}R$ e com {:.2f}km adiciona mais {:.2f}R$ \n'
      'Então o valor total é de {:.2f}'.format(dias, preco_dias, km, preco_km, preco_pagar))
