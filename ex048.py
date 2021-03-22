# Calcula a soma entre todos os ímpares que são múltiplos de três
soma_impar = 0
cont = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        cont += 1
        soma_impar += c
print('A soma dos {} ímpares múltiplos de 3 de 0 a 500 é {}'.format(cont, soma_impar))