aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = "\033[32m APROVADO"
elif aluno['media'] < 5:
    aluno['situacao'] = "REPROVADO"
else:
    aluno['situacao'] = "EM RECUPERAÇÃO"
print('-=' * 30)
print(f'O aluno {aluno["nome"]} teve média {aluno["media"]} e encontra-se em {aluno["situacao"]}!')