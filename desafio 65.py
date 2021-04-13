i = 0
c = 1
maior = 0
menor = 0
m = 0
s = 0
while i == 0:
    n = int(input('Informe o valor: '))
    s += n
    if c==1:
        menor = n
        maior = n
        c += 1
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n  
    
    d = str(input('Deseja comtinuar [y/n]: ')).lower()
    if d == 'n':
        i = 1
   
    m = m + 1
media = s/m
print('A media dos valores inserudis e {:.1f}'.format(media))
print('O maior valor e {}'.format(maior))
print('O menor valor e {}'.format(menor))