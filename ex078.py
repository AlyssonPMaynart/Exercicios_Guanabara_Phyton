valores = list()
maior = 0
menor = 0
print('Declare 5 valores inteiros')
for i in range(0,5):
    valores.append(int(input(f'Valor {i+1}:')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor < valores[i]
print(f'Você declarou os valores: {valores}')
print()
print(f'O maior valor declarado foi {maior}, na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor declarado foi o {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')


