for _ in range(int(input())):
	i =int(input())
	if i == 0:
		print('NULL')
	else:
		if i % 2 == 0:
			if i > 0:
				print('EVEN POSITIVE')
			else:
				print('EVEN NEGATIVE')
		else:
			if i > 0:
				print('ODD POSITIVE')
			else:
				print('ODD NEGATIVE')