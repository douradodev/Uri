def maior_e_posicao():
	maior = 0
	posicao = 0
	count = 1
	while count <= 100:
		numero = int(input())
		if numero > maior:
			maior = numero
			posicao = count
		count += 1

	print(maior)
	print(posicao)


maior_e_posicao()