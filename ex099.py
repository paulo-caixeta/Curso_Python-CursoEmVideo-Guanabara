"""Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""

from time import sleep

def linha():
    print('-=' * 20)

def maior(* tupla):
    linha()
    print('Analisando os valores passados...')
    for v in tupla:
        print(f'{v}', end=' ')
        sleep(0.3)
    print(f'- Foram informados {len(tupla)} valores ao todo. ')
    if len(tupla) != 0:
        maior = tupla[0]
        for v in tupla:
            if v > maior:
                maior = v
        print(f'O maior valor informado foi {maior}')
    linha() 
# Programa principal:
maior(3, 4, 1, 5, 9)
maior(3, 4, 7, 50, -9)
maior(2, -100)
maior()
