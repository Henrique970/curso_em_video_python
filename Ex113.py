"""
EXERCÍCIO 113: Funções aprofundadas em Python
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
possibikidade da digitação de um número de tipo inválido. Aproveite e crie
também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaInt(mensagem):
    while True:
        # é um tratamento de excecão verifica o tipo de valor a ser digitado
        try:
            numero = int(input(mensagem))
        # verifica se vai ocorrer alguns desses erros
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo cliente')
            break
        else:
            return numero


def leiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo cliente.\033[m')
            return 0
        else:
            return numero


numero_inteiro = leiaInt('Informe um valor inteiro: ')
print(f'O valor inteiro digitado foi {numero_inteiro}')

numero_real = leiaFloat('Informe um valor real: ')
print(f'O valor real digitado foi {numero_real}')