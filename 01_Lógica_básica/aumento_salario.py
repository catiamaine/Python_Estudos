salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    aumento = salario * 15 / 100
    novo = salario + aumento
    print(f'Salário atual: R${salario:.2f}')
    print('Aumento de 15% aplicado.')
else:
    aumento = salario * 10 / 100
    novo = salario + aumento
    print(f'Salário atual: R${salario:.2f}')
    print('Aumento de 10% aplicado.')

print(f'Novo salário: R${novo:.2f} (acréscimo de R${aumento:.2f})')
