from random import randint
itens = ["PEDRA", "PAPEL", "TESOURA"]
pc = randint(0,2)
print(f"=-" * 10)
print("PEDRA PAPEL TESOURA")
print(f"=-" * 10)
print('''Suas opções:
[0] PEDRA"
[1] PAPEL"
[2] TESOURA''')
jogador = int(input("Qual é a sua Jogada? "))
if jogador not in [0, 1, 2]:
    print("JOGADA INVÁLIDA")
print("-=" * 11)
print(f"O computador escolheu {itens[pc]}")
print(f"Jogador escolheu: {itens[jogador]}")
if pc == 0:
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print('COMPUTADOR VENCE')
elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print("JOGADOR VENCE")
elif pc == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATOU')
