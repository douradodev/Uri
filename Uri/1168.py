def main():
	leds = {'1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6, '0':6}

	times = int(input())
	numbers = []	

	for test in range(times):
		numbers.append(input())

	for num in numbers:
		total = 0
		for i in num:
			total += leds[i]
		print(total, 'leds')

main()