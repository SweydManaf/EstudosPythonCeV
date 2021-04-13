from datetime import date
from os import system
system('cls')
ano = int(input('Informe o seu ano de nascimento:'))
y = date.today().year
a = y - ano
print(f'Quem nasceu em {ano} tem {a} em {y}')
if a > 18:
    print('Ja se passam {} ano de voce se alistar.'.format(a-18))
    print('Seu alistamento foi em {}'.format(y-(a-18)))
elif a < 18:
    print('Ainda nao e a hora de voce se alistar, falta {} ano para voce se alistar.'.format(18-a))
    print('Seu alistamento sera em {}'.format(y+(18-a)))

else:
    print('E a hora de voce se alistar.')