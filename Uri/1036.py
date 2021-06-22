def main():
	A, B, C = map(float, input().split())

	DELTA = (B**2) - 4*(A*C)

	if DELTA < 0 or A == 0:
	    print("Impossivel calcular")
	else:
	    R1 = (-B + DELTA**0.5)/(2*A)
	    R2 = (-B - DELTA**0.5)/(2*A)
	    print("R1 = %.5f" % R1)
	    print("R2 = %.5f" % R2)


main()