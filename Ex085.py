"""
EXERCÍCIO 085: Listas com Pares e Ímpares
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
listNumbers = [[], []]

counter = 1

while counter <= 7:
    numbers = int(input(f'Inform the {counter}st number: '))

    if numbers % 2 == 0:
        listNumbers[0].append(numbers)
    else:
        listNumbers[1].append(numbers)

    counter += 1

print(f'The even numbers are: {listNumbers[0]}')
print(f'The odd numbers are {listNumbers[1]}')