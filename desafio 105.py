def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao.
    :return: dicionario com varias informacoes sobre a situacao da turma.
    """
    resp = {'total': len(n), 
            'maior': max(n), 
            'menor': min(n),
            'media': sum(n)/len(n)
            }
    if sit:
        if resp['media'] >= 7:
            resp['situacao'] = 'BOA'
        elif resp['media'] >= 5:
            resp['situacao'] = 'RAZOAVEL'
        else:
            resp['situacao'] = 'RUIM'
    return resp


#Programa Principal
resp = notas(3.5, 10, 6.5, sit=True)
print(resp)