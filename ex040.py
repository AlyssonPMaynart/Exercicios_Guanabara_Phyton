print("-=" * 8)
print("Cálculo de média")
print("-=" * 8)
n1 = float(input("informe a primeira nota do aluno: "))
n2 = float(input("informe a segunda nota do aluno: "))
media = (n1 + n2) / 2
if media >= 7:
    print('Parabéns, você foi APROVADO com média {}'.format(media))
elif media < 5:
    print('lamentamos seu resultado, você está REPROVADO com média {}'.format(media))
else:
    print('Com média {}, Você está em RECUPERAÇÃO'.format(media))
