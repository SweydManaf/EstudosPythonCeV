s = float(input('Informe o seu salario: '))
if s > 1250:
    a = s + (s * (10/100))
    print('O seu novo salario sera R${}{:.2f}{}.'.format('\033[33m', a, '\033[m'))
else:
    a = s + (s * (15/100))
    print('O seu novo salario sera R${}{:.2f}{}.'.format('\033[33m', a, '\033[m'))
    
    