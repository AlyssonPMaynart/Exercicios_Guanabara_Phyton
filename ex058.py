#Jogo da adivinhação melhorado
from random import randint
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Será qe você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente outra vez.')
        elif jogador > computador:
            print('Menos... Tente outra vez.')
    print('Acertou com {} tentativas. Parabéns!'.format(palpites))
print("=== Fim da partida ===")