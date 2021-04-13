def maior(* n):
    from time import sleep
    maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for numero in n:
        print(numero, end = ' ', flush= True) ######ativar o sleep na def
        sleep(0.4)
        if numero > maior:
            maior = numero
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()