x = int(input())
y = int(input())

x, y = sorted([x, y])

total = 0
for num in range(x+1, y):
	if num % 5 == 2 or num % 5 == 3:
		print(num)

