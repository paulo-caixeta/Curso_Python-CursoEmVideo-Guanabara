print('Digite a seguir 3 comprimentos de retas:')
a = int(input('Reta a: '))
b = int(input('Reta b: '))
c = int(input('Reta c: '))
modulo = b-c
if modulo < 0:
    modulo = modulo * (-1)
if modulo < a and a < (b+c):
    print('Estas retas podem formar um triângulo.')
    if a == b == c:
        print('O triângulo formado é \033[1mEQUILÁTERO\033[m')
    elif a != b and a != c:
        print('O triângulo formado é \033[1mESCALENO\033[m')
    else:
        print('O triangulo formado é \033[1mISÓCELES\033[m')
else:
    print('Estas retas NÃO podem formar um triângulo.')


# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes