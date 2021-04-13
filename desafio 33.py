import math
print('===== \033[32mMAIOR E MENOR\033[m =====')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))

if n1>=n2 and n1>=n3:
    print('O numero {} e o maior.'.format(n1))
elif n2>=n1 and n2>=n3:
    print('O numero {} e o maior.'.format(n2))
elif n3>=n1 and n3>=n2:
    print('O numero {} e o maior.'.format(n3))
    
if n1<=n2 and n1<=n3:
    print('O numero {} e o menor.'.format(n1))
elif n2<=n1 and n2<=n3:
    print('O numero {} e o menor.'.format(n2))
elif n3<=n1 and n3<=n2: 
    print('O numero {} e o menor.'.format(n3))
