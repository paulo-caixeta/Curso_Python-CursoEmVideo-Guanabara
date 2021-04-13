palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'ptraticar', 'trabalhar', 'mercado', 'programador')
print(palavras)
for pos, palavra in enumerate(palavras):
    print(f'\nNa palavra {palavras[pos].upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')