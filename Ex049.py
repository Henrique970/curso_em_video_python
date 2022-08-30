"""
EXERCÍCIO 049: Tabuada v2.0
Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""
numero = int(input('Informe um número para a tabuada: '))
for contador in range(1, 11):
    print(f'{numero} + {contador} = {numero + contador}')
print()
for contador in range(1, 11):
    print(f'{numero} - {contador} = {numero - contador}')
print()
for contador in range(1, 11):
    print(f'{numero} x {contador} = {numero * contador}')
print()
for contador in range(1, 11):
    print('{} / {} = {:.2f}'.format(numero, contador, numero / contador))