from datetime import date

print('*' * 26)
print("CLASSIFICADOR DE CATEGORIA")
print('*' * 26)

nascimento = int(input("Informe a data de nascimento do atleta: "))
data_atual = date.today().year
idade = data_atual - nascimento
if idade < 10:
    print(f"O atleta possui {idade} anos.\n"
          f"Classificação: JUNIOR")
elif idade < 15:
    print(f"O atleta possui {idade} anos.\n"
          f"Classificação: INFANTIL")
elif idade < 20:
    print(f"O atleta possui {idade} anos.\n"
          f"Classificação: JÚNIOR")
elif idade < 26:
    print(f"O atleta possui {idade} anos.\n"
          f"Classificação: SENIOR")
else:
    print(f"O atleta possui {idade} anos.\n"
          f"Classificação: MASTER")
