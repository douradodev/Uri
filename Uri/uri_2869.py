def factoration(number):
    factors = []
    primes = primes_gen(number)

    result = number/1

    while result != 1:

        for pri in primes:
            if result % pri == 0:
                factors.append(pri)
                result = result/pri
                break

    return factors[::-1]


def primes_gen(qtd):

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


def minimum_number(inpt):

    prime_factors = factoration(inpt)
    primes_list = primes_gen(len(prime_factors))
    min_number = 1
    index = 0

    for prime_number in primes_list:

        x = (prime_number**(prime_factors[index]-1))
        min_number = min_number * x
        index += 1

    print(min_number % 1000000007)


def main():
    times = int(input())
    check_list = []

    for _ in range(times):
        check_list.append(int(input()))

    for num in check_list:
        minimum_number(num)



main()
