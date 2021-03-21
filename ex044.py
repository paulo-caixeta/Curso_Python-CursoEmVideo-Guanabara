# Calcula o valor a ser pago por um produto em função da forma de pagamento
print('-==-' * 25)
print('\033[1mCÁLCULO DO VALOR FINAL DO PRODUTO\033[m')
print('-==-' * 25)
preço = float(input('\033[1mDigite o valor do produto: \033[m'))
print('\033[1m\nConfira as formas de pagamento:\033[m \n1) À vista (dinheiro ou cheque) = 10% desconto\n2) À vista (cartão) = 5% desconto\n3) Prazo - 2x (cartão) = 2x preço normal\n4) Prazo - 3x ou mais (cartão) = 20% juros\n')
forma = int(input('\033[1mDigite a opção desejada:\033[m '))
opção1 = 0.90
opção2 = 0.95
opção3 = 1.00
opção4 = 1.20
if forma == 1:
    print('O preço do produto é \033[1;32mR${:.2f}\033[m e, na forma de pagamento escolhida, sairá por: \033[1;34mR${:.2f}\033[m'.format(preço, opção1 * preço))
elif forma == 2:
    print('O preço do produto é \033[1;32mR${:.2f}\033[m e, na forma de pagamento escolhida, sairá por: \033[1;34mR${:.2f}\033[m'.format(preço, opção2 * preço))
elif forma == 3:
    print('O preço do produto é \033[1;32mR${:.2f}\033[m e, na forma de pagamento escolhida, sairá por: \033[1;34mR${:.2f}\033[m'.format(preço, opção3 * preço))
elif forma == 4:
    print('O preço do produto é \033[1;32mR${:.2f}\033[m e, na forma de pagamento escolhida, sairá por: \033[1;34mR${:.2f}\033[m'.format(preço, opção4 * preço))
elif forma not in [1, 2, 3, 4]:
    print('Forma de pagamento não identificada. Tente outra vez.')
from time import sleep
sleep (1)
print('')
print('Obrigado pela preferência!')
