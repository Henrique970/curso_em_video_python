"""
EXERCÍCIO 094: Unindo Dicionários e Listas
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
"""
dictPeoples = {}

listPeoples = []
listWoman = []
ageList = []

counter = 0
sum = 0
average = 0

while True:
    dictPeoples['Name'] = str(input('Inform your name: '))
    dictPeoples['Gender'] = str(input('Inform your gender[M/F]: ')).upper().strip()
    dictPeoples['Age'] = int(input('Inform your age: '))

    listPeoples.append(dictPeoples.copy())

    if dictPeoples['Gender'] == 'F':
        listWoman.append(dictPeoples.copy())

    counter += 1
    sum += dictPeoples['Age']
    average = sum / counter

    if dictPeoples['Age'] > average:
        ageList.append(dictPeoples.copy())

    dictPeoples.clear()

    answer = str(input('Do you wish to continue[Y/N]? ')).strip()

    if answer not in 'Yy':
        break

print('-=' * 30)
for peoples in listPeoples:
    print(peoples)

print('-=' * 30)
print(f'The average age is {average :.2f}')

print('-=' * 30)
print(f'There are {len(listPeoples)} people registered!')

print('-=' * 30)
print(f'The registered women are ', end='')
for woman in listWoman:
    print(f'{woman["Name"]}', end=' ')
print()

print('-=' * 30)
print('People older than average are ', end='')
for age in ageList:
    print(f'{age["Name"]}', end=' ')
print()