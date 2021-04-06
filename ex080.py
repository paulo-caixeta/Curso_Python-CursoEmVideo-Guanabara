lista = []
for pos, i in enumerate(range(0, 5)):
    valor = int(input("Digite um valor numérico: "))
    if pos == 0:
        lista.insert(len(lista), valor)
        print('Inserido ao final da lista')

    #segundo número
    if valor > lista[0]:
        lista.insert(len(lista), valor)
        print('Inserido ao final da lista')
    elif valor < lista[0]:
        lista.insert(0, valor)
        print(f'O valor {valor} foi inserido na posição {lista.index(valor)} da lista.')

    #terceiro numero:
    elif valor > lista[1]:
        lista.insert(len(lista), valor)
        print('Inserido ao final da lista')
    elif valor < lista[0]:
        lista.insert(0, valor)
        print(f'O valor {valor} foi inserido na posição {lista.index(valor)} da lista.')
    else:
        lista.insert(1, valor)
        print(f'O valor {valor} foi inserido na posição {lista.index(valor)} da lista.')

print(lista)
lista.sort()
print(lista)

