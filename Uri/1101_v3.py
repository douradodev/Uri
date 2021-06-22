def min_and_max(num1, num2):
	if num1 > num2:
		return num2, num1
	else:
		return num1, num2


def main():
	while True:
		num1, num2 = (map(int, input().split()))
		num1, num2 = min_and_max(num1, num2)

		if num1 or num2 <= 0:
			break

		seq = list(range(min(num1, num2), max(num1, num2)+1))
		sumt = 0

		for t in seq:
			sumt += t

		print(' '.join(map(str, seq)), 'Sum={}'.format(sumt))


main()