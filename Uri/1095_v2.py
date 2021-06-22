def seq_IJ01(I=1, J=60):	
	if J >= 0:
		print('I={}'.format(I), 'J={}'.format(J))		
		seq_IJ01(I+3, J-5)

seq_IJ01()