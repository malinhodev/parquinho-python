idade = input('quantos anos você tem? ')
if int(idade) < 16:
    print('você é menor de idade.')
elif int(idade) >= 16 and int(idade) <= 18:
    print('você é ou pode ser emancipado.')
elif int(idade) > 18:
    print('você possui maior de idade legal')
