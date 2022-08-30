"""
EXERCÍCIO 022: Analisador de Textos
Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite um nome completo : ')).strip()

print(f'Seu nome em letras totalmente maiúsculas fica {nome.upper()} \n'
      f'Seu nome em letras totalmente menúsculas fica {nome.lower()} \n'
      f'A quantidade de letras dos seu nome é {len(nome) - nome.count(" ")}')
