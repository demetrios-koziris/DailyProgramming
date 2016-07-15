# Project Euler Problem 1: Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_multiples(factors, upper_bound):
    return sum([num for num in range(1, upper_bound) if 0 in [num % factor for factor in factors]])

print(sum_multiples([3, 5], 1000))
