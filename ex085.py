"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""
lista = [[], []]
# lista = [[pares], [impares]]
for i in range (0, 7):
    n = int(input(f'Digite o {i+1}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print('-=' * 25)
print(f'Os números pares digitados foram: {lista[0]}')
print(f'Os números impares digitados foram: {lista[1]}')
    