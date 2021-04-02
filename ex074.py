from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'A tupla gerada aleatoriamente foi: {tupla}')
for pos, numero in enumerate(tupla):
    print(f'Numero {pos+1}: {numero}')
print(f'O maior número gerado é: {max(tupla)}')
print(f'O menor número gerado é: {min(tupla)}')