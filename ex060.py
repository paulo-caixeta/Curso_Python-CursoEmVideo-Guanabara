# O programa lê um número e mostra o seu fatorial
numero = int(input('Digite um número: '))
i = numero
while i > 1:
    resultado =  i
    i = i - 1
    resultado = resultado * (i-1)6
print(resultado)