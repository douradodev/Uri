def main():

	number = input().split()

	for index in range(len(number)):
		number[index] = int(number[index])

	number.sort()

	if number[1] % number[0] == 0:
		print('Sao Multiplos')
	else:
		print('Nao sao Multiplos')


main()