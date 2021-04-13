from random import randint
from os import system
c = 0
#Limpa tela
system('cls')
print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
#Loop do programa
while True:
    n = int(input('Diga um valor: '))
    computador = randint (0, 10)
    
    while True:
        decisao = str(input('Par ou impar [P/I] ')).upper()
        if decisao in 'PI':
            break
        else:
            print('Por favor escolha par ou impar')
    
    if (n + computador) % 2 == 0:
        print('-'*40)
        print(f'Voce jogou {n} e o computador {computador}. Total {n+computador} deu PAR')
        if decisao == 'P':
            print('=-'*20)  
            print('Voce venceu')
            c += 1
        elif decisao == 'I':
            print('Voce perdeu')
            print('=-'*20)
            print(f'GAME OVER! Voce venceu {c} vezes')
            break
    else:
        print('-'*40)
        print(f'Voce jogou {n} e o computador {computador}. Total {n+computador} deu IMPAR')
        print('-'*40)
        if decisao == 'I':
            print('=-'*20)  
            print('Voce venceu')
            c += 1
        elif decisao == 'P':
            print('Voce perdeu')
            print('=-'*20)
            print(f'GAME OVER! Voce venceu {c} vezes')
            break
    print('='*20)
    
#SOLUCAO ORIGINAL COM 28 LINHAS