def cobaias(testes):

	total, total_coelhos, total_ratos, total_sapos = 0, 0, 0, 0
	while testes:
		qtd, tipo = input().split()

		qtd = int(qtd)
		total += qtd

		if tipo == 'C':
			total_coelhos += qtd
		elif tipo == 'R':
			total_ratos += qtd
		elif tipo == 'S':
			total_sapos += qtd
		testes -= 1


	print('Total: {} cobaias'.format(total))
	print('Total de coelhos:', total_coelhos)
	print('Total de ratos:', total_ratos)
	print('Total de sapos:', total_sapos)
	print('Percentual de coelhos: {:.2f} %'.format((total_coelhos/total)*100))
	print('Percentual de ratos: {:.2f} %'.format((total_ratos/total)*100))
	print('Percentual de sapos: {:.2f} %'.format((total_sapos/total)*100))


cobaias(int(input()))