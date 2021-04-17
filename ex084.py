"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
print('-=' * 25)
print('CADASTRO DE PESSOAS'.center(50))
print('-=' * 25)
pessoas = list()
dados = list()
tot_pessoas = 0
pesadas = list()
leves = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (Kg): ')))
    pessoas.append(dados[:])
    tot_pessoas += 1
    dados.clear()
    continua = (str(input('Deseja continuar? [S/N]'))).upper().strip()
    while continua not in ('SN'):
        continua = (str(input('Não entendi. Deseja continuar? [S/N]'))).upper().strip()
    if continua == 'N':
        break
print('-=' * 25)
print('RESUMO CADASTRO'.center(50))
print('-=' * 25)
maior_peso = menor_peso = pessoas[0][1]
for p in pessoas:
    print(f'{p[0]}: {p[1]} Kg.')
    if p[1] > maior_peso:
        maior_peso = p[1]
    if p[1] < menor_peso:
        menor_peso = p[1]
for p in pessoas:
    if p[1] == maior_peso:
        pesadas.append(p[0])
    if p[1] == menor_peso:
        leves.append(p[0])
print('-' * 50)
print(f'A) Foram cadastradas {tot_pessoas} pessoas.')
print(f'B) O maior peso é {maior_peso} Kg e a lista das pessoas mais pesadas é: {pesadas}.')
print(f'C) O menor peso é {menor_peso} Kg e a lista das pessoas mais leves é: {leves}.')