# Desafio 28 "melhorado", com o jogador tentando advinhar até que o computador acerte.
import random
from time import sleep
numero_pc = random.randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente advinhar...')
print('-=-' * 20)
sleep(1)
numero_user = int(input('Qual número escolhi? Digite um valor entre 0 e 10: '))
print('PROCESSANDO...')
sleep(0.5)
tentativas = 1
while numero_user != numero_pc:
    print('Errou! Tente novamente!')
    tentativas += 1
    numero_user = int(input('Qual número escolhi? Digite um valor entre 0 e 10: '))
    print('PROCESSANDO...')
    sleep(1)
print('Parabéns!! Após \033[1;34m{}\033[m tentativas, você advinhou! O PC também escolheu \033[1;34m{}\033[m.'.format(tentativas, numero_pc))