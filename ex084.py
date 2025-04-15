pessoa = list()
grupo = list()
maior = menor = 0
while True:
    pessoa.append(str(input('Nome da pessoa: ')))
    pessoa.append(float(input('Informe o peso da pessoa: ')))
    if len(grupo) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    resp = input('Deseja continuar? [S/N] ')
    if resp in 'nN':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(grupo)} pessoas')
print(f'O maior peso cadastrado foi {maior}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso cadastrado foi {menor}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'{p[0]}', end='')