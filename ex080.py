list = []
for i in range(0,5):
    n = int(input("digite um numero: "))
    if i == 0 or n > list[-1]:
        list.append(n)
    else:
        pos = 0
        while pos <= len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                break
            pos += 1
print(f'Você digitou os numeros: {list}')
