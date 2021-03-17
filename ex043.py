# Cálculo do IMC
print('-==-' * 25)
print('CÁLCULO DO IMC (Índice de Massa Corporal)')
print('-==-' * 25)
peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura * altura)
print('Seu \033[1mIMC\033[m é de \033[1;32m{:.2f}\033[m, considerado:'.format(imc))
if imc < 18.5:
    print('\033[1;33mAbaixo do Peso.\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[1;32mPeso Ideal.\033[m')
elif imc >= 25 and imc < 30:
    print('\033[1;33mSobrepeso.\033[m')
elif imc >= 30 and imc < 40:
    print ('\033[1;33mObesidade.\033[m')
else:
    print('\033[1;31mObesidade mórbida.\033[m')