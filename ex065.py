resp = 'S'
maior = soma = cont = media = menor = 0
while resp in 'Ss':
    n = int(input('Informe um número inteiro: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media = soma / cont
print('Você digitou {} numeros,\n'
      'a média entre todos os números informados é {},\n'
      'sendo {} o maior numero informado e {} o menor.'.format(cont, media, maior, menor))