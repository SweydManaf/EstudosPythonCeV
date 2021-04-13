x = ' \033[33mDESAFIO 06\033[m '
print('{:=^22}'.format(x))
n = float(input('Digite um numero: '))
print('O dobro e \033[34m{}\033[m'.format(n*2))
print('O triplo e \033[34m{}\033[m'.format(n*3))
print('A raiz quadrada e \033[34m{:.1f}\033[m'.format(n**(1/2)), end='!!!')