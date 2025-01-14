cont = ('zero', 'um', 'dois', 'trê', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezesete', 'dezoito', 'dezenove', 'vinte')
continuar = ' '
while True:
    resp = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= resp <= 20:
        print(f'Você digitou o numero {cont[resp]}')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp > 20:
        print('Tente Novamente.')
    if continuar == 'N':
        break
