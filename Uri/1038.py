def main():
	code, qtd = map(int, input().split())	

	if code == 1:
	    print("Total: R$ %.2f" % (qtd * 4.00))
	elif code == 2:
	    print("Total: R$ %.2f" % (qtd * 4.50))
	elif code == 3:
	    print("Total: R$ %.2f" % (qtd * 5.00))
	elif code == 4:
	    print("Total: R$ %.2f" % (qtd * 2.00))
	elif code == 5:
	    print("Total: R$ %.2f" % (qtd * 1.50))


main()