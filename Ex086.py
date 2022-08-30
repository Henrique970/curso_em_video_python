"""
EXERCÍCIO 086: Matriz em Python
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
No final, mostre a matriz na tela, com a formatação correta.
"""

listaMatriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        listaMatriz[linha][coluna] = (int(input(f'Informe o [{linha} - {coluna}] número: ')))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{listaMatriz[linha][coluna] :^5}]', end='')
    print()