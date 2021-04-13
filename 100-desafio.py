from time import sleep
from random import randint


def sorteia():
    print(f'Sorteando 5 valores da lista:', end = ' ')
    for n in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[n],end = ' ', flush=True)
        sleep(0.4)
    print('PRONTO!')
    
    
def somaPar():
    soma = 0
    for n in numeros:
        if n%2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}', end =' ')
    
#Programa principal    
numeros = list()    
sorteia()
somaPar()
