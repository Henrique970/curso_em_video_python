"""
EXERCÍCIO 039: Alistamento Militar
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
nascimento = int((input('Informe o seu ano de nascimento: ')))

hoje = date.today().year
idade = hoje - nascimento

if idade == 18:
    print('Voçê ainda poderá se alistar!')

elif idade < 18:
    if idade == 17:
        print(f'Falta {18 - idade} ano para voçê se alistar!')
    else:
        print(f'Falta {18 - idade} anos para voçê se alistar!')

elif idade > 18:
    if idade == 19:
        print(f'Voçê passou {idade - 18} ano do tempo limite para se alistar')
    else:
        print(f'Voçê passou {idade - 18} anos do tempo limite para se alistar')