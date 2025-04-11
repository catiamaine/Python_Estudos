from time import sleep
from random import randint

itens = ('pedra', 'papel', 'tesoura')
historico = []

while True:
    computador = randint(0, 2)

    print('\nSuas opções:')
    print('[0] PEDRA')
    print('[1] PAPEL')
    print('[2] TESOURA')
    
    try:
        jogador = int(input('Qual é a sua jogada? '))
        if jogador not in [0, 1, 2]:
            print('Jogada inválida! Tente novamente.')
            continue
    except ValueError:
        print('Entrada inválida! Use apenas números.')
        continue

    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO !!!')
    sleep(0.5)

    print('-=' * 20)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 20)

    if computador == jogador:
        resultado = 'EMPATE'
    elif (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
        resultado = 'COMPUTADOR VENCEU'
    else:
        resultado = 'JOGADOR VENCEU'

    print(resultado)
    historico.append(f'Jogador: {itens[jogador]} | Computador: {itens[computador]} => {resultado}')

    continuar = input('Quer jogar novamente? [S/N] ').strip().upper()
    if continuar != 'S':
        break

print('\n Histórico de partidas:')
for i, h in enumerate(historico, start=1):
    print(f'Rodada {i}: {h}')

print('\n Fim de jogo! Obrigado por jogar.')
