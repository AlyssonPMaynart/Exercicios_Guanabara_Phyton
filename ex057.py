sexo = str(input('Qual o seu sexo [M/F]: ')).upper().strip()[0]
while  'F' != sexo != 'M':
    sexo = str(input('Sexo invalido, tente novamente!\n'
                     'Qual o seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
