"""
EXERCÍCIO 014: Conversor de Temperaturas
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""

celsius = float(input('Informe a temperatura em graus Celsius(ºC): '))

fahrenheit = (celsius * 1.8) + 32

print('A temperatura de {}ºC corresponde a {}ºF!'.format(celsius, fahrenheit))