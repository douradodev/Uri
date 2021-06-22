def imprime_seq(I, J, num=3):
	if num:
		print('I={}'.format(I), 'J={}'.format(J))
		imprime_seq(I, J-1, num-1)


def seq_IJ03(I=1, J=7):
	if I <= 9:
		imprime_seq(I,J)
		seq_IJ03(I+2, J+2)


seq_IJ03()
