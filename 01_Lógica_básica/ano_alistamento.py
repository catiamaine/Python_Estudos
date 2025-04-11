from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} anos para seu alistamento.')
    print(f'Seu alistamento será em {ano}.')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {ano}.')

    

