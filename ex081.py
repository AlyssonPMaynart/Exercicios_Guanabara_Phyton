valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja Continuar? [S/N] '))
    if resp in "nN":
        break
print('='* 30)
print(f"Você digitou {len(valores)} numeros. ")
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print("O numero 5 faz parte da lista!")
else:
    print('O valor 5 não faz parte da lista!')


