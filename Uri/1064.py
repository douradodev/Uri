total = 0
pos = 0

for i in range(6):
	x = float(input())
	if x >= 0:
		pos += 1
		total += x
print(pos, 'valores positivos')
print('{:.1f}'.format(total/pos))