# Jogo de Jokenpô, vulgo "Pedra, papel e tesoura"
from time import sleep
print('-==-' * 25)
print('\033[1mPEDRA X PAPEL X TESOURA\033[m')
print('-==-' * 25)
print('Vamos jogar?\n')
from random import randint
from time import sleep
jogada = ['nulo', 'Pedra', 'Papel', 'Tesoura']
jogador = int(input('Escolha sua jogada: \n( 1 ) Pedra\n( 2 ) Papel\n( 3 ) Tesoura\n'))
if jogador not in [1, 2, 3]:
    print('Jogada inválida! Tente outra vez.')
else:
    print('Ok! Você escolheu: \033[1m{}\033[m!\n'.format(jogada[jogador]))
    computador = randint(1,3)
    print('O computador escolheu: \033[1m{}\033[m!\n'.format(jogada[computador]))
    if(jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        print('\033[1m{}\033[m x \033[1m{}\033[m = \033[1m{}\033[m! Você ganhou!'.format(jogada[jogador], jogada[computador], jogada[jogador]))
    elif (jogador == computador):
        print('Empate! Tente outra vez.')
    else:
        print('\033[1m{}\033[m x \033[1m{}\033[m = \033[1m{}\033[m! O computador ganhou!\n'.format(jogada[jogador], jogada[computador], jogada[computador]))
