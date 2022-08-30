"""
EXERCÍCIO 092: Cadastro de Trabalhador em Python
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime

dictTrabalhador = {}

dictTrabalhador['nome'] = str(input('Informe o nome do trabalhador: '))
ano_nascimento = int(input('Informe o ano de nascimento do trabalhardor: '))
dictTrabalhador['idade'] = datetime.now().year - ano_nascimento
dictTrabalhador['ctps'] = int(input('Informe os números da carteira de trabalho(se não possuir tal documento digite somente "0"): '))

if dictTrabalhador['ctps'] != 0:
    dictTrabalhador['contratacao'] = int(input('Informe o ano de contratação: '))
    dictTrabalhador['salario'] = float(input('Informe o salário do trabalhador: R$'))
    dictTrabalhador['aposentadoria'] = dictTrabalhador['idade'] + ((dictTrabalhador['contratacao'] + 35) - datetime.now().year)

for keys, values in dictTrabalhador.items():
    print(f'{keys}: - {values}')