"""
EXERCÍCIO 104: Validando entrada de dados em Python
Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante
à função input() do Python, só que fazendo a validação para aceitar apenas um valor
numérico
Ex:
n = leiaInt('Digite um n')
"""
def leiaInt(variavel):
    """
    -> Faz com que aja uma validação caso o valor informado for um número inteiro
    :param variavel: valor a ser verificado
    :return: valor verificado caso seja um número inteiro
    Códico criado pro Henrique dos Santos
    """
    validacao = False
    valor = 0
    while True:
        numero = str(input(variavel))
        if numero.isnumeric():
            valor = int(numero)
            validacao = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if validacao:
            break
    return valor


numero = leiaInt('Informe uma mensagem: ')
print(f'Você digitou o número {numero}')