from datetime import date
ano = int(input('Informe o seu ano de nascimento: '))
y = date.today().year
a = y - ano
print('Quem nasceu em {} tem {} anos'.format(ano, a))
if a <= 9:
    print('MIRIM')
elif a <= 14:
    print('INFANTIL')
elif a <= 19:
    print('JUNIOR')
elif a <= 25: 
    print('Senior')
else:
    print('MASTER')