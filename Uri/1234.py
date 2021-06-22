while True:
	try:
		sentence = ''
		change_case = True
		for char in input():
			if char.isalpha():
				if change_case:
					sentence += char.upper()
					change_case = False
				else:
					sentence += char.lower()
					change_case = True
			else:
				sentence += char
		else:
			print(sentence)

	except EOFError:
		break