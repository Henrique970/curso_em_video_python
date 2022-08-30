"""
EXERCÍCIO 107: Exercitando módulos em Python
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas
funções.
"""
import moeda


preco = int(input('Informe um número: '))
taxa = int(input('Informe a taxa para aumentar e diminuir: '))

print(f'{preco} mais {taxa}% fica {moeda.aumentar(preco, taxa)}')
print(f'{preco} menos {taxa}% fica {moeda.diminuir(preco, taxa)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'O triplo de {preco} é {moeda.triplo(preco)}')