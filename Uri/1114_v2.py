def verifica_senha(senha=2002):
	if int(input()) == senha:
		print('Acesso Permitido')
	else:
		print('Senha Invalida')
		verifica_senha()


verifica_senha()
