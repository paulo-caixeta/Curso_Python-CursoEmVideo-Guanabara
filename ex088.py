"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""
print('-=' * 25)
print(f'{"JOGO DA MEGA SENA":^50}')
print('-=' * 25)
total_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-' * 50)
print(f'{"Sorteando...":^50}')
print('-' * 50)
matrix = [[0], [0], [0], [0], [0], [0]]
print(matrix)
from random import randint
for l in range (0, total_jogos):
    for c in range (0, 6):
        matrix[l][c].append(randint(1, 60))
print(matrix)