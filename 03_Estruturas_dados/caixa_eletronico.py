saldo = 1000.00
transacoes = []

def menu():
    print('=' * 30)
    print('{:^30}'.format('BANCO CEV'))
    print('=' * 30)
    print('[1] Ver saldo')
    print('[2] Sacar')
    print('[3] Depositar')
    print('[4] Extrato')
    print('[5] Sair')
    print('=' * 30)

def registrar(tipo, valor):
    # Se for saque, armazena como valor negativo
    if tipo == 'Saque':
        valor = -valor
    transacoes.append({'tipo': tipo, 'valor': valor})

while True:
    menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print(f'Seu saldo atual é: R${saldo:.2f}')

    elif opcao == '2':
        try:
            saque = float(input('Digite o valor para saque: R$ '))
            if saque <= 0:
                print('Valor inválido.')
            elif saque > saldo:
                print('Saldo insuficiente.')
            else:
                saldo -= saque
                registrar('Saque', saque)
                print(f'Saque de R${saque:.2f} realizado com sucesso.')
        except ValueError:
            print('Digite um valor numérico válido.')

    elif opcao == '3':
        try:
            deposito = float(input('Digite o valor para depósito: R$ '))
            if deposito <= 0:
                print('Valor inválido.')
            else:
                saldo += deposito
                registrar('Depósito', deposito)
                print(f'Depósito de R${deposito:.2f} realizado com sucesso.')
        except ValueError:
            print('Digite um valor numérico válido.')

    elif opcao == '4':
        print('\n=== EXTRATO ===')
        if not transacoes:
            print('Nenhuma movimentação registrada.')
        else:
            for t in transacoes:
                print(f'{t["tipo"]:<10} R${t["valor"]:.2f}')
        print(f'\nSaldo atual: R${saldo:.2f}')
        print('================\n')

    elif opcao == '5':
        print('Encerrando... Obrigado por usar o BANCO CEV!')
        break

    else:
        print('Opção inválida. Tente novamente.')

    print()