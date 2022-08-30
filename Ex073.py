"""
EXERCÍCIO 073: Tuplas com Times de Futebol
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Coritiba.
"""

times = 'Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'Internacional', 'São Paulo', 'Santos', 'Flamengo', 'Botafogo', \
        'Bragantino', 'Goiás', 'Cuiabá', 'Coritiba', 'América-MG', 'Avaí', 'Ceará SC', 'Atlético-GO', 'Juventude', 'Fortaleza'

print(f'Os 5 primeiros times são {times[0:5]}')
print('=-' * 30)
print(f'Os 4 ultimos colocados são {times[-4:]}')
print('=-' * 30)
print(f'Os times em ordem alfabética: \n'
      f'{sorted(times)}')
print('=-' * 30)
print(f'A posição do time do coxa é a {times.index("Coritiba") + 1}ª posição')