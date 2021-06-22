total, total_coelhos, total_ratos, total_sapos = 0, 0, 0, 0
for i in range(int(input())):
	test = input().split()

	total += int(test[0])

	if test[1] == 'C':
		total_coelhos += int(test[0])
	elif test[1] == 'R':
		total_ratos += int(test[0])
	elif test[1] == 'S':
		total_sapos += int(test[0])
else:
	print('Total: {} cobaias'.format(total))
	print('Total de coelhos:', total_coelhos)
	print('Total de ratos:', total_ratos)
	print('Total de sapos:', total_sapos)
	print('Percentual de coelhos: {:.2f} %'.format((total_coelhos/total)*100))
	print('Percentual de ratos: {:.2f} %'.format((total_ratos/total)*100))
	print('Percentual de sapos: {:.2f} %'.format((total_sapos/total)*100))
