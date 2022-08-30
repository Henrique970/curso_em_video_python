"""
EXERCÍCIO 034: Aumentos Múltiplos
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input('Informe o salário do funcionário: '))

if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print(f'Esse salário de {salario} é acima de 1250,50 então o aumento é de 10% e fica {aumento}')
else:
    aumento = salario + (salario * 15 / 100)
    print(f'Esse salário de {salario} é abaixo de 1250,50 então o aumento é de 15% e fica {aumento}')