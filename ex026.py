frase = str(input('Digite uma frase: ').lower().strip())
print('Quantas vezes aparece a letra "a": {}'.format(frase.count('a')))
print('Em que posição ela aparece pela primeira vez: {}'.format(frase.find('a')+1))
print('Em que posição ela aparece pela última vez: {}'.format(frase.rfind('a')+1))