
'''#numeros
inteiro = 1
fracional = 1.5
equacional = 1+2j

a = "hello"
b = " word!"
#concatenação
c = a + b
print(c)'''

# casting
'''
a = int(2)
b = int(2.8)
c = int('2')

# print(a, b, c)

# associação
x = "pernambuco"
y = 'perna'

print(y in x)'''

# bloco if | else if = elif em python
'''
x = 5
y = 8

if y > x:
    print('y é maior do que x')
elif y == x:
    print('y e x ou x e y são iguais!')
elif x > y:
    print('x é maior que y')'''

# operador ternário (encurtando os if/else)
a = 10
b = 8
c = 2
# if b > a: print('b é maior que a.')

# animhamento de if

if a > b:
    print("a maior que b.")
    if a > c:
        print('a maior que c.')
