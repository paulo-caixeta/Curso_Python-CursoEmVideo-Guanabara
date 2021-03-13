x = input('Digite algo: ')
print('"{}" é do tipo {}'.format(x, type(x)))
# Confere quantos caracteres
print('"{}" possui {} caracteres'.format(x, len(x)))

# Confere se é numérico, alfabético ou alfanumérico
if x.isnumeric():
    print('"{}" é do tipo numérico'.format(x))
elif x.isalpha():
    print('"{}" é do tipo alpha'.format(x))
else:
    print('"{}" é do tipo alphanumérico'.format(x))

# Confere se é maiúsculo ou minúsculo
maiusculo = x.isupper ()
minusculo = x.islower()
if maiusculo:
    print('"{}" é MAIÚSCULO'.format(x))
elif minusculo:
    print('"{}" é minúsculo'.format(x))
else:
    print('"{}" contém letras maiúsculas e minúsculas'.format(x))


