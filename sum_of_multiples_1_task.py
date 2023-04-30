"""
1 task

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

_
"""

def sum_of_multiples(max_value):
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(max_value)))
print("The number of multiples is: ", sum_of_multiples(1000))

