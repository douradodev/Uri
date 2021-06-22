new_line = False
while True:
	words = []
	bigger_len = 0

	test = int(input())
	if test == 0:
		break
	else:
		for _ in range(test):
			words.append(input().strip())

		new_words = []		
		for phrase in words:
			test_phrase = ''
			for char in phrase:				
				if len(test_phrase) and char == test_phrase[-1] and char == ' ':
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
