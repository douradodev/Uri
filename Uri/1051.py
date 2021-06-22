def main():

	salary = float(input())

	if 0 < salary <= 2000:
		print('Isento')
	elif 2000 < salary <= 3000:
		print('R$ {:.2f}'.format((salary - 2000) * 0.08))
	elif 3000 < salary <= 4500:
		print('R$ {:.2f}'.format(((salary - 3000) * 0.18)+(1000*0.08)))
	elif 4500 < salary:
		print('R$ {:.2f}'.format(((salary - 4500) * 0.28)+(1000*0.08)+(1500*0.18)))


main()