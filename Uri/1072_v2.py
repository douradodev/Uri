def checa_intervalo(testes):
	inside, out = 0, 0
	while testes:
		numero = int(input())
		
		if numero >= 10 and numero <= 20:
			inside +=1
		else:
			out += 1

		testes -= 1

	print('{} in'.format(inside))
	print('{} out'.format(out))


checa_intervalo(int(input()))