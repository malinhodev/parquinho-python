"""
como achar o fatorial de um numero

fatorial?
9! = 9*8*7*6*5*4*3*2*1
4! = 4*3*2*1
0! = 1
1! = 1
"""
print(30 * '-')
print('vamos achar o  fatorial do numero')
numero = int(input('insira um numero: '))

Fatorial = 1

if numero < 0:
    print('Não existe fatorial de numeros negativos!')
elif numero == 0:
    print(f'O fatorial de {numero} é 1')
else:
    for x in range(1, numero+1):
        Fatorial = Fatorial*x
    print(f'O fatorial de {numero} é {Fatorial}')

print(30 * '-')
