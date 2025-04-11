valores = []
par = []
impar = []

while True:
    while True:
        try:
            num = int(input('Digite um valor: '))
            break
        except ValueError:
            print('Por favor, digite um número inteiro válido.')
    
    valores.append(num)

    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()
        if resp in 'SN':
            break
        print('Resposta inválida! Digite apenas S ou N.')

    if resp == 'N':
        break

for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print(f'\nA lista completa é: {valores}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')