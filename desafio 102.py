def factorial(n=1, show=False):
    """
        => Calcula factorial de um numero.
        :param n: O numero a ser calculado 
        :param show: (opcional) Mostrar ou nao a conta
        :return: O valor do factorial de um numero n.
    """
    f = 1
    for i in range(n, 0, -1):
        f = f * i
        if show:
            print(i, end = '')
            if i > 1:
                print(f' x ', end='')
            else:
                print(' =', end= ' ')  
    return f

#Programa principal  
print(factorial(5, show=True))

#GuanaSweet