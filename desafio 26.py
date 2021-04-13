from os import system
system('cls')
print('===== DESAFIO 26 =====')
frase = input('Informe a frase : ').upper().strip()
print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('A letra A aparece na posicao {} pela primeira vez.'.format(frase.find('A') + 1))
print('A letra A aparece na posicao {} pela ultima vez.'.format(frase.rfind('A') + 1))
