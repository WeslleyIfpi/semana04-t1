altura = float(input())
comprimento = float(input())
largura = float(input())

areaDoPiso = largura * comprimento
volume = largura * comprimento * altura
areaDasParedes = 2 * altura * largura + 2 * altura * comprimento

print(f'{areaDoPiso}')
print(f'{volume}')
print(f'{areaDasParedes}')