"""
EXERCÍCIO 042: Analisando Triângulos v2.0
Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
lado1 = float(input('Informe o primeiro reta: '))
lado2 = float(input('Informe o segundo reta: '))
lado3 = float(input('Informe o terceiro reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima podem formar triângulo!')
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero!')
    elif lado1 != lado2 != lado3 and lado1 != lado3:
        print('Triângulo Escaleno!')
    else:
        print('Triângulo Isósceles!')
else:
    print('Os segmentos acima não podem formar triângulo!')