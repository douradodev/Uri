I = 0
J = [1,2,3]

while 2 > I:
	for j in J:
		if str(round(j,1))[-1] != '0':
			print('I={}'.format(round(I,1)), 'J={}'.format(round(j,1)))
		else:
			print('I={}'.format(round(I)), 'J={}'.format(round(j)))

	J = [j+0.2 for j in J]
	I += 0.2