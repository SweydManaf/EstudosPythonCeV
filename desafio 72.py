extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'catorze', 'quinze', 'dezasseis','dezasete', 'dezoito', 'dezanove',
           'vinte')
numero = int(input('Digte um numero ente 0 e 20: '))
while numero <0  or numero > 20:
    numero = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Voce digitou o numero {extenso[numero]}')
