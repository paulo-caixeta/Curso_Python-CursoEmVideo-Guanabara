"""Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""
histórico = dict()
gols = list()
histórico['jogador'] = str(input('Nome do jogador: ' ))
qde_partidas = int(input(f'Quantas partidas o {histórico["jogador"]} jogou? '))
for i in range(0, qde_partidas):
    gols.append(int(input(f'   Quantos gols na partida {i}? ')))
    histórico['gols'] = gols[:]
"""total = 0
for i in histórico['gols']:
    total = total + i"""
histórico['total'] = sum(gols)
print('-=' * 30)
print(histórico)
print('-=' * 30)
for k, v in histórico.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {histórico["jogador"]} jogou {len(histórico["gols"])} partidas.')
for i, v in enumerate(histórico['gols']):
    print(f'   -> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {histórico["total"]} gols.')
print('-=' * 30)