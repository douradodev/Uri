def min_and_max(num1, num2):
	if num1 > num2:
		return num2, num1
	else:
		return num1, num2


def converte_par(numero):
	'''Transforma um número par em um número sucessor impar'''
	return numero + ((numero+1)%2)

def soma_impares(inicio, fim):

	if inicio%2 == 0:
		inicio = converte_par(inicio)
	else:
		inicio += 2

	soma = 0
	while inicio < fim:		
		soma += inicio
		inicio += 2

	return soma


def main():
	num1 = int(input())
	num2 = int(input())

	num1, num2 = min_and_max(num1, num2)

	print(soma_impares(num1, num2))


main()