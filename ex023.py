numero = int(input('Digite um número de 0 a 9999: '))

if numero < 1000:
    numero = numero + 1000
    numero = str(numero)
    print('Unidade: ', numero[3])
    print('Dezena: ', numero[2])
    print('Centena: ', numero[1])
    print('Milhar: ', int(numero[0])-1)

else:
    numero = str(numero)
    print('Unidade: ', numero[3])
    print('Dezena: ', numero[2])
    print('Centena: ', numero[1])
    print('Milhar: ', int(numero[0]))

print('Testando métudo matemático:')
numero = int(numero)
unidade = numero % 10
dezena = numero % 100 // 10
centena = numero % 1000 // 100
milhar = numero % 10000 // 1000
print('Unidade = {}'.format(unidade))
print('Dezena = {}'.format(dezena))
print('Centena = {}'.format(centena))
print('Milhar = {}'.format(milhar))



