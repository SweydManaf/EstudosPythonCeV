print('===== \033[34mDESAFIO 40\033[m =====')
n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))
m = (n1+n2)/2
print('Tirando {} e {}, a media do aluno e {:.1f}'.format(n1, n2, m))
if m < 5:
    print('\033[31mREPROVADO\033[m')
elif m >= 5 and m < 6.9:
    print('\033[33mRECUPERACAO\033[m')
elif m >= 7:
    print('\033[32mAPROVADO\033[m')