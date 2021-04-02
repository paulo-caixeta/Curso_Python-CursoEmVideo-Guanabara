rankingPEC = ('João Pedro', 'Lucas Ribas', 'Adriano Gontijo', 'Ricardo Delgado',
              'João Raphael', 'Sergio Borges', 'Breno Queiroz', 'Robinson Contins',
              'Abraao Moura', 'Vitor Torres', 'Gabriel Pereira', 'Tiago Teixeira',
              'Douglas Silva', 'Guilherme Alves', 'Leonardo Assis', 'Lucas Anjos',
              'Celton Nunes', 'Antonio Coroinha', 'Sylvio Colle', 'Marcelo Fortunato')
print('=-=' * 20)
título = '\033[1;37;40mR a n k i n g  P E C  -  P R O \033[m'
print('{:^20}'.format(título))
print('=-=' * 20)
print('\033[1;34mA) TOP 5\033[m')
for atleta in range(0, 5):
    print(f'#{atleta+1} = {rankingPEC[atleta]}')
print('-' * 30)
print('\033[1;34mB) 4 ÚLTIMOS DO #TOP20\033[m')
for atleta in range(16, 20):
    print(f'#{atleta+1} = {rankingPEC[atleta]}')
print('-' * 30)
print('\033[1;34mC) ORDENADOS POR ORDEM ALFABÉTICA 5\033[m')
print(sorted(rankingPEC))
print('-' * 30)
print('\033[1;34mD) QUAL POSIÇÃO ESTÁ VITOR TORRES?\033[m')
print(f"{rankingPEC.index('Vitor Torres')+1}ª posição.")
