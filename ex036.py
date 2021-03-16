import time
print(('-=-')*20)
print('ANÁLISE DE CRÉDITO')
print(('-=-')*20)
valor_imovel = float(input('Digite o valor do imóvel (R$): '))
salario = float(input('Digite o salário do solicitante (R$): '))
anos = int(input('Quantos anos para pagamento? '))
print('-'*20)
print('Aguarde. Análise em andamento...')
time.sleep(2)
print('---'*20)
meses = anos * 12
valor_parcela = valor_imovel / meses
if valor_parcela > 0.3 * salario:
    print('\033[31mSeu financiamento foi negado. O valor da parcela não pode ser inferior a 30% do salário do solicitante.\033[31m')
    print('O valor da parcela é de R${:.2f}, superior a 30% do salário do solicitante (R${:.2f})'.format(valor_parcela, 0.3 * salario))
    print('Defina um período maior para pagamento.')
else:
    print('Seu financiamento foi aprovado!')
    print('Quantidade de parcelas (meses): {}'.format(meses))
    print('Valor da parcela (R$): {:.2f}'.format(valor_parcela))