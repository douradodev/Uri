def primes_gen(qtd):
    global primes_GLOBL
    primes_GLOBL = []
    number = 2

    while len(primes_GLOBL) < qtd:

        if len(primes_GLOBL) == 0:
            primes_GLOBL.append(number)
            number += 1

        else:

            for i in primes_GLOBL:
                if number % i == 0:
                    break
            else:
                primes_GLOBL.append(number)

            number += 2

    return primes_GLOBL


def factoration(number):
    factors = []

    result = number/1

    while result != 1:

        for pri in primes_GLOBL:
            if result % pri == 0:
                factors.append(pri)
                result = result/pri
                break

    return factors[::-1]


def factors_handling(factors, primes_test):

    test_two = factors.count(2)//3

    if test_two < 1:
        return factors, primes_test

    for i in range(test_two):  # Test conditions
        if factors[0] == 2:
            # Continue this function
            break
        elif factors.count(2) % 3 == 0 and factors[0] != 3:
            # End this fuction
            return factors, primes_test
        else:
            # Continue this function
            break

    for i in range(test_two):
        primes_test.pop()
        factors.pop()

        if factors[0] == 3 and factors[0] == factors[1]:
            factors[0] = factors[0]*2
            continue

        factors[-1] = factors[-1]*2
        factors.sort(reverse=True)

    return factors, primes_test


def minimum_number(inpt):

    prime_factors = factoration(inpt)
    primes_list = primes_GLOBL[:len(prime_factors)]

    prime_factors, primes_list = factors_handling(prime_factors, primes_list)

    min_number = 1
    index = 0
    for prime_number in primes_list:

        x = (prime_number**(prime_factors[index]-1))
        min_number = min_number * x
        index += 1

    print(min_number % 1000000007)


def main():
    primes_gen(26)

    times = int(input())
    check_list = []

    for _ in range(times):
        check_list.append(int(input()))

    for num in check_list:
        minimum_number(num)


main()
