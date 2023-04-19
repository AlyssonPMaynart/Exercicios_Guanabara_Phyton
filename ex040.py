print("-=" * 8)
print("Cálculo de média")
print("-=" * 8)
n1 = float(input("informe a primeira nota do aluno: "))
n2 = float(input("informe a segunda nota do aluno: "))
media = (n1 + n2) / 2
if media >= 7:
    print(f"Parabéns, você foi APROVADO com média {media}")
elif media < 5:
    print(f"lamentamos seu resultado, você está REPROVADO com média {media}")
else:
    print(f"Com média {media}, Você está em RECUPERAÇÃO")
