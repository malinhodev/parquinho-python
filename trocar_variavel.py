'''
exerc. trocar variáveis
'''
# trocando variaves em python
x = input("insira o valor de x: ")
y = input('insira o valor de y: ')

# criaremos uma variavel temporaria

temp = x
x = y
y = temp

print(f'o valor de x após a troca: {x}')
print(f'o valor de y após a troca: {y}')
