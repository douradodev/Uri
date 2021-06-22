first_time = True
while True:
	try:	

		year = int(input())

		if not first_time:
			print("")

		if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
			print('This is leap year.')
			if year % 15 == 0:
				print('This is huluculu festival year.')
			if year % 55 == 0:
				print('This is bulukulu festival year.')
		elif year % 15 == 0:
			print('This is huluculu festival year.')
		else:
			print('This is an ordinary year.')

		first_time = False

	except EOFError:
		break
