from os import system
system('cls')

p = float(input('Informe o preco: '))
print('''\033[32m========== \033[mCONDICAO DE PAGAMENTO \033[33m==========\033[m    
1) A vista dinheiro/cheque;
2) A vista no cartao;
3) 2x no cartao;
4) 3x ou mais no cartao.''')
print('='*43)
e = int(input('Como deseja pagar: '))
if e == 1:
    d = p - (p*(10/100))
    print(f'Voce pagara \033[33m{d}\033[m')
elif e == 2:
    d = p - (p*(5/100))
    print(f'Voce pagara \033[33m{d}\033[m')
elif e == 3:
    print('Sua compra sera parcelada em 2x de {} sem juros.'.format(p/2))
    print(f'Voce pagara \033[33m{p}\033[m no final') 
elif e == 4:
    parcela = int(input('Quantas parcelas? '))
    pa = p / parcela
    juros = pa * (20/100)
    print('Sua compra sera parcela em {}x de {} com juros'.format(parcela, pa+juros))
    print('Sua compra de {} vai custar {} no final.'.format(p, p+(p*(20/100))))
else:
    print('Opcao invalida de pagamento. Tente novamente!')
    print(f'Sua compra de {p} vai custar {p} no final')
    