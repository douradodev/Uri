inside, out = 0 , 0
for _ in range(int(input())):
	test = int(input())
	if test >= 10 and test <= 20:
		inside +=1
	else:
		out += 1
else:
	print('{} in'.format(inside))
	print('{} out'.format(out))