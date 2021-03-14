salario = float(input('Qual o salário do funcionário? '))
aumento1 = 0.1
aumento2 = 0.15
if salario <= 1250:
    aumento = aumento2 * salario
else:
    aumento = aumento1 * salario
print('O aumento será de R${:.2f}'.format(aumento))