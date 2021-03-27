# Lê o primeiro termo e a razão de uma PA utilizando comando While
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
i = 0
while i < 10:
    PA = primeiro + razão * i
    i += 1
    print(PA, end=' -> ')
print('FIM')