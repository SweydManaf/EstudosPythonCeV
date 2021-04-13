from random import randint
from time import sleep
jogo = []
print('-'*30)
print(f'{"JOGO NA MEGA SENA":^30}')
print('-'*30)
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
print('-=' * 3, f'  SORTEANDO {jogos} JOGOS', '-=' *3)
for c in range(1, jogos+1):
    print()
    for i in range(0, 6):
        n = randint(1, 60) 
        while n in jogo:
            n = randint(0, 60)
        jogo.append(n)
    jogo.sort()
    print(f'Jogo {c}: {jogo}', end = ' ')
    sleep(1)
    jogo.clear()
print('\n-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')

# Colocar no YouTube
