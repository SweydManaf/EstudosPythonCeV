peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura**2)
print('O IMC dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso')
elif imc < 25:
    print('Voce esta com peso ideial')
elif imc < 30:
    print('Voce esta acima do peso ideal')
elif imc < 40:
    print('Voce esta com obesidade')
else:
    print('Voce esta com obesidade morbida')
    