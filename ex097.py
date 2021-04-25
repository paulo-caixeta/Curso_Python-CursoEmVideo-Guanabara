"""Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. """

def escreva(txt):
    caracteres = len(txt)
    print('~' * (caracteres + 4))
    print(f'  {txt}')
    print('~' * (caracteres + 4))


# Programa principal:
texto = str(input('Digite uma mensagem: '))
escreva(texto)