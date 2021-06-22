def main():
	value = int(input())

	cem = int(value/100)
	cinquenta = int((value - (cem * 100))/50)
	vinte = int((value - (cem * 100) -(cinquenta * 50))/20)
	dez = int((value - (cem * 100) -(cinquenta * 50) -(vinte * 20))/10)
	cinco = int((value - (cem * 100) -(cinquenta * 50) 
		-(vinte * 20) -(dez * 10))/5)
	dois = int((value - (cem * 100) -(cinquenta * 50) -(vinte * 20) 
		-(dez * 10) -(cinco * 5))/2)
	um = int((value - (cem * 100) -(cinquenta * 50) -(vinte * 20) 
		-(dez * 10) -(cinco * 5) -(dois * 2)))


	print(value)
	print("%i nota(s) de R$ 100,00" % cem)
	print("%i nota(s) de R$ 50,00" % cinquenta)
	print("%i nota(s) de R$ 20,00" % vinte)
	print("%i nota(s) de R$ 10,00" % dez)
	print("%i nota(s) de R$ 5,00" % cinco)
	print("%i nota(s) de R$ 2,00" % dois)
	print("%i nota(s) de R$ 1,00" % um)


main()