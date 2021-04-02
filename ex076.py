produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 30)
for cont in range(0, len(produtos)-1, 2):
    print(f'{produtos[cont]:.<20}', f'R$ {produtos[cont+1]:>6.2f}')
print('-' * 30)