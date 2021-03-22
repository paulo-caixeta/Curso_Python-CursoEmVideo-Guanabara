print('Digite o ano de nascimento de cada pessoa: ')
from datetime import date
pessoas_nascimento = []
pessoas_idade = []
pessoas_maioridade = 0
pessoas_menoridade = 0
for c in range(1,8):
    print('Pessoa',(c),': ')
    nascimento = int(input())
    idade = date.today().year - nascimento
    pessoas_nascimento += [nascimento]
    pessoas_idade += [idade]
    if idade >= 21:
        pessoas_maioridade = pessoas_maioridade + 1
    else:
        pessoas_menoridade = pessoas_menoridade + 1
# print(pessoas_nascimento)
# print(pessoas_idade)
print('O total de pessoas com maioridade é: {}'.format(pessoas_maioridade))
print('O total de pessoas com maioridade é: {}'.format(pessoas_menoridade))