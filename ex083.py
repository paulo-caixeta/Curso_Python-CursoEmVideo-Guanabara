expressão = str(input('Digite uma expressão: ')).strip()
termos = []
for t in expressão:
    if t == '(':
        termos.append('(')
    elif t == ')':
        if len(termos) > 0:
            termos.pop()
        else:
            termos.append(')')
            break
if len(termos) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')