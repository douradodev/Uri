def min_and_max(num1, num2):
	if num1 > num2:
		return num2, num1
	else:
		return num1, num2


def imprime_numeros(inicio, fim):
	inicio += 1	
	while inicio < fim:
		if inicio%5 ==2 or inicio%5==3:
			print(inicio)
		inicio += 1


def main():
	num1 = int(input())
	num2 = int(input())
	
	num1, num2 = min_and_max(num1, num2)

	imprime_numeros(num1,num2)


main()