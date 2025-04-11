from time import sleep

def contador(i, f, p):
    """Faz uma contagem de i até f, com passo p"""
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
    print('FIM')
    print('-=' * 20)

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem!')
print('Você pode usar números positivos ou negativos.')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)