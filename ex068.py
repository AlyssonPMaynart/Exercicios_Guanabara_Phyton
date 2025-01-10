from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)

vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = 0
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Paro ou ímpar? [P/I] ').upper().strip()[0])
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 ++ 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você Venceu')
            vitorias += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitorias} vezes. ')