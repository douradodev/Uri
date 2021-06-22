def main():
	times = int(input())
	numbers = []	

	for _ in range(times):
		numbers.append(input().split())


	for test in numbers:
		result = int(test[0])**int(test[1])
		print(len(str(result)))


main()

