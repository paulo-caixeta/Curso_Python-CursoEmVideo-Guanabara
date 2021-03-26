# Lê 6 números inteiros e mostra a soma dos pares
soma_par = 0
for c in range(1, 7):
    c = int(input('Digite um número inteiro: '))
    if c % 2 == 0:
        soma_par += c
print('A soma dos números pares digitados é {}'.format(soma_par))
