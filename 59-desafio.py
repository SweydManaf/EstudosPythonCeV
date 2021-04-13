from os import system
system('cls')
i  = 0 
n1 = float(input('Informe o primeiro numero: '))
n2 = float(input('Informe o segundo numero: '))
while i == 0:
    print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numero
[5] sair do programa ''')
    
    e = int(input('O_que voce deseja: '))
    print()
    if e == 1:
        print('A soma de {} e {} e {}'.format(n1, n2, n1+n2))
    elif e == 2:
        print('A multiplicacao de {} e {} e {}.'.format(n1, n2, n1*n2))
    elif e == 3:
        if n1 > n2:
            print('O {} e maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('O {} e maior que {}'.format(n2, n1))
        else:
            print('O numero {} e {} sao iguais'.format(n1, n2))
    elif e == 4:
        n1 = float(input('Informe o primeiro numero: '))
        n2 = float(input('Informe o segundo numero: '))
    elif e == 5:
        i = 1
    else:
        print('Informe uma opcao valida')