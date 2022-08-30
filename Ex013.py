"""
EXERCÍCIO 013: Reajuste Salarial
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Informe o salário do funcionário em Reais(R$): '))

novo_salario = salario + (salario * 15 / 100)

print('O salário do funcionário é {:.2f}R$, mais com o aumento salarial de 15% fica com {:.2f}R$'.format(salario, novo_salario))