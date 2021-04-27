"""Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""

from moeda import metade, dobro, aumentar, diminuir, moeda

preço = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(preço)} é {metade(preço, True)}.')
print(f'O dobro de {moeda(preço)} é {dobro(preço, True)}.')
print(f'Aumentando 10%, temos {aumentar(preço, 10, True)}.')
print(f'Diminuindo em 30%, temos {diminuir(preço, 30, True)}')