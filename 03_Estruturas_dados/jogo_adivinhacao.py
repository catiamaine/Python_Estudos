# Jogo simples de adivinhação
import random
num_secreto = random.randint(1, 10)
palpite = int(input("Adivinhe o número de 1 a 10: "))
if palpite == num_secreto:
    print("Parabéns! Você acertou.")
else:
    print(f"Errou! O número era {num_secreto}.")