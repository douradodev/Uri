def main():

	while True:
		#test = list(map(int, input().split()))

		rows = list(range(1,9))
		cols = list(range(1,9))

		total = []

		for r in rows:
			for c in cols:
				total.append([r,c])

		for i in range(0,9):
			for y in range(0,9):
				print(total[i * y], end='')
			print()

		input()

main()