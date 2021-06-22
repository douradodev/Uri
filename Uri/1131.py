def main():
	
	grenais, inter, gremio, empate = 0, 0, 0, 0

	novo = 1
	while novo != 2:
		g_inter, g_gremio = map(int, input().split())

		if g_inter > g_gremio:
			inter += 1
		elif g_inter < g_gremio:
			gremio += 1
		elif g_inter == g_gremio:
			empate += 1

		grenais += 1

		while True:
			novo = int(input('Novo grenal (1-sim 2-nao)\n'))
			if novo in [1, 2]:
				break

	print('{} grenais'.format(grenais))
	print('Inter:{}'.format(inter))
	print('Gremio:{}'.format(gremio))
	print('Empates:{}'.format(empate))
	if inter > gremio:
		print('Inter venceu mais')
	elif inter < gremio:
		print('Gremio venceu mais')
	else:
		print('Nao houve vencedor')


main()