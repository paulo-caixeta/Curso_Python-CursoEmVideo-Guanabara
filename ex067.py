# Exercício de tabuada utilizando comando for e break.
titulo = 'TABUADA'
print(f'{titulo:-^25}')
n = int(input('Quer ver a tabuada de qual valor? '))
while n > 0:
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n*c))
    n = int(input('Quer ver a tabuada de qual valor? '))
print('FIM')
