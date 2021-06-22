def imprime_impares(numero, valor=6):
	if not numero%2:	
		numero = numero + ((numero+1)%2)
	if valor:
		print(numero)
		imprime_impares(numero+2, valor-1)


imprime_impares(int(input()))