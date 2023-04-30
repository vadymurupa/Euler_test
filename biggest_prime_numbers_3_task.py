'''


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


'''

# Imperative

def largest_prime_factor_imperative(number):
    factor = 2
    while factor <= number:
        if number % factor == 0:
            number /= factor
        else:
            factor += 1
    return factor

imperative_result = largest_prime_factor_imperative(600851475143)
print("Largest prime factor in imperative is: ", imperative_result)


# Declerative

from math import sqrt

def largest_prime_factor_declerative(number_d):
    def is_prime(n):
        return all(n % i != 0 for i in range(2, int(sqrt(n))+1))
    return max(filter(lambda x: number_d % x == 0 and is_prime(x), range(2, int(sqrt(number_d))+1)))

result_declerative = largest_prime_factor_declerative(600851475143)
print("Largest prime factor in declerative style is:  ", result_declerative)

# Functional style

from functools import reduce

def largest_prime_factor_functional(number_f):
    return reduce(lambda a, b: b if number_f % b == 0 and all(b % i != 0 for i in range(2, int(sqrt(b))+1)) else a, range(2, int(sqrt(number_f))+1), 1)


result_functional = largest_prime_factor_functional(600851475143)
print("Largest prime factor in functional is : ", result_functional)
