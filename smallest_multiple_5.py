from functools import reduce
from math import gcd

def lcm(a,b):
    return ( a * b) // gcd(a, b)

def smallest_divisible_number(n):
    return reduce(lcm, range(1, n+1))


result_functional = smallest_divisible_number(20)
print("Smallest divisible number for number 1 to 20:  ", result_functional)