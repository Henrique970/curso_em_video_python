"""
EXERCÍCIO 036: Aprovando Empréstimo
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""
valor = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário do comprador: '))
anos = float(input('Quantos anos vai dividir o valor do imóvel: '))

mes = anos * 12
parcelas = valor / mes
comfirmacao = salario * 30 / 100

if parcelas > comfirmacao:
    print('Infelizmente o senhor não poderá realizar esse financiamento, pois as parcelas de {:.2f} \n'
          'são maiores que 30% do seu salário.'.format(parcelas))
else:
    print('Financiamento concluído com sucesso, senhor pagará {:.2f} por mês durante {} anos'.format(parcelas, anos))