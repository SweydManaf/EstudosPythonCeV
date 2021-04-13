from math import cos, tan, sin, radians
print('===== DESAFIO 18 =====')
n = int(input('Informe o valor do angulo: '))
print('O seno de {} e {:.2f}'.format(n, sin(radians(n))))
print('O cosseno de {} e {:.2f}'.format(n, cos(radians(n))))
print('A tangete de {} e {:.2f}'.format(n, tan(radians(n))))