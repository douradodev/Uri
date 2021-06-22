def divisoes_simples(testes):
	while testes:
		x, y = map(int, input().split())
		if y == 0:
			print('divisao impossivel')
		else:
			print('{:.1f}'.format(x/y))
		testes -= 1


divisoes_simples(int(input()))
