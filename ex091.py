"""Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado."""
from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
resultados = {'Jogado 1': randint(1, 6),
            'Jogador 2': randint(1, 6),
            'Jogador 3': randint(1, 6),
            'Jogador 4': randint(1,6)}
print(resultados)
print('Valores sorteados')
print('-='*25)
for k, v in resultados.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('   == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')