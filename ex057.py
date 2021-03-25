# Lê o sexo da pessoa, mas só aceita valores 'M' ou 'F'.
sexo = str(input('Digite o sexo (Masculino = [M] / Feminino = [F]): ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Sexo não identificado. Favor tentar novamente.')
    sexo = str(input('Digite o sexo (Masculino = [M] / Feminino = [F]): ')).upper()
print('Obrigado')
