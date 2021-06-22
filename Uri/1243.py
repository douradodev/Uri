while True:
	try:
		sentence = input().split()
		sentence_words = []
		average_len = 0

		for word in sentence:
			if word.isalpha():
				sentence_words.append(word)
			else:
				if word[-1] == '.':					
					if word[1:-1].isalpha():						
						sentence_words.append(word[1:-1])

		total_len = 0
		for word in sentence_words:
			total_len += len(word)
		else:
			if len(sentence_words) > 0:
				average_len = int(total_len/len(sentence_words))

		if average_len <= 3:
			print(250)
		elif 4 <= average_len <= 5:
			print(500)
		elif average_len >= 6:
			print(1000)


	except EOFError:
		break