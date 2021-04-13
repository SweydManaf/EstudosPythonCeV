print('===== DESAFIO 10 =====')

valor = float(input('Quantos reais voce tem? R$ '))
dolar = valor/3.27
print('Voce pode comprar US$\033[4;36m{:.2f}\033[m!'.format(dolar))