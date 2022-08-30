def aumentar(preco=0, taxa=0, formato=False):
    """
    Função para diminuir o valor informado pelo usuário de acordo com a porcentagem desejada.
    :param preco: recebe o preço do usuário
    :param taxa: recebe a taxa em porcentagem que deseja que seja aplicada no aumento do preço
    :param formato:
    :return: recebe a resposta do usuário se deseja os valores devem ser formatados
    Função criada por Henrique dos Santos.
    """
    aumentar = preco + (preco * (taxa / 100))
    # vai retornar somente quando a variavel formato for verdadeira.
    return aumentar if formato is False else moeda(aumentar)


def diminuir(preco=0, taxa=0, formato=False):
    """
    Função para diminuir o valor informado pelo usuário de acordo com a porcentagem desejada.
    :param preco: recebe o preço do usuário
    :param taxa: recebe a taxa em porcentagem que deseja que seja aplicada na diminuição do preço
    :param formato: recebe a resposta do usuário se deseja os valores devem ser formatados
    :return: o valor menos a taxa em porcentagem informada
    Função criada por Henrique dos Santos.
    """
    diminuir = preco - (preco * (taxa / 100))
    return diminuir if formato is False else moeda(diminuir)


def dobro(preco=0, formato=False):
    """
    Função para dobrar o preço informado pelo usuário
    :param preco: recebe o preço do usuário
    :param formato: recebe a resposta do usuário se deseja os valores devem ser formatados
    :return: o triplo do valor informado pelo usuário.
    Função criada por Henrique dos Santos.
    """
    dobro = preco * 2
    return dobro if formato is False else moeda(dobro)


def triplo(preco=0, formato=False):
    """
    Função para triplicar o preço informado pelo usuário.
    :param preco: recebe o preço do usuário
    :param formato: recebe a resposta do usuário se deseja os valores devem ser formatados
    :return: o triplo do valor informado pelo usuário.
    Função criada por Henrique dos Santos.
    """
    triplo = preco * 3
    # faz a mesma coisa
    return triplo if not formato else moeda(triplo)


def moeda(preco=0, moeda ='R$'):
    """
    Função para formatação dos valores.
    :param preco: recebe o preço do usuário
    :param moeda: recebe a indentificação da moeda
    :return: retorna os valores formatados
    Função criada por Henrique dos Santos.
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')