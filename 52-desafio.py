n = int(input('Informe um numero inteiro: '))
v = 0
for c in range(1, n+1):
    if n%c==0:
        print('\033[33m{}'.format(c), end = ' ')
        v += 1
    else:
        print('\033[31m{}'.format(c), end= ' ')

print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, v))
if v == 2:
    print('Ele e primo')
else:
    print('Ele nao e primo')
    