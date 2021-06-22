def main():
	while True:
		try:
			numbers = input().split()

			numbers[0] = str(bin(int(numbers[0]))[2:])
			numbers[1] = str(bin(int(numbers[1]))[2:])

			while len(numbers[0]) < len(numbers[1]):
					numbers[0] = '0' + numbers[0]
			while len(numbers[0]) > len(numbers[1]):
				numbers[1] = '0' + numbers[1]

			result = ''
			for i in range(len(numbers[0])-1,0-1,-1):

				if numbers[0][i] == '1' and numbers[0][i] == numbers[1][i]:
					result = '0' + result
				elif numbers[0][i] != numbers[1][i]:
					result = '1' + result
				else:
					result = '0' + result

			if result == '':
				result = '0'		

			print(int(result, 2))

		except EOFError:
			break


main()