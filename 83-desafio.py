expressao = str(input('Digite a expressao: '))
ca = 0
cf = 0
for s in expressao:
    if s == '(':
        ca+=1
    if s == ')':
        cf+=1
if ca==cf:
    print('Sua expressao esta certa')
else:
    print('Sua expressao esta errada')
    
#Colocar no YouTube