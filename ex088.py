"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""
print('-=' * 25)
print(f'{"JOGO DA MEGA SENA":^50}')
print('-=' * 25)
total_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-' * 50)
print(' ' * 15, f'Sorteando {total_jogos} jogos', ' ' * 15)
print('-' * 50)
from time import sleep
from random import randint
c = 0
jogo = list()
jogos = list()
for i in range(0, total_jogos):
    while True:
        n = randint(1, 61)
        if n not in jogo:
            jogo.append(n)
            c += 1
        if c >= 6:
            break
    c = 0
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
for i, jogo in enumerate(jogos):
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(0.5)
print('-' * 50)
print(f'{"Boa sorte!":^50}')

