def leiaInt(n):
    n = input(n)
    while n.isnumeric() == False:
        print('\033[31mERRO! Digite um numero inteiro valido.\033[m')
        n = input('Digite um numero: ')
    n = int(n)
    return n
            
    
#Programa principal
n = leiaInt('Dgite um numero: ')
print(f'Voce acabou de digitar o numero {n}')

#Colocar no YouTube