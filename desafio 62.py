primeiro = int(input('Inform o primeiro termo da PA: '))
razao = int(input('Informe a razao da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{primeiro} -> ', end = '')
        primeiro += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('FIM')

#Guanabara Soluction