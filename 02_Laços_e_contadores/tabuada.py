while True:
    num = int(input("Digite um número para ver a tabuada: "))
    print('-' * 30)
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print('-' * 30)
    
    continuar = input("Quer ver outra tabuada? [S/N] ").strip().upper()
    if continuar != 'S':
        print("Encerrando o programa... Até logo!")
        break
