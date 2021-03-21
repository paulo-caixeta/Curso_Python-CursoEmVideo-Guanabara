# Compara dois números inteiros e diz qual é maior.
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
if numero1 > numero2:
    print('O primeiro valor ({}) é MAIOR'.format(numero2))
elif numero2 > numero1:
    print('O segundo valor ({}) é MAIOR'.format(numero2))
else:
    print('Não existe valor maior. Os dois são iguais.')