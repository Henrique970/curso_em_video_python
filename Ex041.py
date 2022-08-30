"""
EXERCÍCIO 041: Classificando Atletas
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date

nascimento = int(input('Informe a idade do atleta: '))

idade = date.today().year - nascimento

if idade <= 9:
    print('Atleta mirin')

elif idade > 9 and idade <= 14:
    print('Atleta infantil')

elif idade > 14 and idade <= 19:
    print('Atleta junior')

elif idade > 19 and idade <= 25:
    print('Atleta sênior')

else:
    print('Atleta master')