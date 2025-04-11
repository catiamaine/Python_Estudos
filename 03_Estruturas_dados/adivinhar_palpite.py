from random import randint

computador = randint(0, 10)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')

palpites = []  # Lista para armazenar os palpites do jogador

while True:
    try:
        jogador = int(input('Qual o seu palpite? '))
    except ValueError:
        print('Digite um número válido!')
        continue

    palpites.append(jogador)  # Armazena o palpite

    if jogador == computador:
        print(f' Acertou com {len(palpites)} tentativa(s)! Parabéns!')
        break
    elif jogador < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')

# Exibe o histórico de palpites
print('\nPalpites feitos:', palpites)
