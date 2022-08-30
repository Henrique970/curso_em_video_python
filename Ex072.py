"""
EXERCÍCIO 072: Número por Extenso
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

extencoes = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', \
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez', \
            'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', \
            'Desesseis', 'Desessete', 'Desoito', 'Desenove', 'Vinte'

while True:
    numero = int(input('Informe um número de 0 a 20: '))

    while numero > 20 or numero < 0:
        numero = int(input('Tente novamente. Informe um número de 0 a 20: '))

    else:
        print(f'Você informou o número {extencoes[numero]}')
 