# Lê nome, idade e sexo de 4 pessoas e mostra: média de idade do grupo, nome dohomem mais velho e quantas mulheres menores de 20 anos.
soma_idade = 0
maior_idade_homem = 0
media_idade = 0
qtd_mulher20 = 0
nome_velho = ''
for c in range(1,5):
    print('Pessoa', (c), ': ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Digite [ F ] para mulheres e [ M ] para homens: ')).strip()
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        qtd_mulher20 += 1
média_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(média_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho))
print('São {} mulheres com menos de 20 anos'.format(qtd_mulher20))
