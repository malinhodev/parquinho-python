print('vamos converter R$ (reais) para D$ (dolares)')
real = input('quantos reais vc quer converter? ')
dolar = input('quanto está valendo o dolar hoje? ')
conversao = float(real) / float(dolar)
print(f'R$ {real} vale D$ {conversao} sem a taxa de câmbio.')
