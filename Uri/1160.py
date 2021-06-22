for _ in range(int(input())):
	PA, PB, G1, G2 = map(float, input().split())

	anos = 0
	while PA <= PB and anos < 101:
		PA += int(int(PA)*(G1/100))
		PB += int(int(PB)*(G2/100))

		anos += 1

	if anos > 100:
		print('Mais de 1 seculo.')
	else:
		print('{} anos.'.format(anos))
