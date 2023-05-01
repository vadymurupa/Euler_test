'''


A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


'''

# Imperative style

def is_polyndrome(number):
    return str(number) == str(number)[::-1]


def largest_polyndrome():
    largest = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if is_polyndrome(product) and product > largest:
                largest = product
    return largest

result_imperative = largest_polyndrome()
print(" The largest polyndrome of two 3-digit numbers: ", result_imperative)


# Declerative style

def largest_polyndrome_d():
    return max([i * j for i in range(100, 1000) for j in range(i, 1000) if is_polyndrome(i * j)])

result_dclerative = largest_polyndrome_d()
print("The largest polyndrome of 3 digit in declerative style is: ", result_dclerative)

# Functional style

from itertools import product

def largest_polyndrome_f():
    return max(filter(is_polyndrome, map(lambda x: x[0] * x[1], product(range(100,1000), range(100, 1000)))))

result_functional = largest_polyndrome_f()
print("The largest polyndrome of 3-digit number in function style is: ", result_functional)



