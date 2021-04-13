import random
print('===== DESAFIO 20 =====')
n1 = input('Informe o primeiro nome: ').capitalize()
n2 = input('Inform o segundo nome: ').capitalize()
n3 = input('Informe o terceiro nome: ').capitalize()
n4 = input('Informe o querto nome: ').capitalize()
sorte = [n1, n2, n3, n4]
random.shuffle(sorte)
print('A ordem de apresentacao sera')
print(sorte)
