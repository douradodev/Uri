while True:
	try:
		num = int(input())		
		test = 1
		while test % num != 0:
			test = int(str(test) + '1')
		else:
			print(len(str(test)))
	except EOFError:
		break
