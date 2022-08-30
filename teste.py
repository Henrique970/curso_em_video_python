numero = int(input())
print(f'O fatorial de {numero}! = ', end='')
fatorial = 1
for contando in range(numero, 1 - 1, -1):
    fatorial *= contando
    print(f'{contando}', end='')
    print(' x ' if contando > 1 else ' = ', end='')
print(f'{fatorial}')