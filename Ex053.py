"""
EXERCÍCIO 053: Detector de Palíndromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""

frase = str(input('Informe qualquer frase: ')).strip().lower()

separado = frase.split()
tudo_junto = "".join(separado)
inverso = tudo_junto[::-1]

print(f'O inverso de {tudo_junto} é {inverso}')

if tudo_junto == inverso:
    print('Temos um palímdromo')
else:
    print('Não é um palindromo  ')