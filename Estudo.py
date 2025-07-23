estado = dict()
brasil = list()

for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    brasil.append(estado())

for k, v in estado.items():
    print(f'{k} = {v}')