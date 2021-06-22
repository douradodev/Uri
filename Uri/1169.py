for _ in range(int(input())):
	total = 0
	for num in range(int(input())):
		total += 2**num
	else:
		print("{:.0f} kg".format((total/12)//1000))
