nome = ' \033[32mDESAFIO 05\033[m '
print('{:=^22}'.format(nome))

n = int(input('Digite um  numero: '))
print('O seu antecessor e \033[33m{}\033[m. O seu sucessor e \033[33m{}\033[m.'.format(n-1, n+1))