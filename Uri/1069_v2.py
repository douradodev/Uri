def imprime_impares(numero, valor=1):	
	if valor <= numero:
		print(valor)
		imprime_impares(numero, valor+2)


imprime_impares(int(input()))