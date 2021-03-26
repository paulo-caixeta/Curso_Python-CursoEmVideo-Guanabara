# Programa lê uma frase e diz se é um palíndromo
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
frase_s_espaço = ''
for c in range(0, len(palavras)):
    frase_s_espaço = frase_s_espaço+palavras[c]
qde_letras = len(frase_s_espaço)
letras_inversa = ''
for b in range((qde_letras-1), -1, -1):
    letras_inversa = letras_inversa+frase_s_espaço[b]
if frase_s_espaço == letras_inversa:
    print('"{}" é um palíndromo.'.format(frase))
else:
    print('"{}" não é um palíndromo.'.format(frase))