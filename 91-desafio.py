from operator import itemgetter
from time import sleep
from random import randint
jogos = {'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'jogador3' : randint(1, 6),
        'jogador4' : randint(1, 6)
        }
ranking = list()
print('Valores sorteados: ')
for k, v in jogos.items():
    print(f'    O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== Ranking dos jogadores ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}o lugar: {v[0]} com {v[1]}.')
    sleep(1)
#GUANABARA SOLUCTION


    
    