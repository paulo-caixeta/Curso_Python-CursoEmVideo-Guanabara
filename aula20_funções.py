def dobra(lst):
    pos = 0
    while pos<len(lst):
        lst[pos] *= 2
        pos += 1


valores= [4, 4, 7, 6, 2]
dobra(valores)
print(valores)