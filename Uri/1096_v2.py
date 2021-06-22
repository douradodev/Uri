def imprime_seq(I, J, num=3):
	if num:
		print('I={}'.format(I), 'J={}'.format(J))
		imprime_seq(I, J-1, num-1)


def seq_IJ02(I=1, J=7):
	if I <= 9:
		imprime_seq(I,J)
		seq_IJ02(I+2, J=7)


seq_IJ02()
