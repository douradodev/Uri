def main():
	tempo = input().split()	

	inicio_minutos = int(tempo[0])*60 + int(tempo[1])
	fim_minutos = int(tempo[2])*60 + int(tempo[3])

	if inicio_minutos >= fim_minutos:
		fim_minutos = (int(tempo[2]) + 24)*60 + int(tempo[3])
		resultado_minutos = fim_minutos - inicio_minutos
	else:
		resultado_minutos = fim_minutos - inicio_minutos

	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(resultado_minutos//60, resultado_minutos%60))


main()