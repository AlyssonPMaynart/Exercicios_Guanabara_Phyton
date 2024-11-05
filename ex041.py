from datetime import date

print('*' * 26)
print('CLASSIFICADOR DE CATEGORIA')
print('*' * 26)

nascimento = int(input('Informe a data de nascimento do atleta: '))
data_atual = date.today().year
idade = data_atual - nascimento
if idade < 10:
    print('O atleta possui {} anos.\n'
          'Classificação: JUNIOR'.format(idade))
elif idade < 15:
    print('O atleta possui {} anos.\n'
          'Classificação: INFANTIL'.format(idade))
elif idade < 20:
    print('O atleta possui {} anos.\n'
          'Classificação: JÚNIOR'.format(idade))
elif idade < 26:
    print('O atleta possui {} anos.\n'
          'Classificação: SENIOR'.format(idade))
else:
    print('O atleta possui {} anos.\n'
          'Classificação: MASTER'.format(idade))
