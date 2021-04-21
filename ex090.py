"""Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""

lista = dict()
situação = str()
lista['Nome'] = str(input('Nome do aluno: '))
lista['Média'] = float(input('Média do aluno: '))
if lista['Média'] >= 7.0:
    situação = 'Aprovado'
elif lista['Média'] >= 5:
    situação = 'Recuperação'
else:
    situação = 'Reprovado'
lista['Situação'] = situação
print(lista)
print('-=' * 25)
#Jeito burro de fazer:
"""print(f'O nome do aluno é {lista["Nome"]}')
print(f'A sua média é {lista["Média"]}')
print(f'Sua situação é {lista["Situação"]}')"""
#Jeito inteligente:
for k, v in lista.items():
    print(f' - {k} é igual a {v}.')