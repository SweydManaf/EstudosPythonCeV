velocidade = int(input('Informe a velocidade do carro (km): '))
if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print('Voce foi multado')
    print('Voce pagara uma multa de R${}.'.format(multa))
else:
    print('Tenha uma boa viagem')