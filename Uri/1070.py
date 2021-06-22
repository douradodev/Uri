x = int(input())
for i in range(6):
	if x % 2 == 0:
		x = x+1
		print(x)
		x += 2
	else:
		print(x)
		x += 2