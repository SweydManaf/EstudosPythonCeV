n = int(input('Informe quantos elementos deseja: '))
c = 0
actual = 1
anterior =0
print('0; 1', end = '; ')
while c < n:
    proximo = actual + anterior
    print(proximo, end = '; ')
    anterior = actual
    actual = proximo
    c+=1
print('FIM')