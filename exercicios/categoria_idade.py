print('vamos descobrir a qual categoria você pertence!')
idade = input('qual é a sua idade? ')

if int(idade) >= 5 and int(idade) <= 7:
    print('Sua categoria é: Infantil A')
elif int(idade) >= 8 and int(idade) <= 10:
    print('Sua categoria é: Infantil B')
elif int(idade) >= 11 and int(idade) <= 13:
    print('Sua categoria é: Juvenil A')
elif int(idade) >= 14 and int(idade) <= 17:
    print('Sua categoria é: Juvenil B')
else:
    print('você não está qualificado a nenhuma categoria!')
