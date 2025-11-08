from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda num1, num2: num1 + num2, numbers)
print(f'sum_of_numbers: {sum_of_numbers}')