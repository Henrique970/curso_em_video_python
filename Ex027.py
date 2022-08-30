"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""
nome = str(input('Informe seu nome completo: ')).strip()

# "split()" vai pegar sua frase e dividir em pedaços divididos por espaço
n = nome.split()

print(f'O seu primeiro nome é: {n[:1]} \n'
      f'O seu útimo nome é {n[len(n) - 1:]}')