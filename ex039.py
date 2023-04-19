from datetime import date
ano = int(input("Informe o ano de seu nascimento "))
idade = date.today().year - ano
print(f"Você tem {idade} anos")
if idade == 18:
    print("Está no tempo exato para alistamento militar. Procure a junta militar mais proxima!")
elif idade < 18:
    print(f"Ainda é cedo para se alistar faltam {18 - idade} anos")
else:
    print(f"Você passou {idade - 18} ano(s) do prazo para o alistamento militar, procure a junta militar imediatamente.")