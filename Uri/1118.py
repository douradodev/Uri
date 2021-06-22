def main():	
	count = 0
	total = 0
	while count < 2:
		nota = float(input())
		if 0 > nota or nota > 10:
			print('nota invalida')
		else:
			total += nota
			count += 1

	print('media = {:.2f}'.format(total/2))	
	
main()

asw = 0
while asw != 2:
	asw = float(input('novo calculo (1-sim 2-nao)\n'))
	if asw == 1:
		asw = 0
		main()
