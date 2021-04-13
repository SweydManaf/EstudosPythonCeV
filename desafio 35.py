import os
os.system('cls')
print('===== Analisador de Triangulos =====')
m1 = float(input('Infome a primeira medida: '))
m2 = float(input('Informe a segunda medida: '))
m3 = float(input('Informe a terceira medida: '))

if m1+m2>m3 and m2+m3>m1 and m3+m1>m2:
    print('\033[33mAs suas rectas podem formar um triangulo.\033[m') 
else:
    print('\033[32mAs suas rectas nao podem formar um triangulo.\033[m')   
print('='*30)
