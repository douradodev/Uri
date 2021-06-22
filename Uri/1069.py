for _ in range(int(input())):
	mine = input()

	veil = ''
	for sub in mine:
		if sub != '.':
			veil = veil + sub

	diamonds = 0
	while '<>' in veil:
		veil = ''.join(veil.split('<>', 1))
		diamonds += 1

	print(diamonds)
