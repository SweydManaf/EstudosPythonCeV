x = ' \033[34mDESAFIO 07\033[m ' 
print('{:=^22}'.format(x))

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1+n2) /2 

print('A sua media e \033[36m{:.1f}\033[m'.format(media))