def imprime_resto2(num):
	count = 1
	while count != 10000:
		if count%num == 2:
			print(count)
		count += 1


imprime_resto2(int(input()))