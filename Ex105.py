"""
EXERCÍCIO 105: Analisando e gerando Dicionários
Faça um programam que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings.
"""
def notas(* numeros, stc=False):
    """
    -> Pega adiciona as notas dos alunos em um dicionário com algumas informações
    :param numeros: recebe as notas dos alunos
    :param stc: (opcional) ver a situação da sala de aula com base na média das notas
    :return: um dicionário com as informações
    """
    dictNotas = {}
    dictNotas['toal'] = len(numeros)
    dictNotas['maior'] = max(numeros)
    dictNotas['menor'] = min(numeros)
    dictNotas['media'] = sum(numeros) / len(numeros)
    if stc:
        if dictNotas['media'] >= 7:
            dictNotas['situacao'] = 'Boa'
        elif dictNotas['media'] >= 5:
            dictNotas['situacao'] = 'Razoável'
        else:
            dictNotas['situacao'] = 'Ruim'

    return dictNotas


notas_alunos = notas(6, 7, 8, 9, 3, 2, 3, 5, 6, 8, 9, stc=True)
print(notas_alunos)









# def notas(* numeros, stc=False):
#     """
#     -> Pega adiciona as notas dos alunos em um dicionário com algumas informações
#     :param numeros: recebe as notas dos alunos
#     :param stc: (opcional) ver a situação da sala de aula com base na média das notas
#     :return: um dicionário com as informações
#     """
#     dictNotas = {}
#     maior = 0
#     menor = 0
#     contador = 0
#     soma = 0
#     media = 0
#     situacao = ''
#     for numero in numeros:
#         contador += 1
#         if contador == 1:
#             maior = numero
#             menor = numero
#         else:
#             if numero > maior:
#                 maior = numero
#             if numero < menor:
#                 menor = numero
#         soma += numero
#         media = soma / contador
#         dictNotas['maior'] = maior
#         dictNotas['menor'] = menor
#         dictNotas['media'] = media
#
#         if stc:
#             if media >= 7:
#                 situacao = 'Boa!'
#             elif media < 7 and media > 5:
#                 situacao = 'Razoável!'
#             else:
#                 situacao = 'Ruim!'
#             dictNotas['situacao'] = situacao
#
#     return dictNotas
#
#
# print(notas(6, 7, 8, 9, 3, 2, 3, 5, 6, 8, 9, stc=True))
