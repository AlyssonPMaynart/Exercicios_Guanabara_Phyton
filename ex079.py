valores = []
while True:
    valor = int(input('Informe um valor inteiro para adicionar à lista: '))
    if valor not in valores:
        valores.append(valor)
    resp = (input('Deseja Continuar[N/S]: '))
    if resp == "N":
        break
print(valores)
valores.sort()
print(valores)





