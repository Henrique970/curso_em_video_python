"""
EXERCÍCIO 109: Formatando Moedas em Python
Modifique as funlções que foram criadas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor se o valor informado por elas vai ser
ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
import moeda


preco = float(input('Informe um número: '))
taxa = float(input('Informe a taxa para aumentar e diminuir: '))
pergunta = str(input('Deseja quue os valores sejam formatados?[S/N]: ')).strip().lower()

if pergunta == 's':
    formato = True
else:
    formato = False

print(f'{preco} mais {taxa}% fica {moeda.aumentar(preco, taxa, formato)}')
print(f'{preco} menos {taxa}% fica {moeda.diminuir(preco, taxa, formato)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, formato)}')
print(f'O triplo de {moeda.moeda(preco)} é {moeda.triplo(preco, formato)}')