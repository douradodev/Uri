for _ in range(int(input())):
	
	total = float(input())
	
	days = 0
	while total > 1:
		total = total/2
		days += 1

	print(days, 'dias') 
