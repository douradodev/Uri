while True:
	try:
		case1 = list(input())
		case2 = list(input())

		matches = 0
		index = 0

		while True:
			sub = ''
			if case1[index] in case2:
				matches += 1

		print(matches)

	except EOFError:
		break