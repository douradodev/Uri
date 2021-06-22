def float_precision(num1, num2, dec=1):
	'''Soma dois valores de ponto flutuante com ajuste de precisão.
	Obs: Falta fazer a checagem para o numero com mais casas decimais'''
	
	while (num1*10**dec) - int(num1*10**dec):
		dec += 1

	mult = 10**dec

	return float(((num1*mult) + (num2*mult))/mult)


def max_recursion_handling(number, function):
	#TODO
	if number//999:
		max_recursion_handling(number%999, function)


def recursions_test(tests=998):
	if tests:
		recursions_test(tests-1)


def min_and_max(num1, num2):
	if num1 > num2:
		return num2, num1
	else:
		return num1, num2


def strip_zero(num):
	'''Retorna um numero inteiro caso ele tenha zero a direita. Ex: 1.0 => 1'''
	if num - int(num):
		return num
	else:
		return int(num)


def even_to_odd(num):
	return num + ((num+1)%2)


def odd_to_even(num):
	return num + ((num)%2)


def my_len(some_list, total=0):
	if not some_list:
		return total
	else:
		return my_len(some_list[1:], total+1)


def my_count(word, char, start=0, total=0):
	while word[start:]:
		if word[start:][0] == char:
			total += 1
		start += 1
	return total


if __name__ == '__main__':
	print(my_count('lacas', 's'))
