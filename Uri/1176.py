for _ in range(int(input())):
	fib = int(input())	

	if fib == 0:
		print('Fib(0) = 0')
		continue
	elif fib == 1:
		print('Fib(1) = 1')
		continue

	fib_lst = [0,1,0]
	total = 0
	for i in range(1,fib):
		fib_lst[2] = fib_lst[0] + fib_lst[1]
		fib_lst[0] = fib_lst[1]
		fib_lst[1] = fib_lst[2]

	else:
		print('Fib({}) = {}'.format(fib, fib_lst[2]))