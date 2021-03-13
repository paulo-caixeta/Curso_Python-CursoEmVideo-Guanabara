cidade = str(input('Ditige o nome de uma cidade: ')).strip()
cidade2 = cidade.upper()
print('"{}" começa com "Santo"?'.format(cidade))
if cidade2.split()[0] == 'SANTO':
    print('SIM')
else:
    print('NÃO')
