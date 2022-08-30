"""
EXERCÍCIO 096: Função que calcula a área
Faça um programa que tenha uma função chamada area(), que receba as dimenções de um
terreno retangular (largura, comprimento) e mostre a area do terreno.
"""
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}m X {comprimento}m é igual a {area}m²')


area(largura=float(input('Informe a largura da área: ')), comprimento=float(input('Informe o comprimento da área: ')))