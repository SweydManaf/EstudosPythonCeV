n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))
if n1 > n2:
    print('O primeiro numero e o maior.')
elif n2 > n1:
    print('O segundo numero e o maior.')
else:
    print('Nao existe valor maior, os dois sao iguais.')