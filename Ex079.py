"""
EXERCÍCIO 079: Valores Únicos em uma Lista
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""

listaValores = []

valor = (int(input('Informe um número: ')))
listaValores.append(valor)
print('Valor adcionado com sucesso!')

while True:
    pergunta = str(input('Deseja continuar?[S/N]: ')).upper().strip()
    if pergunta == 'S':
        valor = (int(input('Informe um número: ')))
        if valor not in listaValores:
            listaValores.append(valor)
            print('Valor adcionado com sucesso!')
        else:
            print('Valor já existente na lista. Não permitido duplicadas.')
    elif pergunta == 'N':
        print('Obrigado por usar nosso programa')
        break
    else:
        print('Digite apenas "s/S" para Sim ou "n/N" para não')

listaValores.sort()

print('Os valores digitados são: \n'
      f'{listaValores}')