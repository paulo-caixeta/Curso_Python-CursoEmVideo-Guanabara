import random
nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('Digite o nome do aluno 2: ')
nome3 = input('Digite o nome do aluno 3: ')
nome4 = input('Digite o nome do aluno 4: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))
