distancia = float(input('Qual a distância da viagem? '))
valor_km_curta = 0.5
valor_km_longa = 0.45
if distancia < 200:
    custo_viagem = valor_km_curta * distancia
else:
    custo_viagem = valor_km_longa * distancia 
print('Como o valor por Km é de R${:.2f} para viagens de até 200 km e R${:.2f} para viagens mais longas, sua viagem irá custar R${:.2f}.'.format(valor_km_curta, valor_km_longa, custo_viagem))