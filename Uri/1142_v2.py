def gera_numeros(inicio, fim):
	resultado = ''
	while inicio < fim:
		resultado += str(inicio) + " "
		inicio += 1
	else:
		resultado += str(inicio)
	return resultado

def main():
	count = int(input())
	start, end = 1, 3
	while count:
		print(gera_numeros(start, end), 'PUM')
		start += 4
		end += 4
		count -= 1

main()