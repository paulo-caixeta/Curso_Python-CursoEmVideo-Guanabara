# Continuação do ex061 (Termos de PA)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
i = 0
n = 10
novos = 1
while novos != 0:
    while i < n:
        PA = primeiro + razão * i
        i += 1
        print(PA, end=' -> ')
    print('FIM')
    novos = int(input('Deseja mostrar mais termos? Quantos? '))
    while i < (n + novos):
        PA = primeiro + razão * i
        i += 1
        print(PA, end=' -> ')
    print('FIM')