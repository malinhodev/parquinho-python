nome = input("Qual seu nome? ")
print("Olá {0}.".format(nome))
idade = input("Qual é a sua idade? ")
# template literas do python
# print("Prazer em conhecer {0} sua idade é: {1} anos!".format(nome, idade))
# template literas do python correto
print(f'Prazer em conhecer {nome}, sua idade é: {idade} anos.')
print("Volte sempre!")
