"""
EXERCÍCIO 102: Função para Fatorial
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
# jeito do curso em video é melhor.

def fatorial(numero, show=False):
    """
    Calcula o Fatorial de um número.
    :param numero: o número a ser calculado
    :param show: (opcional) mostrar ou não o processo
    :return: o valor do fatorial da variavel numero
    """
    fatorial = 1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial *= contador
    return fatorial


# print(fatorial(5, True))
help(fatorial)







# meu jeito
# def fatorial(numero=1, show='s'):
#     """
#     Calcula o Fatorial de um número.
#     :param numero: o número a ser calculado
#     :param show: (opcional) mostrar ou não o processo
#     :return: o valor do fatorial da variavel numero
#     """
#     if show == 's':
#         fatorial = 1
#         print(f'O fatorial de {numero}! = ', end='')
#         for contando in range(numero, 1 - 1, -1):
#             fatorial *= contando
#             print(f'{contando}', end='')
#             print(' x ' if contando > 1 else ' = ', end='')
#         print(f'{fatorial}')
#     elif show == 'n':
#         fatorial = 1
#         for contando in range(numero, 1 - 1, -1):
#             fatorial *= contando
#         print(fatorial)
#     else:
#         print('Resposta inválida')
#
#
# numero = int(input('Informe um número para fazer o fatorial: '))
# show = str(input('Deseja ver o processo da conta[S/N](se não responder será executado): ')).strip().lower()
# fatorial(numero, show)