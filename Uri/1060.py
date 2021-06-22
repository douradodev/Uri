COUNT = 0
for _ in range(6):
	num = float(input())
	if num > 0:
		COUNT +=1
print('{} valores positivos'.format(COUNT))