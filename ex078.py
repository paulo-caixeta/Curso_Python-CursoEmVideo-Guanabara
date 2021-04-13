lista = []
maior = 0
menor = 0
for pos, i in enumerate(range(1, 6)):
    lista.append(int(input("Digite um valor numérico: ")))
    if pos == 0:
        maior = menor = lista[pos]
    else:
        if lista[pos] > maior:
            maior = lista[pos]
        if lista[pos] < menor:
            menor = lista[pos]
print('-='* 30)
lista_ordenada = lista[:]
lista_ordenada.sort()
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições ' , end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ' , end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')