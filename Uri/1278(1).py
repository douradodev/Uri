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

		new_words = []
		test_phrase = []
		for phrase in words:
			for char in phrase:
				if char == test_phrase[-1] and char == ' ':
					continue
				else:
					test_phrase += char
			else:
				new_words.append(test_phrase)

		for word in new_words:
			if len(word) > bigger_len:
				bigger_len = len(word)

		if new_line:
			print()

		for word in new_words:
			print(" "*(bigger_len - len(word)) + word)

	new_line = True
