"""Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""
registro = dict()
cadastro = list()
listaMulheres = list()
listaAcimaMed = list()
while True:
    registro['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    registro['sexo'] = sexo
    registro['idade'] = int(input('Idade: '))
    cadastro.append(registro.copy())
    #jeito difícil:
    if sexo == 'F':
        listaMulheres.append(registro['nome'])
    registro.clear()
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
print(cadastro)
soma = 0
for i, v in enumerate(cadastro):
    soma = soma + cadastro[i]['idade']
média = soma/len(cadastro)
#jeito difícil:
for i, v in enumerate(cadastro):
    if cadastro[i]['idade'] > média:
        listaAcimaMed.append(cadastro[i]['nome'])
print('-=' * 30)
print(f'A) Foram cadastradas {len(cadastro)} pessoas.')
print(f'B) A média de idade das pessoas cadastradas é: {média:.2f}.')
print(f'C) A lista de mulheres é: ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) A lista de pessoas com idade acima da média é: ', end='')
for p in cadastro:
    if p['idade'] >= média:
        print(f'{p["nome"]} | Sexo: {p["sexo"]} | Idade: {p["idade"]}.')
        print()
