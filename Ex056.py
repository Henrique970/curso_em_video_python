"""
EXERCÍCIO 056: Analisador Completo
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
media_idade = 0
mais_velho = 0
nome_velho = ''
mulher_20_anos = 0

for quant in range(1, 5):
    nome = str(input(f'informe o nome da {quant}º pessoa: ')).strip()
    idade = int(input(f'Informe a idade da {quant}º pessoa: '))
    sexo = str(input(f'Informe o sexo da {quant}º pessoa[M/F]: ')).upper().strip()
    media_idade = idade / 4
    if quant == 1 and sexo == 'M':
        mais_velho = idade
        nome_velho = nome
    else:
        if idade > mais_velho and sexo == 'M':
            mais_velho = idade
            nome_velho = nome

    if quant == 1 and sexo == 'F':
        mulher_20_anos = 1
    else:
        if idade > 20 and sexo == 'F':
            mulher_20_anos += 1

print(f'A media da idade das peossas informadas informadas é de {media_idade}')
print(f'O nome do mais homem mais velho é {nome_velho}')

if mulher_20_anos == 0:
    print('Não foi registrado nemhuma mulher com mais de 20 anos')
else:
    print(f'A quantidade de mulheres com mais de 20 anos é de {mulher_20_anos}')
