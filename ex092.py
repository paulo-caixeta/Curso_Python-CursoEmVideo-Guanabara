"""Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar"""
from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Ano nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['CTPS'] = int(input("Nº da CTPS: (Digite 0 se não tiver CTPS: "))
if cadastro['CTPS'] != 0:
    cadastro['ano_contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: R$'))
    cadastro['ano_aposentadoria'] = cadastro['ano_contratação'] + 35
    cadastro['idade_aposentadoria'] = cadastro['ano_aposentadoria'] - nasc
print('-=' * 25)
for k, v in cadastro.items():
    print(f'   - {k} tem o valor {v}')
