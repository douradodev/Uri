def main():

	while True:
		try:
			numbers = input().split()
			total = 0

			for num in numbers:
				fact = 1
				for x in range(1, int(num)+1):
					fact = fact * x
				total = total + fact

			print(total)

		except EOFError:
			break

main()