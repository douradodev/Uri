def main():
	
	animal0 = input()
	animal1 = input()
	animal2 = input()

	if animal0== 'vertebrado':

		if animal1 == 'ave':
			if animal2 == 'carnivoro':
				print('aguia')
			elif animal2 == 'onivoro':
				print('pomba')

		elif animal1 == 'mamifero':
			if animal2 == 'onivoro':
				print('homem')
			elif animal2 == 'herbivoro':
				print('vaca')

	elif animal0 == 'invertebrado':

		if animal1 == 'inseto':
			if animal2 == 'hematofago':
				print('pulga')
			elif animal2 == 'herbivoro':
				print('lagarta')

		elif animal1 == 'anelideo':
			if animal2 == 'hematofago':
				print('sanguessuga')
			elif animal2 == 'onivoro':
				print('minhoca')


main()