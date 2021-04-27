def moeda(p = 0, moeda = 'R$'):
    return (f'{moeda}{p:.2f}'.replace('.',','))


def metade(p = 0, formato=False):
    res = p/2
    return res if formato is False else moeda(res)


def dobro(p = 0, formato=False):
    res = p*2
    return res if formato is False else moeda(res)


def aumentar(p = 0, taxa = 0, formato=False):
    res = p * (1+taxa/100)
    return res if formato is False else moeda(res)


def diminuir(p = 0, taxa = 0, formato=False):
    res = p - (p * taxa/100)
    return res if formato is False else moeda(res)


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)