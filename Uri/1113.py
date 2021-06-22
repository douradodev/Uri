x, y = 0, 1
while x != y:
	x, y = map(int, input().split())
	if x < y:
		print('Crescente')
	elif x > y:
		print('Decrescente')