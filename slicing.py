"""
o slicing é representado por: [::]
nos permite imprimir 1 ou varios index de livre escolha
"""
lista = ['banana', 'melão', 'uva', True, 5, 6.3]

print(lista[::])
print(lista[2:])
print(lista[3:])# retorna do index 3 até o final
print(lista[4:6])# retorna do index escolhido até o index final-1
print(lista[0:2])# se eu quiser apenas banana e melão
