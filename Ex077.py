"""
EXERCÍCIO 077: Contando Vogais em Tupla
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""


palavras =  'aprender', 'programar', 'linguagem', 'python', \
            'curso', 'gratis', 'estudar', 'praticar', \
            'trabalhar', 'mercado', 'programador', 'futuro'

for palavra in palavras:
    print()
    print(f'As vogais da palavra {palavra.upper()} são ', end='')

    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')

