def main():
	while True:
		try:
			password = input()

			if 6 > len(password) or 32 < len(password):
				print('Senha invalida.')
				continue
			if len(password.split()) > 1:
				print('Senha invalida.')
				continue
			if not password.isalnum():
				print('Senha invalida.')
				continue

			check_char = []
			for char in list(set(password)):
				if char.islower():
					break
			else:
				print('Senha invalida.')
				continue

			for char in list(set(password)):
				if char.isupper():
					break
			else:
				print('Senha invalida.')
				continue

			for char in list(set(password)):
				if char.isdigit():
					break
			else:
				print('Senha invalida.')
				continue
			
			print('Senha valida.')
			

		except EOFError:
			break

main()