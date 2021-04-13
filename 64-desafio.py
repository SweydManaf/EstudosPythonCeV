i = s = c= 0
n = int(input('Informe o valor, [999] para parar:'))
while n != 999:
    s = n + s
    n = int(input('Informe o valor, [999] para parar:'))
    c += 1
print('Voce digitou {} numeros'.format(c))
print('A soma dos valores introduzidos e {}'.format(s))