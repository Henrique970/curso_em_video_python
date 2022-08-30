"""
EXERCÍCIO 081: Extraindo Dados de uma Lista
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
listaNumeros = []
contador = 1

numero = int(input(f'Informe o {contador}ª número: '))
listaNumeros.append(numero)
print('Número adcionado com sucesso!')

while True:
    pergunta = str(input('Deseja continuar?[S/N]: ')).upper().strip()

    if pergunta == 'S':
        contador += 1
        numero = int(input(f'Informe o {contador}ª número: '))
        listaNumeros.append(numero)
        print('Número adcionado com sucesso!')
    elif pergunta == 'N':
        print('Obrigado por usar nosso programa: ')
        break
    else:
        print('Digite apenas "s/S" para Sim ou "n/N" para Não')

listaNumeros.sort(reverse = True)

print('Os números ordenados em decrescente: \n'
      f'{listaNumeros}')

print(f'Foram digitados {len(listaNumeros)} números no total')

if 5 in listaNumeros:
    print('O valor 5 está sim digitado!')
else:
    print('O valor 5 não foi digitado!')

