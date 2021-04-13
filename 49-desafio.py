n = int(input('Informe o numero: '))
print(f'\n===== TABUADA DE {n} =====')
for c in range(0, 11):
    print('{} x {:2} = \033[33m{}\033[m'.format(n, c, n*c))
print('='*20)