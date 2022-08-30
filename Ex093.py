"""
EXERCÍCIO 093: Cadastro de Jogador de Futebol
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
dictJogador = {}
dictGolsAssistencias = {}

listGols = []
listAssistencia = []

total_gols = 0
total_assistencia = 0

dictJogador['Nome'] = str(input('Informe o nome do jogador: '))
dictJogador['Partidas'] = int(input(f'Informe quantos jogos {dictJogador["Nome"]} jogou: '))

for partidas in range(1, dictJogador['Partidas'] + 1):
    gols = int(input(f'Informe quantos gols {dictJogador["Nome"]} fez na {partidas}ª partida: '))
    asssistencias = int(input(f'Informe quantas assistências {dictJogador["Nome"]} fez na {partidas}ª partida: '))

    listGols.append(gols)
    listAssistencia.append(asssistencias)

    total_gols += gols
    total_assistencia += asssistencias

dictJogador['Gols'] = listGols
dictJogador['Assistencias'] = listAssistencia
dictJogador['Total Gols'] = total_gols
dictJogador['Total Assistencia'] = total_assistencia

print('-=' * 30)
print(dictJogador)

print('-=' * 30)
for keys, values in dictJogador.items():
    print(f'{keys}: {values}')

print('-=' * 30)
print(f'O jodagor {dictJogador["Nome"]} jogou {dictJogador["Partidas"]} partida(s)!')
for partida, gol in enumerate(listGols):
    print(f'Na {partida + 1}ª partida o {dictJogador["Nome"]} fez {gol} gol(s) e distribuiu {listAssistencia[partida]} assistencia(s)!')
print(f'O jodagor {dictJogador["Nome"]} tem um total de {total_gols} gol(s) e {total_assistencia} assistencia(s)')
print(f'Um total de {total_gols + total_assistencia} participações de gols em {dictJogador["Partidas"]} partidas jogadas')