while True:
	test_case = input().split()

	if test_case == ['0', '0']:
		break

	test_case[1] = test_case[1].split(test_case[0])
		
	result = "".join(test_case[1])

	if result == '':
		print(0)
	else:
		print(int(result))
