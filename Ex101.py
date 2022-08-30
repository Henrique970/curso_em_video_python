"""
EXERCÍCIO 101: Funções para votação
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando que uma pessoa
tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""
def voto(nascimento):
    from datetime import date

    idade = date.today().year - nascimento

    if idade < 16:
        return f'Com {idade} anos de idade o voto é NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos de idade o voto é OPCIONAL'
    else:
        return f'Com {idade} anos de idade o voto é OBRIGATÓRIO'


ano = int(input('Informe o ano do seu nascimento: '))
print(voto(ano))