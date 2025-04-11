from random import randint

v = 0  # vitórias
print('=-' * 20)
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('=-' * 20)

while True:
    while True:
        try:
            jogador = int(input('Diga um valor: '))
            break
        except ValueError:
            print('Digite um número válido!')

    computador = randint(0, 10)
    total = jogador + computador

    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)

    if (tipo == 'P' and total % 2 == 0) or (tipo == 'I' and total % 2 == 1):
        print('🎉 Você VENCEU!\nVamos jogar novamente...')
        v += 1
    else:
        print('❌ Você PERDEU!')
        break

print(f'\n🏁 GAME OVER! Você venceu {v} vez(es).')