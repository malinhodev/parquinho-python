print('vamos calcular seu desconto')
compra = input('qual o valor da sua compra? ')
valor_desconto = input('qual o valor do desconto? ')
valor = float(compra) * float(valor_desconto) / 100
desconto = float(compra) - float(valor)
print(f'o valor da sua compra é: R$ {
      desconto} com {valor_desconto} % de desconto.')
