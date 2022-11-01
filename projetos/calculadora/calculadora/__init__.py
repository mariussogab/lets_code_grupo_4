from .funcoes import soma, subtracao, multiplicacao, divisao
def calcule():
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    op = input('Digite a operação: ')
    switcher={
        'soma': soma,
        'subtracao': subtracao,
        'multiplicacao': multiplicacao,
        'divisao': divisao,
        '+': soma,
        '-': subtracao,
        '*': multiplicacao,
        '/': divisao
        }
    if op in switcher.keys():
        resultado = switcher[op](a,b)
        return resultado
    else:
        print(f'operação não reconhecida, escolha entre {list(switcher.keys())}')

