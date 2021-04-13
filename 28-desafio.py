import random, time, os
os.system('cls')
num = random.randint(0,5)
print('-='*30)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-='*30)
n = int(input('Em que numero eu pensei?: '))
print('Processando...')
time.sleep(3)
if n == num:
    print('Parabens! Voce conseguiu me vencer.')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}!.'.format(num, n))
