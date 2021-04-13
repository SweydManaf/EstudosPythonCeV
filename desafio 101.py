def voto(ano):
    from datetime import date
    y = date.today().year
    a = y - ano
    if ano > 18 and ano < 65:
        return f'Com {a} anos: VOTO OBRIGATORIO'
    elif ano < 18:
        return f'Com {a} anos: NAO VOTA'
    else:
        return f'Com {a} anos: VOTO OPCIONAL'

    
# Programa principal
nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))

