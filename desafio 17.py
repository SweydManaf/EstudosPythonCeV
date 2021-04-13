from math import hypot

print('===== DESAFIO 17 =====')
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
print('O comprimento da hipotenusa e {:.2f}'.format(hypot(ca, co)))
