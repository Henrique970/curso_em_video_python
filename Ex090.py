"""
EXERCÍCIO 090: Dicionário em Python
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
dictAluno = {}

dictAluno['Nome'] = str(input('Informe o nome do aluno: '))
dictAluno['Media'] = float(input(f'Informe á média do {dictAluno["Nome"]}: '))

for keys, values in dictAluno.items():
    print(f'{keys}: {values}')

if dictAluno['Media'] >= 7:
    print('Situação: APROVADO!')
elif dictAluno['Media'] < 7 and dictAluno['Media'] >= 5:
    print('Situação: RECUPERAÇÃO!')
else:
    print('Situação: REPROVADO!')