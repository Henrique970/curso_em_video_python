"""
EXERCÍCIO 080: Lista Ordenada sem Repetições
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
listaNumero = []

for contador in range(0, 5):
    numero = int(input(f'informe o {contador + 1}ª número de 5: '))

    # se o contador for igual a 0 iu se é maior que o ultimo número
    if contador == 0 or numero > listaNumero[-1]:
        listaNumero.append(numero)
    else:
        posicao = 0

        while posicao < len(listaNumero):
            if numero <= listaNumero[posicao]:
                listaNumero.insert(posicao, numero)
                break
            posicao += 1

print('Os valores em ordem são: \n'
      f'{listaNumero}')
