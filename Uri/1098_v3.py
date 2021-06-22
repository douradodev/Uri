def strip_zero(num):
	'''Retorna um numero inteiro caso ele tenha zero a direita. Ex: 1.0 => 1'''
	if num - int(num):
		return num
	else:
		return int(num)


def float_precision(num1, num2, dec=1):
	'''Soma dois valores de ponto flutuante com ajuste de precisão.
	Obs: Falta fazer a checagem para o numero com mais casas decimais'''
	
	while (num1*10**dec) - int(num1*10**dec):
		dec += 1

	mult = 10**dec

	return float(((num1*mult) + (num2*mult))/mult)


def imprime_seq(I, J, num=3):
	if num:
		print('I={}'.format(I), 'J={}'.format(J))
		imprime_seq(I, J+1, num-1)


def seq_IJ04(I=0, J=1, lim=20, inc=0.2):
	I, J = strip_zero(I), strip_zero(J)
	
	if I <= lim:
		imprime_seq(I,J)		
		seq_IJ04(float_precision(I, inc), float_precision(J, inc))


seq_IJ04()
