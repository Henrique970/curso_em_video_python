"""
EXERCÍCIO 035: Analisando Triângulo v1.0
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""
lado1 = float(input('Informe o primeiro reta: '))
lado2 = float(input('Informe o segundo reta: '))
lado3 = float(input('Informe o terceiro reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos acima não podem formar triângulo!')