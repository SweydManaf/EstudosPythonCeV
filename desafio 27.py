from os import system
system('cls')
print('===== DESAFIO 27 =====')
nome = input('Informe seu nome completo: ').title().split()
nome1 = len(nome)
nome1 = nome
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[len(nome)-1]))
