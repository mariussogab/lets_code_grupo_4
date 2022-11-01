def soma(a,b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return a+b
    else:
        return f'Impossível somar, tipos não compátivel com a operação'

def subtracao(a,b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return a-b
    else:
        return f'Impossível somar, tipos não compátivel com a operação'

def multiplicacao(a,b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return a*b
    else:
        return f'Impossível somar, tipos não compátivel com a operação'

def divisao(a,b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        if b == 0:
            print('Erro de divisão por zero')
            return 0
        else:
            return a/b 
    else:
        return f'Impossível somar, tipos não compátivel com a operação'
    i
