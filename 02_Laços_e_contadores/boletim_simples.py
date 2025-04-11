ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print('-' * 30)
print(f'{"No.":<4}{"NOME":<12}{"MÉDIA":>8}')
print('-' * 30)
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<12}{aluno[2]:>8.1f}')

print('-' * 30)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if 0 <= opc < len(ficha):
        print(f'Notas de {ficha[opc][0]}: {ficha[opc][1]}')
    else:
        print('Número inválido. Tente novamente.')
print('<<< VOLTE SEMPRE >>>')