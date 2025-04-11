valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = valor / (anos * 12)
minimo = salario * 0.3  # 30% do salário

print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}.')

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO.')
else:
    print('Empréstimo NEGADO!')
