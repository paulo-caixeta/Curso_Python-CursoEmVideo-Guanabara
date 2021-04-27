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