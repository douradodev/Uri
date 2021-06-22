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
