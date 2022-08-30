"""
EXERCÍCIO 065: Maior e Menor Valores
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""
resposta = 'S'
soma = quantidade = media = maior = menor = 0

while resposta != 'N':
    if resposta == 'S':
        numero = int(input('Digite um número: '))

        soma += numero
        quantidade += 1

        if quantidade == 1:
            maior = menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero

        resposta = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    elif resposta == 'N':
        resposta = 'N'
    else:
        print('Digite apenas "S/s" para sim ou "N/n" para não!')
        resposta = str(input('Quer continuar [S/N]? ')).upper().strip()[0]

media = soma / quantidade

if quantidade > 1:
    print('Você digitou {} números e a média é de {:.2f}.'.format(quantidade, media))
    print('O maior valor é de {} e o menor é de {}.'.format(maior, menor))
else:
    print('Você digitou apenas {} número e a média é {}.'.format(quantidade, media))
    print('O maior eo menor valor é esse mesmo valor ({})'.format(maior or menor))