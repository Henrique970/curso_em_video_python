"""
EXERCÍCIO 006: Dobro, Triplo, Raiz Quadrada
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

numero = int(input('Informe um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

# '\n' faz com haja uma quebra linha 'e :.2f' faz com que haja uma formatação limitando a duas casas decimais.
print('O dobro de {} é {}, \no triplo é {} \ne a raiz quadrada é {:.2f}'.format(numero, dobro, triplo, raiz))