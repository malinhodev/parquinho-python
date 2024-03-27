'''
 estruturas de repetição - loops

 while
 for
 do while

'''
a = 0
# com o while simplificado o loop não sai correto
'''
while a <= 5:
    print(a <= 5)
    print(a)
    a = a + 1

print('resultado final de a: ', a)
print(a <= 5)

while a <= 5:
    print(a <= 5)
    print(a)
    if a == 3:
        break
    a = a + 1

print('resultado final de a: ', a)
print(a <= 5)

while a <= 5:
    print(a <= 5)
    print(a)
    a = a + 1
else:
    print(f'a não é menor igual a 5. valor de a: {a}')
'''
# for
'''
s = 'ceara'
for x in s:
    print(x)
'''
# for(x = 0; x <= 5; x++) no python é feito igual abaixo
'''
for x in range(6):  # range 6 significa 6 index 0-5
    print(x)

for x in range(3, 8):  # index 3 ao 7
    print(x)

for x in range(0, 8, 2):  # 3 parametro encrementa de 2 em 2
    print(x)
'''

for x in range(5):
    print(x)
else:
    print('chegamos ao fim!')
