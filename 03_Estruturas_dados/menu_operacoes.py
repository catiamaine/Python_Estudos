from time import sleep

historico = []  # Lista para guardar as operações feitas

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('''\n   [1] somar
   [2] multiplicar
   [3] maior
   [4] novos números
   [5] sair do programa ''')
    opcao = int(input('Qual é sua opção? '))

    if opcao == 1:
        soma = v1 + v2
        print(f'A soma entre {v1} + {v2} é {soma}')
        historico.append(f'Soma: {v1} + {v2} = {soma}')
    elif opcao == 2:
        mult = v1 * v2
        print(f'O resultado de {v1} x {v2} é {mult}')
        historico.append(f'Multiplicação: {v1} x {v2} = {mult}')
    elif opcao == 3:
        maior = v1 if v1 > v2 else v2
        print(f'Entre {v1} e {v2}, o maior valor é {maior}')
        historico.append(f'Maior: entre {v1} e {v2}, maior é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
        historico.append('=== Novos números informados ===')
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print(' Opção inválida. Tente novamente.')

print('\n Histórico de operações:')
for operacao in historico:
    print(f' - {operacao}')
print('\n Fim do programa. Volte sempre!')

        
        