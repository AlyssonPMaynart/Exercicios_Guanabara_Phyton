#10 Primeiros termos de uma progressão aritimética
print('-'*10)
print('Gerador de PA')
print('-'*10)
primeiro = int(input('Primeiro termo: '))
a = primeiro
r = int(input('Informe a razão: '))
cont = 1
while cont <= 10:
    print('{} -> '.format(a), end='')
    a += r
    cont += 1
print('FIM')
