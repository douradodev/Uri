codigo, alcool, gasolina, diesel = 0, 0, 0, 0
while codigo != '4':
	codigo = input()
	if codigo == '1':
		alcool += 1
	elif codigo == '2':
		gasolina += 1
	elif codigo == '3':
		diesel += 1

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))
