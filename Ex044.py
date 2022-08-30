"""
EXERCÍCIO 044: Gerenciador de Pagamentos
Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

valor_produto = float(input('Informe o valor do produto: '))
print('###################################################\n'
        '# 1 para pagamento a vista no dinheiro/cheque     #\n'
        '# 2 para pagamento a vista/praso no cartão        #\n'
        '###################################################')
modo_pagamento = int(input('Escolha uma forma de pagamento: '))

if modo_pagamento == 1:
    total = valor_produto - (valor_produto * 10 / 100)
    print('Você escolheu pagar a vista no dinheiro/cheque, portanto terá ter 10% de desconto \n'
          'Então o valor é de {:.2f}'.format(total))
elif modo_pagamento == 2:
    quantas_vezes = int(input('informe em quantas vezes irá dividir o preço do produto [digite 1 para pagar a vista]: '))
    if quantas_vezes == 1:
        total = valor_produto - (valor_produto * 5 / 100)
        print('Você escolheu pagar a vista no cartão, portanto terá 5% de desconto \n'
              'Então o valor é de {:.2f}'.format(total))
    elif quantas_vezes == 2:
        print('Então está querendo dividir em 2x, portanto terá 0% de juros \n'
              'O valor de cada parcela é de {:.2f}'.format(valor_produto / 2))
    elif quantas_vezes > 2:
        total = valor_produto + (valor_produto * 20 / 100)
        parcelas = total / quantas_vezes
        print('Você escolheu pagar em {} vezes no cartão, portanto terá um acrescimo de 20% de juros \n'
              'O valor de cada parcela é de {:.2f}'.format(quantas_vezes, parcelas))
else:
    print('Opção inválida!')