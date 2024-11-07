nomeHomemMaisVelho = ''
idadeHomemMaisVelho = 0
mulheresMenores20 = 0
somaIdade = 0
for pessoas in range(1,5):
    print('-----{}ª PESSOA -----'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    somaIdade += idade
    sexo = str(input('sexo [M/F]: ')).strip()
    if idade > idadeHomemMaisVelho and sexo in 'Mm':
        idadeHomemMaisVelho = idade
        nomeHomemMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresMenores20 += 1
média = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(média))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadeHomemMaisVelho, nomeHomemMaisVelho))
print('Ao todo são {} mulheres com monos de 20 anos'.format(mulheresMenores20))

