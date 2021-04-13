#Lê vários números e insere em uma lista. Retorna quantos números digitados, lista ordenada decrescente e se contém o valor 5.
lista = []
while True:
    n = int(input('Digite um valor:  '))
    teste = str(input('Deseja continuar? [S/N]' )).upper().strip()
    lista.append(n)
    while teste not in ('SN'):
        teste = str(input('Resposta inválida. Deseja continuar? [S/N] ')).upper().strip()
    if teste == ('N'):
        break
print('-=' *30)
print(f'A) Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'B) Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'C) O valor 5 foi digitado e está na posição {lista.index(5)+1} (do maior pro menor).')
else:
    print('C) O valor 5 não foi identificado.')


