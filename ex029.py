velocidade = float(input('Digite a velocidade do carro: '))
valor_multa = 7.00
limite = 80
total_multa = (velocidade - limite)*valor_multa
if velocidade > limite:
    print('Xiii.. Você foi multado.')
    print('A multa será de R${:.2f}'.format(total_multa))
else:
    print('Ufa!! Você não foi multado')