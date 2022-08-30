"""
EXERCÍCIO 108: Formatando Moedas em Python
Adapte o código do desafio 107, criando uma função adicional chamada moeda() que
consiga mostrar os valores como um valor monetário formatado.
"""
import moeda


preco = float(input('Informe um número: '))
taxa = float(input('Informe a taxa para aumentar e diminuir: '))

print(f'{preco} mais {taxa}% fica {moeda.moeda(moeda.aumentar(preco, taxa))}')
print(f'{preco} menos {taxa}% fica {moeda.moeda(moeda.diminuir(preco, taxa))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'O triplo de {moeda.moeda(preco)} é {moeda.moeda(moeda.triplo(preco))}')