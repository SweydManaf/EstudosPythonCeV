from datetime import date
ano = int(input('Informe o ano? Coloque 0 para analisar o ano actual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}{}{}, e bissexto.'.format('\033[33m', ano, '\033[m' ))
else:
    print('O ano {}{}{}, nao e bissexto'.format('\033[31m', ano, '\033[m'))

    