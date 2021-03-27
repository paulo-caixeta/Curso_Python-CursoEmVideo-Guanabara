ação = 0
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
ação = int(input('''Escolha a ação desejada:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
        '''))
while ação != 5:
    if ação == 1:
        print('O resultado é {}'.format(n1 + n2))
        ação = int(input('''Escolha a ação desejada:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
        '''))
    elif ação == 2:
        print('O resultado é {}'.format(n1 * n2))
        ação = int(input('''Escolha a ação desejada:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
        '''))
    elif ação == 3:
        if n1 > n2:
            print('O maior número é: {}'.format(n1))
            ação = int(input('''Escolha a ação desejada:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
            '''))
        elif n2 > n1:
            print('O maior núméro é: {}'.format(n2))
            ação = int(input('''Escolha a ação desejada:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
        '''))
        else:
            print('Os números são iguais')
            ação = int(input('''Escolha a ação desejada:
            [1] somar
            [2] multiplicar
            [3] maior
            [4] novos números
            [5] sair do programa
            '''))
    else:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        ação = int(input('''Escolha a ação desejada:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
        '''))
print('Você saiu do programa.')

