from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif 10 <= idade <= 14:
    print('Classificação: INFANTIL')
elif 15 <= idade <= 19:
    print('Classificação: JUNIOR')
elif 20 <= idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')