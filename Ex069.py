"""
EXERCÍCIO 069: Análise de Dados do Grupo
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""
mais18 = homens = mulhermenos20 = 0

while True:
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo[M/F]: ')).strip().upper()[0]

    while sexo not in 'MF':
        print('Digite "m/M" para o sexo masculino ou "f/F" para o sexo feminino.')
        sexo = str(input('Informe seu sexo[M/F]: ')).strip().upper()[0]

    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1

    resposta = str(input('Você deseja continuar[S/N]? ')).strip().upper()[0]

    while resposta not in 'SN':
        print('Digite "s/S" para sim ou "m/M" para não.')
        resposta = str(input('Você deseja continuar[S/N]? ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {mais18} \n'
      f'Ao todo são {homens} homens cadastrados \n'
      f'E são {mulhermenos20} mulheres com menos de 20 anos')
