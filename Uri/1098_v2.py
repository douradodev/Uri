def min_and_max(num1, num2):
	if num1 > nu

def nao_sou_uma_lista(var1, var2):
	return var1, var2

def strip_zero(num):
	'''Retorna um numero inteiro caso ele tenha zero a direita. Ex: 1.0 => 1'''
	if num - int(num):
		return num
	else:
		return int(num)

def imprime_seq(I, J, num=3):
	if num:
		print('I={}'.format(I), 'J={}'.format(J))
		imprime_seq(I, J+1, num-1)


def seq_IJ04(I=0, J=1):
	I, J = map(strip_zero, nao_sou_uma_lista(I, J))

	if I <= 2:
		imprime_seq(I,J)
		seq_IJ04((10*I+2)/10, (10*J+2)/10) # Evitando problemas de imprecisão como: 0.60000000001


seq_IJ04()