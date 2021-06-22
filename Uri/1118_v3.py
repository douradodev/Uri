def validacao_notas(count=0, total=0):	
	while count < 2:
		nota = float(input())
		if 0 > nota or nota > 10:
			print('nota invalida')
		else:
			total += nota
			count += 1

	print('media = {:.2f}'.format(total/2))


def main():
	validacao_notas()

	res = 0
	while res != 2:
		res = float(input('novo calculo (1-sim 2-nao)\n'))
		if res == 1:			
			validacao_notas()


main()