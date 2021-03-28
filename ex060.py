n = int(input("Digite um número inteiro para calcular o seu fatorial: "))
print('{}! = '.format(n), end='')
fatorial = 1
while n >= 1:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    fatorial = fatorial * n
    n = n - 1
print('{}.'.format(fatorial))
