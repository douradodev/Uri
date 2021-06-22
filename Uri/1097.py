I = 1
start, end = 7, 4

while 10 > I:
	J = list(range(start,end,-1))
	for j in J:
		print('I={}'.format(I), 'J={}'.format(j))

	start +=2
	end +=2
	I += 2