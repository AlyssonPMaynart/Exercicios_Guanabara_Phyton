maior = 0
menor = 999999999999
n1 = float(input('informe um número: '))
n2 = float(input('informe um segundo número: '))
n3 = float(input('informe um terceiro número: '))
if n1 > maior:
    maior = n1
    if n2 > maior:
        maior = n2
        if n3 > maior:
            maior = n3
            if n1 < menor:
                menor = n1
                if n2 < menor:
                    menor = n2
                    if n3 < menor:
                        menor = n3
print(f'O maior numero escolhido foi o {maior}')
print(f'O menor numero escolhido foi o {menor}')
