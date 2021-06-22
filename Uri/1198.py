while True:
	try:
		x, y = map(int, input().split())

		x, y = sorted([x, y])

		print(abs(y - x))

	except EOFError:
		break
		