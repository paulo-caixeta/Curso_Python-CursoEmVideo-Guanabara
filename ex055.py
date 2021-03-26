print('Digite o peso de cada pessoa: ')
pesos = []
for c in range (1,6):
    print('Pessoa', (c), ': ')
    peso = float(input())
    pesos += [peso]
pesos.sort()
print('O menor peso foi: {}'.format(pesos[0]))
print('O maior peso foi: {}'.format(pesos[len(pesos)-1]))
