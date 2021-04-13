from os import system
system('cls')
print('===== DESAFIO 25 =====')
nome = input('Informe o nome: ').upper().strip()
print('O seu nome tem SILVA? {}'.format('SILVA' in nome))