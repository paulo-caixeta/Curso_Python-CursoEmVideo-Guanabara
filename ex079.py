lista = []
while True:
    elemento = int(input('Digite um valor numérico: '))
    if elemento not in lista:
        lista.append(elemento)
        continua = str(input('Deseja continuar [S/N]?')).upper().strip()
        while continua != 'N' and continua != 'S':
            continua = str(input('Deseja continuar [S/N]?')).upper().strip()
        if continua == 'N':
            break
    else:
        print(f'{elemento} já existe. Digite outro valor: ')
lista.sort()
print('-=' * 20)
print(f'A lista digitada, em ordem crescente, foi: {lista}')