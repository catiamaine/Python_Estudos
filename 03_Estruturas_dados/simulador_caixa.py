# Simulador de caixa com troco
valor = float(input("Digite o valor da compra: R$"))
pago = float(input("Valor pago: R$"))
troco = pago - valor
print(f"Troco: R${troco:.2f}")