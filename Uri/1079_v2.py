def medias_ponderadas(num):
	while num:
		x, y, z = map(float, input().split())
		print('{:.1f}'.format(((x*2)+(y*3)+(z*5))/10))
		num -= 1


medias_ponderadas(int(input()))