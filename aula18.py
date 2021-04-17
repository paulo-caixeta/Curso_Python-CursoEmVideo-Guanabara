galera = list()
dado = list()
tot_maior = tot_menor = 0
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        tot_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        tot_menor +=1
    
print(f'Temos {tot_maior} maiores e {tot_menor} menores de idade.')