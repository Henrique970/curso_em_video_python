"""
EXERCÍCIO 062: Super Progressão Aritmética v3.0
Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
contador = 1
mais = 10
total = 0
termos = 0

while mais != 0:
    total += mais
    while contador <= total:
        print(f'{primeiro}', end=' ')
        primeiro += razao
        contador += 1
        termos += 1
    print('Pausa')
    mais = int(input('Vai querer mais termos? Se sim informe quantos, se não digite 0(zero): '))

print('Fim')
print(f'Foi mostrado no total {termos} termos!')
