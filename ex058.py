# Desafio 28 "melhorado", com o jogador tentando advinhar até que o computador acerte.
import random
from time import sleep
numero_pc = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
sleep(1)
numero_user = int(input('Qual número escolhi? Digite um valor entre 0 e 5: '))
print('PROCESSANDO...')
sleep(1)
tentativas = 1
while numero_user != numero_pc:
    print('Errou! Tente novamente!')
    tentativas += 1
    numero_user = int(input('Qual número escolhi? Digite um valor entre 0 e 5: '))
    print('PROCESSANDO...')
    sleep(1)
print('Parabéns!! Após {} tentativas, você advinhou! O PC também escolheu {}'.format(tentativas, numero_pc))