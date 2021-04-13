
n = '\033[32mDESAFIO 01\033[m'
print('-='*30)
print('{:^70}'.format(n))
print('-='*30)
nome = input("Qual e seu nome? ")
print('Ola \033[34m{}\033[m. Prazer em te conhecer!'.format(nome.capitalize()))
