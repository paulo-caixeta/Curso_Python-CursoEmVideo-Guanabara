nome = str(input('Digite o nome completo de uma pessoa: ')).strip()
nome = nome.lower()
if nome.find('silva') == (-1):
    print('{} NÃO POSSUI "Silva" no nome.'.format(nome))
else:
    print('{} POSSUI "Silva" no nome.'.format(nome))