temp = list()
princ = list()
quant = mai = men = 0

while True:
    nome = input('Nome: ')
    while True:
        try:
            peso = float(input('Peso: '))
            break
        except ValueError:
            print('Por favor, digite um número válido para o peso.')

    temp.append(nome)
    temp.append(peso)

    if len(princ) == 0:
        mai = men = peso
    else:
        if peso > mai:
            mai = peso
        if peso < men:
            men = peso

    princ.append(temp[:])
    temp.clear()
    quant += 1

    while True:
        cont = input('Quer continuar? [S/N] ').strip().upper()
        if cont in 'SN':
            break
        print('Resposta inválida. Digite apenas S ou N.')
    
    if cont == 'N':
        break

print(f'\nAo todo, você cadastrou {quant} pessoas.')

maiores = [p[0] for p in princ if p[1] == mai]
menores = [p[0] for p in princ if p[1] == men]

print(f'O maior peso foi de {mai}kg. Peso de {", ".join(maiores)}.')
print(f'O menor peso foi de {men}kg. Peso de {", ".join(menores)}.')