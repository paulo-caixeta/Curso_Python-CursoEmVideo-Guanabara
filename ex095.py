"""Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""
histórico = dict()
temp = dict()
gols = list()
time = list()
while True:
    histórico['jogador'] = str(input('Nome do jogador: ' ))
    qde_partidas = int(input(f'Quantas partidas o {histórico["jogador"]} jogou? '))
    for i in range(0, qde_partidas):
        gols.append(int(input(f'   Quantos gols na partida {i+1}? ')))
        histórico['gols'] = gols[:]
    histórico['total'] = sum(gols)
    gols.clear()
    time.append(histórico.copy())
    temp = histórico.copy()
    histórico.clear()
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
print(time)
print('-=' * 25)
print(f'{"Cod":<5}', end='')
for i in temp.keys():
    print(f'{i:<20}', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for i in v.values():
        print(f'{str(i):<20}', end='')
    print()
print('-' * 50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["jogador"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')


"""print('-=' * 30)
for k, v in histórico.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {histórico["jogador"]} jogou {len(histórico["gols"])} partidas.')
for i, v in enumerate(histórico['gols']):
    print(f'   -> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {histórico["total"]} gols.')
print('-=' * 30)"""