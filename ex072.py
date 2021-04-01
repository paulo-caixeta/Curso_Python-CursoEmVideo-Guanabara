numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numeral = int(input('Digite um número inteiro entre 0 e 20: '))
while numeral < 0 or numeral > 20:
    numeral = int(input('Digite um número inteiro entre 0 e 20: '))
print(f'Você digitou o número {numeros[numeral]}')