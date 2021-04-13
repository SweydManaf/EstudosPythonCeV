import random
print('===== DESAFIO 19 =====')
n1 = str(input('Informe o primeiro nome: '))
n2 = str(input('Informe o segundo nome: '))
n3 = str(input('Informe o terceiro nome: '))
n4 = str(input('Informe o quarto nome: '))
sorte = (n1, n2, n3, n4)
print('\nO {} vai apagar o quadro hoje.\n'.format(random.choice(sorte)))