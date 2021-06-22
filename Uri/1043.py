def main():

	L = input().split()
	
	for index in range(len(L)):
		L[index] = float(L[index])

	L_ST = sorted(L)  # L_ST stands for Sorted

	if L_ST[2] < L_ST[0] + L_ST[1]:
		perimeter = L[0] + L[1] + L[2]
		print('Perimetro = {:.1f}'.format(perimeter))
	else:
		area = ((L[0] + L[1]) * L[2])/2
		print('Area = {:.1f}'.format(area))
		

main()
