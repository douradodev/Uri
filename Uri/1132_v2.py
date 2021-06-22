def min_and_max(num1, num2):
	if num1 > num2:
		return num2, num1
	else:
		return num1, num2


def soma_nao_multiplos(inicio, fim, num=13, soma=0):
	while inicio <= fim:
		if inicio%num:
			soma += inicio
		inicio += 1

	return soma


def main():
	num1 = int(input())
	num2 = int(input())
	
	num1, num2 = min_and_max(num1, num2)

	print(soma_nao_multiplos(num1,num2))


main()