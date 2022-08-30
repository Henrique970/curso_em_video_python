"""
EXERCÍCIO 037: Conversor de Bases Numéricas
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""
numero = int(input('Informe um número inteiro: '))
print('''
#########################
Escolha um opção:       #
[1] PARA BINÁRIO;       #
[2] PARA OCTAL;         #
[3] PARA HEXADECIMAL.   #
#########################
''')

opcao = int(input('Informe a opção desejada: '))

if opcao == 1:
    print(f'O número {numero} em binário fica {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} em octal fica {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O número {numero} em hexadecimal fica {hex(numero)[2:]}')
else:
    print('opção inválida!')
