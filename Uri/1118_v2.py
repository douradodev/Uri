def validacao_notas(count=0, total=0):	
	while count < 2:
		nota = float(input())
		if 0 > nota or nota > 10:
			print('nota invalida')
		else:
			total += nota
			count += 1

	print('media = {:.2f}'.format(total/2))


def novo_calculo():
	'''!!!Possível limite de recursividade no URI'''
	res = int(input('novo calculo (1-sim 2-nao)\n'))
	if res == 1:		
		main()
	elif res == 2:
		return
	else:	
		novo_calculo()


def main():
	validacao_notas()
	novo_calculo()


main()