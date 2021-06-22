def min_and_max(num1, num2):
	if num1 > num2:
		return num2, num1
	else:
		return num1, num2


def converte_par(numero):	
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


def mult_print(testes):
	if testes:
		num1, num2 = map(int, input().split())

		num1, num2 = min_and_max(num1, num2)

		print(soma_impares(num1, num2))
		mult_print(testes-1)


mult_print(int(input()))
