"""
EXERCÍCIO 018: Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import radians, sin, cos, tan

angulo = float(input('Informe um ângulo: '))

sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print('O ângulo {:.2f} tem /n'
      'Seno de {:.2f} \n'
      'Cosseno de {:.2f} \n'
      'Tangente de {:.2f}'
      .format(angulo, sen, cos, tan))