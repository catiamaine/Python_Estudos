v=float(input('Qual a velocidade atual do carro?'))
if v >80:
    print('Multado!Você excedeu o limite permitido que é de 80km/hr')
    multa = (v - 80) * 7
    print('Você deve pagar uma multa de {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')



