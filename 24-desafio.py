from os import system
system('cls')
print('===== DESAFIO 24 =====')

nome = input('Informe nome de uma cidade: ').title().strip()
nome1 = nome.split()
print('A cidade {}, tem SANTO? {}'.format(nome, 'Santo' in nome1[0]))
