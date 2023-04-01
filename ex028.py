from random import randint
from time import sleep
n = randint(0,5)
resposta = int(input('Advinhe o número de 0 a 5 escolhido pelo comptador: '))
print('PROCESSANDO...')
sleep(3)
if resposta == n:
    print("Parabéns, você acertou o número sorteado!")
else:
    print(f'Errou, o número sorteado foi o {n} ')
print("=== Fim da partida ===")