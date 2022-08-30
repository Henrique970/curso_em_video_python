"""
EXERCÍCIO 011: Pintando Parede
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""
comprimento = float(input('Informe o comprimento da área em metros(m): '))
altura = float(input('Informe a altura da área em metros(m): '))

area = comprimento * altura
tinta = area / 2

print('Com o comprimento de {}m e o altura de {}m a área vai ser de {}m² \n'
      'A quantidade de tinta em litros(l) necessária para realizar a pintu será de {}l'.format(comprimento, altura, area ,tinta))