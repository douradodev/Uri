def main():
	'''# melhorar este código 2000%'''
	pontos_ifpi = 29666
	pontos_primeiro = 164527
	pontos_top10 = 58167
	pontos_top20 = 36045
	pontos_pag1 = 32551
	pontos_proximo = 30403
	qtd_alunos = 40

	print('\033c')
	print('Quatidade de questões para o IFPI chegar em primeiro lugar: {}'.format(pontos_primeiro - pontos_ifpi + 1))
	print('Media por aluno: {}'.format((pontos_primeiro - pontos_ifpi + 1)/qtd_alunos))

	print('\nQuatidade de questões para o IFPI chegar no top10: {}'.format(pontos_top10 - pontos_ifpi + 1))
	print('Media por aluno: {}'.format((pontos_top10 - pontos_ifpi + 1)/qtd_alunos))

	print('\nQuatidade de questões para o IFPI chegar no top20: {}'.format(pontos_top20 - pontos_ifpi + 1))
	print('Media por aluno: {}'.format((pontos_top20 - pontos_ifpi + 1)/qtd_alunos))

	print('\nQuatidade de questões para o IFPI chegar na primeira página: {}'.format(pontos_pag1 - pontos_ifpi + 1))
	print('Media por aluno: {}'.format((pontos_pag1 - pontos_ifpi + 1)/qtd_alunos))

	print('\nQuatidade de questões para o IFPI subir uma posição {}'.format(pontos_proximo - pontos_ifpi +1))
	print('Media por aluno: {}'.format((pontos_proximo - pontos_ifpi + 1)/qtd_alunos))
	print('\n'*10)


main()