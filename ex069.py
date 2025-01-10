maiores = homens = mulheresMenores = 0
while True:
    print('-=' * 20)
    print('CADASTRE UMA PESSOA')
    print('-=' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-=' * 20)
    if idade >= 18:
        maiores += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheresMenores += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {maiores} pessoas com mais de 18 anos \n'
      f'sendo {homens} homens e {mulheresMenores} mulheres com menos de 20 anos.')

