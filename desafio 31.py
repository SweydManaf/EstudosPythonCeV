d = int(input('Informe a distancia percorida em km: '))
v = d * 0.5 if d < 200 else d * 0.45
print('A sua passagem custa R${}{}{}.'.format('\033[7;37m', v, '\033[m'))



'''if d < 200: 
    v = d * 0.5
    print('A sua passagem custa R${}'.format(v))
else:
    v = d * 0.45
    print('A sua passagem custa R${}'.format(v))'''