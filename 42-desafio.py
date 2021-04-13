r1 = float(input('Informe a primeira recta:'))
r2 = float(input('Informe a segunda recta: '))
r3 = float(input('Informe a terceira recta: '))
if r1+r2>r3 and r2+r3>r1 and r3+r1>r2:
    print('As suas rectas podem formar um triangulo', end=' ')
    if r1==r2!=r3 or r1==r3!=r2 or r2==r3!=r1:
        print('isosceles')
    elif r1==r2 and r1==r3:
        print('equilatero') 
    else:
        print('escaleno')
else:
    print('As suas rectas nao podem formar um triangulo.')   
