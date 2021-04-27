"""Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""

from moeda import metade, dobro, aumentar, diminuir

preço = float(input('Digite o preço: R$'))
print(f'A metade de {preço} é R${metade(preço)}.')
print(f'O dobro de {preço} é R${dobro(preço)}.')
print(f'Aumentando 10%, temos R${aumentar(preço, 10)}.')
print(f'Diminuindo em 30%, temos R%{diminuir(preço, 30)}')