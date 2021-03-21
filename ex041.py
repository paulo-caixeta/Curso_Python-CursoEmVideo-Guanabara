# Define categorias de natação com base na idade.
from datetime import date
nascimento = int(input('Digite a data de nascimento do atleta: '))
idade = date.today().year - nascimento
print('Idade: {}'.format(idade))
print('A Categoria do atleta é: ')
if idade < 9:
    print('\033[1mMirim\033[m')
elif idade < 14:
    print('\033[1mInfantil\033[m')
elif idade < 19:
    print('\033[1mJunior\033[m')
elif idade < 20:
    print ('\033[1mSênior\033[m')
else:
    print('\033[1mMaster\033[m')