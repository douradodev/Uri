for _ in range(int(input())):
	x, y = map(int, input().split())
	resultado = 0


	for i in range(min(x,y)+1,max(x,y)):
		if i % 2 != 0:
			resultado += i

	print(resultado)