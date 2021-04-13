from time import sleep

def PyHELP(msg):
    print('\033[44m')    
    p = f"    Acessando o manual do comando '{msg}'"
    print('`' * (len(p)+4))
    print(f'{p}')
    print('`'* (len(p)+4))
    print('\033[7;40m')
    return help(msg)

#Programa Principal
while True:
    sleep(1)
    print('\033[m')
    print('\033[43m')
    p = '    SITEMA DE AJUDA PyHELP'
    print('`' * (len(p)+4))
    print(f'{p}')
    print('`'* (len(p)+4))
    print('\033[m')
    ajuda = str((input('Funcao ou biblioteca > ')).lower().strip())
    sleep(2)
    if ajuda == 'fim':
        print('\033[41m')
        fim = 'ATE LOGO'
        print('`' * (len(fim)+4))
        print(f'  {fim}')
        print('`'* (len(fim)+4))
        print('\033[m')
        break
    PyHELP(ajuda)