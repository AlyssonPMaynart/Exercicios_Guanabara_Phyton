from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['Carteira de Trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['Carteira de Trabalho'] == 0:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')    
else:
    dados['Ano_contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados ['Aposentadoria'] = dados['idade'] + dados['Ano_contratação'] + 35 - (datetime.now().year) 
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')