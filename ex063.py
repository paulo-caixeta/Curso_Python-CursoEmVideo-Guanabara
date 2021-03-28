# Lê um número inteiro n e mostra os n primeiros elementos de uma Sequencia de Fibonacci
print('-=-' * 10)
print('SEQUENCIA DE FIBONACCI')
print('-=-' * 10)
n = int(input('Quantos termos você quer mostrar? '))
i = 0
i0 = 0
i1 = 1
print('Esta é a Sequencia de Fibonacci para os {} primeiros termos:'.format(n))
print('0 -> 1 -> ', end='')
while i < (n-1):
    i2 = i0 + i1
    i0 = i1
    i1 = i2
    i += 1
    print('{}'.format(i2), end=' -> ')
print('FIM')

