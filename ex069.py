print('='*25)
print('  CADASTRE UMA PESSOA')
print('='*25)
continua = 'S'
cont_pessoa = 0
cont_homem = 0
cont_mulher20 = 0
while continua == 'S':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo não identificado. Tente novamente [M/F]: ')).upper()[0]
    if idade >= 18:
        cont_pessoa += 1
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher20 += 1
    continua = str(input('Deseja continuar [S / N]?' )).upper()[0]
    if continua == 'N':
        break
    while continua != 'S':
        continua = str(input('Deseja continuar [S / N]?')).upper()[0]
    print('-'*20)
print('='*20)
print('RESUMO DO CADASTRO:')
print(f'''
Pessoas com mais de 18 anos: {cont_pessoa}
Homens cadastrados: {cont_homem}
Mulheres com menos de 20 anos: {cont_mulher20}
''')
print('='*20)
print('CADASTRO CONCLUÍDO')
print('='*20)