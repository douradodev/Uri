new_line = False
while True:
	words = []
	bigger_len = 0

	test = int(input())
	if test == 0:
		break
	else:
		for _ in range(test):
			words.append(input())

		for word in words:
			if len(word) > bigger_len:
				bigger_len = len(word)

		if new_line:
			print()

		for word in words:
			print(" "*(bigger_len - len(word)) + word)

	new_line = True
