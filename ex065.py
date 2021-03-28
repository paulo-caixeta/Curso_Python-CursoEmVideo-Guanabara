# Lê vários números inteiros calcula a média, o menor e o maior,
i = 1
continua = 'S'
soma = 0
maior = 0
menor = 0
while continua == 'S':
    n = int(input('Digite um número inteiro: '))
    i += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor or menor == 0:
        menor = n
    continua = str(input('Deseja continuar inserindo números? Digite [S] para sim e [N] para não.')).upper().strip()[0]
print('''Foram digitados \033[1;34m{}\033[m números, sendo:
Soma = \033[1;34m{}\033[m
Média = \033[1;34m{}\033[m
Maior = \033[1;34m{}\033[m
Menor = \033[1;34m{}\033[m'''.format(i-1, soma, soma/(i-1), maior, menor))


