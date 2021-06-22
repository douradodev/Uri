def quadrado_pares(num):
	inicio = 2
	while inicio <= num:
		print('{}^2 = {}'.format(inicio, inicio**2))
		inicio += 2


quadrado_pares(int(input()))