def main():

	hours = input().split()

	for index in range(len(hours)):
		hours[index] = int(hours[index])

	if hours[0] >= hours[1]:
		print('O JOGO DUROU {} HORA(S)'.format((hours[1] + 24) - hours[0]))
	else:
		print('O JOGO DUROU {} HORA(S)'.format(hours[1] - hours[0]))


main()
