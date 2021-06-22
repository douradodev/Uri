def main():
	while True:
		numbers = input().split()
		carry_count = 0		

		if numbers == ['0', '0']:
			break

		while len(numbers[0]) < len(numbers[1]):
			numbers[0] = '0' + numbers[0]
		while len(numbers[0]) > len(numbers[1]):
			numbers[1] = '0' + numbers[1]

		carry = 0
		for i in range(len(numbers[0])-1,0-1,-1):

			sub_sum = int(numbers[0][i]) + int(numbers[1][i]) + carry

			if sub_sum >= 10:
				carry_count +=1
				carry = 1				
			else:
				carry = 0

		if carry_count == 0:
			print('No carry operation.')
		elif carry_count == 1:
			print('1 carry operation.')
		else:
			print('{} carry operations.'.format(carry_count))


main()