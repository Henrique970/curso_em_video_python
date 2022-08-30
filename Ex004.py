"""
EXERCÍCIO 004: Dissecando uma Variável
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""

a = input('Digite algo: ')
print('O tipo primitivo deste valor é: {}'.format(type(a)))
#print(f'O tipo primitivo deste valor é: {type(a)}')
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Está maiúsculas? {}'.format(a.isupper()))
print('Está menúsculas? {}'.format(a.islower()))
# Só a primeira letra está maiuscula, isso é estar capitalizada.
print('Está capitalizada? {}'.format(a.istitle()))



