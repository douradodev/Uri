while True:
	try:
		vowels = input()
		text = input()

		total = 0
		for v in vowels:
			for char in text:
				if char == v:
					total += 1
		else:
			print(total)

	except EOFError:
		break