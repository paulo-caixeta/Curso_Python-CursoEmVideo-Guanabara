nome = input('Digite seu nome: ').strip()
print('Nome MAIÚSCULAS: {}'.format(nome.upper()))
print('Nome minúsculas: {}'.format(nome.lower()))
print('Qte letras sem espaços: {}'.format(len(nome)-nome.count(' ')))
print('Qte letras no primeiro nome: {} '.format(len(nome.split()[0])))

