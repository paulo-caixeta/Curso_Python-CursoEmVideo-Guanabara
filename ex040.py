# Lê duas notas de um aluno, calcula a média e retorna se está aprovado ou não.
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluna: '))
média = (nota1+nota2)/2
if média < 5.0:
    print('A média obtida foi \033[31m{:.1f}\033[m: \033[1;31mREPROVADO\033[m'.format(média))
elif 5.0 <= média and média <= 6.9:
    print('A média obtida foi \033[33m{:.1f}\033[m: \033[1;33mRECUPERAÇÃO\033[m'.format(média))
else:
    print('A média obtida foi \033[32m{:.1f}\033[m: \033[1;32mAPROVADO\033[m'.format(média))