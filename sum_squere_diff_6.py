from functools import reduce
import operator


def sum_square_difference(n):
    numbers = range(1, n+1)
    sum_of_squares = reduce(operator.add, map(lambda x: x*x, numbers))
    square_of_sum = reduce(operator.add, numbers)**2
    return square_of_sum - sum_of_squares

result = sum_square_difference(100)
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is:", result)