"""
EXERCÍCIO 017: Catetos e Hipotenusa
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

co = float(input('Informe o comprimento cateto oposto do triãngulo retângulo: '))
ca = float(input('Informe o comprimento cateto adjacente do triãngulo retângulo: '))

h = ((co ** 2 + ca ** 2 ) ** (1/2))

print('Sabendo que o comprimento do cateto oposto de {} e o comprimento do cateto adjacente é {} \n'
      'Com esses valores usando a fórmula de Bhaskara o comprimento da hipotenusa é de {:.2f}'.format(co, ca, h))