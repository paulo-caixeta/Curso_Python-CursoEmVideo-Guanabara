loja = ('loja super baratão').upper()
print('='*25)
print(f'{loja:^25}')
print('='*25)
continua = 'S'
total = 0
cont1000 = cont = 0
produto_barato = ''
menor = 0
lista_preços = []
while continua == 'S':
    produto = str(input('Nome do Produto: ')).lower().strip()
    preço = float(input('Preço = R$'))
    total += preço
    cont += 1
    if preço > 1000:
        cont1000 +=1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    continua = str(input('Deseja continuar [S / N]?' )).upper()[0]
    if continua == 'N':
        break
    while continua != 'S':
        continua = str(input('Deseja continuar [S / N]?')).upper()[0]
print(f'''
Compra finalizada com sucesso. Resumo:
Total em compras: {total:.2f};
{cont1000} produtos custam mais de R$1.000,00;
O produto mais barato é o {produto_barato} e custa {menor:.2f}.
''')
