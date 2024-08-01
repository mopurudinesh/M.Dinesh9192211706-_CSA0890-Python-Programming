def sum_square_difference(n):
    sum_of_squares = sum(i**2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1))**2
    return square_of_sum - sum_of_squares
n=200
sum_of_squares_200 = sum(i**2 for i in range(1, n + 1))
square_of_sum_200 = sum(range(1, n + 1))**2
difference_200 = square_of_sum_200 - sum_of_squares_200
print("The sum of the squares of the first 200 natural numbers is:", sum_of_squares_200)
print("The square of the sum of the first 200 natural numbers is:", square_of_sum_200)
print("The difference between the sum of squares and The square of the sum of first 200 natural numbers:",difference_200)
