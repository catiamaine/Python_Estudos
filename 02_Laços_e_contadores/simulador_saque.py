saldo = 1000  # Saldo inicial fictício

def menu():
    print('='*30)
    print('{:^30}'.format('BANCO CEV'))
    print('='*30)
    print('[1] Ver saldo')
    print('[2] Sacar')
    print('[3] Depositar')
    print('[4] Sair')
    print('='*30)

while True:
    menu()
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        print(f'Seu saldo atual é: R${saldo:.2f}')

    elif opcao == '2':
        try:
            saque = int(input('Digite o valor que deseja sacar: R$ '))
            if saque <= 0:
                print('Valor inválido. Tente novamente.')
            elif saque > saldo:
                print('Saldo insuficiente!')
            else:
                saldo -= saque
                n50 = n20 = n10 = n1 = 0
                resto = saque
                while resto > 0:
                    if resto >= 50:
                        resto -= 50
                        n50 += 1
                    elif resto >= 20:
                        resto -= 20
                        n20 += 1
                    elif resto >= 10:
                        resto -= 10
                        n10 += 1
                    else:
                        resto -= 1
                        n1 += 1
                print(f'Você receberá {n50}x R$50, {n20}x R$20, {n10}x R$10 e {n1}x R$1.')
        except ValueError:
            print('Digite um valor válido.')

    elif opcao == '3':
        try:
            deposito = float(input('Digite o valor a depositar: R$ '))
            if deposito <= 0:
                print('Valor inválido.')
            else:
                saldo += deposito
                print(f'Depósito de R${deposito:.2f} realizado com sucesso.')
        except ValueError:
            print('Digite um valor numérico válido.')

    elif opcao == '4':
        print('Obrigado por usar o BANCO CEV. Até logo!')
        break

    else:
        print('Opção inválida. Tente novamente.')

    print()
print(f'Você receberá {n50} notas de 50, {n20} de 20, {n10} de 10 e {n1} de 1.')