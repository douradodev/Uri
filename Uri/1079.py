for i in range(int(input())):
	x, y, z = map(float, input().split())
	print('{:.1f}'.format(((x*2)+(y*3)+(z*5))/10))