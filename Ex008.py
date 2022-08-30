"""
EXERCÍCIO 008: Conversor de Medidas
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

metros = int(input('Informe o valor em metros(M): '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f'{metros} m \n'
      f'em kilômetros fica {km} km \n'
      f'em hectômetro fica {hm} hm \n'
      f'em decâmetro fica {dam} dam \n'
      f'em decímetro fica {dm} dm \n'
      f'em centímetros fica {cm} cm \n'
      f'e em milímetros fica {mm} mm')