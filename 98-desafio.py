from time import sleep

def contador(inicio, fim, passo):
    
    print('-='*30)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    sleep(1)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        actual = inicio
        while actual <= fim:
            print(f'{actual}', end=' ', flush = True)
            sleep(0.4)
            actual += passo
        print('FIM!')

    else:
        actual = inicio
        while actual >= fim:
            print(f'{actual}', end=' ', flush=True)
            sleep(0.4)
            actual -= passo
        print('FIM!')
            
            
contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Inicio: '))
f = int(input('Fim:    '))
p = int(input('Passo:   '))
contador(i, f, p)
#GUANABARA SOLUCTION