lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista. ')
                break
            pos +=1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')


"""lista = []
v = posição = 0
for pos, i in enumerate(range(0, 5)):
    valor = int(input("Digite um valor numérico: "))
    if pos == 0:
        lista.insert(len(lista), valor)
        print('Inserido ao final da lista')

    #segundo número
    elif pos == 1:
        if valor > lista[0]:
            lista.insert(len(lista), valor)
            print('Inserido ao final da lista')

        else:
            lista.insert(0, valor)
            print(f'O valor {valor} foi inserido na posição {lista.index(valor)} da lista.')

    #quarto numero:
    else:
        if v < len(lista):
            while True:
                if valor < lista[v-1] or v >= len(lista):
                    lista.insert(v, valor)
                    break
                v += 1
        lista.insert(v+1, valor)
        print(f'O valor {valor} foi inserido na posição {lista.index(valor)} da lista.')
        v = 0
print(f'Os valores digitados em ordem crescente foram {lista}')

"""# terceiro numero (checar se é maior):
"""elif pos == 2:
if valor > lista[pos - 1]:
    lista.insert(pos, valor)
    print(f'O valor {valor} foi inserido ao final da lista.')
elif valor < lista[pos - 2]:
    lista.insert(pos - 2, valor)
    print(f'O valor {valor} foi inserido na posição {lista.index(valor)} da lista.')
else:
    lista.insert(pos - 1, valor)
    print(f'O valor {valor} foi inserido na posição {lista.index(valor)} da lista.')"""
