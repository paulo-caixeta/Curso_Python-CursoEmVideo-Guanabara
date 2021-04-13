# Continuação do ex061 (Termos de PA)
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
i = 0
n = 10
novos = 10
total = 0
while novos != 0:
    total = total + novos
    while i < total:
        termo = primeiro + razão * i
        i += 1
        print(termo, end=' -> ')
    print('PAUSA')
    novos = int(input('Deseja mostrar mais termos? Quantos? '))
print('FIM')