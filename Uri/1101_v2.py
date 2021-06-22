def min_and_max(num1, num2):
	if num1 > num2:
		return num2, num1
	else:
		return num1, num2


def seq_e_soma(inicio, fim, soma=0):
	if inicio <= fim:
		print(inicio, end=" ")
		seq_e_soma(inicio+1, fim, soma+inicio)
	else:
		print('Sum={}'.format(soma))


def main_loop():
	num1, num2 = map(int, input().split())
	if num1 > 0 and num2 > 0:
		num1, num2 = min_and_max(num1, num2)
		seq_e_soma(num1, num2)
		main_loop()
	

main_loop()
