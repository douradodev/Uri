def main():

	while True:

		try:
			test_seq = int(input())
			numbers = input().split()
			lucky_test = input()

			order_test = 2
			while len(numbers)+1 > order_test:
				if lucky_test not in numbers:
					print('N')
					break
				elif (numbers.index(lucky_test)+1) % order_test == 0:
					print('N')
					break
				else:
					numbers = numbers[0::order_test]
					order_test += 1					
					continue
			else:
				if lucky_test not in numbers:
					print('N')
				else:
					print('Y')

		except EOFError:
			break


main()
