tupla = (int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')))
par = 0
print(f'Você digitou os valores {tupla}')

#Quantas vezes apareceu o valor 9?
print(f'O valor 9 apareceu {tupla.count(9)}')

#Em que posição foi digitado o primeiro valor 3?
if tupla.count(3) == 0:
    print(f'O valor 3 não foi encontrado.')
else:
    print(f'O valor 3 apareceu na posição nº {tupla.index(3)+1}')

#Número de pares digitados:
for n in tupla:
    if n % 2 == 0:
        par += 1
print(f'A quantidade de pares digitados foi: {par}')
