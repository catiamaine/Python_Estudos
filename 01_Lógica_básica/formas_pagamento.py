# Exercício que calcula o preço final de uma compra com base na forma de pagamento
print('{:=^40}'.format(' LOJAS MAINE')) 
preço=float(input('Preço das compras:R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro ou cheque (10% de desconto)
[2] à vista no cartão (5% de desconto)
[3] 2x no cartão (preço normal)
[4] 3x ou mais no cartão (20% de juros)''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço - (preço*10/100)
elif opção == 2:
    total = preço - (preço*5/100)
elif opção == 3:
    total = preço
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço*20/100)
    totalparcela=int(input('Quantas parcelas?'))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {} vezes de R${:.2f} COM JUROS'.format(totalparcela,parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento.Tente novamente!')
print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))


