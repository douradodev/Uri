while True:

		try:
			test_seq = int(input())
			numbers = input().split()
			lucky_num = input()
			
			order_test = 2
			while True:

				if lucky_num not in numbers:
						print('N')
						break

				num_pos = numbers.index(lucky_num)+1

				if num_pos <= order_test:
					print('Y')
					break
				elif num_pos % order_test == 0:
					print('N')
					break
				else:
					numbers = numbers[::order_test]
					order_test += 1
					if lucky_num not in numbers:
						print('N')
						break


		except EOFError:
			break