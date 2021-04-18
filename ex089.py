'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
lista = list()
while True:
    aluno = str(input('Nome: ')).upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    lista.append([aluno, nota1, nota2, média])
    continua = str(input('Deseja continuar? [S/N]? ')).upper().strip()
    while continua not in 'SN':
        continua = str(input('Não entendi. Deseja continuar? [S/N]? ')).upper().strip()
    if continua == 'N':
        break
print('-=' * 20)
'''print(f'{"ID":<5}', end = '')
print(f'{"NOME":<15}', end = '')
print(f'{"MÉDIA":>5}')'''
# Impressão com várias strings formatados:
print(f'{"ID":<5}{"NOME":<15}{"MÉDIA":>8}')
print('-' * 40)
for id, i in enumerate(lista):
    print(f'{(id):<5}', end = '')
    print(f'{lista[id][0]:<15}', end = '')
    print(f'{lista[id][3]:>8.1f}')
print('-' * 40)
while True:
    escolhe_id = int(input('Mostrar notas de qual aluno? (Digite 999 para interromper) '))
    for id, i in enumerate(lista):
        if id == escolhe_id:
            print(f'As notas de {lista[id][0]} são {lista[id][1]} e {lista[id][2]}.')
    if escolhe_id == 999:
        print('Finalizando...')
        break
