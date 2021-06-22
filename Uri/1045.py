def main():

	number = input().split()

	for index in range(len(number)):
		number[index] = float(number[index])

	number.sort(reverse=True)

	if number[0] >= number[1] + number[2]:
		print('NAO FORMA TRIANGULO')
	else:
		if number[0]**2 == number[1]**2 + number[2]**2:
			print('TRIANGULO RETANGULO')
		elif number[0]**2 > number[1]**2 + number[2]**2:
			print('TRIANGULO OBTUSANGULO')
		elif number[0]**2 < number[1]**2 + number[2]**2:
			print('TRIANGULO ACUTANGULO')

		if number[0] == number[1] == number[2]:
			print('TRIANGULO EQUILATERO')
		elif number[0] == number[1] or number[1] == number[2]:
			print('TRIANGULO ISOSCELES')


main()