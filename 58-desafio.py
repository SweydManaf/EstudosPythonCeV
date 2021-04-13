from random import randint
n = randint(0, 10)
i = 0
c = 0 
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue advinhar qual foi?')
while i ==0:
    e = int(input('Qual e seu palpite?: '))
    if e > n:
        print('Menos... Tente mais uma vez')
    if e < n:
        print('Mais... Tente mais uma vez') 
    if e ==n:
        i = 1
    else:
         c +=1
print('Foram necessarios {} palpites para acertar.'.format(c))