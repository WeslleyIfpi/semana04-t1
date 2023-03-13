print('Esse programa calcula a área do piso da sala, o volume da sala e a area das paredes da sala.')

altura = float(input('Digite a altura da sala (m): '))
comprimento = float(input('Digite o comprimento da sala (m): '))
largura = float(input('Digite a largura da sala (m): '))

areaDoPiso = largura * comprimento
volume = largura * comprimento * altura
areaDasParedes = 2 * altura * largura + 2 * altura * comprimento

print(f'A área dp piso é de: {areaDoPiso}m²')
print(f'A sala tem um volume de: {volume}m³')
print(f'As paretes tem área toral de: {areaDasParedes}m²')