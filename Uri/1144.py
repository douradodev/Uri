def main():
	count = int(input())
	num = 1
	while count > 0:
		print(num, num**2, num**3)
		print(num, (num**2)+1, (num**3)+1)
		num += 1
		count -= 1


main()
