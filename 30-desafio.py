n = int(input('Informe um numero inteiro: '))
num = n % 2
if num == 0:
    print('O numero {}{}{} e par.'.format('\033[33m', n, '\033[m'))
else:
    print('O numero {}{}{} e impar.'.format('\033[31m', n, '\033[m'))