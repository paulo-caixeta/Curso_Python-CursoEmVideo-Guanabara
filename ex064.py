# Soma vários números inteiros e para após digitar 999. Ainda, o programa calcula a soma e quantos números foram digitados.
i = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    i += 1
    soma += n
print('Foram digitados \033[1;34m{}\033[m números cuja soma é igual a \033[1;34m{}\033[m'.format((i-1), (soma-999)))
