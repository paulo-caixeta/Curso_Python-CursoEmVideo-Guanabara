# Lê o primeiro termo e a razão de uma PA utilizando comando While
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
i = 0
while i < 10:
    termo = primeiro + razão * i
    i += 1
    print(termo, end=' -> ')
print('FIM')