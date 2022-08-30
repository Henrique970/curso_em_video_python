"""
EXERCÍCIO 098: Função de Contador
Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo. Seu programa tem realizar três
contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada
"""
from time import sleep

# Resolução com for
# def contador(inicio, fim, passo):
#     if inicio < fim:
#         print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}:')
#         for contando in range(inicio, fim + 1, passo):
#             print(f'{contando}', end=' ')
#             sleep(0.5)
#         print('FIM!')
#         sleep(2)
#     if inicio > fim:
#         print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}:')
#         for contando in range(inicio, fim - 1, -passo):
#             print(f'{contando}', end=' ')
#             sleep(0.5)
#         print('FIM!')
#         sleep(2)



# Resolução com while
def contador(inicio, fim, passo):
    if passo < 0:
        passo -= 1
    if passo == 0:
        passo = 1

    print(f'Contando de {inicio} até {fim}, de {passo} em {passo}')

    if inicio < fim:
        contando = inicio
        while contando <= fim:
            print(f'{contando}', end=' ', flush=True)
            sleep(0.5)
            contando += passo
        print('FIM!')

    else:
        contando = inicio
        while contando >= fim:
            print(f'{contando}', end=' ', flush=True)
            sleep(0.5)
            contando -= passo
        print('FIM!')


def umaLinha():
    print('-' * 40)


umaLinha()
contador(1, 10, 1)
umaLinha()
contador(10, 0, 2)
umaLinha()
print('Agora é sua vez!')
print('Contagem personalizada!')
comeca = int(input('Informe o início: '))
termina = int(input('Informe o fim: '))
pulo = int(input('Informe o passo: '))
contador(comeca,termina,pulo)
umaLinha()
