while True:
	num1, num2 = (map(int, input().split()))

	if 0 >= num1 or num2 <= 0:
		break

	seq = list(range(min(num1, num2), max(num1, num2)+1))
	sumt = 0

	for t in seq:
		sumt += t

	print(' '.join(map(str, seq)), 'Sum={}'.format(sumt))

