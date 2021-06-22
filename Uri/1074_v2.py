def odd_or_even(tests_amount):
	while tests_amount:
		tests_amount -= 1
		number = int(input())		

		if number == 0:
			print('NULL')
			continue

		result = ''		
		
		if number%2 == 0:
			result += 'EVEN '
		else:
			result += 'ODD '

		if number > 0:
			result += 'POSITIVE'
		else:
			result += 'NEGATIVE'

		print(result)


odd_or_even(int(input()))