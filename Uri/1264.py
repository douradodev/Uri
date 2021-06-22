def main():	
	while  True:
		try:		
			test_num = input()

			nums_bases = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
			num_sis_dict = {'0':2, '1':2}

			count = 3
			for i in nums_bases[2:]:
				x = {i : count}
				num_sis_dict.update(x)
				count += 1

			test_sis = num_sis_dict[sorted(set(list(test_num)))[-1]]

			print(test_sis)

		except EOFError:
			break

	
main()