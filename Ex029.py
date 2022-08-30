"""
EXERCÍCIO 029: Radar Eletrônico
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""
velocidade = float(input('Informe a velocidade do veículo: '))

multa = 0

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Voçê ultrapassou o limite da velocidade permitida então multa vai ser de {multa}')
else:
    print('Tenha um bom dia! Dirija com segurança!')
