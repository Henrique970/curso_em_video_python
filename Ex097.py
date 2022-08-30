"""
EXERCÍCIO 097: Um print especial
Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com um tamanho adaptável.

Ex:
escreva("Olá, Mundo")
Saída:
~~~~~~~~~~~~~~
  Olá, mundo
~~~~~~~~~~~~~~
"""
def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(f'  {mensagem}')
    print('~' * tamanho)


escreva('Henrique dos Santos')
escreva('Curso de python no youtube')
escreva('Curso em video')
escreva('Olá, mundo')