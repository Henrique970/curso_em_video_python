"""
EXERCÍCIO 112: Entrada de dados monetários
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado
dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a
função input(), mas com uma validação de dados para aceitar apenas valores que sejam
monetários
"""
from Ex112.utilidadesCeV.dado import leiaDinheiro
from Ex112.utilidadesCeV.moeda import resumo

preco = leiaDinheiro('Informe um preço: ')
resumo(preco, 25, 22)