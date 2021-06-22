def primes_gen(qtd):
	global primes
	primes = []
	number = 2

	while len(primes) < qtd:

	    if len(primes) == 0:
	        primes.append(number)
	        number += 1

	    else:

	        for i in primes:
	            if number % i == 0:
	                break
	        else:
	            primes.append(number)

	        number += 2

	return primes


def main():
	times = int(input())
	numbers = []	

	for _ in range(times):
		numbers.append(int(input()))

	for num_check in numbers:
		if num_check == 2:
			print('Prime')
			continue

		else:
			loop = True
			while loop:

				for pri_div in primes:

					if num_check == pri_div:
						print('Prime')
						loop = False
						break

					elif num_check % pri_div == 0:
						print('Not Prime')
						loop = False
						break
					
				else:
					print('Prime')
					loop = False



primes_gen(3514)
main()