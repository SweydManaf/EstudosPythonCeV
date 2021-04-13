print('===== DESAFIO 11 =====')
altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
area = altura * largura
litros = area / 2
print('A quantidade de tinta necessaria para pintar \033[4m{:.2f}\033[m m^2  e \033[4m{:.2f}\033[m litros.'.format(area,litros))
