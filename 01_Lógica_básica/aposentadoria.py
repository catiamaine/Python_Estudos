from datetime import datetime

dados = {}

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc

tem_carteira = int(input('Tem carteira assinada? Digite 0 se NÃO tem, ou 1 se TEM: '))
dados['tem_carteira'] = tem_carteira

if dados['tem_carteira'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('-' * 40)
print('DADOS CADASTRADOS:')

print(f'Nome: {dados["nome"].title()}')
print(f'Idade: {dados["idade"]} anos')
print(f'Carteira assinada: {"Sim" if dados["tem_carteira"] != 0 else "Não"}')

if dados["tem_carteira"] != 0:
    print(f'Ano de contratação: {dados["contratação"]}')
    print(f'Salário: R$ {dados["salario"]:.2f}')
    print(f'Idade para aposentadoria: {dados["aposentadoria"]} anos')