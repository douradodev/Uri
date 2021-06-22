def main():
	salary = float(input())

	if 0 < salary <= 400:		
		earned = salary * 0.15
		percentage = 15
	elif 400 < salary <= 800:
		earned = salary * 0.12
		percentage = 12
	elif 800 < salary <= 1200:
		earned = salary * 0.10
		percentage = 10
	elif 1200 < salary <= 2000:
		earned = salary * 0.07
		percentage = 7
	elif 2000 < salary:
		earned = salary * 0.04
		percentage = 4

	new_salary = earned + salary

	print('Novo salario: {:.2f}'.format(new_salary))
	print('Reajuste ganho: {:.2f}'.format(earned))
	print('Em percentual: {} %'.format(percentage))


main()