"""Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""



def voto(anoNascimento):
    from datetime import date
    idade = date.today().year - anoNascimento
    if idade < 16:
        return(f'Com {idade} anos: VOTO NEGADO.')
    elif 18 <= idade < 65:
        return(f'Com {idade} anos: VOTO OBRIGADO.')
    else:
        return(f'Com {idade} anos: VOTO OPCIONAL.')

anoNascimento = int(input('Em que ano você nasceu? '))
print(voto(anoNascimento))

