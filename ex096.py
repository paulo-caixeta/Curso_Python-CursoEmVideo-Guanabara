"""Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""

def area(l, c):
    area = l * c
    print(f'A área de um terreno {l} x {c} é de {area} m².')

# Programa principal:
print('-=' * 20)
print('Controle de Terrenos')
print('-=' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)