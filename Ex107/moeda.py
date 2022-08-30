def aumentar(preco, taxa):
    aumentar = preco + (preco * (taxa / 100))
    return aumentar


def diminuir(preco, taxa):
    diminuir = preco - (preco * (taxa / 100))
    return diminuir


def dobro(preco):
    return preco * 2


def triplo(preco):
    return preco * 3