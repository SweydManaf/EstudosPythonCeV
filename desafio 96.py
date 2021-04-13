def terreno(l, c):
    area = l * c
    print(f'A area de um terreno {l}x{c} e de {area}m2')

#Programa principal
print(f'{"CONTROLE DE TERRENOS":^30}')
print('-'*30)
terreno(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
