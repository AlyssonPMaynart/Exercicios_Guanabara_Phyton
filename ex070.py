total = maiorMil = cont = menor = 0
maisBarato = ' '
while True:
    nomeProduto = str(input('Nome do produto: '))
    precoProduto = float(input('Preço do produto: '))
    total = total + precoProduto
    cont += 1
    if precoProduto > 1000:
        maiorMil += 1
    if cont == 1 or precoProduto < menor:
        menor = precoProduto
        maisBarato = nomeProduto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O Valor Total gasto nesta compra foi R$ {total:.2f} \n'
      f'{maiorMil} produtos custaram mais de R$ 1.000,00. \n'
      f'O Produto mais barato foi o {maisBarato}, que custou R$ {menor:.2f} \n')