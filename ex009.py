n = int(input('Digite um número inteiro: '))
i = 1
print('='*20)
while i<10:
    print('{} x {} = {:2}'.format(n, i, n*i))
    i = i + 1
print('='*20)
