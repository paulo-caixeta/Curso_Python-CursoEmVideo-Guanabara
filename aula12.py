nome = str(input('Qual é seu nome? '))
if nome == 'Paulo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Chico':
    print('Seu nome é bem popular no Brasil.')
elif nome in ('Ana Cláudia Jéssica Juliana'):
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}.'.format(nome))