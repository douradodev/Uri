def main():
	times = int(input())
	numbers = []

	for i in range(times):		
		numbers.append(input().split())
	
	
	for test in numbers:
		
		total = 0
		for num in test[1:]:
			if float(num) <= 0:
				continue
			total = total + float(num)

		average = total/float(test[0])		

		above = 0
		for num in test[1:]:
			if int(num) > average:
				above += 1

		result = above/float(test[0])*100

		print("{:.3f}%".format(result))

main()
