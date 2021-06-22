x = int(input())
y = int(input())

x, y = sorted([x, y])

total = 0
for num in range(x, y+1):
	if num % 13 != 0:
		total += num
else:
	print(total)