while True:
	test = int(input())

	if test == 0:
		break
		
	print(" ".join(list(map(str, range(1, test+1)))))
