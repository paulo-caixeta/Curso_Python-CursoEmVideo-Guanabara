lista = []
for pos, i in enumerate(range(1, 6)):
    lista.append(int(input("Digite um valor numérico: ")))
lista_ordenada = lista[:]
lista_ordenada.sort()
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {lista_ordenada[4]} na posição {lista.index(lista_ordenada[4])+1}')
print(f'O menor valor digitado foi {lista_ordenada[0]} na posição {lista.index(lista_ordenada[0])+1}')