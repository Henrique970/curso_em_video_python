def aumentar(preco=0, taxa=0):
    aumentar = preco + (preco * (taxa / 100))
    return aumentar


def diminuir(preco=0, taxa=0):
    diminuir = preco - (preco * (taxa / 100))
    return diminuir


def dobro(preco=0):
    return preco * 2


def triplo(preco=0):
    return preco * 3


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')