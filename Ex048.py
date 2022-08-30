"""
EXERCÍCIO 048: Soma Ímpares Múltiplos de Três
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
soma = 0
quant = 0
for contador in range(1,501,2):
    if contador % 3 == 0:
        quant += 1
        soma += contador
print(f'A soma de {quant} números contados é de {soma}')
