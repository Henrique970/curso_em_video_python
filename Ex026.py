
"""
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String
Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""
frase = str(input('Informe uma frase: ')).strip().lower()

print(f'Nessa frase a letra "A" aparece {frase.count("a")} vezes \n'
      f'A posição em que a letra "A" aparece pela primeira vez é {frase.find("a") + 1} \n'
      f'A posição em que a letra "A" aparece pela ultima vez é {frase.rfind("a") + 1} \n')