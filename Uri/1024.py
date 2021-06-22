for _ in range(int(input())):
	msg = input()

	first_step = ''
	for sub in msg:
		if sub.isalpha():
			first_step += chr(ord(sub) + 3)
		else:
			first_step += sub

	second_step = first_step[::-1]
	last_step = ''
	for sub in second_step[int(len(second_step)/2):]:
		last_step += chr(ord(sub) - 1)

	print(second_step[:int(len(second_step)/2)] + last_step)
	