"""
EXERCÍCIO 087: Mais Sobre Matriz em Python
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
"""
listaMatriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        listaMatriz[linha][coluna] = int(input('Informe um número: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{listaMatriz[linha][coluna] :^5}]', end='')
    print()

for numeros in listaMatriz:
    for numero in numeros:
        if numero % 2 == 0:
            soma_pares += numero

for linha in range(0, 3):
    for terceira_coluna in range(0, 1):
        soma_terceira_coluna += listaMatriz[linha][2]

# uma maneira de descobrir o maior da segunda linha.
# for segunda_linha in range(0, 1):
#     maior_segunda_linha = max(listaMatriz[1])

# outra maneira de descobrir o maior da segunda fileira
for coluna in range(0, 3):
    if coluna == 0:
        maior_segunda_linha = listaMatriz[1][coluna]
    else:
        if listaMatriz[1][coluna] > maior_segunda_linha:
            maior_segunda_linha = listaMatriz[1][coluna]

print('=-' * 30)
print(f'A soma de todos números pares da matriz são: {soma_pares}')
print(f'A soma da terceira coluna da matriz é: {soma_terceira_coluna}')
print(f'A maior da segunda linha da matriz é: {maior_segunda_linha}')