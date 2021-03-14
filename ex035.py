print('Digite a seguir 3 comprimentos de retas:')
a = int(input('Reta a: '))
b = int(input('Reta b: '))
c = int(input('Reta c: '))
modulo = b-c
if modulo < 0:
    modulo = modulo * (-1)
if modulo < a and a < (b+c):
    print('Estas retas podem formar um triângulo.')
else:
    print('Estas retas NÃO podem formar um triângulo.')