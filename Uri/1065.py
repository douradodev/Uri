x = []
for i in range(5):
	x.append(int(input()))

print('{} valores pares'.format(len(list(filter(lambda y : y % 2 == 0, x)))))
