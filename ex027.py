nome = str(input('Digite o nome completo de uma pessoa: ')).strip()
print(nome)
print('Primeiro nome: {}'.format(nome.split()[0]))
print('Último nome: {}'.format(nome.split()[len(nome.split())-1]))
