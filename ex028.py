import random
from time import sleep
numero_pc = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
sleep(2)
numero_user = int(input('Qual número escolhi? Digite um valor entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if numero_pc == numero_user:
    print('Parabéns, você advinhou!. O PC também escolheu {}'.format(numero_pc))
else:
    print('Errou! Você escolheu {} e o PC escolheu {}'.format(numero_user, numero_pc))