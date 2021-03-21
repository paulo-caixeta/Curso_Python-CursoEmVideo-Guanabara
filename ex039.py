# Avalia o status de alistamente de um jovem.
import datetime
nascimento = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - nascimento
tempo = 18 - idade
print('Você possui \033[1;34m{} anos\033[m.'.format(idade))
if idade < 18:
    print('Você deve se alistar ao serviço militar em {} anos.'.format(tempo))
elif idade == 18:
    print('Você possui idade para alistamento ao serviço militar.')
else:
    print('\033[1;31mAtenção!\033[mJá passou o seu tempo de alistamento em \033[4m{} anos\033[m.'.format(-1 * tempo))
