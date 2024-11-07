from datetime import date
ano = date.today().year
quantMaior = 0
quantMenor = 0
for i in range (1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    if ano - nascimento >= 21:
        quantMaior += 1
    else:
        quantMenor += 1
print('A todo tivemos {} pessoas maiores de idade\n'
'E também tivemos {} pessoas menores de idade'.format(quantMaior, quantMenor))