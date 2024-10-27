peso = float(input('Insira seu peso em KG: '))

altura = float(input('Insira sua altura em metros: '))

imc = peso / (altura*altura)

print(f'seu imc é {imc: .2f}')

if imc < 17:
    print('Você está muito abaixo do peso.')

elif imc > 17 and imc < 18.5:
    print('Você está Abaixo do peso.')

elif imc > 18.5 and imc < 24.9:
    print('Você está em seu peso ideal, Parabéns !')

elif imc > 25 and imc < 29.9:
    print('Você está acima do peso.')

elif imc > 30 and imc < 34.9:
    print('Você está em Obesidade grau I, não deixe isso evoluir')

elif imc > 35 and imc < 39.9: 
    print('Você está em Obesidade grau II, procure um médico e mude sua alimentação')

elif imc > 40:
    print('Você está em Obesidade grau III, caixão e vela preta')
else:
    print('Insira uma informação válida.')