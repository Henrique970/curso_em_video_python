"""
EXERCÍCIO 083: Validando Expressões Matemáticas
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
expressao = str(input('Informe um expressão; '))

listaParenteses = []

for simbolo in expressao:
    if simbolo == '(':
        listaParenteses.append('(')
    elif simbolo == ')':
        if len(simbolo) > 0:
            listaParenteses.pop()
        else:
            listaParenteses.append(')')
            break

if len(listaParenteses) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida')
