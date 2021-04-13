listaCompleta = []
listaPar = []
listaImpar = []
while True:
    n = int(input('Digite um valor:  '))
    listaCompleta.append(n)
    teste = str(input('Deseja continuar? [S/N]' )).upper().strip()
    while teste not in ('SN'):
        teste = str(input('Resposta inválida. Deseja continuar? [S/N] ')).upper().strip()
    if teste == ('N'):
        break
for i, v in enumerate(listaCompleta):
    if v % 2 == 0:
        listaPar.append(v)
    else:
        listaImpar.append(v)
    print(listaPar)
print('-=' * 30)
print(f'Lista completa: {listaCompleta}')
print(f'Lista de pares: {listaPar}')
print(f'Lista de ímpares: {listaImpar}')
