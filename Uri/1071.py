x = int(input())
y = int(input())

total = 0
for num in range(min(x,y)+1,max(x,y)):
	if num % 2 != 0:
	 total += num
else:
	print(total)