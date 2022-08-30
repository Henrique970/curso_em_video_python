"""
EXERCÍCIO 075: Análise de Dados em uma Tupla
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

valores = int(input('Informe um número: ')), \
          int(input('Informe outro número: ')), \
          int(input('Informe outro número: ')), \
          int(input('Informe o último número: '))


if 9 in valores:
    print(f'O valor 9 apareceu {valores.count(9)} vezes')
else:
    print('O número 9 não paraceu nenhuma vez')
if 3 in valores:
    print(f'O valor 3 foi digitado na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')

print('Os valores pares são ', end='')
for valor in valores:
    if valor % 2 == 0:
        print(f'{valor}', end=' ')

