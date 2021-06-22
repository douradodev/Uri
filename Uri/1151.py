seq = '0 1'
fib = int(input())	

if fib == 1:
	print('0')
else:
	fib_lst = [0,1,0]
	total = 0
	for i in range(1,fib-1):
		fib_lst[2] = fib_lst[0] + fib_lst[1]

		seq += " " + str(fib_lst[2])


		fib_lst[0] = fib_lst[1]
		fib_lst[1] = fib_lst[2]

	else:
		print(seq)