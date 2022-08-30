"""
EXERCÍCIO 111: Transformando módulos em pacotes
Crie um pacote chamado utilidadesCeV que tenha dois módolos internos chamados moedas e dado.
Trasfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
mantenha tudo funcionando.
"""
from Ex111.utilidadesCeV import moeda

preco = float(input('Informe um número: '))
moeda.resumo(preco)