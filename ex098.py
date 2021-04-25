"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep

def linha():
    sleep(0.5)
    print('-=' * 20)

def escreva(txt):
    caracteres = len(txt)
    print('=' * (caracteres + 4))
    print(f'  {txt}')
    print('=' * (caracteres + 4))

def contador(i, f, p):
    if p == 0:
        p = 1
    elif p < 0:
        p = -p
    print(f'Contagem de {i} até {f} de {p} em {p}:')  
    if f > i:
        for v in range(i, f+1, p):
            print(f'{v}', end=' ')
            sleep(0.1)
        print('FIM!')
    elif f < i:
        for v in range(i, f-1, -p):
            print(f'{v}', end=' ')
            sleep(0.1)
        print('FIM!')

# Programa principal:
escreva('CONTADOR')
linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
# Recebe parâmetros:
print(f'Agora é sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)
linha()
