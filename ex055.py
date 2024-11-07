#indica peso maior e menor
pesoMaior = 0
pesoMenor = 0
for pessoa in range(1, 6):
    peso = float(input('Peso de {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > pesoMaior:
         pesoMaior = peso
        if peso < pesoMenor:
         pesoMenor = peso
print('O maior peso lido foi de {}Kg\n'
      'O menor peso lido foi de {}Kg'.format(pesoMaior, pesoMenor))