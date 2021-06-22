def main():
	count = int(input())
	start, end = 1, 4
	while count > 0:
		print(" ".join(map(str, list(range(start, end)))), 'PUM')
		start += 4
		end += 4
		count -= 1

main()