print('Esse programa calcula o total de segundos após a meia noite: ')
hora = int(input('Digite a hora: '))
minuto = int(input('Digite os minutos: '))
segundo = int(input('Digite os segundos: '))

totalSegundos = (hora*60*60) + (minuto*60) + segundo

print(f'O total de segundos é: {totalSegundos}')