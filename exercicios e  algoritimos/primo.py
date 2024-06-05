"""
decobrir se um numero é primo

primo é o numero  que só pode ser dividido por 
ele mesmo ou por 1 e o resto da divisão tem que resultar em 0
"""

print(30 * "-")

numero = int(input('Insira um numero para descobrir se é numero primo: '))

if numero > 1:
    for x in range(2,numero):
        if(numero % x) == 0:
            print('Esse número não é primo')
            break
    else:
        print('É numero primo!!!')
else:
    print('Esse número não é primo!')

print(30 * "-")
