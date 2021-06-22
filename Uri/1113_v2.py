def imprime_ordem():
	num1, num2 = (map(int, input().split()))
	if num1 != num2:
		if num1 < num2:
			print('Crescente')
		else:
			print('Decrescente')
		imprime_ordem()


imprime_ordem()
