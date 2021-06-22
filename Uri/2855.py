def main():
	test_seq = int(input())
	numbers = list(map(int, input().split()))
	lucky_test = int(input())

	order_test = 2
	
	while len(numbers) > order_test:
		print('INDEX: ', numbers.index(lucky_test)+1)
		new_numbers = numbers[0::order_test]
		print('NEW LEN: ', len(new_numbers))
		if lucky_test not in new_numbers:
			print('NEW:', new_numbers)
			print('N')
			return
		else:
			numbers = new_numbers
			print('NUM: ', numbers)

		order_test +=1

	print('Y')
	

main()