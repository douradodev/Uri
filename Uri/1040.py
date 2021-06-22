def main():
	N1, N2, N3, N4 = map(float, input().split())	

	media = float(((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1))/(2 + 3 + 4 + 1))

	if media >= 7:
	    print("Media: %.1f" % media)
	    print("Aluno aprovado.")

	elif media <= 4.9:
	    print("Media: %.1f" % media)
	    print("Aluno reprovado.")

	elif media >= 5 and media < 7:
	    print("Media: %.1f" % media)
	    print("Aluno em exame.")
	    exame = float(input())
	    media_final = (media + exame)/2
	    print("Nota do exame: %.1f" % exame)
	    if media_final >= 5:
	        print("Aluno aprovado.")
	    elif media_final <= 4.9:
	        print("Aluno reprovado.")
	    print("Media final: %.1f" % media_final)


main()