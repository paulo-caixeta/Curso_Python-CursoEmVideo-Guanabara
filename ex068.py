from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
n_user = int(input('Digite um valor de 0 a 10: '))
escolha_user = str(input('Par ou ímpar? [P/I] ')).upper()[0]
while escolha_user not in ('PI'):
    escolha_user = str(input('Par ou ímpar? [P/I] ')).upper()[0]
n_pc = randint(0,11)
resultado = n_user + n_pc
vitórias = 0
if resultado % 2 ==0:
    teste = 'P'
else:
    teste = 'I'
while teste == escolha_user:
    print(f'Você VENCEU! O PC escolheu {n_pc} e você escolheu {n_user}.')
    vitórias += 1
    print('Vamos jogar novamente...')
    n_user = int(input('Digite um valor de 0 a 10: '))
    escolha_user = str(input('Par ou ímpar? [P/I] ')).upper()[0]
    resultado = n_user + n_pc
    if resultado % 2 == 0:
        teste = 'P'
    else:
        teste = 'I'
print(f'Você PERDEU! O PC escolheu {n_pc} e você escolheu {n_user}.')
print(f'GAME OVER! Você venceu {vitórias} vezes')
print('FIM')
