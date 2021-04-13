import random, time, os
os.system('cls')
m = random.randint(1, 3)
if m == 1:
    pc = 'PEDRA'
elif m == 2:
    pc= 'PAPEL'
elif m == 3:
    pc = 'TESOURA'

print('\033[32m===== \033[mJOKENPO\033[32m =====\033[m')
print('''1) PEDRA
2) PAPEL
3) TESOURA''')
print('\033[32m='*19)
print('\033[m', end = '')
escolha = int(input('Qual sua jogada: '))
time.sleep(0.5)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(0.3)
if escolha == m:
    print(f'Tivemos um empate voce escolheu {pc} e eu escolhi {pc}.')
elif escolha==1 and m ==2:
    print(f'VOCE PERDEU. Voce escolheu PEDRA  e eu escolhi {pc}')
elif escolha==1 and m ==3:
    print(f'VOCE VENCEU. Voce escolheu PEDRA  e eu escolhi {pc}')
elif escolha==2 and m==3:
    print(f'VOCE PERDEU. Voce escolheu PAPEL  e eu escolhi {pc}')
elif escolha==2 and m==1:
    print(f'VOCE VENCEU. Voce escolheu PAPEL  e eu escolhi {pc}')
elif escolha==3 and m==1:
    print(f'VOCE PERDEU. Voce escolheu PAPEL  e eu escolhi {pc}')
elif escolha==3 and m==2:
    print(f'VOCE PERDEU. Voce escolheu PAPEL  e eu escolhi {pc}')
else:
    print('\033[31mVOCE E UM GRANDE BATOTEIRO\033[m')
