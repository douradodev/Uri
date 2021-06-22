def tabuada(num):
	count = 1
	while count <= 10:
		print('{} x {} = {}'.format(count, num, num*count))
		count += 1


tabuada(int(input()))
