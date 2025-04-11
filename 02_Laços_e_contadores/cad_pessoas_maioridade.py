tot18 = totH = totM20 = 0

while True:
    # Validação de idade
    while True:
        try:
            idade = int(input('Idade: '))
            if idade < 0:
                print('Idade não pode ser negativa. Tente novamente.')
            else:
                break
        except ValueError:
            print('Por favor, digite um número válido para a idade.')

    # Validação de sexo
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    # Contagens
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    # Validação de resposta
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

# Resultado final
print('\n===== RESUMO DA PESQUISA =====')
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')

