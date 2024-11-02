#sorteio de nomes
from random import choice
a1 = str(input('Informe o nome do primeiro aluno: '))
a2 = str(input(('Informe o nome do segundo aluno: ')))
a3 = str(input('Informe o nome do terceiro aluno: '))
a4 = str(input('Informe o nome do quatro aluno: '))
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print(escolhido.upper())
