'''
    mini-game
    adivinhe o numero
    forma do python de gerar um do while
'''

palpite = 0
numero = 9

while True:  # executando sem verificar
    print('qual é o numero correto?')
    palpite = int(input('dê o seu palpite: '))
    if palpite == numero:  # verificando
        print('parabens vc acertou!')
        break
    else:
        print('você errou!, tente novamente.')
else:
    print('erro na aplicação')
    print(bool(palpite))
